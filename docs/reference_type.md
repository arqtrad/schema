---
search:
  boost: 5.0
---

# Slot: reference_type

<div data-search-exclude markdown="1">



URI: [wasth:reference_type](https://tradicional.arq.br/schema/reference_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceType](ReferenceType.md) |
| Domain Of | [TypedReference](TypedReference.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(uri)` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:reference_type |
| native | wasth:reference_type |




## LinkML Source

<details>
```yaml
name: reference_type
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: string(uri)
alias: type
domain_of:
- TypedReference
range: ReferenceType

```
</details></div>
