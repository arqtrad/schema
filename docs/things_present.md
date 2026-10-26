---
search:
  boost: 5.0
---

# Slot: things_present


_A set of structured information for a related object or work that is or was present at the event in focus. Repeated if there are multiple related objects or works._



<div data-search-exclude markdown="1">



URI: [wasth:things_present](https://tradicional.arq.br/schema/things_present)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelatedWork](RelatedWork.md) |
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
| self | wasth:things_present |
| native | wasth:things_present |




## LinkML Source

<details>
```yaml
name: things_present
description: A set of structured information for a related object or work that is
  or was present at the event in focus. Repeated if there are multiple related objects
  or works.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: RelatedWork
multivalued: true

```
</details></div>
