---
search:
  boost: 5.0
---

# Slot: rights_type 


_Determina se os direitos ora descritos são uma licença específica (padrão) ou expressão genérica de copyright._

_---------------------------------------------------------------------_

_Qualifies the kind of rights type, whether it refers to a generic kind of right, like copyright or performance rights, or is a specific rights or license statement, for instance, Rights Statements or Creative Commons Licenses._

__



<div data-search-exclude markdown="1">



URI: [wasth:rights_type](https://tradicional.arq.br/schema/rights_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RightsType](RightsType.md) |
| Domain Of | [Right](Right.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Right](Right.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:rights_type |
| native | wasth:rights_type |




## LinkML Source

<details>
```yaml
name: rights_type
description: 'Determina se os direitos ora descritos são uma licença específica (padrão)
  ou expressão genérica de copyright.

  ---------------------------------------------------------------------

  Qualifies the kind of rights type, whether it refers to a generic kind of right,
  like copyright or performance rights, or is a specific rights or license statement,
  for instance, Rights Statements or Creative Commons Licenses.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Right
domain_of:
- Right
range: RightsType
required: true

```
</details></div>