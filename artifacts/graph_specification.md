# Technology–Problem–Algorithm Graph Specification

The first graph will be generated from:

- `evidence/technology_problem_algorithm_graph.csv`
- `evidence/technology_problem_algorithm_edges.csv`

## Planned visual encoding

Node shape represents node type:

- technology
- problem
- algorithm family

Edge labels preserve analytical meaning. Candidate relations must be visually distinguishable from evidence-supported relations in the generated artifact.

## Planned expansions

The graph will later add:

- metrics
- datasets/workloads
- standards
- reproducibility artifacts
- validated gaps

The final graph should allow a researcher to trace:

`technology → problem → algorithm → evaluation → evidence → unresolved condition`

without implying that all nodes are directly comparable.
