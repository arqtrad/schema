---
search:
  boost: 5.0
---

# Slot: measurement_value 


_Valor numérico, usar ponto como separador decimal._



<div data-search-exclude markdown="1">



URI: [wasth:measurement_value](https://tradicional.arq.br/schema/measurement_value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |  no  |






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
| self | wasth:measurement_value |
| native | wasth:measurement_value |




## LinkML Source

<details>
```yaml
name: measurement_value
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