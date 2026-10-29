---
search:
  boost: 5.0
---

# Slot: repository_type 

<div data-search-exclude markdown="1">



URI: [wasth:repository_type](https://tradicional.arq.br/schema/repository_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RepositoryType](RepositoryType.md) |
| Domain Of | [Repository](Repository.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `RepositoryType(corporate)` |
| Owner | [Repository](Repository.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:repository_type |
| native | wasth:repository_type |




## LinkML Source

<details>
```yaml
name: repository_type
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: RepositoryType(corporate)
owner: Repository
domain_of:
- Repository
range: RepositoryType

```
</details></div>