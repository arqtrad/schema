---
search:
  boost: 5.0
---

# Slot: relation 


_Um conceito com o qual existe um relacionamento semântico associativo. Usar em referência ao nosso próprio vocabulário controlado._



<div data-search-exclude markdown="1">



URI: [skos:related](http://www.w3.org/2004/02/skos/core#related)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Concept](Concept.md) |
| Slot URI | [skos:related](http://www.w3.org/2004/02/skos/core#related) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Concept](Concept.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:related |
| native | wasth:relation |




## LinkML Source

<details>
```yaml
name: relation
description: Um conceito com o qual existe um relacionamento semântico associativo.
  Usar em referência ao nosso próprio vocabulário controlado.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:related
owner: Concept
domain_of:
- Concept
range: ConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>