---
search:
  boost: 5.0
---

# Slot: collection 


_Descreve conjuntos conceituais nos quais a edificação foi incluída, por exemplo catálogos raisonnés, obras de referência, exposições, ou agrupamentos *ad-hoc* para formar coleções temáticas de acordo com as necessidades do projeto de investigação._

_Para o pertencimento a perímetros de sítios históricos tombados/classificados, preencher o grupo `identifiers`. Para a identificação de proprietários ou responsáveis, preencher o grupo `work_rights`._

__



<div data-search-exclude markdown="1">



URI: [lido:collection](http://www.lido-schema.org/collection)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Thing](Thing.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [lido:collection](http://www.lido-schema.org/collection) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Work](Work.md) |










## Notes

* A set of identifying and indexing information about the collection the object/work in focus is gathered into or is a member of.
Collection applies to any accumulated group of physical or digital items, conceptually or physically brought together on the basis of a focal characteristic. Use cases for grouping items into a collection are various and may span curated holdings in museums, departmental collections, sets of items to be displayed in an exhibition, or aggregations bound informally for cataloging and retrieval purposes.



## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lido:collection |
| native | wasth:collection |




## LinkML Source

<details>
```yaml
name: collection
description: 'Descreve conjuntos conceituais nos quais a edificação foi incluída,
  por exemplo catálogos raisonnés, obras de referência, exposições, ou agrupamentos
  *ad-hoc* para formar coleções temáticas de acordo com as necessidades do projeto
  de investigação.

  Para o pertencimento a perímetros de sítios históricos tombados/classificados, preencher
  o grupo `identifiers`. Para a identificação de proprietários ou responsáveis, preencher
  o grupo `work_rights`.

  '
notes:
- 'A set of identifying and indexing information about the collection the object/work
  in focus is gathered into or is a member of.

  Collection applies to any accumulated group of physical or digital items, conceptually
  or physically brought together on the basis of a focal characteristic. Use cases
  for grouping items into a collection are various and may span curated holdings in
  museums, departmental collections, sets of items to be displayed in an exhibition,
  or aggregations bound informally for cataloging and retrieval purposes.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: lido:collection
owner: Work
domain_of:
- Work
range: Thing
multivalued: true
inlined_as_list: false

```
</details></div>