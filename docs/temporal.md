---
search:
  boost: 5.0
---

# Slot: temporal


_Temporalidade do objeto._



<div data-search-exclude markdown="1">



URI: [wasth:temporal](https://tradicional.arq.br/schema/temporal)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Event](Event.md) |
| Domain Of | [Thing](Thing.md) |
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
| self | wasth:temporal |
| native | wasth:temporal |




## LinkML Source

<details>
```yaml
name: temporal
description: Temporalidade do objeto.
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Thing
range: Event
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
