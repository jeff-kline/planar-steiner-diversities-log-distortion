# Exact symbolic dual certificate — version 2

Status: VERIFIED by PROOF-AUDIT.md and accepted in ADJUDICATION.md. Only this status line changed after audit; CERTIFICATE-v2.md preserves the submitted bytes. Use unit-edge D_d, d>=1, E=4^d, and V_j consisting of vertices already present after generation j.

- alpha_(V_j)=2^(d-j)/4^d for 1<=j<d.
- alpha_(V_d)=2/4^d.
- beta_({u,v})=1/4^d for each final graph edge uv.
- All other weights are zero.

There are d alpha subsets and 4^d beta pairs; all weights are positive rationals. No cut enumeration or product distribution is part of this certificate.

Normalization: sum_A beta_A delta(A)=1.
Feasibility: sum_A alpha_A chi_S(A)<=|boundary S|/4^d=sum_A beta_A chi_S(A), by PROOF.md Section 3.
Objective: sum_A alpha_A delta(A)=(6d+7+2/4^d)/9, by PROOF.md Sections 4–5.

At d=1, alpha(V_1)=1/2 and beta(edge)=1/4; objective 3/2.
At d=2, alpha(V_1)=alpha(V_2)=1/8 and beta(edge)=1/16; costs 6,11 give objective 17/8.

This proves a lower bound, not equality with optimal distortion at arbitrary depth.

