---
search:
  boost: 5.0
---

# Slot: geometry_type


_Tipo da geometria descrita pelas coordenadas._



<div data-search-exclude markdown="1">



URI: [wasth:geometry_type](https://tradicional.arq.br/schema/geometry_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeometryType](GeometryType.md) |
| Domain Of | [GeographicExtent](GeographicExtent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeographicExtent](GeographicExtent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:geometry_type |
| native | wasth:geometry_type |




## LinkML Source

<details>
```yaml
name: geometry_type
description: Tipo da geometria descrita pelas coordenadas.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
owner: GeographicExtent
domain_of:
- GeographicExtent
range: GeometryType
required: true

```
</details></div>
