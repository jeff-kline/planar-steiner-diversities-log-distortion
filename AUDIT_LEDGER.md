# Audit ledger

Pre-release draft. Not admitted, not peer reviewed.

## Research evidence inherited unchanged

The source `PROOF-AUDIT.md` records a fresh full audit of the second proof
version. `ADJUDICATION.md` accepts that argument and the audited scope of
`STRENGTHENING.md`. The earlier isolated examination was labelled NOT-BROKEN,
which does not itself verify a proof. The adopted alternative argument was
then reviewed in the full audit. These are AI-assisted research checks,
not peer review, independent human review, or proof-assistant certification.
The copied records retain their own claim-by-claim distinctions and limits.

`SMALL_CASES.md` and the saved JSON records describe 28 finite optimality
certificates. The new stdlib verifier independently reconstructs their
Steiner costs and verifies all rational inequalities; it does not rerun
optimization or prove the all-depth theorem.

## Draft preparation on 2026-10-25

The owner read the authoritative proof and strengthener, checked the
Bryant–Tupper packing and cut definitions against the saved primary source,
and transcribed the proof with explicit scope qualifications. One executor
extracted bibliographic information; all mathematical wording remained with
the owner. One of at most three authorized executor dispatches was used.
No new proof campaign, LP solve, or general prior-art search was run.

The three inherited scans are summarized in `audit/PRIOR_WORK.md`. Novelty
is unresolved. Source exposure is recorded in `audit/BIBLIOGRAPHY-EXTRACTION.md`.
`VERIFICATION.md` records the exact checker, reproducible build, README
rendering and page inspection. These checks establish only their stated
mechanical and editorial scope.

No release-gate audit, freeze, admission, external archive, remote, push, tag,
or public site operation was performed. Those decisions belong to the
coordinating session. This file is a provenance record, not a release verdict.

## Editing pass, 2026-10-25

The coordinating session made a plain-language pass over the README and the
paper's reader-facing prose (see VERIFICATION.md). Proofs and claims are
unchanged; A1 consistency and the proof transcription still need the
release audits before any candidate freeze.

## Release audit at 36dbf07, 2026-10-25 (two read-only AI lanes)

Lane 1, proof and parameters (frontier model): PASS. Every result re-derived
from definitions; Corollary 5 checked against Bryant–Tupper 2014 Section 5
(LP (11), Theorems 17–18). Lane 2, claims and prose: PARTIAL. Lane A,
citations: PARTIAL (optional items only). Lane B, reproducibility: PASS
(clean `git archive` build byte-identical; verifier and manifest pass).

| # | Finding | Class | Disposition |
|---|---|---|---|
| 1 | "AI review checked the full proof" overstated scope | documentation | fixed: source proofs, then full paper text including Cor. 5 |
| 2 | README pair-demand gap claim unsupported in paper | gap | fixed: remark after Cor. 5 citing GNRS Thm 3.2 via OAIplanar §1.1, and CJLV |
| 3 | README "shows" vs paper "suggests" (trees) | documentation | fixed: both say "shows", via the random-tree upper bound |
| 4 | JS credited with the general lower bound | documentation | fixed: BTopen notes it, JS repeat it |
| 5 | "sharp bound 2" credited to CJLV alone | documentation | fixed: "sharp" removed |
| 6 | README omits $d\ge1$ | missing hypothesis | fixed |
| 7 | "of the same shape" undefined | missing hypothesis | fixed: shape stated |
| 8 | "Equivalently" for flow–cut form | sharpening | fixed: "In flow–cut terms", "recasts its certificate" |
| 9 | README overstated checker scope | documentation | fixed |
| 10 | "settled"/"prove" rest on recent preprints | sharpening | fixed: "recent preprints ... prove"; abstract contrast uses diamonds (CJLV) |
| 11 | Title class reading | optional | kept (class-level worst case, as in #089 titles) |
| 12 | BT correspondence stated per diversity | sharpening | fixed: per hypergraph |
| 13 | "known only for d<=2" | documentation | fixed: "determined here only" |
| 14 | define distortion in README | optional | fixed |
| 15 | figure unreferenced; connectivity sentence; Thm 1 wording | documentation | fixed |
| 16 | public correction policy; private paths; CFF; FRT credit | documentation | fixed except CFF repository/date, set at freeze |
| A1 | README: GNRS/CJLV read second-hand | documentation | fixed |
| A2 | FRT input to BTopen Thm 2 uncredited | documentation | fixed: bibitem FRT (as cited in BTopen) |
| A3 | predecessor DOI missing | documentation | fixed: DOI resolves (HTTP 302) |
| A5 | OpenAI PDF links | documentation | fixed: both return HTTP 200 |
| B6 | private absolute paths in BUILD.md | documentation | fixed: `$HOME`; public scripts no longer require a venv |
| B7 | PLAN.md, AGENTS.md internal | optional | kept; referenced by audit records |

The remark after Corollary 5 uses the wording the auditor proposed; it was
added after the audit and has not had a separate review.
