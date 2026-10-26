---
search:
  boost: 5.0
---

# Slot: alt


_Altitude em metros (separador decimal: ponto)_



<div data-search-exclude markdown="1">



URI: [wasth:alt](https://tradicional.arq.br/schema/alt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [GeographicPoint](GeographicPoint.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeographicPoint](GeographicPoint.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | -1000 |
| Maximum Value | 10000 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:alt |
| native | wasth:alt |




## LinkML Source

<details>
```yaml
name: alt
description: 'Altitude em metros (separador decimal: ponto)'
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: GeographicPoint
domain_of:
- GeographicPoint
range: float
minimum_value: -1000
maximum_value: 10000

```
</details></div>
