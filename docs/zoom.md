---
search:
  boost: 5.0
---

# Slot: zoom 


_Usado para visualizar o mapa mais de longe se a precisão das coordenadas for baixa._

__



<div data-search-exclude markdown="1">



URI: [wasth:zoom](https://tradicional.arq.br/schema/zoom)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [GeographicPoint](GeographicPoint.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `integer(13)` |
| Owner | [GeographicPoint](GeographicPoint.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 18 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:zoom |
| native | wasth:zoom |




## LinkML Source

<details>
```yaml
name: zoom
description: 'Usado para visualizar o mapa mais de longe se a precisão das coordenadas
  for baixa.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: integer(13)
owner: GeographicPoint
domain_of:
- GeographicPoint
range: integer
minimum_value: 0
maximum_value: 18

```
</details></div>