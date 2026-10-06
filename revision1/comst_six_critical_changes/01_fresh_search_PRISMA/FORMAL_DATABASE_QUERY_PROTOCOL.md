# Prospective corpus-validation search protocol

**Search label:** Prospective corpus-validation search conducted in October 2026.

## Concept blocks
A — Metaverse/XR:
("metaverse" OR "networked metaverse" OR "industrial metaverse" OR "extended reality" OR XR OR "virtual reality" OR "augmented reality")

B — communications/systems:
(network* OR communication* OR wireless OR 5G OR 6G OR edge OR MEC OR cloud OR rendering OR offload* OR "resource allocation" OR "digital twin*" OR synchroni* OR "semantic communication*" OR "federated learning" OR "generative AI" OR security OR privacy OR interoperab* OR standard* OR sustainab* OR energy OR dataset* OR testbed*)

## Canonical search
A AND B

## Prospective limits
- Publication years: 2013–2026
- Language: English
- Document types: journal article, conference paper, review/survey; standards handled in a separate normative register
- Search fields: title/abstract/keywords where supported

## IEEE Xplore
Use Advanced Search with:
(("All Metadata":"metaverse" OR "All Metadata":"networked metaverse" OR "All Metadata":"industrial metaverse" OR "All Metadata":"extended reality" OR "All Metadata":"virtual reality" OR "All Metadata":"augmented reality")
AND
("All Metadata":network OR "All Metadata":communication OR "All Metadata":wireless OR "All Metadata":5G OR "All Metadata":6G OR "All Metadata":edge OR "All Metadata":MEC OR "All Metadata":"digital twin" OR "All Metadata":"semantic communication" OR "All Metadata":"federated learning" OR "All Metadata":security OR "All Metadata":privacy OR "All Metadata":interoperability OR "All Metadata":sustainability OR "All Metadata":energy OR "All Metadata":dataset OR "All Metadata":testbed))
Record exact returned count before export.

## Scopus
TITLE-ABS-KEY(
(metaverse OR "networked metaverse" OR "industrial metaverse" OR "extended reality" OR XR OR "virtual reality" OR "augmented reality")
AND
(network* OR communication* OR wireless OR 5G OR 6G OR edge OR MEC OR cloud OR rendering OR offload* OR "resource allocation" OR "digital twin*" OR synchroni* OR "semantic communication*" OR "federated learning" OR "generative AI" OR security OR privacy OR interoperab* OR standard* OR sustainab* OR energy OR dataset* OR testbed*)
)
AND PUBYEAR > 2012 AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE,"English"))

## Web of Science Core Collection
TS=((metaverse OR "networked metaverse" OR "industrial metaverse" OR "extended reality" OR XR OR "virtual reality" OR "augmented reality")
AND
(network* OR communication* OR wireless OR 5G OR 6G OR edge OR MEC OR cloud OR rendering OR offload* OR "resource allocation" OR "digital twin*" OR synchroni* OR "semantic communication*" OR "federated learning" OR "generative AI" OR security OR privacy OR interoperab* OR standard* OR sustainab* OR energy OR dataset* OR testbed*))
Refine years=2013-2026; language=English.

## ACM Digital Library
[[Abstract: metaverse] OR [Abstract: "extended reality"] OR [Abstract: "virtual reality"] OR [Abstract: "augmented reality"]]
AND
[[Abstract: network] OR [Abstract: communication] OR [Abstract: edge] OR [Abstract: "digital twin"] OR [Abstract: "semantic communication"] OR [Abstract: security] OR [Abstract: privacy] OR [Abstract: interoperability] OR [Abstract: sustainability]]
Apply 2013–2026.

## Supplementary
Repeat concept blocks in ScienceDirect and SpringerLink for coverage validation. Supplementary results must not be mixed with formal database counts unless explicitly included in the prospective protocol before screening.

## Export
Export full available metadata, abstract, DOI, keywords, source, year, and database provenance. Preserve raw exports unchanged.
