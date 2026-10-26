---
search:
  boost: 5.0
---

# Slot: coordinates


_No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do polígono (`extent`) com a opção `Get JSON` — copiar apenas os colchetes `[[[ ]]]` e os valores numéricos dentro deles._

__



<div data-search-exclude markdown="1">



URI: [wasth:coordinates](https://tradicional.arq.br/schema/coordinates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeoJSONCoordinateArray](GeoJSONCoordinateArray.md) |
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
| self | wasth:coordinates |
| native | wasth:coordinates |




## LinkML Source

<details>
```yaml
name: coordinates
description: 'No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do polígono
  (`extent`) com a opção `Get JSON` — copiar apenas os colchetes `[[[ ]]]` e os valores
  numéricos dentro deles.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: GeographicExtent
domain_of:
- GeographicExtent
range: GeoJSONCoordinateArray
required: true

```
</details></div>
