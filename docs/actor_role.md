---
search:
  boost: 5.0
---

# Slot: actor_role


_Identificação de um agente e do seu papel no evento._



<div data-search-exclude markdown="1">



URI: [wasth:actor_role](https://tradicional.arq.br/schema/actor_role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Actor](Actor.md) |
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
| self | wasth:actor_role |
| native | wasth:actor_role |




## LinkML Source

<details>
```yaml
name: actor_role
description: Identificação de um agente e do seu papel no evento.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: Actor
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
