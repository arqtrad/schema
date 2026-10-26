---
search:
  boost: 5.0
---

# Slot: media

<div data-search-exclude markdown="1">



URI: [wasth:media](https://tradicional.arq.br/schema/media)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaObject](MediaObject.md) |
| Domain Of | [RelatedObject](RelatedObject.md), [Event](Event.md), [Work](Work.md) |
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
| self | wasth:media |
| native | wasth:media |




## LinkML Source

<details>
```yaml
name: media
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- RelatedObject
- Event
- Work
range: MediaObject
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
