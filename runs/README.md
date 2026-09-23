# Trial runs, 15 August 2026

Three runs made while building the generation pipeline, all on OpenRouter's free tier. Model versions were not pinned. **These are pipeline checks, not findings, and are not citable as results.**

| Run | Languages | Models | Calls | Answered | Empty | Rate-limited | Model removed |
|---|---|---|---|---|---|---|---|
| `coverage_20260815_060059` | Kurmanji | gemma-3-27b, llama-3.3-70b, qwen3-235b | 18 | 0 | 0 | 0 | 18 |
| `coverage_20260815_060620` | Kurmanji | gemma-4-31b, gemma-4-26b, nemotron-3-ultra | 18 | 10 | 2 | 6 | 0 |
| `all_free_20260815_062527` | all five | gemma-4-31b, gemma-4-26b, nemotron-3-ultra | 90 | 45 | 2 | 43 | 0 |
| **Total** | | | **126** | **55** | **4** | **49** | **18** |

The first run failed entirely because all three free models had been withdrawn shortly before. The second and third replaced them.

## Most empty cells are not the model

Of 71 calls that produced no text, **only 4 reached a model that returned nothing.** The other 67 never reached a model: 49 were refused by the provider's rate limit, 18 asked for a model that no longer existed. In particular, one model (`gemma-4-31b`) was rate-limited on every call in the full run, so its row says nothing about any language.

## What was changed for publication

The model outputs, prompts and parameters are unedited. Three things were changed:

1. **An account identifier was redacted.** Provider error messages included the OpenRouter user ID of the account that made the calls; it is replaced with `user_[redacted]`.
2. **The diagnostics were recomputed and the summaries regenerated.** The script that made these runs labelled a failed call `EMPTY`, the same as a model that answered with nothing. The current script labels failed calls `NOT_RUN(...)` with the reason. The `diagnostics` field of every record and each `summary.md` were regenerated from the unchanged outputs with that rule.
3. **Two responses were reclassified as empty.** In the second run, an earlier version of the script did not handle a response with no content and recorded it as a client-side `TypeError`. The model had been reached and returned nothing, so these two calls are counted as `EMPTY`.

## Reading the outputs

Two things to keep in mind:

- **Reasoning leaks.** Several outputs, especially from `nemotron-3-ultra`, consist mostly of the model's own reasoning in English before, or instead of, an answer in the language. The `SCRIPT_MISMATCH` flags on Adyghe and Kabardian come from this English text, not from Circassian written in the wrong script.
- **The Homshetsma prompt.** The prompt describes Homshetsma as "the Armenic variety spoken by the Hemshin". Output in Armenian script should be read with that description in mind.
