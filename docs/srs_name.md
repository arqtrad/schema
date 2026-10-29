---
search:
  boost: 5.0
---

# Slot: srs_name 


_Names the coordinate reference system (CRS) that defines the semantics of the lat/long pair according to the ISO6709 standard. Sempre que possível, usar EPSG:4326, senão os sistemas de referência nacionais._



<div data-search-exclude markdown="1">



URI: [wasth:srs_name](https://tradicional.arq.br/schema/srs_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [GeographicPoint](GeographicPoint.md), [GeographicExtent](GeographicExtent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:srs_name |
| native | wasth:srs_name |




## LinkML Source

<details>
```yaml
name: srs_name
description: Names the coordinate reference system (CRS) that defines the semantics
  of the lat/long pair according to the ISO6709 standard. Sempre que possível, usar
  EPSG:4326, senão os sistemas de referência nacionais.
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- GeographicPoint
- GeographicExtent
range: uriorcurie
recommended: true

```
</details></div>