---
search:
  boost: 5.0
---

# Slot: event_place 


_Lugares associados ao evento, sem incluir o próprio local no qual se situa a edificação._

__



<div data-search-exclude markdown="1">



URI: [wasth:event_place](https://tradicional.arq.br/schema/event_place)
Alias: place

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
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
| self | wasth:event_place |
| native | wasth:event_place |




## LinkML Source

<details>
```yaml
name: event_place
description: 'Lugares associados ao evento, sem incluir o próprio local no qual se
  situa a edificação.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: place
owner: Event
domain_of:
- Event
range: Site
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>