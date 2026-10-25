# Release gates

Current verdict: NOT YET ADMITTED. Release candidate for version 0.1.0.
No tag, archive or DOI exists yet. Route: Zenodo GitHub integration.

Standard: [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html),
version 0.4 draft, read by the release auditors on October 25, 2026 UTC.
Presentation model: the predecessor covering-hitting-diversities.
Admission is a project-defined release decision, not peer review, a correctness
certificate, or proof of global novelty.

| Gate | Status | Disposition |
|---|---|---|
| P1: prior work and credit | PARTIAL | Three bounded scans (diversity terms, flow–cut terms, papers citing the anchor sources) found no earlier statement; novelty is not established. Credit for the upper bound, the flow–cut correspondence and the pair-demand bound is cited. See audit/PRIOR_WORK.md. |
| A1: claim and artifact consistency | PASS | README, abstract, introduction and metadata agree after the release audit at 36dbf07; dispositions in AUDIT_LEDGER.md. |
| R1: release and stewardship | PENDING | Reproducible build, verifier, manifest, correction policy and CFF in place; tag, archive, DOI and provider byte identity not yet done. |

## P1 rows

PASS: Bryant–Tupper credited for diversities, the flow–cut correspondence and
the O(log n) upper bound (with its random-tree input). PASS: the general
lower bound of order log n credited to the metric literature as noted by
Bryant–Tupper and Jozefiak–Shepherd. PASS: Gupta–Newman–Rabinovich–Sinclair
and Chakrabarti–Jaffe–Lee–Vincent cited as stated in OpenAI's #089 papers,
and marked as not read in the original. PARTIAL: bounded searches cannot
certify novelty of the result or of its certificate.

## A1 rows

PASS: principal result, flow–cut form and further results stated identically
on README, abstract, introduction and CITATION.cff, with their hypotheses.
PASS: limits stated everywhere: unit lengths, graphs not hypergraphs, exact
value open for d >= 3, novelty not established.
PASS: proof lane re-derived every result from definitions (process evidence,
not peer review). The pair-demand remark after Corollary 5 was added after
that audit, in the auditor's proposed wording.

## R1 rows

PASS: clean `git archive` build byte-identical to the committed PDF;
`make verify` passes; manifest covers every tracked file.
PASS: public correction and withdrawal policy; publication-safe CFF without
DOI or release date.
PENDING: private push, public visibility, Zenodo enablement, tag, GitHub
Release, archive and DOI verification, site listing.
