---
search:
  boost: 5.0
---

# Slot: perspective


_Tipo de vista do desenho. Usar a numeração da ISO 19650–2 :_

__

_  - 0 = geral_

_  - 1 = planta baixa (padrão, pode ser omitido)_

_  - 2 = elevação_

_  - 3 = corte_

_  - 4 = mapa de elementos_

_  - 5 = detalhe_

_  - 6 = mapa de revestimentos_

_  - 7 = planta de forro_

_  - 8 = vista ou modelo 3D_

_  - 9 = definido pelo agente_

__



<div data-search-exclude markdown="1">



URI: [wasth:perspective](https://tradicional.arq.br/schema/perspective)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Resource](Resource.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `integer(1)` |
| Owner | [Resource](Resource.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 9 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:perspective |
| native | wasth:perspective |




## LinkML Source

<details>
```yaml
name: perspective
description: "Tipo de vista do desenho. Usar a numeração da ISO 19650–2 :\n\n  - 0\
  \ = geral\n  - 1 = planta baixa (padrão, pode ser omitido)\n  - 2 = elevação\n \
  \ - 3 = corte\n  - 4 = mapa de elementos\n  - 5 = detalhe\n  - 6 = mapa de revestimentos\n\
  \  - 7 = planta de forro\n  - 8 = vista ou modelo 3D\n  - 9 = definido pelo agente\n"
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: integer(1)
owner: Resource
domain_of:
- Resource
range: integer
minimum_value: 0
maximum_value: 9

```
</details></div>
