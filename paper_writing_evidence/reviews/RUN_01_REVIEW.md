# Adversarial Review — RUN 01

Date: 2026-10-05

## Initial recommendation: REJECT

### Strongest rejection argument

The repository's CI could not be treated as a valid evidence-integrity gate because the dependency file contained malformed literal newline escapes around PyYAML, and the PNE017 fidelity validator was not invoked by the GitHub Actions workflow. Therefore a nominally green or previously successful workflow would not demonstrate that the current benchmark-fidelity rules were being checked.

## Findings

| ID | Severity | Reviewer objection | Required correction | Status |
|---|---|---|---|---|
| R01-01 | CRITICAL | requirements.txt contained literal \\n around PyYAML, risking dependency-install failure | Replace with actual newline-delimited requirement | CORRECTED |
| R01-02 | HIGH | PNE017 validate_fidelity.py existed but CI did not run it | Add explicit PNE017 fidelity validation step | CORRECTED |
| R01-03 | HIGH | Workflow path filters omitted benchmarks/**, so benchmark-only changes could bypass CI | Add benchmarks/** to push and PR path filters | CORRECTED |
| R01-04 | MEDIUM | A successful historical workflow cannot establish the status of the corrected workflow | Verify a workflow run after the corrections | OPEN until GitHub run is observed |

## Claim correction

Allowed: "Repository CI now includes evidence validation, parameter-provenance validation, and the PNE017 fidelity gate; the corrected workflow still requires a post-fix run verification."

Forbidden: "All current CI gates have passed" until the corrected run is observed.

## Internal gate

RUN 01 remains **CONDITIONALLY OPEN** until the corrected workflow run is confirmed. The structural defects identified by the reviewer are corrected.
