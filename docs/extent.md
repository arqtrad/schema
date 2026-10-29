---
search:
  boost: 5.0
---

# Slot: extent 


_Área da implantação da edificação ou sítio cadastrado. Usar o sistema de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível._

_---------------------------------------------------------------------_

_Polygonal, multipolygonal, or linear geographic extent associated with the place._



<div data-search-exclude markdown="1">



URI: [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeographicExtent](GeographicExtent.md) |
| Domain Of | [Site](Site.md) |
| Slot URI | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) |
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
| native | wasth:extent |




## LinkML Source

<details>
```yaml
name: extent
description: 'Área da implantação da edificação ou sítio cadastrado. Usar o sistema
  de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível.

  ---------------------------------------------------------------------

  Polygonal, multipolygonal, or linear geographic extent associated with the place.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: geo:hasGeometry
owner: Site
domain_of:
- Site
range: GeographicExtent
inlined: true

```
</details></div>