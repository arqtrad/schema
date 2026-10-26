---
search:
  boost: 5.0
---

# Slot: id


_Unique identifier for this object._



<div data-search-exclude markdown="1">



URI: [dcterms:identifier](http://purl.org/dc/terms/identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  yes  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  yes  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:identifier](http://purl.org/dc/terms/identifier) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:identifier |
| native | wasth:id |




## LinkML Source

<details>
```yaml
name: id
description: Unique identifier for this object.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:identifier
identifier: true
owner: Thing
domain_of:
- Thing
range: uriorcurie
required: true

```
</details></div>
