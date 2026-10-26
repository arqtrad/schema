---
search:
  boost: 5.0
---

# Slot: tags


_Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms._



<div data-search-exclude markdown="1">



URI: [wasth:tags](https://tradicional.arq.br/schema/tags)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Thing](Thing.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:tags |
| native | wasth:tags |




## LinkML Source

<details>
```yaml
name: tags
description: Provisional uncontrolled keywords. Prefer `classifications` or `subject`
  for curated vocabulary terms.
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: string
multivalued: true

```
</details></div>
