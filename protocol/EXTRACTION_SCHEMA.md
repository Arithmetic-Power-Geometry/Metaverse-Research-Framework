# Evidence Extraction Schema

Each included study should record, where applicable:

- study_id
- title
- authors
- year
- venue
- DOI or persistent identifier
- publication type
- study domain
- metaverse layer
- capability
- technical problem
- proposed method
- algorithm family
- mathematical objective
- assumptions
- workload
- dataset
- dataset availability
- code availability
- artifact availability
- hardware
- software environment
- network conditions
- baselines
- evaluation metrics
- statistical analysis
- ablation analysis
- sensitivity analysis
- evidence maturity
- claimed contribution
- demonstrated contribution
- limitations reported by authors
- limitations identified during review
- reproducibility status
- standards relevance
- deployment relevance
- candidate gap class
- candidate gap statement
- contrary evidence
- notes

## Comparison key

Two algorithmic results should not be directly ranked unless their problem definition and sufficient experimental conditions are compatible. Comparability should be established using:

`C = (P, W, D, H, N, B, M, E)`

where:

- P — problem definition
- W — workload
- D — dataset/input
- H — hardware/computing environment
- N — network/system conditions
- B — baselines
- M — metrics
- E — evaluation protocol

The tuple is used to determine whether direct numerical comparison is justified.
