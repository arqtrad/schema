---
search:
  boost: 5.0
---

# Slot: intended_site


_Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser construída._



<div data-search-exclude markdown="1">



URI: [wasth:intended_site](https://tradicional.arq.br/schema/intended_site)
Alias: intended

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
| Domain Of | [Work](Work.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | wasth:intended_site |
| native | wasth:intended_site |




## LinkML Source

<details>
```yaml
name: intended_site
description: Sinaliza que a edificação devia ocupar um certo local, mas não chegou
  a ser construída.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: intended
owner: Work
domain_of:
- Work
range: Site
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
