---
search:
  boost: 5.0
---

# Slot: broader


_Um conceito de significação mais genérica. Conceitos genéricos são tipicamente representados como pais em uma hierarquia de conceitos (árvore)._



<div data-search-exclude markdown="1">



URI: [skos:broader](http://www.w3.org/2004/02/skos/core#broader)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BroaderConceptReference](BroaderConceptReference.md) |
| Domain Of | [Concept](Concept.md) |
| Slot URI | [skos:broader](http://www.w3.org/2004/02/skos/core#broader) |
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
| self | skos:broader |
| native | wasth:broader |




## LinkML Source

<details>
```yaml
name: broader
description: Um conceito de significação mais genérica. Conceitos genéricos são tipicamente
  representados como pais em uma hierarquia de conceitos (árvore).
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:broader
owner: Concept
domain_of:
- Concept
range: BroaderConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
