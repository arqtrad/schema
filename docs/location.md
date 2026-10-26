---
search:
  boost: 5.0
---

# Slot: location


_Representative point location for the place, normally in EPSG:4326 (WGS 84)._



<div data-search-exclude markdown="1">



URI: [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeographicPoint](GeographicPoint.md) |
| Domain Of | [Site](Site.md) |
| Slot URI | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Site](Site.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geo:hasGeometry |
| native | wasth:location |




## LinkML Source

<details>
```yaml
name: location
description: Representative point location for the place, normally in EPSG:4326 (WGS
  84).
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: geo:hasGeometry
owner: Site
domain_of:
- Site
range: GeographicPoint
required: true
inlined: true

```
</details></div>
