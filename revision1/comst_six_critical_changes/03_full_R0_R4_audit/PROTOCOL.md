# 3. Denominator-complete R0-R4 reproducibility audit

## Eligible study classes
Include:
- evaluated algorithm/system
- implemented benchmark / artifact-bearing system
- empirical operational field study, with tagged expectations

Exclude from the primary computational denominator:
- dataset-only records
- surveys/reviews
- standards
- purely conceptual architectures

## Eight binary audit fields
code,data,configuration,seeds,dependencies,instructions,persistent_archive,independent_reproduction

## R-class mapping
R0: 0-1/8
R1: 2-3/8
R2: 4-5/8
R3: 6-7/8
R4: 8/8 and independently identified reproduction evidence

## Required outputs
- eligible-study ledger
- one row per eligible study
- evidence URL/DOI for every positive field
- distinguish ABSENT from NOT_IDENTIFIED_IN_AUDITED_SOURCES
- domain-specific and overall R-class counts
- no field-wide percentage until the denominator is frozen
