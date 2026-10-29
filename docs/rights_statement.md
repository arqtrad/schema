---
search:
  boost: 5.0
---

# Slot: rights_statement 


_Referencia, preferencialmente por meio de uma URI, as informações específicas dos direitos autorais incidentes sobre o item descrito._

_Por padrão, as casas tradicionais pertencem ao domínio público até prova em contrário. Essa informação e a declaração de direitos NKC (Sem direito autoral conhecido) NÃO PODE ser omitida da ficha. Para o domínio público, portanto, indicar a referência : <https://rightsstatements.org/vocab/NKC/1.0/>._

_---------------------------------------------------------------------_

_An index element for rights information being recorded. This can refer to a generic kind of right, such as copyright or a related right, but also be a specific rights or license statement like a standardized statement on copyright, usage, or access rights._

__



<div data-search-exclude markdown="1">



URI: [wasth:rights_statement](https://tradicional.arq.br/schema/rights_statement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
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
| self | wasth:rights_statement |
| native | wasth:rights_statement |




## LinkML Source

<details>
```yaml
name: rights_statement
description: 'Referencia, preferencialmente por meio de uma URI, as informações específicas
  dos direitos autorais incidentes sobre o item descrito.

  Por padrão, as casas tradicionais pertencem ao domínio público até prova em contrário.
  Essa informação e a declaração de direitos NKC (Sem direito autoral conhecido) NÃO
  PODE ser omitida da ficha. Para o domínio público, portanto, indicar a referência :
  <https://rightsstatements.org/vocab/NKC/1.0/>.

  ---------------------------------------------------------------------

  An index element for rights information being recorded. This can refer to a generic
  kind of right, such as copyright or a related right, but also be a specific rights
  or license statement like a standardized statement on copyright, usage, or access
  rights.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Right
domain_of:
- Right
range: TypedReference
required: true
inlined: true

```
</details></div>