---
search:
  boost: 5.0
---

# Slot: style_period


_An index element for the period in which the event happened,_

_comprising information about geologic time scale, archaelogical,_

_historical, or artistic period, style, or art movement, whose_

_characteristics are represented by the object or work._

__

_Note that "Period/Style" corresponds to "Style" in CDWA as shorthand_

_for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)._

__

_Examples may be Neolithic for a period, Impressionist for a style, or_

_Cubism for a movement._

__



<div data-search-exclude markdown="1">



URI: [wasth:style_period](https://tradicional.arq.br/schema/style_period)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StylePeriod](StylePeriod.md) |
| Domain Of | [Event](Event.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Event](Event.md) |












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
description: 'An index element for the period in which the event happened,

  comprising information about geologic time scale, archaelogical,

  historical, or artistic period, style, or art movement, whose

  characteristics are represented by the object or work.


  Note that "Period/Style" corresponds to "Style" in CDWA as shorthand

  for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html).


  Examples may be Neolithic for a period, Impressionist for a style, or

  Cubism for a movement.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: StylePeriod
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
