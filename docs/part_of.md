---
search:
  boost: 5.0
---

# Slot: part_of 


_Permite identificar o contexto geográfico ou administrativo ao qual a edificação se subordina, ou ainda um conjunto arquitetônico, urbanístico ou conceitual (por exemplo, uma série de casas) do qual ela faz parte._

_---------------------------------------------------------------------_

_A set of structured information about a place that is the broader context for the place in focus, such as the district, state, or nation to which a city belongs._



<div data-search-exclude markdown="1">



URI: [dcterms:isPartOf](http://purl.org/dc/terms/isPartOf)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [dcterms:isPartOf](http://purl.org/dc/terms/isPartOf) |
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
| self | dcterms:isPartOf |
| native | wasth:part_of |




## LinkML Source

<details>
```yaml
name: part_of
description: 'Permite identificar o contexto geográfico ou administrativo ao qual
  a edificação se subordina, ou ainda um conjunto arquitetônico, urbanístico ou conceitual
  (por exemplo, uma série de casas) do qual ela faz parte.

  ---------------------------------------------------------------------

  A set of structured information about a place that is the broader context for the
  place in focus, such as the district, state, or nation to which a city belongs.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:isPartOf
owner: Work
domain_of:
- Work
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>