---
search:
  boost: 5.0
---

# Slot: narrower


_Um conceito de significação mais específica. Conceitos específicos são tipicamente representados como descendentes em uma hierarquia de conceitos (árvore)._



<div data-search-exclude markdown="1">



URI: [skos:narrower](http://www.w3.org/2004/02/skos/core#narrower)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Concept](Concept.md) |
| Slot URI | [skos:narrower](http://www.w3.org/2004/02/skos/core#narrower) |
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
| self | skos:narrower |
| native | wasth:narrower |




## LinkML Source

<details>
```yaml
name: narrower
description: Um conceito de significação mais específica. Conceitos específicos são
  tipicamente representados como descendentes em uma hierarquia de conceitos (árvore).
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:narrower
owner: Concept
domain_of:
- Concept
range: ConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
