---
search:
  boost: 5.0
---

# Slot: site


_A localização real, atual da edificação — é o que será usado em quase todos os casos._



<div data-search-exclude markdown="1">



URI: [wasth:site](https://tradicional.arq.br/schema/site)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
| Domain Of | [Place](Place.md), [Repository](Repository.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:site |
| native | wasth:site |




## LinkML Source

<details>
```yaml
name: site
description: A localização real, atual da edificação — é o que será usado em quase
  todos os casos.
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Place
- Repository
range: Site
required: true
inlined: true

```
</details></div>
