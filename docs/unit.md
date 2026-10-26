---
search:
  boost: 5.0
---

# Slot: unit


_Unidade de medida usada no dimensionamento da representação, por exemplo metros ou milímetros. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096) do AAT, ou do nosso próprio [vocabulário controlado]._

__



<div data-search-exclude markdown="1">



URI: [wasth:unit](https://tradicional.arq.br/schema/unit)
Alias: unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Resource](Resource.md), [Measurement](Measurement.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:unit |
| native | wasth:unit |




## LinkML Source

<details>
```yaml
name: unit
description: 'Unidade de medida usada no dimensionamento da representação, por exemplo
  metros ou milímetros. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096)
  do AAT, ou do nosso próprio [vocabulário controlado].

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: unit
domain_of:
- Resource
- Measurement
range: TypedReference
required: true
inlined: true

```
</details></div>
