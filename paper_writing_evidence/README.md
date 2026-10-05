# Paper-Writing Evidence and COMST Execution Control

This folder is the persistent manuscript-facing control area for the Metaverse Research Framework.

## Working files

- `Metaverse_Paper_Writing_Evidence_Master.xlsx` — working Excel master generated from the repository evidence registers. The structured repository records remain the source of truth.
- `Metaverse_COMST_Execution_Roadmap.docx` — formatted execution-control document maintained alongside the workbook.
- `COMST_EXECUTION_ROADMAP.md` — Git-native mirror of the execution roadmap and sequential run queue.

## Operating rule

Every future research run starts from the first unfinished RUN in the roadmap unless a blocker requires a dependency. Each run must:

1. perform the defined evidence/reproducibility task;
2. save structured outputs in the appropriate repository folder;
3. commit the outputs;
4. verify critical committed paths;
5. update the run ledger/status;
6. report the GitHub links and the next RUN.

The manuscript is written only after the mandatory evidence-freeze gates are passed. Unresolved metadata, parameters, equations, artifact availability, or candidate gaps are never promoted to verified findings.
