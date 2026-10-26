---
search:
  boost: 5.0
---

# Slot: culture


_An index element for the cultural context from which the object/work in focus originated. Used if the creator or producer is unknown, or if the cultural context is of particular interest. Examples may include the name of a culture, a nation, or an ethnic group._



<div data-search-exclude markdown="1">



URI: [wasth:culture](https://tradicional.arq.br/schema/culture)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
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
| self | wasth:culture |
| native | wasth:culture |




## LinkML Source

<details>
```yaml
name: culture
description: An index element for the cultural context from which the object/work
  in focus originated. Used if the creator or producer is unknown, or if the cultural
  context is of particular interest. Examples may include the name of a culture, a
  nation, or an ethnic group.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
