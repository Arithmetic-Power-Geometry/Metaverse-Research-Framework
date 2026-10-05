# Metaverse COMST Revision 1 - Final empirical package

This self-contained revision folder contains the revised IEEE two-column manuscript and the manuscript-facing evidence artifacts used in the current revision.

## Main files
- main.tex - revised manuscript source
- metaverse_comst_master.bib - frozen 200-entry BibTeX database
- references_generated.tex - generated reference listing used by the checked build

## Artifact organization
- equations/ - every named equation source
- tables/ - manuscript-facing table sources
- figures/ - manuscript-facing figure sources
- algorithms/ and protocols/ - comparability, reproducibility, and gap-falsification procedures
- data/ - corpus role map, pair-level compatibility, evidence summaries, threshold sensitivity
- coverage_audit/ - dated post-freeze coverage audit
- reviews/ - reviewer traceability plus the independent-coder protocol/template

## Integrity boundary
The package does not fabricate a historical PRISMA trajectory, a database session that was never executed, a complete all-eligible R0-R4 distribution that is not supported by the frozen evidence, or a second-coder kappa value without a genuine independent human recoding. Those items remain explicit limitations or external validation tasks.

## Build
The checked PDF was compiled locally from main.tex. The manuscript uses references_generated.tex directly, so the checked build does not require BibTeX. Run pdflatex repeatedly until cross-references stabilize.
