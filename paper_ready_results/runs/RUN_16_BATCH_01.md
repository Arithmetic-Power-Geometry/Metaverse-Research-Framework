# RUN 16 — Artifact-Level Reproducibility Audit Batch 01

## Workflow pre-check
The current GitHub workflow and requirements were re-fetched before this audit. Requirements remain newline-valid and the workflow invokes the expected evidence, parameter-provenance and PNE017 fidelity validators. No workflow or unresolved benchmark was executed.

## Audit design
Eight binary evidence fields are recorded separately: code, data, configuration/parameters, seeds/randomness protocol, environment/dependencies, execution instructions, persistent artifact, and independent reproduction.

The resulting R0-R4 class is descriptive. It is not a quality score and does not imply that a scientifically strong paper is weak because artifacts are unavailable.

## Positive control
XRBench is currently a strong positive control: its public repository provides dependencies, build instructions and figure-reproduction scripts, explicitly discusses deterministic versus nondeterministic outputs, and the paper's plot data are archived on Zenodo with DOI 10.5281/zenodo.7857382.

## Important rule
**Code available != reproducible.** A repository link receives only the code field unless the remaining artifact requirements are independently supported.

## Next
Expand this audit across all eligible computational primary studies, then report denominators and confidence-safe counts only after artifact searches are completed.
