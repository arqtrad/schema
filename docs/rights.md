---
search:
  boost: 5.0
---

# Slot: rights 

<div data-search-exclude markdown="1">



URI: [wasth:rights](https://tradicional.arq.br/schema/rights)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Right](Right.md) |
| Domain Of | [MediaObject](MediaObject.md) |
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
| self | wasth:rights |
| native | wasth:rights |




## LinkML Source

<details>
```yaml
name: rights
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- MediaObject
range: Right
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>