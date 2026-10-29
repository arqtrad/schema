---
search:
  boost: 5.0
---

# Slot: date_type 


_Qualifica a confiabilidade da data como sendo conhecida ou estimada. A confiabilidade independe do grau de precisão da data._

__



<div data-search-exclude markdown="1">



URI: [wasth:date_type](https://tradicional.arq.br/schema/date_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EventDate](EventDate.md) | Expressão complexa de uma data que pode se referir ao começo ou ao término de... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DateType](DateType.md) |
| Domain Of | [EventDate](EventDate.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EventDate](EventDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:date_type |
| native | wasth:date_type |




## LinkML Source

<details>
```yaml
name: date_type
description: 'Qualifica a confiabilidade da data como sendo conhecida ou estimada.
  A confiabilidade independe do grau de precisão da data.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
owner: EventDate
domain_of:
- EventDate
range: DateType
required: true

```
</details></div>