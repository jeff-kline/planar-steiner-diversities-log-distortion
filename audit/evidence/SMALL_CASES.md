# Exact small-case table

All nontrivial terminal subsets and all cuts modulo complement. LP status 0 means optimal; status 1 is a solver limit. Values labeled exact have independently verified rational primal and dual certificates and independently recomputed Steiner costs.

| Instance | Vertices | Exact c1 | LP status |
|---|---:|---:|---:|
| C10 | 10 | 9/5 | 0 |
| C12 | 12 | 11/6 | 0 |
| C4 | 4 | 3/2 | 0 |
| C5 | 5 | 8/5 | 0 |
| C6 | 6 | 5/3 | 0 |
| C7 | 7 | 12/7 | 0 |
| C8 | 8 | 7/4 | 0 |
| K3 | 3 | 4/3 | 0 |
| K4 | 4 | 3/2 | 0 |
| K5 | 5 | 8/5 | 0 |
| K6 | 6 | 5/3 | 0 |
| K8 | 8 | 7/4 | 0 |
| diamond2 | 12 | 17/8 | 0 |
| fan5 | 5 | 8/5 | 0 |
| fan8 | 8 | 7/4 | 0 |
| grid2x3 | 6 | 5/3 | 0 |
| grid2x4 | 8 | 7/4 | 0 |
| grid2x5 | 10 | 9/5 | 0 |
| grid2x6 | 12 | 11/6 | 0 |
| grid3x3 | 9 | 11/6 | 0 |
| grid3x4 | 12 | 29/15 | 0 |
| path8 | 8 | 1 | 0 |
| random2tree8-seed17 | 8 | 4/3 | 0 |
| random2tree8-seed31 | 8 | 14/11 | 0 |
| random2tree8-seed53 | 8 | 26/19 | 0 |
| star8 | 8 | 1 | 0 |
| wheel5 | 5 | 5/3 | 0 |
| wheel8 | 8 | 38/21 | 0 |

For diamond2, grid2x6, and grid3x4 the first full-matrix LPs reached 90 seconds. Their initial outputs are preserved in results/initial-full-lp/. Equivalent reductions keep all subset lower constraints, impose upper bounds only on edge pairs, and verify every subset upper bound afterward. KILLS.md gives the exact implication, so this is not a subset-size restriction.

Reproduce: `/Users/klinellc/.venvs/claude/bin/python verify_small.py` (use run_job.py for tracked execution).
