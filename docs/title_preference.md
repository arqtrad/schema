---
search:
  boost: 5.0
---

# Slot: title_preference 


_Indica se o nome em questão deve ser oculto ou não, se é uma versão alternativa ou uma variante de grafia, etc._



<div data-search-exclude markdown="1">



URI: [wasth:title_preference](https://tradicional.arq.br/schema/title_preference)
Alias: label_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Appellation](Appellation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LabelType](LabelType.md) |
| Domain Of | [Appellation](Appellation.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `LabelType(alternative)` |
| Owner | [Appellation](Appellation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:title_preference |
| native | wasth:title_preference |




## LinkML Source

<details>
```yaml
name: title_preference
description: Indica se o nome em questão deve ser oculto ou não, se é uma versão alternativa
  ou uma variante de grafia, etc.
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: LabelType(alternative)
alias: label_type
owner: Appellation
domain_of:
- Appellation
range: LabelType

```
</details></div>