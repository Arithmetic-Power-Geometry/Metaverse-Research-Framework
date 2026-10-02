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
