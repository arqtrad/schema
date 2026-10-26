---
search:
  boost: 5.0
---

# Slot: method


_An index element for the method by which the event is or was carried out. Examples may include an acquisition method or a field collection method._



<div data-search-exclude markdown="1">



URI: [wasth:method](https://tradicional.arq.br/schema/method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
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
| self | wasth:method |
| native | wasth:method |




## LinkML Source

<details>
```yaml
name: method
description: An index element for the method by which the event is or was carried
  out. Examples may include an acquisition method or a field collection method.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: ConceptReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
