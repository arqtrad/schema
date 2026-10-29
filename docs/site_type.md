---
search:
  boost: 5.0
---

# Slot: site_type 

<div data-search-exclude markdown="1">



URI: [wasth:site_type](https://tradicional.arq.br/schema/site_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RepositoryType](RepositoryType.md) |
| Domain Of | [Site](Site.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `RepositoryType(geographic)` |
| Owner | [Site](Site.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:site_type |
| native | wasth:site_type |




## LinkML Source

<details>
```yaml
name: site_type
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: RepositoryType(geographic)
alias: type
owner: Site
domain_of:
- Site
range: RepositoryType

```
</details></div>