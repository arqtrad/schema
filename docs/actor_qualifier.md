---
search:
  boost: 5.0
---

# Slot: actor_qualifier


_For the Attribution Qualifier Actor element choose a concept URI from_

_the [attribution qualifiers hierarchy](http://vocab.getty.edu/hier/aat/300404264)_

_of the Art & Architecture Thesaurus, or another linked open_

_vocabulary._

__



<div data-search-exclude markdown="1">



URI: [wasth:actor_qualifier](https://tradicional.arq.br/schema/actor_qualifier)
Alias: qualifier

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
| self | wasth:actor_qualifier |
| native | wasth:actor_qualifier |




## LinkML Source

<details>
```yaml
name: actor_qualifier
description: 'For the Attribution Qualifier Actor element choose a concept URI from

  the [attribution qualifiers hierarchy](http://vocab.getty.edu/hier/aat/300404264)

  of the Art & Architecture Thesaurus, or another linked open

  vocabulary.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: qualifier
owner: Actor
domain_of:
- Actor
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
