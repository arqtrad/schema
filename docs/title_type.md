---
search:
  boost: 5.0
---

# Slot: title_type


_Indica se o título é um nome próprio, descritivo, etc._



<div data-search-exclude markdown="1">



URI: [wasth:title_type](https://tradicional.arq.br/schema/title_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Appellation](Appellation.md) |  |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  yes  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TitleType](TitleType.md) |
| Domain Of | [Thing](Thing.md), [Appellation](Appellation.md) |
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
| self | wasth:title_type |
| native | wasth:title_type |




## LinkML Source

<details>
```yaml
name: title_type
description: Indica se o título é um nome próprio, descritivo, etc.
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
domain_of:
- Thing
- Appellation
range: TitleType
required: true

```
</details></div>
