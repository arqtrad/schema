---
search:
  boost: 5.0
---

# Slot: location_historic


_Antigas jurisdições ou designações para o lugar onde o objeto se encontra. Para um sítio de onde o objeto foi fisicamente removido, usar `former_site:`._



<div data-search-exclude markdown="1">



URI: [wasth:location_historic](https://tradicional.arq.br/schema/location_historic)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HistoricPlace](HistoricPlace.md) |
| Domain Of | [Work](Work.md) |
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
| self | wasth:location_historic |
| native | wasth:location_historic |




## LinkML Source

<details>
```yaml
name: location_historic
description: Antigas jurisdições ou designações para o lugar onde o objeto se encontra.
  Para um sítio de onde o objeto foi fisicamente removido, usar `former_site:`.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Work
domain_of:
- Work
range: HistoricPlace
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
