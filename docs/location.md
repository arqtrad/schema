---
search:
  boost: 5.0
---

# Slot: location 


_Coordenadas geográficas do ponto que permite situar a edificação no mapa para fins ilustrativos. Usar o sistema de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível._

_---------------------------------------------------------------------_

_Representative point location for the place, normally in EPSG:4326 (WGS 84)._



<div data-search-exclude markdown="1">



URI: [geo:hasDefaultGeometry](http://www.opengis.net/ont/geosparql#hasDefaultGeometry)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeographicPoint](GeographicPoint.md) |
| Domain Of | [Site](Site.md) |
| Slot URI | [geo:hasDefaultGeometry](http://www.opengis.net/ont/geosparql#hasDefaultGeometry) |
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
| self | geo:hasDefaultGeometry |
| native | wasth:location |




## LinkML Source

<details>
```yaml
name: location
description: 'Coordenadas geográficas do ponto que permite situar a edificação no
  mapa para fins ilustrativos. Usar o sistema de coordenadas geográficas EPSG:4326
  (WGS84) sempre que possível.

  ---------------------------------------------------------------------

  Representative point location for the place, normally in EPSG:4326 (WGS 84).'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: geo:hasDefaultGeometry
owner: Site
domain_of:
- Site
range: GeographicPoint
required: true
inlined: true

```
</details></div>