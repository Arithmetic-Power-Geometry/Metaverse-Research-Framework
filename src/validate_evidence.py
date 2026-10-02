from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []

def rows(rel):
    p = ROOT / rel
    if not p.exists():
        ERRORS.append("missing: " + rel)
        return []
    with p.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def unique(rel, key):
    seen = set()
    out = rows(rel)
    for n, r in enumerate(out, 2):
        v = (r.get(key) or "").strip()
        if not v:
            ERRORS.append(f"{rel}:{n} missing {key}")
        elif v in seen:
            ERRORS.append(f"{rel}:{n} duplicate {key}={v}")
        seen.add(v)
    return out

nodes = unique("evidence/technology_problem_algorithm_graph.csv", "node_id")
ids = {r["node_id"].strip() for r in nodes if r.get("node_id")}
for n, r in enumerate(rows("evidence/technology_problem_algorithm_edges.csv"), 2):
    if (r.get("source") or "").strip() not in ids:
        ERRORS.append(f"edges:{n} broken source")
    if (r.get("target") or "").strip() not in ids:
        ERRORS.append(f"edges:{n} broken target")
    if (r.get("evidence_status") or "").strip() not in {"supported","candidate","invalidated","superseded"}:
        ERRORS.append(f"edges:{n} invalid evidence_status")

levels = unique("taxonomy/evidence_levels.csv", "level")
if {r["level"].strip() for r in levels if r.get("level")} != {f"E{i}" for i in range(9)}:
    ERRORS.append("evidence levels must be E0-E8")

unique("taxonomy/gap_types.csv", "code")
for rel, key in [
    ("evidence/primary_network_edge_seed.csv","study_id"),
    ("evidence/primary_6g_semantic_xr_seed.csv","study_id"),
    ("evidence/closest_reviews.csv","review_id"),
    ("evidence/closest_reviews_expansion.csv","review_id"),
    ("evidence/ai_genai_agent_seed.csv","record_id"),
    ("evidence/security_interop_standards_seed.csv","record_id"),
    ("evidence/sustainability_deployment_seed.csv","record_id"),
]:
    unique(rel, key)

review_ids = {}
for rel in ["evidence/closest_reviews.csv","evidence/closest_reviews_expansion.csv"]:
    for n, r in enumerate(rows(rel), 2):
        rid = (r.get("review_id") or "").strip()
        if rid and rid in review_ids:
            ERRORS.append(f"{rel}:{n} review_id {rid} also in {review_ids[rid]}")
        elif rid:
            review_ids[rid] = rel

if ERRORS:
    for e in ERRORS:
        print("ERROR:", e, file=sys.stderr)
    raise SystemExit(1)
print("Evidence validation passed.")
