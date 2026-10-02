# Evidence Graph Rules

The graph is a research-navigation artifact, not a causal model by default.

## Node classes

- technology
- capability
- problem
- algorithm family
- dataset/workload
- metric
- evidence artifact
- standard/specification
- validated gap

## Edge states

- supported — backed by extracted literature evidence
- candidate — plausible relation under active testing
- invalidated — tested and not supported
- superseded — replaced by stronger/more precise relation

## Edge semantics

Every relation must use an explicit verb such as:

- enables
- constrains
- addresses
- optimizes
- evaluated_by
- requires
- trades_off
- interoperates_with
- threatens
- protects
- standardized_by
- reproduced_by

Avoid ambiguous edges such as "related_to" in final analytical artifacts.

## Evidence requirement

Before an edge is used to support a substantive conclusion, it must link to one or more study/standard IDs and the relevant extracted fields.

## Causality rule

Observational co-occurrence or conceptual dependence is not labeled causal unless the underlying evidence supports a causal interpretation.
