---
search:
  boost: 5.0
---

# Slot: event_name 


_Identifica o evento ralacionado._

__



<div data-search-exclude markdown="1">



URI: [wasth:event_name](https://tradicional.arq.br/schema/event_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedEvent](RelatedEvent.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Event](Event.md) |
| Domain Of | [RelatedEvent](RelatedEvent.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RelatedEvent](RelatedEvent.md) |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Symmetric | Yes |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:event_name |
| native | wasth:event_name |




## LinkML Source

<details>
```yaml
name: event_name
description: 'Identifica o evento ralacionado.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: RelatedEvent
domain_of:
- RelatedEvent
symmetric: true
range: Event
required: true
multivalued: true
inlined: false

```
</details></div>