---
search:
  boost: 5.0
---

# Slot: technique

<div data-search-exclude markdown="1">



URI: [wasth:technique](https://tradicional.arq.br/schema/technique)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MaterialTech](MaterialTech.md) |
| Domain Of | [Event](Event.md), [Work](Work.md) |
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
| self | wasth:technique |
| native | wasth:technique |




## LinkML Source

<details>
```yaml
name: technique
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Event
- Work
range: MaterialTech
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
