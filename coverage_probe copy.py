#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Dicle Öztürk
"""
coverage_probe.py — Do these models produce anything usable in these languages?

Runs BEFORE any study material is prepared. Needs no speakers, no stimuli, no
transcription. Answers one question: for each model and language, is there
output at all, is it in the right language and script, or is it fabrication?

The flags it attaches are crude heuristics for reading the output quickly.
They are not judgments of intelligibility, which only a speaker can make.

Usage:
    export OPENROUTER_API_KEY=sk-or-...
    python coverage_probe.py --dry-run          # print prompts, call nothing
    python coverage_probe.py                    # full run
    python coverage_probe.py --models anthropic/claude-sonnet-5
    python coverage_probe.py --languages kirmancki adyghe
"""

import argparse
import json
import os
import sys
import time
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG — edit before running
# ─────────────────────────────────────────────────────────────────────────────

# Verify these slugs on https://openrouter.ai/models before the real run.
# Model names move fast; whatever runs gets logged verbatim, so the paper
# reports what actually ran rather than what was planned.
PRESETS = {
    # Paper-grade: pinned snapshots, three different training regimes.
    "paper": {
        "models": [
            "anthropic/claude-sonnet-5",       # frontier closed A
            "openai/gpt-5.6",                  # frontier closed B, different provider
            "qwen/qwen3.5-72b-instruct",       # open multilingual
        ],
        "base_url": "https://openrouter.ai/api/v1",
        "api_key_env": "OPENROUTER_API_KEY",
        "pause": 0.6,
        "paper_grade": True,
    },
    # Pipeline validation only. Free variants are typically quantised, version
    # -ambiguous, and rotate without notice — fine for "does the code work",
    # not citable. Runs are stamped paper_grade=false so they can never be
    # mistaken for study data later.
    #
    # THIS LIST GOES STALE. Checked 15 Aug 2026; the Llama and Qwen free tiers
    # were delisted shortly before that date. If you get 404s saying "unavailable
    # for free", check https://openrouter.ai/collections/free-models and pass
    # current slugs with --models. `openrouter/free` is a router that picks from
    # whatever is free at the time — it survives delistings, but you cannot know
    # which model answered, so it is for smoke-testing only.
    "free": {
        "models": [
            "google/gemma-4-31b-it:free",              # strong multilingual coverage
            "nvidia/nemotron-3-ultra-550b-a55b:free",  # largest free model
            "google/gemma-4-26b-a4b-it:free",
        ],
        "base_url": "https://openrouter.ai/api/v1",
        "api_key_env": "OPENROUTER_API_KEY",
        "pause": 4.0,                          # free tiers rate-limit hard
        "paper_grade": False,
    },
    # Last resort when the free list has rotated again: one router, one model,
    # no idea which. Enough to prove the pipeline runs end to end.
    "smoke": {
        "models": ["openrouter/free"],
        "base_url": "https://openrouter.ai/api/v1",
        "api_key_env": "OPENROUTER_API_KEY",
        "pause": 4.0,
        "paper_grade": False,
    },
    # Local via Ollama. Slowest to set up, but the version is genuinely pinned
    # and nothing is sent anywhere. `ollama serve` must be running.
    "local": {
        "models": [
            "gemma3:12b",
        ],
        "base_url": "http://localhost:11434/v1",
        "api_key_env": None,                   # Ollama ignores the key
        "pause": 0.0,
        "paper_grade": False,
    },
}

MODELS = PRESETS["paper"]["models"]

TEMPERATURE = 1.0
MAX_TOKENS = 400
SAMPLES_PER_PROBE = 2      # two samples to see whether output is stable or noise
REQUEST_PAUSE = 0.6        # seconds between calls, be polite

LANGUAGES = {
    "kirmancki": {
        "label": "Kirmanckî (Zazaki)",
        "prompt_name": "Kirmanckî (also called Zazaki)",
        "expect_script": "latin",
    },
    "adyghe": {
        "label": "Adyghe (West Circassian)",
        "prompt_name": "Adyghe (West Circassian)",
        "expect_script": "cyrillic",
    },
    "kabardian": {
        "label": "Kabardian (East Circassian)",
        "prompt_name": "Kabardian (East Circassian)",
        "expect_script": "cyrillic",
    },
    "homshetsma": {
        "label": "Homshetsma (Hemshin)",
        "prompt_name": "Homshetsma (the Armenic variety spoken by the Hemshin)",
        "expect_script": "unknown",
    },
    # Control: comparatively better resourced. If a model fails here too,
    # the problem is the setup, not the resource gradient.
    "kurmanji": {
        "label": "Kurmanji Kurdish [control]",
        "prompt_name": "Kurmanji Kurdish",
        "expect_script": "latin",
    },
}

# Three probes, increasing in difficulty. Deliberately NOT the study seeds —
# those stay unpublished and unexposed until the real generation run.
PROBES = {
    "free_narrative": (
        "Write three or four sentences in {lang}. "
        "Tell a very short story about someone walking to a village. "
        "Write only in {lang} — no translation, no explanation, no English."
    ),
    "translation": (
        "Translate this sentence into {lang}:\n\n"
        "\"The water was cold and the children did not want to go in.\"\n\n"
        "Give only the translation, nothing else."
    ),
    "everyday_scene": (
        "Write two or three sentences in {lang} describing this: "
        "guests arrive at a house and the table is not ready yet. "
        "Write only in {lang} — no translation, no explanation, no English."
    ),
}

# ─────────────────────────────────────────────────────────────────────────────
# HEURISTICS — cheap signals only. NOT a substitute for speaker judgment.
# The real intelligibility filter is applied by a collaborator, later.
# ─────────────────────────────────────────────────────────────────────────────

TURKISH_MARKERS = {
    "ve", "bir", "bu", "için", "ile", "olarak", "değil", "çok", "daha",
    "gibi", "sonra", "ama", "kadar", "her", "olan",
}
ENGLISH_MARKERS = {
    "the", "and", "of", "to", "in", "is", "that", "was", "here", "sorry",
    "cannot", "language", "translation", "note", "unfortunately",
}
REFUSAL_MARKERS = [
    "i cannot", "i can't", "i'm not able", "i am not able", "i don't have",
    "as an ai", "unfortunately", "i apologize", "üzgünüm", "yapamam",
]


def script_profile(text):
    """Proportion of letters by script family."""
    counts = Counter()
    for ch in text:
        if not ch.isalpha():
            continue
        try:
            name = unicodedata.name(ch)
        except ValueError:
            continue
        if "CYRILLIC" in name:
            counts["cyrillic"] += 1
        elif "ARMENIAN" in name:
            counts["armenian"] += 1
        elif "ARABIC" in name:
            counts["arabic"] += 1
        elif "LATIN" in name:
            counts["latin"] += 1
        else:
            counts["other"] += 1
    total = sum(counts.values())
    if total == 0:
        return {}, 0
    return {k: round(v / total, 3) for k, v in counts.items()}, total


def diagnostics(text, expect_script):
    """Flags for eyeballing, not verdicts."""
    lowered = text.lower()
    words = [w.strip(".,!?;:\"'()[]«»—–") for w in lowered.split()]
    words = [w for w in words if w]
    profile, letters = script_profile(text)

    turkish_hits = sum(1 for w in words if w in TURKISH_MARKERS)
    english_hits = sum(1 for w in words if w in ENGLISH_MARKERS)
    unique_ratio = round(len(set(words)) / len(words), 3) if words else 0.0

    flags = []
    if not words:
        flags.append("EMPTY")
    if any(m in lowered for m in REFUSAL_MARKERS):
        flags.append("REFUSAL_OR_HEDGE")
    if words and english_hits / len(words) > 0.15:
        flags.append("ENGLISH_LEAK")
    if words and turkish_hits / len(words) > 0.15:
        flags.append("TURKISH_LEAK")
    if unique_ratio < 0.5 and len(words) > 8:
        flags.append("REPETITIVE")
    if expect_script != "unknown" and profile:
        if profile.get(expect_script, 0) < 0.5:
            flags.append(f"SCRIPT_MISMATCH(expected {expect_script})")

    return {
        "n_words": len(words),
        "n_letters": letters,
        "script_profile": profile,
        "unique_word_ratio": unique_ratio,
        "turkish_marker_hits": turkish_hits,
        "english_marker_hits": english_hits,
        "flags": flags,
    }


def failure_flag(meta):
    """Name the reason a call produced nothing, when the reason was not the model.

    An empty output from a call that failed says nothing about the language:
    the request never reached the model. Only an empty output from a call
    that succeeded is a result about the model. Keeping the two apart is what
    makes the summary table honest.
    """
    if meta.get("ok"):
        return None
    err = str(meta.get("error") or "")
    if "429" in err or "RateLimitError" in err:
        return "NOT_RUN(rate_limited)"
    if "404" in err or "unavailable for free" in err or "NotFoundError" in err:
        return "NOT_RUN(model_unavailable)"
    # Runs made before call_model handled a response with no choices recorded
    # that case as a client-side TypeError. The model was reached and returned
    # nothing, so it is an empty output, not a failed call.
    if "NoneType" in err and "subscriptable" in err:
        return "EMPTY"
    return "NOT_RUN(error)"


def diagnose(text, meta, expect_script):
    """Diagnostics, with infrastructure failures kept out of the EMPTY flag."""
    d = diagnostics(text, expect_script)
    reason = failure_flag(meta)
    if reason:
        d["flags"] = [reason]
    return d


# ─────────────────────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────────────────────

def build_prompt(probe_key, lang_key):
    return PROBES[probe_key].format(lang=LANGUAGES[lang_key]["prompt_name"])


def call_model(client, model, prompt, temperature, max_tokens):
    """Returns (text, meta). Never raises — a failure is itself a result."""
    started = time.time()
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        # Providers sometimes return a response with no choices at all, or a
        # choice whose message/content is null — a filtered, truncated, or
        # empty generation. That is a result about the model, not a crash.
        choices = getattr(resp, "choices", None) or []
        if not choices:
            finish = None
            text = ""
            note = "no choices returned"
        else:
            choice = choices[0]
            finish = getattr(choice, "finish_reason", None)
            message = getattr(choice, "message", None)
            content = getattr(message, "content", None) if message else None
            text = (content or "").strip()
            note = None if content else "null content"
        meta = {
            "ok": True,
            "error": None,
            "note": note,
            "finish_reason": finish,
            "latency_s": round(time.time() - started, 2),
            "response_id": getattr(resp, "id", None),
            "reported_model": getattr(resp, "model", None),
        }
        return text, meta
    except Exception as exc:
        return "", {
            "ok": False,
            "error": f"{type(exc).__name__}: {exc}",
            "note": None,
            "finish_reason": None,
            "latency_s": round(time.time() - started, 2),
            "response_id": None,
            "reported_model": None,
        }


def call_with_retry(client, model, prompt, temperature, max_tokens, attempts=3):
    """Retry transient rate limits. A delisted model fails instantly, so
    only 429s and server errors are worth waiting for."""
    delay = 8
    for attempt in range(1, attempts + 1):
        text, meta = call_model(client, model, prompt, temperature, max_tokens)
        if meta["ok"]:
            meta["attempts"] = attempt
            return text, meta
        err = str(meta["error"])
        transient = ("RateLimitError" in err or "429" in err
                     or "500" in err or "502" in err or "503" in err
                     or "Timeout" in err or "APIConnectionError" in err)
        if not transient or attempt == attempts:
            meta["attempts"] = attempt
            return text, meta
        print(f"      ↳ transient error, retrying in {delay}s "
              f"(attempt {attempt}/{attempts})")
        time.sleep(delay)
        delay *= 2
    return text, meta


def main():
    ap = argparse.ArgumentParser(description="Coverage probe for the human-model gap study")
    ap.add_argument("--dry-run", action="store_true", help="print prompts, make no calls")
    ap.add_argument("--preset", choices=list(PRESETS), default="paper",
                    help="paper = pinned snapshots (citable) · free = free tiers "
                         "(pipeline validation only) · local = Ollama")
    ap.add_argument("--models", nargs="+", default=None)
    ap.add_argument("--languages", nargs="+", default=list(LANGUAGES))
    ap.add_argument("--probes", nargs="+", default=list(PROBES))
    ap.add_argument("--samples", type=int, default=SAMPLES_PER_PROBE)
    ap.add_argument("--temperature", type=float, default=TEMPERATURE)
    ap.add_argument("--outdir", default="runs")
    args = ap.parse_args()

    preset = PRESETS[args.preset]
    if args.models is None:
        args.models = preset["models"]
    pause = preset["pause"]

    if not preset["paper_grade"]:
        print(f"\n  ⚠  preset '{args.preset}' — PIPELINE VALIDATION ONLY.")
        print("     Versions are not pinned. Do not use this run as study data.")
        print("     Every record is stamped paper_grade=false.\n")

    for key in args.languages:
        if key not in LANGUAGES:
            sys.exit(f"Unknown language key: {key}. Known: {', '.join(LANGUAGES)}")
    for key in args.probes:
        if key not in PROBES:
            sys.exit(f"Unknown probe key: {key}. Known: {', '.join(PROBES)}")

    def _slug(parts, all_label, cap=3):
        """Short, filesystem-safe label. Collapses long lists to a count."""
        if len(parts) > cap:
            return f"{all_label}{len(parts)}"
        cleaned = []
        for p in parts:
            # model slugs are provider/name:variant → keep the name only
            name = p.split("/")[-1].split(":")[0]
            name = "".join(c if c.isalnum() else "-" for c in name).strip("-")
            cleaned.append(name.lower())
        return "-".join(cleaned)

    lang_slug = ("all" if set(args.languages) == set(LANGUAGES)
                 else _slug(args.languages, "langs"))
    # Name the models only when they differ from the preset's own list,
    # otherwise the preset name already says which models ran.
    model_slug = ("" if args.models == preset["models"]
                  else "_" + _slug(args.models, "models", cap=2))

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    run_name = f"{lang_slug}_{args.preset}{model_slug}_{stamp}"
    outdir = Path(args.outdir) / run_name

    plan = [
        (m, lang, probe, i)
        for m in args.models
        for lang in args.languages
        for probe in args.probes
        for i in range(args.samples)
    ]
    print(f"Planned calls: {len(plan)}  →  {outdir}")

    if args.dry_run:
        for lang in args.languages:
            for probe in args.probes:
                print(f"\n── {lang} / {probe} " + "─" * 40)
                print(build_prompt(probe, lang))
        print(f"\n[dry run] {len(plan)} calls would be made. Nothing sent, nothing written.")
        return

    outdir.mkdir(parents=True, exist_ok=True)

    if preset["api_key_env"]:
        api_key = os.environ.get(preset["api_key_env"])
        if not api_key:
            sys.exit(f"Set {preset['api_key_env']} first:  "
                     f"export {preset['api_key_env']}=...")
    else:
        api_key = "not-needed"      # Ollama ignores it

    from openai import OpenAI
    client = OpenAI(base_url=preset["base_url"], api_key=api_key)

    records = []
    delisted = set()
    raw_path = outdir / "raw.jsonl"
    with raw_path.open("w", encoding="utf-8") as fh:
        for n, (model, lang, probe, idx) in enumerate(plan, 1):
            prompt = build_prompt(probe, lang)
            text, meta = call_with_retry(client, model, prompt, args.temperature, MAX_TOKENS)
            rec = {
                "run_id": run_name,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "preset": args.preset,
                "paper_grade": preset["paper_grade"],
                "base_url": preset["base_url"],
                "model_requested": model,
                "model_reported": meta["reported_model"],
                "language_key": lang,
                "language_label": LANGUAGES[lang]["label"],
                "probe": probe,
                "sample_index": idx,
                "temperature": args.temperature,
                "max_tokens": MAX_TOKENS,
                "prompt": prompt,
                "output": text,
                "meta": meta,
                "diagnostics": diagnose(text, meta, LANGUAGES[lang]["expect_script"]),
            }
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            records.append(rec)

            status = "ok " if meta["ok"] else "ERR"
            flags = ",".join(rec["diagnostics"]["flags"]) or "-"
            if meta.get("note"):
                flags += f"  ({meta['note']})"
            print(f"[{n:>3}/{len(plan)}] {status} {model:<34} {lang:<12} {probe:<16} {flags}")

            # A delisted :free slug fails every single call — say so once, early,
            # instead of letting the user watch 90 identical 404s scroll past.
            if not meta["ok"] and "unavailable for free" in str(meta["error"]):
                if model not in delisted:
                    delisted.add(model)
                    suggested = str(meta["error"]).split("use this slug instead: ")
                    hint = suggested[1].split("'")[0] if len(suggested) > 1 else "(see error)"
                    print(f"      ↳ '{model}' is no longer free. Paid slug: {hint}")
                    print("        Current free list: https://openrouter.ai/collections/free-models")
                    print("        Then re-run with --models <slug> ... , or try --preset smoke")

            time.sleep(pause)

    write_summary(outdir, records, args, preset)
    print(f"\nRaw:     {raw_path}")
    print(f"Summary: {outdir / 'summary.md'}")


def write_summary(outdir, records, args, preset):
    """Readable side-by-side output — this is what gets eyeballed and put on a slide."""
    lines = []
    lines.append(f"# Coverage probe — {records[0]['run_id']}\n")
    langs = ", ".join(sorted({r["language_label"] for r in records}))
    models = ", ".join(sorted({r["model_requested"] for r in records}))
    lines.append(f"**Languages:** {langs}  \n**Models:** {models}\n")
    lines.append(f"Temperature {args.temperature} · max_tokens {MAX_TOKENS} "
                 f"· {args.samples} sample(s) per cell · preset `{args.preset}`\n")
    if not preset["paper_grade"]:
        lines.append("> **Pipeline validation only.** Model versions are not pinned "
                     "on this preset. Not study data, not citable.\n")
    lines.append("Flags are crude heuristics, not judgments. "
                 "Real intelligibility is marked by a speaker, later.\n")

    lines.append("\n## At a glance\n")
    lines.append("| Model | Language | Probe | Words | Script | Flags |")
    lines.append("|---|---|---|---|---|---|")
    for r in records:
        if r["sample_index"] != 0:
            continue
        d = r["diagnostics"]
        script = ", ".join(f"{k} {v}" for k, v in sorted(
            d["script_profile"].items(), key=lambda kv: -kv[1])[:2]) or "—"
        lines.append(
            f"| {r['model_requested']} | {r['language_label']} | {r['probe']} "
            f"| {d['n_words']} | {script} | {', '.join(d['flags']) or '—'} |"
        )

    lines.append("\n## Raw output\n")
    for lang in dict.fromkeys(r["language_key"] for r in records):
        label = next(r["language_label"] for r in records if r["language_key"] == lang)
        lines.append(f"\n### {label}\n")
        for r in records:
            if r["language_key"] != lang:
                continue
            lines.append(f"**{r['model_requested']} · {r['probe']} · sample {r['sample_index']}**\n")
            if not r["meta"]["ok"]:
                lines.append(f"> _error: {r['meta']['error']}_\n")
            elif not r["output"]:
                lines.append("> _empty_\n")
            else:
                for para in r["output"].split("\n"):
                    lines.append(f"> {para}" if para.strip() else ">")
                lines.append("")
            flags = ", ".join(r["diagnostics"]["flags"]) or "none"
            lines.append(f"`flags: {flags}`\n")

    (outdir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
