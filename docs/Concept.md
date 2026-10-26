---
search:
  boost: 5.0
---

# Slot: concept

<div data-search-exclude markdown="1">



URI: [wasth:concept](https://tradicional.arq.br/schema/concept)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Topic](Topic.md) | Subject or iconographic topic |  yes  |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos direitos ou ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md) |
| Domain Of | [Right](Right.md), [Topic](Topic.md) |
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
| self | wasth:concept |
| native | wasth:concept |




## LinkML Source

<details>
```yaml
name: concept
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: name
domain_of:
- Right
- Topic
range: Concept
required: true

```
</details></div>
