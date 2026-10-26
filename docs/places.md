---
search:
  boost: 5.0
---

# Slot: places


_Lugares associados ao evento, sem incluir o próprio local no qual se situa a edificação._

__



<div data-search-exclude markdown="1">



URI: [wasth:places](https://tradicional.arq.br/schema/places)
Alias: places

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EventPlace](EventPlace.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
| Domain Of | [EventPlace](EventPlace.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EventPlace](EventPlace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:places |
| native | wasth:places |




## LinkML Source

<details>
```yaml
name: places
description: 'Lugares associados ao evento, sem incluir o próprio local no qual se
  situa a edificação.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: places
owner: EventPlace
domain_of:
- EventPlace
range: Site
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
