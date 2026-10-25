# Copied evidence and provenance

Pre-release draft. Not admitted, not peer reviewed.

Source: `/Users/klinellc/Documents/hm-ai/quarantine/steiner-diversity-tw-2026-10-25/`.
The source is a read-only non-Git directory, so there is no source commit.
Its original manifest was checked first: 150 entries passed, none failed.
The later flow-cut and citing scan logs are outside that original 150-file
manifest; their individual copied hashes are pinned below.

The seven named research records below came from the source root. The two
scan logs came from `searches/flowcut/FLOWCUT-SCAN.md` and
`searches/citing/CITING-SCAN.md`. All nine are copied byte for byte into
`audit/evidence/`. They retain historical paths, references and scope labels.
References into the larger research directory are not all bundled here.
The requirement to copy raw evidence unchanged retains earlier papers'
historical bibliographic identifiers in those records; none identifies this
draft. Draft metadata and paper title material have no assigned publication
identifier. Raw records will need the coordinator's normal release review.

| Copied record | SHA-256 |
|---|---|
| `PROOF.md` | `70570485370461c21ffbb927acc60a6f313123e8485dbeb5e98411dfa47a5f09` |
| `CERTIFICATE.md` | `d96107a8c4cd1aa32372a3ad041d945a94361bcf845c0434a98fde320ec42ca6` |
| `PROOF-AUDIT.md` | `e04071f7e374d6baa4e503226fb901dd207517f14b0a1d866bf933538521a2c0` |
| `ADJUDICATION.md` | `b02956a7bb88239e2e6503f7e77beece2caf5977f262ded829a294d3bee3342a` |
| `STRENGTHENING.md` | `d92ad1fdef28e722e3bfd11b80a2cf314e903f60da2daf80ab8e74a74fdac44c` |
| `SMALL_CASES.md` | `5e2efae887d36ea80c3251e782a61fb6ebc719f56c4afa3e4cac2d497f4751ec` |
| `LITERATURE.md` | `13b920563a1c14f519d83a50933d8aedefa9ea15f16f1a2632ae5cbc2dc788d5` |
| `FLOWCUT-SCAN.md` | `a5915e09c01f5b0c50beb8362c26e21cd7906fe463b3ec19dc908cf83b5b6d5c` |
| `CITING-SCAN.md` | `74e6006448465f282a2cfb12991f4cd736561b54b620b8cce80bac5b6801aa1c` |

Original source manifest SHA-256: `72b811c092ef8f46408b84e9f06be47b0243b0fbbd356f10756e352f27bec818`.

All 57 top-level `results/*.json` files are copied unchanged to `data/`:
28 graph/certificate records, 28 saved size estimates, and the earlier
independent-verification summary. The 28 graph records hold the exact edges,
Steiner costs and rational primal/dual weights. Their hashes, along with the
nine evidence records, are in `audit/imports.sha256` (66 entries).
The new verifier recomputes the mathematical finite checks and does not
trust the earlier summary's verdict in place of checking the certificates.

The GPL license was copied with `cp` from the read-only predecessor
`covering-hitting-diversities` at `60d135d`; its bytes match. That predecessor
also supplies the repository organization and clean double-build workflow.
Its metadata, dates and publication status are not inherited by this draft.

Run the following to check imported file bytes locally:

```sh
shasum -a 256 -c audit/imports.sha256
```

For a deliberate recheck against the source directory, the named inventory
script verifies equality before rewriting this evidence index:

```sh
/Users/klinellc/.venvs/claude/bin/python scripts/draft_inventory.py --evidence
```

`MANIFEST.sha256` covers every current draft file except itself and ignored
build/cache/Git files. The inventory script updates it only on explicit
`--manifest`; the verifier never rewrites it. This is local integrity
bookkeeping, not a release freeze, admission or archive action.
