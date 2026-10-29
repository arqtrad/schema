---
search:
  boost: 5.0
---

# Slot: location_historic_name 


_Identificação do local com referência a um vocabulário controlado ou repositório de topônimos tal como o geonames._

__



<div data-search-exclude markdown="1">



URI: [wasth:location_historic_name](https://tradicional.arq.br/schema/location_historic_name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocationHistoric](LocationHistoric.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [LocationHistoric](LocationHistoric.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LocationHistoric](LocationHistoric.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:location_historic_name |
| native | wasth:location_historic_name |




## LinkML Source

<details>
```yaml
name: location_historic_name
description: 'Identificação do local com referência a um vocabulário controlado ou
  repositório de topônimos tal como o geonames.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: name
owner: LocationHistoric
domain_of:
- LocationHistoric
range: TypedReference
required: true
inlined: true

```
</details></div>