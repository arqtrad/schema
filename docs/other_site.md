---
search:
  boost: 5.0
---

# Slot: other_site


_Para casos não contemplados em nenhuma das categorias acima._



<div data-search-exclude markdown="1">



URI: [wasth:other_site](https://tradicional.arq.br/schema/other_site)
Alias: other

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
| Domain Of | [Place](Place.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Place](Place.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:other_site |
| native | wasth:other_site |




## LinkML Source

<details>
```yaml
name: other_site
description: Para casos não contemplados em nenhuma das categorias acima.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: other
owner: Place
domain_of:
- Place
range: Site
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
