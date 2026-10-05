# Deterministic corpus-navigation map generator for the frozen 200-entry BibTeX.
# This layer classifies title/venue metadata only; it MUST NOT be used as deep evidence coding.
import re,csv
from pathlib import Path
bib=Path('../../paper_ready_results/metaverse_comst_master.bib').read_text(encoding='utf-8')
chunks=[x for x in re.split(r'\n(?=@)',bib) if x.strip()]
RULES=[('Networking/edge/XR',['network','wireless','6g','5g','edge','mec','resource allocation','offload','o-ran','virtual reality','extended reality','xr','vr']),('Digital twin',['digital twin','twin']),('Semantic communication',['semantic communication','semantic']),('AI/GenAI',['artificial intelligence','generative','genai','machine learning','reinforcement','federated','llm','agent']),('Security/privacy',['security','privacy','authentication','identity','trust','attack','intrusion','zero-trust','blockchain']),('Standards/interoperability',['standard','interoperab','cross-platform','recommendation']),('Sustainability',['sustainab','energy','carbon','environment','green','life cycle']),('Datasets/testbeds',['dataset','benchmark','testbed','trace','recording'])]
PRIORITY=['Standards/interoperability','Datasets/testbeds','Semantic communication','Digital twin','Security/privacy','Sustainability','AI/GenAI','Networking/edge/XR','Foundations/applications/other']
def field(e,n):
 m=re.search(r'\\b'+re.escape(n)+r'\\s*=\\s*\\{([^}]*)\\}',e,re.I|re.S); return re.sub(r'\\s+',' ',m.group(1)).strip() if m else ''
rows=[]
for e in chunks:
 m=re.match(r'@(\\w+)\\{([^,]+),',e); typ,key=m.groups(); title=field(e,'title'); year=field(e,'year'); venue=field(e,'journal') or field(e,'booktitle') or field(e,'publisher'); doi=field(e,'doi'); text=(title+' '+venue).lower(); tags=[d for d,ks in RULES if any(k in text for k in ks)] or ['Foundations/applications/other']; primary=next(x for x in PRIORITY if x in tags); role='Secondary/review' if any(k in text for k in ['survey','review','systematic','bibliometric','taxonomy']) else 'Primary/context'; rows.append([key,year,title,venue,doi,'; '.join(tags),primary,role])
assert len(rows)==200
with open('D_R1_01_corpus_role_map_200.csv','w',newline='',encoding='utf-8') as f:
 w=csv.writer(f); w.writerow(['ID','year','title','venue','doi','domain','primary_domain','role']); w.writerows(rows)
