---
search:
  boost: 5.0
---

# Slot: actor_extent


_Parte da obra sobre a qual o agente interveio._



<div data-search-exclude markdown="1">



URI: [wasth:actor_extent](https://tradicional.arq.br/schema/actor_extent)
Alias: extent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Actor](Actor.md) | Agent and role in an event |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Actor](Actor.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Actor](Actor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:actor_extent |
| native | wasth:actor_extent |




## LinkML Source

<details>
```yaml
name: actor_extent
description: Parte da obra sobre a qual o agente interveio.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: extent
owner: Actor
domain_of:
- Actor
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
