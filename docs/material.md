---
search:
  boost: 5.0
---

# Slot: material

<div data-search-exclude markdown="1">



URI: [wasth:material](https://tradicional.arq.br/schema/material)
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
| self | wasth:material |
| native | wasth:material |




## LinkML Source

<details>
```yaml
name: material
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
