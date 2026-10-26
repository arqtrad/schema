---
search:
  boost: 5.0
---

# Slot: measurements


_A wrapper for information about the dimensions, or other measurements, of the object/work in focus. May also include extents of the parts of a complex object or work._

__



<div data-search-exclude markdown="1">



URI: [wasth:measurements](https://tradicional.arq.br/schema/measurements)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Measurement](Measurement.md) |
| Domain Of | [MediaObject](MediaObject.md), [Event](Event.md), [Work](Work.md) |
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
| self | wasth:measurements |
| native | wasth:measurements |




## LinkML Source

<details>
```yaml
name: measurements
description: 'A wrapper for information about the dimensions, or other measurements,
  of the object/work in focus. May also include extents of the parts of a complex
  object or work.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- MediaObject
- Event
- Work
range: Measurement
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
