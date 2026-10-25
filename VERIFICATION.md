# Draft verification record

Date: 2026-10-25. Pre-release draft. Not admitted, not peer reviewed.

## Environment and bounds

Every Python workload used `~/.venvs/claude/bin/python`.
Its recorded prefix is `~/.venvs/claude`; the base prefix is
`/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9`.
The prefix inequality passed. All new checker, inventory and build scripts
use only the standard library; no optimization solver or package install
was run. No system Python workload was run.

The exact-check size estimate was 21,992 induced vertex subsets, 10,968
nontrivial cut representatives and 21,964 nonempty terminal sets across the
28 saved instances, plus 16 and 4,096 induced subsets for the two newly
constructed diamonds. No graph above twelve vertices was enumerated. The
higher-depth check evaluates a rational formula only.

## Exact verification

Command, from the repository root:

```sh
~/.venvs/claude/bin/python scripts/run_job.py --cpu 90 --wall 120 verify-final -- ~/.venvs/claude/bin/python scripts/verify.py
```

Child PID 18627 exited 0. Recorded child CPU: 0.766621 seconds; runner wall:
1.017031 seconds; maximum resident memory: 12,951,552 bytes. No kill occurred;
the child PID was absent after wait. The checker itself measured 0.663003
CPU seconds and 0.664177 wall seconds. Differences are interpreter startup
and runner overhead. Machine-local raw logs are under ignored
`build/jobs/verify-final/`; this output is preserved here:

```text
SIZE saved certificates: 28 instances; 21992 induced subsets; 10968 cut representatives; 21964 nonempty terminal sets; <=32 MiB, <30 seconds expected.
SIZE diamond d=1: vertices=4, induced subsets=16, cuts=8 (including empty representative)
PASS diamond d=1: all cuts, exact costs [3], objective=3/2
SIZE diamond d=2: vertices=12, induced subsets=4096, cuts=2048 (including empty representative)
PASS diamond d=2: all cuts, exact costs [6, 11], objective=17/8
PASS objective identity: d=1..12 (exact Fraction arithmetic)
PASS C10: c1=9/5
PASS C12: c1=11/6
PASS C4: c1=3/2
PASS C5: c1=8/5
PASS C6: c1=5/3
PASS C7: c1=12/7
PASS C8: c1=7/4
PASS K3: c1=4/3
PASS K4: c1=3/2
PASS K5: c1=8/5
PASS K6: c1=5/3
PASS K8: c1=7/4
PASS diamond2: c1=17/8
PASS fan5: c1=8/5
PASS fan8: c1=7/4
PASS grid2x3: c1=5/3
PASS grid2x4: c1=7/4
PASS grid2x5: c1=9/5
PASS grid2x6: c1=11/6
PASS grid3x3: c1=11/6
PASS grid3x4: c1=29/15
PASS path8: c1=1
PASS random2tree8-seed17: c1=4/3
PASS random2tree8-seed31: c1=14/11
PASS random2tree8-seed53: c1=26/19
PASS star8: c1=1
PASS wheel5: c1=5/3
PASS wheel8: c1=38/21
INFO manifest absent during draft bootstrap
PASS: 2 diamond constructions; 12 exact objective identities; 28 rational primal/dual certificates; no LP solves.
CPU 0.663003s; wall 0.664177s
```

The manifest was intentionally absent during this recorded bootstrap run.
The completed 90-file inventory subsequently passed the same verifier in
`verify-manifest`: child PID 19146, exit 0, 0.733024 CPU seconds,
0.760116 wall seconds, 13,078,528 bytes maximum resident memory, no kill,
and PID absent after wait. That run repeated all finite checks successfully.
The final inventory excludes only itself and documented build/cache/Git
files. No checks were skipped on
the mathematical certificates. Primal feasibility is tested on every
nonempty subset, dual feasibility on every nontrivial cut up to complement,
and the exact rational objectives agree. Empty-set constraints vanish.

## Reproducible PDF and visual inspection

Command:

```sh
~/.venvs/claude/bin/python scripts/run_job.py --cpu 120 --wall 180 paper-first -- ~/.venvs/claude/bin/python scripts/build_paper.py
```

Child PID 18314 exited 0, with 3.422175 child CPU seconds, 3.543352 wall
seconds and 24,944,640 bytes maximum resident memory. No kill occurred;
the child PID was absent after wait. Two clean two-pass builds produced
identical bytes. Both final TeX logs had no warnings, undefined controls,
overfull boxes or underfull boxes. The compiler and epoch are in BUILD.md.

PDF: 8 US Letter pages, 228,629 bytes.
SHA-256: `b9017df4e915e5f9dc1b93b5cab655c2d493820302b1a53d3c7826be429fe833`.

All eight pages were rendered with Poppler at 110 dpi and visually inspected.
The title and date are centered; equations and references are legible; no
text is clipped or overlapping. The diamond has four filled generation-one
vertices, eight hollow newer vertices and sixteen edges. The 28-value table
fits within the page with its weight conventions in the caption. Page
numbers and references are visible. Floats follow normal article placement,
including a table at the top of page six. This is a visual review, not a
new proof audit. The resulting PDF is the file whose bytes were compared.

## README rendering

The requested `gh api markdown` call succeeded after the sandbox's first
connection attempt failed. It rendered the README without creating a remote
or publishing a repository. A second rendering followed a spelling change
from a strict inequality to its equivalent integer upper bound, avoiding
HTML angle-bracket escaping. The named checker compares each expression as
well as the counts of `js-inline-math` and `js-display-math` elements.

Result: **23 inline and 2 display expressions**, each matching its source
expression; all **15 local link occurrences** resolve. The first checker
attempt exposed a whitespace-regex error in the new checker, corrected to
distinguish spaces/tabs from newlines. A later attempt correctly detected
the not-yet-created manifest link; it passed once the file inventory existed.
No README math was silently dropped or treated as code.

README SHA-256: `8e8452d5ba19e6e56edd31631e53bcd1cfcd4e5883039944de5adb97d5ea1b4c`.
Rendered HTML SHA-256: `f038bc2522cd2c9456faab530d9adbbd48114967c5f3b74027d427de2c128868`.
The HTML and machine-readable check record remain in ignored `build/`.

## Provenance and local repository

The original source manifest passes all 150 entries. All nine copied research
records and 57 JSON files match the source byte for byte, and LICENSE matches
the predecessor at `60d135dad75bd7d05e6a50f78a7b121f056874ff`. The predecessor
remains clean. The copied-file manifest has 66 entries. Hashes and the two
later scan logs' relation to the original manifest are explained in
`audit/EVIDENCE.md`.

Repo-local author identity is Jeff Kline with the requested GitHub noreply
address. The repository has no remote or tag. No admission record, release
metadata, archive action, push, site edit or email was created. The raw
copied scans retain earlier papers' bibliographic identifiers as required
by byte-for-byte preservation; no identifier is assigned to this draft.

Staged whitespace checking passes on all authored files. The complete
initial diff flags only inherited blank final lines in the unchanged
`ADJUDICATION.md`, `CERTIFICATE.md` and `PROOF.md` evidence copies. Those
bytes are deliberately preserved; no source evidence is reformatted to
silence the warnings. Unstaged whitespace checking passes.

## Limits and coordinator questions

The finite verifier is not a proof of the all-depth result. The authoritative
proof and review remain in the preserved research records. This draft task
did not redo the mathematics or run a new adversarial audit. The external
logarithmic upper bound and contextual metric results are cited dependencies,
not independently audited proofs. Novelty is unresolved after bounded scans.
CJLV and GNRS full texts were not read; BT2012 was checked bibliographically,
and no revised JS journal version was verified. The BT upper-bound source's
printed 2021 date and arXiv 2017 version date remain unexplained. The earlier
archive's live metadata could not be checked during bibliographic extraction.
All bibliography entries are supported by inspected saved sources or records;
these exposure limits are explicitly retained.

## Plain-language editing pass, 2026-10-25 (coordinating session)

The coordinating Claude session rewrote the README and edited the paper's
abstract, introduction, Section 4 prose, Section 5 and the AI-assistance
note for plain language. No theorem statement, proof, certificate or table
value changed. Two claims were corrected: OpenAI's problem #089 is not an
Erdős problem, and the GNRS tree-distortion statement is now attributed as
cited in the OpenAI treewidth paper (Section 1, reference [10], Theorem 5.6).
The README adds a verification-status table.

After the edits: `make paper` passed (two byte-identical clean builds; 7 US
Letter pages, 227,716 bytes, SHA-256
`4dad4d9e9b5371007fb20ab034930bb411a3f0edb6b4c04d84c13bf174158b77`).
Pages 1, 2, 5, 6 and 7 were rendered at 70 dpi and inspected; the title fits
on one centered line. `gh api markdown` plus `scripts/check_readme.py` passed:
56 inline and 2 display expressions render as math, 15 local links resolve.
The earlier hashes above describe the superseded draft.
