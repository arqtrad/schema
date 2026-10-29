---
search:
  boost: 5.0
---

# Slot: lat 


_Latitude em graus decimais (separador decimal: ponto)._



<div data-search-exclude markdown="1">



URI: [wasth:lat](https://tradicional.arq.br/schema/lat)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Latitude](Latitude.md) |
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
| self | wasth:lat |
| native | wasth:lat |




## LinkML Source

<details>
```yaml
name: lat
description: 'Latitude em graus decimais (separador decimal: ponto).'
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: GeographicPoint
domain_of:
- GeographicPoint
range: Latitude
required: true

```
</details></div>