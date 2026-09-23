# Coverage probe

Do language models produce anything usable in an endangered language, and if so, in the right language and the right script?

This script asks a set of models to write short texts in Kirmanckî (Zazaki), Adyghe, Kabardian and Homshetsma, with Kurmanji as a better-resourced control. It records every call in full and attaches a few quick flags to make the output easy to read through.

It is a preliminary tool. It was built to check a generation pipeline and to see, before any study material existed, whether the languages differ in what models can do with them. It is part of the study *The Generations of Speakers and Models: Measuring the Human–Model Semantic Gap in Endangered Languages* (FEL XXX, 2026).

## What it is not

**The flags are not judgments.** `SCRIPT_MISMATCH`, `ENGLISH_LEAK`, `REPETITIVE` and the others are crude heuristics for reading output quickly. Whether a text is intelligible in the language can only be decided by a speaker of it.

**Free-tier runs are not data.** Free model variants are often quantised, their versions are not pinned, and the list of free models changes without notice. Runs on those presets are stamped `paper_grade: false` in every record and in the summary, so they cannot later be mistaken for study data.

## Install

```bash
pip install -r requirements.txt
export OPENROUTER_API_KEY=sk-or-...
```

Models are reached through [OpenRouter](https://openrouter.ai), which gives one interface to several providers. The key is read from the environment and never written to disk.

## Presets

| Preset | Purpose | `paper_grade` |
|---|---|---|
| `paper` | Pinned model versions from different providers and training regimes | `true` |
| `free` | Free tier — checking that the pipeline works | `false` |
| `smoke` | OpenRouter's `openrouter/free` router — you cannot know which model answered | `false` |
| `local` | Local models via [Ollama](https://ollama.com); versions are pinned and nothing leaves the machine | `false` |

Model identifiers change often. Check the `paper` list against [openrouter.ai/models](https://openrouter.ai/models) before running it; the script records the model that actually answered, not the one that was planned.

## Usage

```bash
python coverage_probe.py --dry-run                       # print the prompts, make no calls
python coverage_probe.py --preset free --languages kurmanji
python coverage_probe.py --preset free                   # all languages
python coverage_probe.py --preset local                  # needs `ollama serve`
python coverage_probe.py --preset paper
python coverage_probe.py --models <slug> <slug> --samples 3
```

Transient failures — rate limits, server errors — are retried with increasing waits. A model that has been removed fails at once and is reported with a pointer to the current free list.

## Output

Each run writes to `runs/<languages>_<preset>_<time>/`:

- **`raw.jsonl`** — one record per call: model requested and model reported, parameters, prompt, full output, latency, error if any, and the diagnostics.
- **`summary.md`** — a table of every call, then the outputs grouped by language.

### Flags

| Flag | Meaning |
|---|---|
| `NOT_RUN(rate_limited)` | The provider refused the call. Says nothing about the language. |
| `NOT_RUN(model_unavailable)` | The model has been removed. Says nothing about the language. |
| `NOT_RUN(error)` | Some other failure before the model answered. |
| `EMPTY` | The model was reached and returned nothing. |
| `SCRIPT_MISMATCH(expected …)` | Under half the letters are in the expected script. |
| `ENGLISH_LEAK`, `TURKISH_LEAK` | Frequent English or Turkish function words. |
| `REPETITIVE` | Few distinct words for the length. |
| `REFUSAL_OR_HEDGE` | Phrases typical of a refusal. |

The distinction between `NOT_RUN` and `EMPTY` matters. On free tiers most calls that return nothing were never answered at all; counting them as the model's failure would misreport the languages.

## Design notes

**A control language.** Kurmanji is better resourced than the others. If a model fails there too, the problem is the setup, not the language.

**The probes are not study material.** The three prompts here are generic. The openings used in the study are kept unpublished until models have been run on them, so that a model's output cannot come from having seen them.

**Two samples per item.** One sample may be luck. The difference between two shows whether the output is stable or noise.

**The prompt shapes the output.** Each language is named to the model in the prompt, and how it is named can steer what comes back — including the script. Languages are named as their speakers name them, without classification, and the prompts are recorded in full with every run so that any such effect can be traced.

The runs from August 2026 in `runs/` were made with an earlier prompt that named Homshetsma by a linguistic classification. Script choices in those outputs should be read with that in mind.

## The runs in this repository

`runs/` holds three trial runs from 15 August 2026, all on the free tier. They are pipeline checks, not findings. See [`runs/README.md`](runs/README.md) for what they contain and how they were prepared for publication.

## Licence

GPL-3.0-or-later. See [`LICENSE`](LICENSE).

## Citation

See [`CITATION.cff`](CITATION.cff).
