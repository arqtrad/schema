---
search:
  boost: 5.0
---

# Slot: legal_body_type

<div data-search-exclude markdown="1">



URI: [wasth:legal_body_type](https://tradicional.arq.br/schema/legal_body_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LegalBody](LegalBody.md) | Personal, corporate, family, or other responsible body |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RepositoryType](RepositoryType.md) |
| Domain Of | [LegalBody](LegalBody.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `string(corporate)` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:legal_body_type |
| native | wasth:legal_body_type |




## LinkML Source

<details>
```yaml
name: legal_body_type
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: string(corporate)
alias: type
domain_of:
- LegalBody
range: RepositoryType

```
</details></div>
