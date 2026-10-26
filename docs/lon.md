---
search:
  boost: 5.0
---

# Slot: lon


_Longitude em graus decimais (separador decimal: ponto)._



<div data-search-exclude markdown="1">



URI: [wasth:lon](https://tradicional.arq.br/schema/lon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Longitude](Longitude.md) |
| Domain Of | [GeographicPoint](GeographicPoint.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeographicPoint](GeographicPoint.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:lon |
| native | wasth:lon |




## LinkML Source

<details>
```yaml
name: lon
description: 'Longitude em graus decimais (separador decimal: ponto).'
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: GeographicPoint
domain_of:
- GeographicPoint
range: Longitude
required: true

```
</details></div>
