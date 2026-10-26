---
search:
  boost: 5.0
---

# Slot: value


_Valor numérico, usar ponto como separador decimal._



<div data-search-exclude markdown="1">



URI: [wasth:value](https://tradicional.arq.br/schema/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Measurement](Measurement.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Measurement](Measurement.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:value |
| native | wasth:value |




## LinkML Source

<details>
```yaml
name: value
description: Valor numérico, usar ponto como separador decimal.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: value
owner: Measurement
domain_of:
- Measurement
range: float
required: true
minimum_value: 0

```
</details></div>
