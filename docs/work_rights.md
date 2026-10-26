---
search:
  boost: 5.0
---

# Slot: work_rights


_> ⚠️  Este bloco se refere a eventuais direitos autorais sobre A > EDIFICAÇÃO E O SEU PROJETO, não sobre o conteúdo da ficha ou sobre > a iconografia relacionada._

__



<div data-search-exclude markdown="1">



URI: [lido:rightsWorkSet](http://www.lido-schema.org/rightsWorkSet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Right](Right.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [lido:rightsWorkSet](http://www.lido-schema.org/rightsWorkSet) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Work](Work.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lido:rightsWorkSet |
| native | wasth:work_rights |




## LinkML Source

<details>
```yaml
name: work_rights
description: '> ⚠️  Este bloco se refere a eventuais direitos autorais sobre A > EDIFICAÇÃO
  E O SEU PROJETO, não sobre o conteúdo da ficha ou sobre > a iconografia relacionada.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: lido:rightsWorkSet
owner: Work
domain_of:
- Work
range: Right
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
