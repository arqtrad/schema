---
search:
  boost: 5.0
---

# Slot: location_historic_type 


_Define se o local histórico designa uma jurisdição, um topônimo antigo, ou outro._

__



<div data-search-exclude markdown="1">



URI: [wasth:location_historic_type](https://tradicional.arq.br/schema/location_historic_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LocationHistoric](LocationHistoric.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RepositoryType](RepositoryType.md) |
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
| self | wasth:location_historic_type |
| native | wasth:location_historic_type |




## LinkML Source

<details>
```yaml
name: location_historic_type
description: 'Define se o local histórico designa uma jurisdição, um topônimo antigo,
  ou outro.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
owner: LocationHistoric
domain_of:
- LocationHistoric
range: RepositoryType
required: true

```
</details></div>