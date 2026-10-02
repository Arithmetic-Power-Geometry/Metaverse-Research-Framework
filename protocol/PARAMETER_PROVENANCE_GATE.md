# Literature Parameter Provenance Gate

No numerical parameter may enter a benchmark scenario merely because it is plausible or conventional.

Each parameter must carry:
- source study or benchmark-design provenance;
- source location when available;
- status: verified, reconstructed, benchmark_choice, or unresolved;
- native unit;
- normalized unit;
- transformation, if any;
- rationale when the value is a benchmark choice rather than a literature value.

## Admission rules
1. verified literature values may be used directly after unit checking;
2. reconstructed values require an explicit derivation and sensitivity analysis;
3. benchmark_choice values must not be attributed to a source paper;
4. unresolved literature values are forbidden in executable scenarios;
5. conflicting source values remain separate scenario profiles;
6. missing values never default silently.

The simulator must fail before execution when a required parameter is unresolved.
