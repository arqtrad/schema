---
search:
  boost: 5.0
---

# Slot: related_works

<div data-search-exclude markdown="1">



URI: [skos:related](http://www.w3.org/2004/02/skos/core#related)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelatedWork](RelatedWork.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [skos:related](http://www.w3.org/2004/02/skos/core#related) |
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
| self | skos:related |
| native | wasth:related_works |




## LinkML Source

<details>
```yaml
name: related_works
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:related
domain_of:
- Work
range: RelatedWork
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
