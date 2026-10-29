---
search:
  boost: 5.0
---

# Slot: classification_subject 


_❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura._

_---------------------------------------------------------------------_

_A broad category for grouping objects or works on the basis of a topical association, including thematic or systematic classification, or an assignment by discipline. The relationship between an object/work and a subject category is a kind of membership based on ascription rather than a generic is-a relation._



<div data-search-exclude markdown="1">



URI: [term:lido00932](http://terminology.lido-schema.org/lido00932)
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
| Slot URI | [term:lido00932](http://terminology.lido-schema.org/lido00932) |
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
| self | term:lido00932 |
| native | wasth:classification_subject |




## LinkML Source

<details>
```yaml
name: classification_subject
description: '❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez
  ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório
  no padrão LIDO nem no perfil de aplicação para arquitetura.

  ---------------------------------------------------------------------

  A broad category for grouping objects or works on the basis of a topical association,
  including thematic or systematic classification, or an assignment by discipline.
  The relationship between an object/work and a subject category is a kind of membership
  based on ascription rather than a generic is-a relation.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido00932
owner: Work
domain_of:
- Work
range: ConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>