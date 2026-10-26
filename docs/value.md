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
| [Measurements](Measurements.md) | O campo `description` permite uma representação textual das medidas da |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Measurements](Measurements.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Measurements](Measurements.md) |


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
owner: Measurements
domain_of:
- Measurements
range: float
required: true
minimum_value: 0

```
</details></div>
