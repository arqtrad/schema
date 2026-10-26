---
search:
  boost: 5.0
---

# Slot: term


_LIDO terminology term._



<div data-search-exclude markdown="1">



URI: [wasth:term](https://tradicional.arq.br/schema/term)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [TypedReference](TypedReference.md) |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^http://terminology\.lido-schema\.org/lido[0-9]{5}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:term |
| native | wasth:term |




## LinkML Source

<details>
```yaml
name: term
description: LIDO terminology term.
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- TypedReference
range: uriorcurie
pattern: ^http://terminology\.lido-schema\.org/lido[0-9]{5}$

```
</details></div>
