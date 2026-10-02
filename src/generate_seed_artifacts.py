from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

nodes = pd.read_csv(ROOT / "evidence/technology_problem_algorithm_graph.csv")
edges = pd.read_csv(ROOT / "evidence/technology_problem_algorithm_edges.csv")
g = nx.DiGraph()
for _, r in nodes.iterrows():
    g.add_node(r["node_id"], label=str(r["label"]).replace("_"," "), node_type=r["node_type"])
for _, r in edges.iterrows():
    g.add_edge(r["source"], r["target"], status=r["evidence_status"])

pos = nx.spring_layout(g, seed=42, k=1.25)
fig, ax = plt.subplots(figsize=(14,10))
for typ, shape in {"technology":"o","problem":"s","algorithm_family":"^"}.items():
    ns=[n for n,d in g.nodes(data=True) if d["node_type"]==typ]
    nx.draw_networkx_nodes(g,pos,nodelist=ns,node_shape=shape,node_size=1350,ax=ax)
sup=[(u,v) for u,v,d in g.edges(data=True) if d["status"]=="supported"]
cand=[(u,v) for u,v,d in g.edges(data=True) if d["status"]=="candidate"]
nx.draw_networkx_edges(g,pos,edgelist=sup,arrows=True,width=1.1,ax=ax)
nx.draw_networkx_edges(g,pos,edgelist=cand,arrows=True,width=1.0,style="dashed",ax=ax)
nx.draw_networkx_labels(g,pos,labels={n:d["label"] for n,d in g.nodes(data=True)},font_size=8,ax=ax)
ax.set_title("Technology-Problem-Algorithm Evidence Graph (Seed Evidence)")
ax.text(.01,.01,"Solid: supported in current seed evidence; dashed: candidate relation under validation.",transform=ax.transAxes,fontsize=8)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT/"technology_problem_algorithm_seed.png",dpi=220,bbox_inches="tight")
fig.savefig(OUT/"technology_problem_algorithm_seed.pdf",bbox_inches="tight")
plt.close(fig)

a=pd.read_csv(ROOT/"evidence/closest_reviews.csv")
b=pd.read_csv(ROOT/"evidence/closest_reviews_expansion.csv")
r1=pd.DataFrame({"review_id":a.review_id,"year":a.year,"title":a.title,"venue":a.venue,"focus":a.scope,"evidence_note":a.reported_corpus_or_method})
r2=pd.DataFrame({"review_id":b.review_id,"year":b.year,"title":b.title,"venue":b.venue,"focus":b.focus,"evidence_note":b.key_reported_scope})
out=pd.concat([r1,r2],ignore_index=True).sort_values(["year","review_id"])
out.to_csv(OUT/"closest_reviews_seed_comparison.csv",index=False)

lines=["# Closest Review Comparison - Seed Register","","> Preliminary artifact generated from the current verified seed register; not the final systematic-review corpus.","","| ID | Year | Review | Venue | Focus | Corpus/method note |","|---|---:|---|---|---|---|"]
clean=lambda x: str(x).replace("|","/").replace("\n"," ")
for _,r in out.iterrows():
    lines.append("| "+" | ".join(clean(x) for x in [r.review_id,r.year,r.title,r.venue,r.focus,r.evidence_note])+" |")
(OUT/"closest_reviews_seed_comparison.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

files=sorted(p.name for p in OUT.iterdir() if p.is_file() and p.name!="MANIFEST.md")
manifest=["# Generated Seed Artifacts","","These outputs use an incomplete seed evidence set and must not be interpreted as field-wide quantitative results.",""]+[f"- `{x}`" for x in files]
(OUT/"MANIFEST.md").write_text("\n".join(manifest)+"\n",encoding="utf-8")
print("Generated seed artifacts.")


# Additional seed diagnostics: descriptive only, never field-wide prevalence.
cap = pd.read_csv(ROOT/"evidence/capability_evidence_matrix_seed.csv").set_index("capability")
status_map = {"yes":1.0,"partial":0.5,"limited-in-seed":0.25,"limited":0.25,"no":0.0}
cols=["foundational_concepts","peer_reviewed_methods","algorithmic_methods","public_datasets_or_workloads","public_code","reproducible_benchmarks","standards_or_specs","cross_layer_evaluation"]
num = cap[cols].applymap(lambda x: status_map.get(str(x).strip().lower(), float("nan")))
fig,ax=plt.subplots(figsize=(11,6))
im=ax.imshow(num.values,aspect="auto",vmin=0,vmax=1)
ax.set_xticks(range(len(cols)),[x.replace("_"," ") for x in cols],rotation=45,ha="right",fontsize=8)
ax.set_yticks(range(len(num.index)),[x.replace("_"," ") for x in num.index],fontsize=8)
ax.set_title("Capability x Evidence Audit Status (Seed; Descriptive Only)")
fig.colorbar(im,ax=ax,label="coded audit status: no=0, partial=.5, yes=1")
fig.tight_layout()
fig.savefig(OUT/"capability_evidence_seed_heatmap.png",dpi=220,bbox_inches="tight")
fig.savefig(OUT/"capability_evidence_seed_heatmap.pdf",bbox_inches="tight")
plt.close(fig)

dep = pd.read_csv(ROOT/"taxonomy/deployment_evidence_levels.csv")
dep.to_csv(OUT/"deployment_evidence_scale.csv",index=False)

repro = pd.read_csv(ROOT/"evidence/network_edge_reproducibility_seed.csv")
repro.to_csv(OUT/"network_edge_reproducibility_seed.csv",index=False)

domain = pd.read_csv(ROOT/"evidence/domain_coverage_status.csv")
domain.to_csv(OUT/"domain_coverage_seed.csv",index=False)

# Refresh manifest after all diagnostics.
files=sorted(p.name for p in OUT.iterdir() if p.is_file() and p.name!="MANIFEST.md")
manifest=["# Generated Seed Artifacts","","These outputs use an incomplete seed evidence set and must not be interpreted as field-wide quantitative results.","","The capability heatmap encodes audit status for navigation; it is not a quality score or maturity ranking.",""]+[f"- `{x}`" for x in files]
(OUT/"MANIFEST.md").write_text("\n".join(manifest)+"\n",encoding="utf-8")
