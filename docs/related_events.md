---
search:
  boost: 5.0
---

# Slot: related_events


_A set of structured information about an event related to the event in focus, indicating the type of relationship where applicable._



<div data-search-exclude markdown="1">



URI: [wasth:related_events](https://tradicional.arq.br/schema/related_events)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelatedEvent](RelatedEvent.md) |
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
| self | wasth:related_events |
| native | wasth:related_events |




## LinkML Source

<details>
```yaml
name: related_events
description: A set of structured information about an event related to the event in
  focus, indicating the type of relationship where applicable.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: RelatedEvent
multivalued: true

```
</details></div>
