---
search:
  boost: 5.0
---

# Slot: part_of


_A set of structured information about a place that is the broader context for the place in focus, such as the district, state, or nation to which a city belongs._



<div data-search-exclude markdown="1">



URI: [lido:partOfPlace](http://www.lido-schema.org/partOfPlace)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeonamesId](GeonamesId.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [lido:partOfPlace](http://www.lido-schema.org/partOfPlace) |
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
| self | lido:partOfPlace |
| native | wasth:part_of |




## LinkML Source

<details>
```yaml
name: part_of
description: A set of structured information about a place that is the broader context
  for the place in focus, such as the district, state, or nation to which a city belongs.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: lido:partOfPlace
owner: Work
domain_of:
- Work
range: GeonamesId
inlined: true

```
</details></div>
