---
search:
  boost: 5.0
---

# Slot: relation


_Um conceito com o qual existe um relacionamento semântico associativo. Usar principalmente em referência a vocabulários externos, como o Getty Art and Architecture Thesaurus._



<div data-search-exclude markdown="1">



URI: [skos:relation](http://www.w3.org/2004/02/skos/core#relation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelatedConceptReference](RelatedConceptReference.md) |
| Domain Of | [Concept](Concept.md) |
| Slot URI | [skos:relation](http://www.w3.org/2004/02/skos/core#relation) |
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
| self | skos:relation |
| native | wasth:relation |




## LinkML Source

<details>
```yaml
name: relation
description: Um conceito com o qual existe um relacionamento semântico associativo.
  Usar principalmente em referência a vocabulários externos, como o Getty Art and
  Architecture Thesaurus.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:relation
owner: Concept
domain_of:
- Concept
range: RelatedConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
