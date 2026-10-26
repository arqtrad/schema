---
search:
  boost: 5.0
---

# Slot: former_site


_Indica que a edificação não se encontra mais no local indicado, seja porque foi deslocada ou demolida._



<div data-search-exclude markdown="1">



URI: [wasth:former_site](https://tradicional.arq.br/schema/former_site)
Alias: former

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
| self | wasth:former_site |
| native | wasth:former_site |




## LinkML Source

<details>
```yaml
name: former_site
description: Indica que a edificação não se encontra mais no local indicado, seja
  porque foi deslocada ou demolida.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: former
owner: Work
domain_of:
- Work
range: Site
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
