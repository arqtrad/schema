---
search:
  boost: 5.0
---

# Slot: lido_term 


_LIDO terminology term._



<div data-search-exclude markdown="1">



URI: [wasth:lido_term](https://tradicional.arq.br/schema/lido_term)
Alias: term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |  no  |






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
| self | wasth:lido_term |
| native | wasth:lido_term |




## LinkML Source

<details>
```yaml
name: lido_term
description: LIDO terminology term.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: term
domain_of:
- TypedReference
range: uriorcurie
pattern: ^http://terminology\.lido-schema\.org/lido[0-9]{5}$

```
</details></div>