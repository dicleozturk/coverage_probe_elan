# Coverage probe — all_free_20260815_062527

**Languages:** Adyghe (West Circassian), Homshetsma (Hemshin), Kabardian (East Circassian), Kirmanckî (Zazaki), Kurmanji Kurdish [control]  
**Models:** google/gemma-4-26b-a4b-it:free, google/gemma-4-31b-it:free, nvidia/nemotron-3-ultra-550b-a55b:free

Temperature 1.0 · max_tokens 400 · 2 sample(s) per cell · preset `free`

> **Pipeline validation only.** Model versions are not pinned on this preset. Not study data, not citable.

Flags are crude heuristics, not judgments. Real intelligibility is marked by a speaker, later.


## At a glance

| Model | Language | Probe | Words | Script | Flags |
|---|---|---|---|---|---|
| google/gemma-4-31b-it:free | Kirmanckî (Zazaki) | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kirmanckî (Zazaki) | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kirmanckî (Zazaki) | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Adyghe (West Circassian) | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Adyghe (West Circassian) | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Adyghe (West Circassian) | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kabardian (East Circassian) | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kabardian (East Circassian) | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kabardian (East Circassian) | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Homshetsma (Hemshin) | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Homshetsma (Hemshin) | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Homshetsma (Hemshin) | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kurmanji Kurdish [control] | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kurmanji Kurdish [control] | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-31b-it:free | Kurmanji Kurdish [control] | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kirmanckî (Zazaki) | free_narrative | 215 | latin 1.0 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kirmanckî (Zazaki) | translation | 215 | latin 1.0 | REPETITIVE |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kirmanckî (Zazaki) | everyday_scene | 8 | latin 1.0 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Adyghe (West Circassian) | free_narrative | 157 | latin 0.747, cyrillic 0.253 | SCRIPT_MISMATCH(expected cyrillic) |
| nvidia/nemotron-3-ultra-550b-a55b:free | Adyghe (West Circassian) | translation | 165 | latin 0.762, cyrillic 0.238 | ENGLISH_LEAK, REPETITIVE, SCRIPT_MISMATCH(expected cyrillic) |
| nvidia/nemotron-3-ultra-550b-a55b:free | Adyghe (West Circassian) | everyday_scene | 168 | latin 0.829, cyrillic 0.171 | SCRIPT_MISMATCH(expected cyrillic) |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kabardian (East Circassian) | free_narrative | 8 | cyrillic 0.975, latin 0.025 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kabardian (East Circassian) | translation | 0 | — | EMPTY |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kabardian (East Circassian) | everyday_scene | 9 | cyrillic 1.0 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Homshetsma (Hemshin) | free_narrative | 209 | latin 0.705, armenian 0.28 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Homshetsma (Hemshin) | translation | 0 | — | EMPTY |
| nvidia/nemotron-3-ultra-550b-a55b:free | Homshetsma (Hemshin) | everyday_scene | 240 | latin 0.859, armenian 0.138 | REPETITIVE |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kurmanji Kurdish [control] | free_narrative | 42 | latin 1.0 | — |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kurmanji Kurdish [control] | translation | 222 | latin 1.0 | REPETITIVE |
| nvidia/nemotron-3-ultra-550b-a55b:free | Kurmanji Kurdish [control] | everyday_scene | 18 | latin 1.0 | — |
| google/gemma-4-26b-a4b-it:free | Kirmanckî (Zazaki) | free_narrative | 31 | latin 1.0 | REPETITIVE |
| google/gemma-4-26b-a4b-it:free | Kirmanckî (Zazaki) | translation | 11 | latin 1.0 | — |
| google/gemma-4-26b-a4b-it:free | Kirmanckî (Zazaki) | everyday_scene | 13 | latin 1.0 | — |
| google/gemma-4-26b-a4b-it:free | Adyghe (West Circassian) | free_narrative | 13 | cyrillic 0.955, latin 0.045 | — |
| google/gemma-4-26b-a4b-it:free | Adyghe (West Circassian) | translation | 5 | cyrillic 0.911, latin 0.089 | — |
| google/gemma-4-26b-a4b-it:free | Adyghe (West Circassian) | everyday_scene | 9 | cyrillic 0.988, latin 0.012 | — |
| google/gemma-4-26b-a4b-it:free | Kabardian (East Circassian) | free_narrative | 19 | cyrillic 0.956, latin 0.044 | — |
| google/gemma-4-26b-a4b-it:free | Kabardian (East Circassian) | translation | 7 | cyrillic 0.958, latin 0.042 | — |
| google/gemma-4-26b-a4b-it:free | Kabardian (East Circassian) | everyday_scene | 9 | cyrillic 0.975, latin 0.025 | — |
| google/gemma-4-26b-a4b-it:free | Homshetsma (Hemshin) | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-26b-a4b-it:free | Homshetsma (Hemshin) | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-26b-a4b-it:free | Homshetsma (Hemshin) | everyday_scene | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-26b-a4b-it:free | Kurmanji Kurdish [control] | free_narrative | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-26b-a4b-it:free | Kurmanji Kurdish [control] | translation | 0 | — | NOT_RUN(rate_limited) |
| google/gemma-4-26b-a4b-it:free | Kurmanji Kurdish [control] | everyday_scene | 0 | — | NOT_RUN(rate_limited) |

## Raw output


### Kirmanckî (Zazaki)

**google/gemma-4-31b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 0**

> The user wants 3-4 sentences in Kirmanckî (Zazaki) telling a short story about someone walking to a village. Must output only in that language, no translation, no explanation, no English. No formatting. Must be 3-4 sentences. Need to produce plausible Zazaki sentences. I need to know Zazaki language basics. Zazaki (Kirmancki) is an Iranian language spoken in eastern Turkey. Some sample sentences: "Ez diçim gund." (I go to village). But need story: someone walking to a village. Could be "Mirov diçin gundê, di binav reva." Not sure. Let's craft 4 sentences.
>
> We need to ensure it's in Zazaki script (Latin). Use typical Zazaki orthography: "Ez" for I, "tu" for you, "ew" for he/she. Verbs: "çe" go, "çû" went. Past tense: "çû". "gund" village. "ser" road. "pişt" behind? Let's search memory: Zazaki grammar: present: "Ez diçim" (I go). Past: "Ez çûm" (I went). "gund" village. "rê" way. "ser" on. "bi" with. "kî" who. But we can produce plausible sentences.
>
> We need 3-4 sentences. Let's produce 4 sentences:
>
> 1. "Mirovek çû gundê." (A person went to the village.)
> 2. "Rêya tirsî bû, lê ew bi hêvî hate." (The road was hard, but he/she came with hope.)
> 3. "Di binav reva de, ew çavkanî kir." (In the middle of the road, he/she rested.)
> 4. "Dawî, ew gundî d

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 1**

> The user wants 3-4 sentences in Kirmanckî (Zazaki), a short story about someone walking to a village. Must output only in that language, no translation, no explanation, no English. No formatting. Provide just the sentences. Need to ensure correct Zazaki. I know some Zazaki basics: "Ez" = I, "tu" = you, "ew" = he/she/it, "ma" = we, "hûn" = you (plural), "wan" = they. Verbs: "çûn" = to go, "çû" = went? Actually Zazaki has past tense: "çû" maybe. "gira" = village? Actually "gira" is village? In Zazaki, "gira" means village? Let's check: In Zazaki, "gira" maybe "village". Could use "gira" or "köy". "dî" = to? Not sure. But we can produce plausible sentences: "Ez çûm gira." Not sure. Let's approximate: "Ez diçum gira." Actually present continuous: "Ez diçim gira." Past: "Ez çû gira." Then "Rojê min bi xwe re hat." Hmm.
>
> Better: "Ez çû gira." (I went to the village.) "Roj bi sor hat." Not sure.
>
> But we need 3-4 sentences. Could do: "Ez çû gira. Rojê min bi xwe re hat. Diroka min bi harî bû. Niha ez li gira dim." But need correct grammar.
>
> Given the instruction not to provide translation, but we must produce something plausible. It's okay if not perfect. Provide 3-4 sentences.
>
> Let's produce 4 sentences:
>
> "Ez çû gira. Rojê min bi xwe re hat. Diroka min bi harî bû

`flags: REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 0**

> The user wants a translation into Kirmanckî (Zazaki) of the sentence: "The water was cold and the children did not want to go in."
> I need to provide only the translation.
>
> Vocabulary check:
> - Water: aw / av (depending on dialect, 'aw' is common in Kirmanckî)
> - Was: hat / bû (past tense of 'to be' -> bûye/hatî, but for 3rd person singular past 'it was' -> 'hate' or 'bû')
> - Cold: sar / sard
> - And: û / î
> - Children: çave / kır / zarok (zarok is more Kurmanji, 'çave' or 'kır' or 'çavek' is Zazaki. 'Çave' usually means child/children. 'Kır' can mean boys/sons. 'Mırık' is another word. Let's use 'çave' or 'zarok' if borrowed, but standard Zazaki: 'çave' (plural 'çaven' or just 'çave').
> - Not: ne / na
> - Want: xwestin / vastin
> - To go: şoştin / roştin
> - In: nê / nav / de
>
> Structure:
> "The water was cold" -> Aw sard hate/bû.
> "The children did not want to go in" -> Çave nexwastine/navastine nê şoşin/roşin.
>
> Dialect variations (Northern vs Southern Zazaki):
> Northern (Kirmanckî proper):
> - Water: Aw
> - Was: hate / bû
> - Cold: sard / sar
> - Children: Çave (or Mırık)
> - Did not want: Nexwastiye / Navastiye (3rd pl past)
> - Go in: Nê şoşin / Nav

`flags: REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 1**

> The user wants a translation into Kirmanckî (Zazaki) of the sentence: "The water was cold and the children did not want to go in."
> I need to provide only the translation.
>
> Zazaki dialects vary (Northern vs Southern). I will provide a standard Northern Zazaki (Kirmanckî) version, as "Kirmanckî" usually refers to the Northern dialect group.
>
> Vocabulary:
> - The water: Â (or O) + definite article usually implied or 'a' -> "A" / "Â"
> - Was: hat / bû (past stem of 'to be' is often 'bû' or just past copula). In past tense narrative, often "bû" or "hat".
> - Cold: sard / xunuk (sard is common).
> - And: û / u.
> - The children: Mirovçik / Kurk / Çavgan. "Mirovçik" or "Kurk" (plural of kur). Let's use "Kurk" or "Mirovçik".
> - Did not want: ne hatine / ne xwestine / ne xwest. Verb "to want" is xwestin / xwestin. Past negative: nexwest.
> - To go in: derve hatin / naverê çûn / naverê hatin. "To enter" is "naverê çûn" or "derve hatin" (came inside). "Go in" implies movement into water. "Naverî çûn" or "derve hatin".
>
> Structure:
> "Â sard bû û kurk nexwestine derve bin/çûn."
>
> Let's refine.
> "Â sard bû" (The water was cold).
> "û" (and).
> "kurk" (children).
> "nexwestin" (they didn't want - 3rd pl

`flags: ENGLISH_LEAK, REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 0**

> Misafirên hate malê. Mase hîn ne amade ye.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 1**

> Mihmanan gatiye xanê. Mase wêdî na hazire. Hîn destar neşewitandiye.

`flags: none`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 0**

> Zeyna hîna kurena de wêne kurena. O, qetê deya de şîna kurena de herê. De de kurena de, o seê de vênena de. O, de kurena de deşonê amayê de dışê.

`flags: REPETITIVE`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 1**

> Arda ra rasta melawe de çêna. Bi kış u bi kevî de deşê de de çêna. Ore kurey de kîno deşê de kurey de çêna. Qeyle mela de kurey de çêna.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 0**

> Awa de sığ ce, çocukê de nêv de amey de nêwayê.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 1**

> Awa dıraz de bırê de, ey deçê de lîçî de kânî de sênê de.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 0**

> Miyânê ey kışeyê, seyê xanê de. Sewê doreyê xanê de tadê nêfê de.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 1**

> Mihmanê qedem ay de çênuonê. Sofra wunê de de amayê, dıma nê amayê.

`flags: none`


### Adyghe (West Circassian)

**google/gemma-4-31b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 0**

> The user wants 3-4 sentences in Adyghe (West Circassian) telling a short story about someone walking to a village. Must be only in Adyghe, no translation, no explanation, no English. No markdown. So plain text. Need to produce correct Adyghe sentences. I must ensure it's Adyghe language. I know some basics: Adyghe (West Circassian) uses Cyrillic script. Example: "Кӏалэр къэшхыны хэку" etc. But need a short story: someone walking to a village. Could write: "Лӏыжьыр къэшхыны къэуаплъэу, ахъщэ къэзэплъыу." But need 3-4 sentences. Use proper grammar. Let's craft:
>
> Sentence 1: "Кӏалэр мафэ пшъашъэу къэшхыны." (The boy walks along the road.) Actually "Кӏалэр" = boy, "мафэ" = road, "пшъашъэу" = along, "къэшхыны" = walks.
>
> Sentence 2: "Хэку аул къыритыгъэу къэуаплъэу." (He reaches the village soon.) Not sure.
>
> Better to use known vocabulary: "аул" = village, "къыритыгъэу" = towards, "къэуаплъэу" = arrives.
>
> Sentence 3: "Ахъщэ къэзэплъыу, лӏыжьыкӏэ къэуаплъэу." (The sun sets, the traveler arrives.)
>
> But need 3-4 sentences. Let

`flags: SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 1**

> The user wants 3-4 sentences in Adyghe (West Circassian), a short story about someone walking to a village. Only Adyghe, no translation, no explanation, no English. No formatting unless asked. So just plain text in Adyghe. Need to produce correct Adyghe sentences. I must ensure it's West Circassian (Adyghe). I can write something like: "КІалэ унэм къысэу къыуагъэ." But need 3-4 sentences. Let's craft:
>
> Sentence 1: "КІалэ унэм къысэу къыуагъэ." (The boy walked along the road.)
> Sentence 2: "Уапэ къыуагъэп, афэ уапэ къысхьыгъэ." (He reached the village, the sun was setting.)
> Sentence 3: "КІалэ ахъщэ къыуагъэ, гъуашъэ къыуагъэ." (The boy entered the house, the fire was burning.)
> Sentence 4: "Уи унэм къыуагъэ, къысэу къыуагъэ." (He sat on the road, walking.)
>
> But need proper grammar. I'm not fluent. But produce plausible Adyghe. Ensure only Adyghe text. No English. No punctuation? Use periods. Provide 3-4 sentences. Let's produce 4 sentences.
>
> I'll output:
>
> КІалэ унэм къысэу къыуагъэ. Уапэ къыуагъэп, афэ уапэ къысхьыгъэ. КІалэ ахъщэ къыу

`flags: SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 0**

> The user wants a translation of "The water was cold and the children did not want to go in" into Adyghe (West Circassian), with only the translation provided.
>
> Let me break down the sentence:
> - "The water" - псы (psə)
> - "was cold" - гъэщхыщт (ǵăščxəšt) or гъэщхыгъэ (ǵăščxəǵă) - past tense of "to be cold"
> - "and" - и (i)
> - "the children" - пшъашъэхэр (pš̂aš̂axăr)
> - "did not want" - мыущынукъым (məwščənəqəm) or similar negative past of "to want"
> - "to go in" - ичъэн (ič̣ən) or еджэн (edžan) - "to enter"
>
> In Adyghe:
> - Water = псы (psə)
> - Cold = гъэщх (ǵăščx)
> - Past tense suffix = -щт (-št) or -гъэ (-ǵă)
> - Children = пшъашъэхэр (pš̂aš̂axăr) - plural with -хэр
> - Not want = мыущынукъым (məwščənəqəm) - negative past
> - To enter/go in = ичъэн (ič̣ən) or еджэн (edžan)
>
> Putting it together:
> "Псы гъэщхыщт и пшъашъэхэр мыущынукъым ичъэн" or similar.
>
> Let me use a more standard orthography:
> Псы гъэщхыщт, пшъ

`flags: ENGLISH_LEAK, REPETITIVE, SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 1**

> The user wants a translation of "The water was cold and the children did not want to go in" into Adyghe (West Circassian).
>
> Vocabulary:
> - Water: псы (psə)
> - Cold: гъэплъ (ğapł) or чъыгъу (čəğu) - "cold" usually гъэплъ for weather/water temperature.
> - Was: -агъ (-aːʁ) past tense suffix.
> - And: сэ (sa) or just juxtaposition/converbs.
> - Children: унэм (wənam) - plural of унэ (wəna).
> - Want: фэс (fas) - "to want", often used with masdar or infinitive.
> - Not: еплъ (japł) - prefix/suffix for negation.
> - Go in / Enter: лъэон (ɬaːwan) or лъэужьын (ɬawʑən) - "to enter". лъэон is generic "go in".
>
> Structure:
> "The water was cold" -> Псы гъэплъагъ (Psə ğapłaːʁ).
> "The children did not want to go in" -> Унэм лъэон фэсеплъагъ (Wənam ɬaːwan fasaːplaːʁ) or Унэм лъэужьын фэсеплъагъ.
>
> Grammar check:
> - Subject: Псы (Absolutive).
> - Adjective predicate: гъэплъ-агъ (cold-PST).
> - Conjunction: сэ (and).
> - Subject: Унэм (Absolutive plural).
> - Verb complex: лъэон (masdar "to enter") фэс-еп

`flags: SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 0**

> The user wants 2-3 sentences in Adyghe (West Circassian) describing guests arriving at a house where the table isn't ready. Must output only Adyghe text, no translations or English.
>
> I need to write proper Adyghe sentences. Adyghe is a Northwest Caucasian language. Let me recall basic vocabulary:
> - guests: хэтх (hetskh) or ахъщэ (axshe) maybe? Actually "guests" is often хэтхэ (hetskhe) or more properly хьэтх (hetskh). Wait, let me think: "guest" is хьэтх (hetskh), plural хьэтхэхэр (hetskhakhir).
> - arrive: кӏуагъ (kwag) - came/arrived
> - house: унэ (une)
> - table: пшашэ (pshashe) or maybe шхын (shkhin)? Actually "table" is пшашэ (pshashe).
> - ready: хэтх (hetskh) no... "ready" is лъэпкӏэ (lhepk'e) or maybe фэд (fed)? Better: "not ready" - мэпкӏэ (mepk'e) or мэфэд (mefed).
> - not yet: зыгу (zigu) or зыгурэ (zigurre).
>
> Let me construct:
> Sentence 1: Guests arrived at the house.
> Хьэтхэхэр унэ кӏуагъ. (Hetskhakhir une kwag.)
>
> Sentence 2: The table is not ready yet.
> Пшашэ зыгу мэпкӏэ. (Pshashe zigu mepk'e.)
>
> Sentence 3: They are waiting. (optional)
> Ахэм эплъын.

`flags: SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 1**

> The user wants 2-3 sentences in Adyghe (West Circassian) describing guests arriving at a house where the table isn't ready yet. Must output only Adyghe text, no translation/explanation/English. Need to ensure correct Adyghe orthography (likely Cyrillic-based). I should produce something like: "Хэтищыгъэу къефэу сыкӏуагъэп, абор щыгъэрыплъыкӏэп." But need to be accurate. Let's think of typical vocabulary: guests = хэтщыгъэ (or хэтщыгъэу?), house = унэ, table = абор (or шъхьэплъы?), ready = щыгъэрыплъыкӏэ (maybe). But I'm not fluent. However produce plausible sentences. Must be 2-3 sentences. No extra punctuation beyond sentences. Provide only Adyghe. Let's craft:
>
> "Хэтщыгъэу унэхэм къефэу сыкӏуагъэп, абор щыгъэрыплъыкӏэп. Хэтщыгъэхэр мафэу шъхьэплъыкӏэу къысфэпхыгъэп."
>
> But need correct grammar. Maybe simpler: "Хэтщыгъэу унэ къефэу сыкӏуагъэп, абор щыгъэрыплъыкӏэп. Хэтщыгъэхэр мафэу шъхьэплъыкӏэу къысфэпхыгъэ

`flags: SCRIPT_MISMATCH(expected cyrillic)`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 0**

> Ашъхьэ пшэъ пэшхъэм къэкIуагъ. Сэбэр къызхъыгъ. УджкIэ къышъыгъ, уджкIэ къышъыгъ. Тхьэм шъэпIэ къыщэтыгъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 1**

> Адыгэм и къабэ къыхьыгъ. Пшъашъэ шэшэпхъэ ешэшэгъ. Тхьэшъхьэ къэшъэжъэ къыхьыгъ. Нагъэ къыхьыгъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 0**

> ШIышъэкIэ къызэшъэ, уншIэнахэм шIышъэ къышхъэпсышъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 1**

> ЩыIэщ къэшхъуагъэ, нэпкъе къышIэшъэ пщэшъэгъэ шъэпIэкӏэ къэшIэшъэгъэ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 0**

> КъегъэIу къалъэшхэр псалъэӏо къэдэкӏуэ; къэӏэшхэр къанэӏэ, икъогъэшэм къашъэшъэм къыщэфышъэщ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 1**

> ЩIыбзэ къыпшIэщ, унэщIэшъ къыгъэшъ. Пэшхъэбзэшъхьэ къышIэщ, сышIэшъ къышIэу къышIэу къышIэшъ.

`flags: none`


### Kabardian (East Circassian)

**google/gemma-4-31b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 0**

> Ар аул къэсхьэ. Ыхъухьэп къэсхьэ. Ар аул еплъыкIэ.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 1**

> Ар псэлъэгъу ахьыщ, къэлэмыщтхьэм еплъын. Лъэпкъым икӏуагъэ, псэухьыгъэхьын. Нэхьыжьыгъэхьын, аул иплъын.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 0**

> _empty_

`flags: EMPTY`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 1**

> The user wants a translation of "The water was cold and the children did not want to go in" into Kabardian (East Circassian).
> I need to provide only the translation.
>
> Kabardian vocabulary:
> - water: псы (psə)
> - cold: гъэшъэ (ǵaš̂a) or къыбыгъэ (qəbəǵa) - "cold" (to touch/feel). гъэшъэ is more general for temperature.
> - children: уажэхэр (waža-xər) or ӏуажэхэр (ʾwaža-xər)
> - to want: фэдун (fadwn) / сэдун (sadwn) - usually "сэфэдун" (I want) but structure is "X wants Y" -> Y X-е сэфэдун.
> - to go in / enter: егъэын (jaʁajan) or илъэын (jəɬajan) - "to enter inside". илъэын is good for "go in (water)".
> - past tense: usually suffix -гъа (-ʁaː) or -щ (-ɕ) for recent past / witnessed. Narrative past often uses -гъа.
> - and: ы (ə) or сэ (sa) / сыу (səw).
>
> Sentence structure:
> "The water was cold" -> Псы гъэшъэп (Psə ǵaš̂ap) - "The water is cold" (present) or Псы гъэшъэпгъа (Psə ǵaš̂apʁaː) - "The water was cold".
> "the children did not want to go in" -> Уа

`flags: ENGLISH_LEAK, SCRIPT_MISMATCH(expected cyrillic)`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 0**

> Хъыбзэхэр пшъашъэ къэзчэу, ахшэ къэкӀуагъэх.  
> Ахшэ къэкӀуагъэх, шъуаплъэ къэзчэу.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 1**

> Шхы хэ къеплъыжьы, кӀалэ уишх. Уишх кӀалэ, шхы иплъыжьы. Хэ уишх кӀалэ, шхы къеплъыжьы.

`flags: REPETITIVE`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 0**

> Адыгэ лъэпкъэ унэр пщэӏэу къэшъэӏыгъ. Унэр къалъэзэ унэр шIытхъэкIэ лъэӏу къэбгъэӏыгъ. УнэмкIэ къещэӏэгъэ лъэӏу шIышъэӏэӏыгъ. УнэмкIэ къэӏэӏэгъэ унэр къышIыгъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 1**

> Ашъэм сыхъу къорхъэн къалъ къыхагъ. Узэшъэм лъагъэ къыщыкIуагъ. Пшъэшъэм унагъэ къыкIуагъ. Пэшъэшъэм къыхьыгъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 0**

> ЩIэ пэшъэшъубзэ хъышIущ ыуа, къалъэм сыгъэшъэ къещэгъэщ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · translation · sample 1**

> ЩIалъыгъэ къатIэ хъым къыгъэшъ, упсэущIэмэ къыщIэӶышъ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 0**

> Шъеӏэ къалъэжъыгъэ къалъэшъэбзъэ къыкIэуэнщ. Пщъэшъэ къыкIэуэнщ, фэщэ бгъэшъэбзэ къыӏэӏыгъэ.

`flags: none`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`


### Homshetsma (Hemshin)

**google/gemma-4-31b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 0**

> The user wants 3-4 sentences in Homshetsma (Western Armenian dialect of the Hemshin people), telling a short story about someone walking to a village. No translations, no explanations, no English. Must output only Homshetsma text.
>
> We need to produce plausible Homshetsma sentences. Homshetsma is a dialect of Western Armenian, with some differences. We can approximate using Western Armenian orthography. Provide 3-4 sentences. Ensure no English. Just the story.
>
> We must not include any extra commentary. Just the sentences.
>
> Let's craft:
>
> "Արդ եկաւ գիշերը, ուր նա làngիchte 워քwärts գնաց։ Նա ճանապարհին ծաղիկներ տեսաւ ու surround արուpuntenը bursting է։ Əљ اواخر նա գ Amor կը գնաց, ուրấy(queue) làngի կողմից accueille արուポイント է։"
>
> But need to keep it in Homshetsma, not mixing English. Use Armenian script. Provide 3-4 sentences.
>
> Better to write something like:
>
> "Գիշերը staan ARMEN. The user wants only Homshetsma. We'll produce something like:
>
> "Գիշերը երբ նա làngի գնաց, ճանապարհին ծաղիկներ տեսաւ։ Նա հաջողությամբ անցաւ լեռնանցքի միջոցով։ Στις վերջում làngի Astana迎接 արուետքները։"
>
> But need to keep it in Homshetsma orthography. Use typical Western Armenian: "Գիշերը, երբ նա làngը գնաց, ճանապարհին ծաղիկներ տեսաւ։ Նա հաջողությամբ անցաւ լեռնանցքը։ Լgangի extremity, նրան հնարավորություն տուեցին։"
>
> But we need 3-4 sentences.
>
> Let's produce 3 sentences:
>
> 1. "Գիշերը, երբ նա làngը գնաց, ճանապարհին ծաղիկներ տեսաւ։"
> 2.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 1**

> The user wants 3-4 sentences in Homshetsma (Western Armenian dialect spoken by Hemshin people) telling a short story about someone walking to a village. No translation, no explanation, no English. Just the Homshetsma text.
>
> I need to write in Homshetsma. This is a Western Armenian dialect. I'll write a simple 3-4 sentence story.
>
> Let me construct it:
> - Someone walking to a village
> - Simple vocabulary
> - 3-4 sentences
>
> In Western Armenian / Homshetsma orthography (using Armenian script):
>
> Քիսşikը գնում էր կyükին։ Թողը Բարտան էր։ Հայրենիքի հովին որոտ էր։ Նա արعة շուտով հասավ։
>
> Wait, let me make it more natural for Homshetsma specifically. Homshetsma has some distinct features. Let me write in Armenian script:
>
> Քիսիկը գնում էր գիւղին։ Ուճղը Պարտան էր։ Ավազը տղայ սրտը հով անում էր։ Ո՞ր قرբ.version։ Նա արագ կ՛հասնէր։
>
> Actually, let me write 4 clear sentences in Homshetsma using Armenian script:
>
> Քիսիկը կը գնայ գիւղին։ Ուճղը Պարտան էր։ Երեկոյան եղան սուր էր։ Նա արագ կը հասնէր։
>
> That's 4 sentences. Let me verify:
> 1. Քիսիկը կը գնայ գիւղին։ (The boy was walking to the village)
> 2. Ուճղը Պարտան էր։ (The road was Bartan - or "the road was muddy" - Պարտան can mean muddy)
> 3. Երեկոյան եղան սուր էր։ (The evening

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 0**

> _empty_

`flags: EMPTY`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 1**

> The user wants a translation into Homshetsma (Western Armenian dialect spoken by Hemshin people).
> The sentence is: "The water was cold and the children did not want to go in."
>
> Key vocabulary in Homshetsma/Western Armenian:
> - Water: Ջուր (Chur / Jur)
> - Was: էր (er) / էր (er) - past tense of "to be"
> - Cold: Սառնող (Sarnogh) / Ծուրտ (Tsurt) - "Sarnogh" is more common for water/weather in Western Armenian dialects.
> - And: եւ (yev) / ու (u)
> - The children: Երիկները (Yeriknere) / Մանուկները (Manuknere) - "Yerikner" is very common in dialects for children.
> - Did not want: Չէին կամեցել (Ch'ein kametsel) / Չէին ուզել (Ch'ein uzel) - "Gam/Ge" conjugation for past.
> - To go in: Մտնել (Mtnel) /urio (Shunel - dialect specific?) - Standard Western "Mtnel".
>
> Homshetsma specificities:
> - Often preserves Classical Armenian case endings more than standard Western Armenian.
> - Vocabulary: "Yerik" (child) is standard Western/dialectal. "Chur" for water.
> - "Cold": Ծուրտ (Tsurt) or Սառնող (Sarnogh).
> - Verb "to want": Գամ (Gam) / Ուզել (Uzel). In Hemshin dialect, "gam" is very common.
> - "To enter/go in": Մտնել (Mtnel).
>
> Structure:
> "The water was cold" -> Ջուրը սառնոգ էր (Churë sarnog er) / Ջուրը ծուրտ էր

`flags: ENGLISH_LEAK, REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 0**

> The user wants two or three sentences in Homshetsma describing guests arriving at a house where the table isn't ready yet. Must output only Homshetsma, no translation, no explanation, no English. No formatting. Provide 2-3 sentences. Need to know Homshetsma language. It's an Armenian dialect spoken by Hemshin people. I need to produce plausible sentences in that language. I must ensure it's in Homshetsma. I can approximate using known words: "Hamshetsma" maybe similar to Western Armenian? But it's a distinct dialect. However, we can produce something like: "Մեկնաբան 할머니..." But need to be in Homshetsma. I might not know exact orthography. But we can produce something plausible: "Հեթոները տուն եկան, բայց սեղանը դեռ պատրաստ չէ։" But that's standard Armenian. Homshetsma may have different vocabulary. But the user likely expects something in that dialect. However, we must output only Homshetsma. Could we produce something like: "Հետի տուն եկան, սեղանը դեռ պատրաստ չէ։" That's still Armenian. Might be acceptable. But they said "Homshetsma (the Armenic variety spoken by the Hemshin)". Could be similar to Western Armenian but with some differences. But we can produce a plausible sentence in that dialect.
>
> We must not include any English. Provide 2-3 sentences. No formatting. Let's produce three sentences.
>
> Potential Homshetsma: "Հետիները տուն եկան, բայց սեղանը դեռ պատրաստ չէ։ Ամենաշատը կուզեն ուտել, բայց սեղանը դեռ հարթակ չէ։ Շուտով պատրաստելու են։" But that's Armenian.
>
> Better to use Homshetsma orthography: maybe uses Latin script? Actually Homshetsma is often

`flags: REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 1**

> Հյուներ տունը գացին, բայց սեղանը_ARRAY պատրաստ չէր։ Գինին դեռ պատրաստում էր սուրճը և հացը, երբ դուռը ս rondինու զանգը луաց։

`flags: none`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`


### Kurmanji Kurdish [control]

**google/gemma-4-31b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-31b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Provider returned error', 'code': 429, 'metadata': {'raw': 'google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/settings/integrations', 'provider_name': 'Google AI Studio', 'is_byok': False, 'provider_error_code': '429', 'limit_source': 'upstream_provider_shared_pool', 'remedy_hint': 'Retry shortly, add your own provider key (https://openrouter.ai/settings/integrations), or route to another provider with provider routing: https://openrouter.ai/docs/features/provider-routing'}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 0**

> Azad di rojavê de bi rêya daristanan gihîşt gundekî xweş. Ew bi qasî di bin daran de çû, hevokên baştirî dît. Di dawiyê de, ew li ser çavkanî gundê ketî, bi xweşî û aramî. Gelên gundê wî bi têkiliyên germ pêşkêş kirin.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · free_narrative · sample 1**

> Yek êrîşî xwe bi şev re destpêkir, bi rêya dûr dişîye gundekî kevin. Rojnameya xwe li ser dûrî nîşan dide, heta ku ew di bin çavkaniyên şev de gundê dibîne. Bi xweşî ew li gundê digire, dengên xweş

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 0**

> The user wants a translation of the sentence "The water was cold and the children did not want to go in." into Kurmanji Kurdish.
> I need to provide only the translation.
>
> Vocabulary:
> - The water: Ava / Avê
> - was: bû / hat (bû is standard for "was" in past tense for states)
> - cold: sar / sard
> - and: û
> - the children: zarokên / mendalên (zarok is common)
> - did not want: naketin / nexwestin (nexwestin is standard for "did not want")
> - to go in:çeaw bikin / derkevin / war bikin / jê bikin. "Çeaw bûne" or "jê bûne" or "war bûne". "Go in" usually translates to "derkevin" (enter) or "jê bûne" (go into it). Since it's water, "jê bûne" or "çeaw bûne" works well. "War bûne" implies going down.
>
> Structure:
> "Av sar bû û zarokên nexwestin jê bin." (Subjunctive after nexwestin)
> Or past narrative: "Av sar bû û zarokên nexwest jê bikin." (Kurmanji often uses subjunctive for "wanted to do").
>
> Let's check standard grammar:
> "Av sard bû" or "Av sar bû". "Sard" is the adjective, "sar" is the root. "Av sard bû" is correct.
> "Zarokên" (plural definite).
> "Nexwest" (3rd person singular for plural inanimate? No, zarok is animate plural. Usually 3rd pl "nexwestin" or 3rd sg "nexwest" depending on dialect/standard. Standard written often uses plural verb for animate

`flags: REPETITIVE`

**nvidia/nemotron-3-ultra-550b-a55b:free · translation · sample 1**

> Av sarı bû û zarokên nexwestin werin binav.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 0**

> Miwan hatine malê, lê mase hîn nehatiye amadekirin.  
> Ew şopandin ku çavkaniyên xwe bigirin, lê mase firavî ye.

`flags: none`

**nvidia/nemotron-3-ultra-550b-a55b:free · everyday_scene · sample 1**

> Mêwan hatine mala, lê mase nehatiye amade kirin.  
> Ez dihewî de dikarim bibe.

`flags: none`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · free_narrative · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · translation · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · translation · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 0**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`

**google/gemma-4-26b-a4b-it:free · everyday_scene · sample 1**

> _error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '50', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1786838400000'}, 'limit_source': 'openrouter_free_tier_daily', 'remedy_hint': 'Wait for the daily reset (see X-RateLimit-Reset), or purchase credits to raise your free-model daily limit.', 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit exceeded: free-models-per-day. Add 10 credits to unlock 1000 free model requests per day'}]}}, 'user_id': 'user_[redacted]'}_

`flags: NOT_RUN(rate_limited)`
