---
search:
  boost: 5.0
---

# Slot: format_extent


_Indica a parte do objeto que está sendo medida — por exemplo, se a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário controlado._

__



<div data-search-exclude markdown="1">



URI: [wasth:format_extent](https://tradicional.arq.br/schema/format_extent)
Alias: extent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Topic](Topic.md) | Subject or iconographic topic |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Measurement](Measurement.md), [Inscription](Inscription.md), [Topic](Topic.md) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:format_extent |
| native | wasth:format_extent |




## LinkML Source

<details>
```yaml
name: format_extent
description: 'Indica a parte do objeto que está sendo medida — por exemplo, se a altura
  é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário
  controlado.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: extent
domain_of:
- Measurement
- Inscription
- Topic
range: TypedReference
inlined: true

```
</details></div>
