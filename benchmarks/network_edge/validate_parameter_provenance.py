from pathlib import Path
import csv
import sys

ROOT=Path(__file__).resolve().parents[2]
REG=ROOT/"benchmarks/network_edge/parameter_registry.csv"

ALLOWED={"verified","reconstructed","benchmark_choice"}
FORBIDDEN={"unresolved","unknown","pending",""}

def main():
    errors=[]
    with REG.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    for i,r in enumerate(rows,2):
        status=(r.get("source_status") or "").strip()
        if status in FORBIDDEN:
            # Design registries may contain unresolved values; executable scenarios may not.
            continue
        if status not in ALLOWED:
            errors.append(f"parameter_registry.csv:{i}: invalid source_status={status}")
    scenario=ROOT/"benchmarks/network_edge/scenario_template.yml"
    text=scenario.read_text(encoding="utf-8")
    if "status: design-only" not in text:
        errors.append("scenario_template.yml must remain design-only until all required parameters are resolved")
    if "unverified_source_values_allowed: false" not in text:
        errors.append("scenario_template.yml must forbid unverified source values")
    if errors:
        print("\n".join("ERROR: "+e for e in errors),file=sys.stderr)
        return 1
    print("Parameter provenance gate passed for design-stage registry.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
