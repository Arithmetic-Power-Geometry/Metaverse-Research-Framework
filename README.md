# Evidence in Networked Metaverse Systems

## Comparability, Reproducibility, and Deployment

This repository contains the research software, structured evidence files, validation scripts, source registers, and supporting artifacts for:

**Mohammad Amir Khusru Akhtar, Anand Nayyar, and Sumendra Yogarayan, “Evidence in Networked Metaverse Systems: Comparability, Reproducibility, and Deployment.”**

The study treats **evidence rather than technology labels as the unit of synthesis**. The framework links claims to problem definitions, workloads, datasets/inputs, hardware, network/system conditions, baselines, metric semantics, evaluation protocols, artifacts, reproduction evidence, deployment evidence, and standards evidence.

## Authors

- **Mohammad Amir Khusru Akhtar** — Faculty of Computing and Information Technology, Usha Martin University, Ranchi, Jharkhand, India.
- **Anand Nayyar** — School of Computer Science and Artificial Intelligence (SCA), Duy Tan University, Da Nang, Viet Nam.
- **Sumendra Yogarayan** — Faculty of Information Science and Technology (FIST), Multimedia University, 75450 Melaka, Malaysia. Email: sumendra@mmu.edu.my.
- Corresponding author: **Sumendra Yogarayan** (sumendra@mmu.edu.my).

## Frozen evidence base

The manuscript uses a frozen bibliography of **200 records** under a non-overlapping primary-domain navigation rule:

| Primary navigation domain | Records |
|---|---:|
| Networking / edge / XR | 38 |
| Digital twin | 21 |
| Semantic communication | 18 |
| AI / GenAI | 25 |
| Security / privacy | 32 |
| Standards / interoperability | 9 |
| Sustainability | 18 |
| Datasets / testbeds | 12 |
| Foundations / applications / other | 27 |
| **Total** | **200** |

These are corpus-navigation counts, not substitutes for claim-specific empirical denominators.

## Evidence architecture

### Cross-paper comparability

Each study is represented by:

`C = (P, W, D, H, N, B, M, E)`

where the dimensions denote problem definition, workload, dataset/input, hardware, network/system conditions, baselines, metric definition, and evaluation protocol.

Pairwise compatibility uses `{0, 0.5, 1, ?}` and the reporting classes **C0–C3**. The executed source-coded validation subset contains **21 pairs**:

- C0 = 2 (9.5%)
- C1 = 6 (28.6%)
- C2 = 13 (61.9%)
- C3 = 0 (0.0%)

These percentages apply only to the 21 executed pairs. The 180-pair register remains a prospective frame and is not imputed.

### Reproducibility and evidence maturity

The framework separates evaluation, artifact, reproduction, and deployment evidence. Artifact reproducibility is audited using **R0–R4** states based on verified code, data, configuration, seeds, dependencies, instructions, persistent archive, and independent reproduction.

The repository preserves bounded artifact audits rather than reporting unsupported field-wide prevalence.

### Human validation

Coder B completed and approved a stratified second-review validation of **50 of 200 records (25%)**. The approved workbook is preserved unchanged as a raw audit artifact. The design was an adjudicative approve/modify/reject review of pre-populated codes rather than blind independent parallel recoding; therefore Cohen’s κ is not reported as independent inter-rater reliability.

### Contrary-evidence gap falsification

Broad absence claims are tested against closest surveys, primary studies, datasets/testbeds, artifacts, and standards. The retained evidence agenda is:

- **G1 — Comparability:** matched problem, workload, data, hardware, network conditions, baselines, metric semantics, and protocol.
- **G2 — Reproducibility:** claim-to-artifact provenance and independent reproduction.
- **G3 — Standards:** implementation, conformance, cross-platform testing, and adoption beyond specification publication.
- **G4 — Security transfer:** validation on native immersive traffic, identity, spatial, behavioral, and adversarial distributions.
- **G5 — Sustainability:** separation of resource proxies, modeled energy, measured energy, carbon accounting, and life-cycle evidence.
- **G6 — Cross-layer evidence:** matched evaluation across networking, rendering, synchronization, semantics, security, and QoE.

## Repository structure

- `protocol/` — review protocol, research questions, inclusion/exclusion rules, and search strategy.
- `taxonomy/` — controlled vocabularies and classification schemes.
- `evidence/` — structured literature, claim-evidence, artifact, and validation records.
- `benchmarks/` — reproducible comparison definitions and implementations.
- `src/` — analysis and artifact-generation code.
- `tests/` — validation tests.
- `artifacts/` — generated figures, tables, timelines, and supporting outputs.
- `revision1/` — manuscript-facing empirical revision, validation, tables, figures, procedures, and audit material.
- `revision1/comst_six_critical_changes/` — evidence-bound execution records for the six critical methodological checks.
- `revision1/final_print_2026-10-06/` — final-print traceability notes.

## Scientific integrity boundary

The repository follows the same evidence rule as the manuscript: unresolved provenance remains unresolved. Historical database return counts are not reconstructed when they were not preserved; unexecuted comparison pairs are not classified from titles; metadata candidate sets are not converted into prevalence denominators; and missing artifact fields are not silently converted into absence.

The software and repository artifacts support independent inspection of the reported synthesis. They do not replace the peer-reviewed sources on which scientific claims are based.

## Citation

For citation, refer to the manuscript: **Akhtar, M. A. K., Nayyar, A., and Yogarayan, S. (2026). _Evidence in Networked Metaverse Systems: Comparability, Reproducibility, and Deployment_.**

Machine-readable citation metadata is provided in `CITATION.cff`; check that it reflects the final author list before release.

## License and copyright

Copyright © 2026 Mohammad Amir Khusru Akhtar.

The repository software and code are released under the **Apache License 2.0**. See `LICENSE` for details.

