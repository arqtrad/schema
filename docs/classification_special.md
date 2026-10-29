---
search:
  boost: 5.0
---

# Slot: classification_special 


_❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura._

_---------------------------------------------------------------------_

_A classification scheme for grouping objects on the basis of criteria defined within specific academic disciplines or cultural domains, such as the "Hornbostel-Sachs Classification of Musical Instruments", the "Nickel-Strunz classification", biological taxonomies etc. Refers to classification schemes that group objects on the basis of object characteristics, not on the basis of themes or topics which the objects or works are related to._



<div data-search-exclude markdown="1">



URI: [term:lido01144](http://terminology.lido-schema.org/lido01144)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [term:lido01144](http://terminology.lido-schema.org/lido01144) |
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
| self | term:lido01144 |
| native | wasth:classification_special |




## LinkML Source

<details>
```yaml
name: classification_special
description: '❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez
  ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório
  no padrão LIDO nem no perfil de aplicação para arquitetura.

  ---------------------------------------------------------------------

  A classification scheme for grouping objects on the basis of criteria defined within
  specific academic disciplines or cultural domains, such as the "Hornbostel-Sachs
  Classification of Musical Instruments", the "Nickel-Strunz classification", biological
  taxonomies etc. Refers to classification schemes that group objects on the basis
  of object characteristics, not on the basis of themes or topics which the objects
  or works are related to.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido01144
owner: Work
domain_of:
- Work
range: ConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>