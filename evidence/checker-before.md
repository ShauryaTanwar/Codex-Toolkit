# Checker output before revision

**Scope:** Reviewed the flawed response against the original request and supplied JSON only. This is a static evidence review; no searches were executed.

**Requirement coverage**

- **Bachelor party / upcoming wedding — FAIL.** None of the supplied excerpts establishes a bachelor party. *We Faw Down* describes men deceiving their wives, not a groom celebrating an upcoming wedding.
- **Friends celebrating — UNVERIFIED.** Some excerpts describe groups or parties, but none establishes friends celebrating a forthcoming marriage.
- **Excessive drinking — PASS for *We Faw Down* only.** Its evidence explicitly says they “get roaring drunk.” This does not establish drinking for every result.
- **Wild fun and an uncontrolled night — UNVERIFIED as a complete match.** *We Faw Down* supports drunken escapades and a chaotic escape, but the excerpt does not establish the requested bachelor-party night.

**Findings**

- **High — Invented plot details and overstated fit.** In sentence 1, “a groom” and “upcoming wedding” have no support in `results[0].plot_evidence`. Calling it a “perfect” match conceals the missing central requirement. Reproduction: compare that sentence with the supplied excerpt.
- **High — Unsupported universal claim.** Sentence 2 says every movie meets every requirement. The supplied excerpts do not substantiate that claim. Missing evidence does not prove the full films lack those elements, but it prevents claiming verified matches.
- **High — Invalid score interpretation.** Sentence 3 converts `0.4204` into a personal enjoyment probability. The JSON explicitly states, “Scores are not probabilities.” No enjoyment calibration is supplied.
- **Medium — Unsupported verification claim.** Sentence 4 claims confirmation from two searches. Only one search-result object is supplied; a second search and its conclusions remain **UNVERIFIED**.

**Verdict:** **Incomplete.** The response invents central plot details, overstates requirement coverage, and misrepresents the score.
