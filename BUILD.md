# Build and verification

Pre-release draft. Not admitted, not peer reviewed.

The verifier and builder need only Python 3 and its standard library; no
solver or package installation is needed. The author runs them in an isolated
virtual environment (`$HOME/.venvs/claude/bin/python`). The maintainer scripts
`run_job.py`, `check_readme.py` and `draft_inventory.py` insist on a virtual
environment. `requirements.txt` records that there are no package dependencies.

The checked compiler is `/opt/local/bin/pdflatex`, pdfTeX 1.40.22
(TeX Live 2021/MacPorts 2021.58693_2). Required TeX packages: amsmath,
amssymb, amsthm, geometry, microtype, graphicx, tikz and hyperref. Fonts are
the installation's default Computer Modern. The figure is inline TikZ.
No shell escape or external bibliography tool is used.

From the repository root:

```sh
make paper PYTHON="$HOME/.venvs/claude/bin/python" PDFLATEX=/opt/local/bin/pdflatex
make verify PYTHON="$HOME/.venvs/claude/bin/python"
```

For tracked, resource-capped jobs, give each run a fresh name:

```sh
$HOME/.venvs/claude/bin/python scripts/run_job.py --cpu 120 --wall 180 paper-check -- $HOME/.venvs/claude/bin/python scripts/build_paper.py
$HOME/.venvs/claude/bin/python scripts/run_job.py --cpu 90 --wall 120 exact-check -- $HOME/.venvs/claude/bin/python scripts/verify.py
```

The runner records child PID, command, caps, exit status, child resource
usage and post-wait PID status under ignored `build/jobs/NAME/`. Its wall
time limit kills the process group. After any kill, check the recorded PID
is gone before continuing. Resource limits are ceilings, not measured usage.

The builder uses two clean temporary directories, running pdfLaTeX twice
in each. It fixes `SOURCE_DATE_EPOCH=1792886400` (2026-10-25 00:00 UTC),
`FORCE_SOURCE_DATE=1` and `TZ=UTC`. This is a reproducibility parameter, not
a publication date. It rejects final warnings, undefined references, and
both overfull and underfull boxes, requires identical PDF bytes, then writes
`paper/main.pdf` and ignored `build/main.log`. PDF identity is checked within
the recorded installation. Other TeX/font/package versions may change bytes
or pagination. Inspect any mismatch; do not rewrite the manifest to hide it.

The verifier independently builds depths one and two, checks every cut up
to complementation, computes Steiner costs by induced-set spanning-tree
enumeration followed by minimization over supersets, and checks the rational
objective. It checks the objective formula at depths one through twelve
without constructing those larger graphs. It recomputes Steiner costs on
all 28 saved graphs and checks every primal subset constraint and every
nontrivial dual cut, nonnegativity, normalization, and equal objectives.
No LP is solved. During initial bootstrap the manifest may be absent; a
completed draft must have a manifest and pass its complete file inventory.
Finite checks do not prove the infinite family, audit external theorems,
or establish novelty.

For visual inspection with Poppler:

```sh
mkdir -p build/pages
pdftoppm -r 110 -png paper/main.pdf build/pages/page
pdfinfo paper/main.pdf
```

The README rendering check uses the user-authorized GitHub Markdown API:

```sh
gh api markdown -f text="$(cat README.md)" -f mode=gfm > build/readme.html
$HOME/.venvs/claude/bin/python scripts/check_readme.py
```

The checker compares source inline and fenced math counts with the rendered
math elements, checks each expression, and checks local Markdown link
existence. The request renders content; it does not create a repository or
publish this draft. No release audit, freeze, admission or archive step is
part of this task.
