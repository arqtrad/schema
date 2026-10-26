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
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Place](Place.md) |
| Domain Of | [Place](Place.md) |
| Slot URI | [lido:partOfPlace](http://www.lido-schema.org/partOfPlace) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Place](Place.md) |












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
owner: Place
domain_of:
- Place
range: Place
inlined: false

```
</details></div>
