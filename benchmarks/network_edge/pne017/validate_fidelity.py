from pathlib import Path
import csv, sys, yaml

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"benchmarks/network_edge/pne017"

def main():
    errors=[]
    with (BASE/"implementation_gate.csv").open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    blockers=[r["component"] for r in rows if r["blocking"].strip().lower()=="yes"]
    spec=yaml.safe_load((BASE/"model_spec.yml").read_text(encoding="utf-8"))
    if spec["guardrails"].get("guessed_coefficients") is not False:
        errors.append("guessed_coefficients must remain false")
    if not blockers and spec["guardrails"].get("executable_fidelity")!="ready":
        errors.append("all blockers resolved but executable_fidelity is not ready")
    if blockers and spec["guardrails"].get("executable_fidelity")=="ready":
        errors.append("scenario marked ready while blockers remain")
    if errors:
        print("\n".join("ERROR: "+x for x in errors),file=sys.stderr)
        return 1
    print(f"PNE017 fidelity gate valid; {len(blockers)} blocking components remain.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
