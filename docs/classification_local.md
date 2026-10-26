---
search:
  boost: 5.0
---

# Slot: classification_local


_A classification scheme for grouping objects on the basis of locally defined criteria, including categories corresponding to the curatorial departments of the repository, such as "prints and drawings", "decorative arts", "North America", "invertebrates", "Bronze Age" or "textiles". [Based on CCO "Class"](https://vraweb.org/wp-content/uploads/2020/04/CatalogingCulturalObjectsFullv2.pdf)_

_❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura._



<div data-search-exclude markdown="1">



URI: [term:lido01135](http://terminology.lido-schema.org/lido01135)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [term:lido01135](http://terminology.lido-schema.org/lido01135) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Work](Work.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | term:lido01135 |
| native | wasth:classification_local |




## LinkML Source

<details>
```yaml
name: classification_local
description: 'A classification scheme for grouping objects on the basis of locally
  defined criteria, including categories corresponding to the curatorial departments
  of the repository, such as "prints and drawings", "decorative arts", "North America",
  "invertebrates", "Bronze Age" or "textiles". [Based on CCO "Class"](https://vraweb.org/wp-content/uploads/2020/04/CatalogingCulturalObjectsFullv2.pdf)

  ❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não
  seja relevante para o documentário de arquitetura doméstica, e não é obrigatório
  no padrão LIDO nem no perfil de aplicação para arquitetura.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido01135
owner: Work
domain_of:
- Work
range: ConceptReference
multivalued: true
inlined_as_list: false

```
</details></div>
