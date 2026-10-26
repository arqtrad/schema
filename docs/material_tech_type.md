---
search:
  boost: 5.0
---

# Slot: material_tech_type


_Tipo da referência a um material ou técnica usado na obra: material de construção (support), revestimento (medium), técnica, instrumento, cor, etc._

__



<div data-search-exclude markdown="1">



URI: [wasth:material_tech_type](https://tradicional.arq.br/schema/material_tech_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MaterialTechType](MaterialTechType.md) |
| Domain Of | [MaterialTech](MaterialTech.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MaterialTech](MaterialTech.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:material_tech_type |
| native | wasth:material_tech_type |




## LinkML Source

<details>
```yaml
name: material_tech_type
description: 'Tipo da referência a um material ou técnica usado na obra: material
  de construção (support), revestimento (medium), técnica, instrumento, cor, etc.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
owner: MaterialTech
domain_of:
- MaterialTech
range: MaterialTechType
required: true

```
</details></div>
