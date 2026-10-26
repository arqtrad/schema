---
search:
  boost: 5.0
---

# Slot: title


_The preferred human-readable label for a Thing._



<div data-search-exclude markdown="1">



URI: [dcterms:title](http://purl.org/dc/terms/title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:title](http://purl.org/dc/terms/title) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | dcterms:title |
| native | wasth:title |
| exact | schema:name |




## LinkML Source

<details>
```yaml
name: title
description: The preferred human-readable label for a Thing.
from_schema: https://tradicional.arq.br/schema
exact_mappings:
- schema:name
rank: 1000
slot_uri: dcterms:title
owner: Thing
domain_of:
- Thing
range: string
required: true

```
</details></div>
