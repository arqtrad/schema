---
search:
  boost: 5.0
---

# Slot: style_period 


_Denomina o(s) período(s) em que o evento decorreu, em qualquer escala relevante para o conhecimento : geológica, arqueológica, histórica ou artística. A identificação do período ou estilo deve ser relevante para as características que o objeto adquiriu devido a esse evento, não somente uma coincidência cronológica._

_---------------------------------------------------------------------_

_An index element for the period in which the event happened, comprising information about geologic time scale, archaelogical, historical, or artistic period, style, or art movement, whose characteristics are represented by the object or work._

_Note that "Period/Style" corresponds to "Style" in CDWA as shorthand for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)._

_Examples may be Neolithic for a period, Impressionist for a style, or Cubism for a movement._

__



<div data-search-exclude markdown="1">



URI: [wasth:style_period](https://tradicional.arq.br/schema/style_period)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StylePeriod](StylePeriod.md) |
| Domain Of | [Event](Event.md), [Work](Work.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:style_period |
| native | wasth:style_period |




## LinkML Source

<details>
```yaml
name: style_period
description: 'Denomina o(s) período(s) em que o evento decorreu, em qualquer escala
  relevante para o conhecimento : geológica, arqueológica, histórica ou artística.
  A identificação do período ou estilo deve ser relevante para as características
  que o objeto adquiriu devido a esse evento, não somente uma coincidência cronológica.

  ---------------------------------------------------------------------

  An index element for the period in which the event happened, comprising information
  about geologic time scale, archaelogical, historical, or artistic period, style,
  or art movement, whose characteristics are represented by the object or work.

  Note that "Period/Style" corresponds to "Style" in CDWA as shorthand for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html).

  Examples may be Neolithic for a period, Impressionist for a style, or Cubism for
  a movement.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Event
- Work
range: StylePeriod
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>