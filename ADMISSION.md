# Release gates

Current verdict: ADMITTED with stated qualifications; P1 remains PARTIAL.
Admission date: October 25, 2026 UTC. Version 0.1.0.
Tag: v0.1.0 at c6ff76e3670b7444add0c9a6b16673be4f3e54e6 (annotated tag object e5f089c).
Version DOI: [10.5281/zenodo.23644875](https://doi.org/10.5281/zenodo.23644875).
Concept DOI: [10.5281/zenodo.23644874](https://doi.org/10.5281/zenodo.23644874).
Record: <https://zenodo.org/records/23644875>.

Standard: [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html),
version 0.4 draft, read by the release auditors on October 25, 2026 UTC.
Presentation model: the predecessor covering-hitting-diversities.
Admission is a project-defined release decision, not peer review, a correctness
certificate, or proof of global novelty.

| Gate | Status | Disposition |
|---|---|---|
| P1: prior work and credit | PARTIAL | Three bounded scans (diversity terms, flow–cut terms, papers citing the anchor sources) found no earlier statement; novelty is not established. Credit for the upper bound, the flow–cut correspondence and the pair-demand bound is cited. See audit/PRIOR_WORK.md. |
| A1: claim and artifact consistency | PASS | README, abstract, introduction and metadata agree after the release audit at 36dbf07; dispositions in AUDIT_LEDGER.md. |
| R1: release and stewardship | PASS | Tag, GitHub Release, resolving DOI, record metadata and exact provider byte identity verified; living metadata updated. |

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
PASS: public correction and withdrawal policy; publication-safe CFF at the tag.
PASS: private push, public visibility, Zenodo enablement (author action),
annotated tag and GitHub Release, each on the author's explicit authorization.
PASS: Zenodo record, resolving DOI and exact provider byte identity (below).
PASS: public-site listing live before this admitted metadata was pushed.

## Archive verification and execution boundary

Route: Zenodo GitHub integration. The author enabled the repository in the
Zenodo portal on October 25, 2026. After the tag was pushed and before the
GitHub Release was created, the GitHub API zipball for v0.1.0 was downloaded
twice; both copies were 374,897 bytes with SHA-256
`2d4b8b81d327e67a677451de3213aff5c911bdbc4aab97afa18b47faea0325ae`.
The release was published at 2026-10-25T15:34:56Z.

Zenodo record 23644875 is published and open: title "Planar Steiner
diversities need logarithmic L1 distortion", creator Kline, Jeff, version
v0.1.0, publication date 2026-10-25, license GPL-3.0, related identifier the
v0.1.0 tree (isSupplementTo). Its file
`jeff-kline/planar-steiner-diversities-log-distortion-v0.1.0.zip` is 374,897
bytes, provider checksum md5:d5d9173083954c30d19ef1e5924fb27d, and is
byte-identical (`cmp`) to the pinned zipball; local SHA-256 and MD5 match.
`https://doi.org/10.5281/zenodo.23644874` resolves to the record.

A secondary deterministic `git archive --format=zip` of the tag, generated
twice, has SHA-256
`eb0f01d38ea61651a734752c17c3f6dc600ae83506a146a5fba1740e0d880d5c`; it is a
different file from the provider zipball and is not claimed to equal it.

Residual: the Zenodo resource type was imported as Software. The author may
change it to Publication / Preprint in the portal; that is a metadata edit
and does not change the DOI or the archived file.

The tag keeps its candidate wording (NOT YET ADMITTED). Living metadata in
README.md, CITATION.cff, paper/main.tex, paper/main.pdf, CORRECTIONS.md and
this file record the admission.

Site: <https://jeff-kline.github.io/#project-planar-steiner-diversities>,
site commit 7a43394, Pages deployment succeeded; the live HTML shows the
title, blurb, repository link and version DOI.
