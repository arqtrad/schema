---
search:
  boost: 5.0
---

# Slot: measurement_type 


_designa a natureza da medida : largura, altura, área, etc. — usar um dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820) do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos um vocabulário controlado próprio._

__



<div data-search-exclude markdown="1">



URI: [wasth:measurement_type](https://tradicional.arq.br/schema/measurement_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MeasurementType](MeasurementType.md) |
| Domain Of | [Measurement](Measurement.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `MeasurementType(proper)` |
| Owner | [Measurement](Measurement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:measurement_type |
| native | wasth:measurement_type |




## LinkML Source

<details>
```yaml
name: measurement_type
description: 'designa a natureza da medida : largura, altura, área, etc. — usar um
  dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820)
  do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos
  um vocabulário controlado próprio.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: MeasurementType(proper)
alias: type
owner: Measurement
domain_of:
- Measurement
range: MeasurementType

```
</details></div>