---
search:
  boost: 5.0
---

# Slot: inscription_type 


_Determina a natureza da inscrição._

__



<div data-search-exclude markdown="1">



URI: [wasth:inscription_type](https://tradicional.arq.br/schema/inscription_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InscriptionType](InscriptionType.md) |
| Domain Of | [Inscription](Inscription.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(text)` |
| Owner | [Inscription](Inscription.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:inscription_type |
| native | wasth:inscription_type |




## LinkML Source

<details>
```yaml
name: inscription_type
description: 'Determina a natureza da inscrição.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: string(text)
alias: type
owner: Inscription
domain_of:
- Inscription
range: InscriptionType
required: true

```
</details></div>