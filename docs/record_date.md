---
search:
  boost: 5.0
---

# Slot: record_date


_Date the record was created or last substantively revised._



<div data-search-exclude markdown="1">



URI: [dcterms:created](http://purl.org/dc/terms/created)
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
| Range | [Date](Date.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |
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
| self | dcterms:created |
| native | wasth:record_date |




## LinkML Source

<details>
```yaml
name: record_date
description: Date the record was created or last substantively revised.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:created
owner: Thing
domain_of:
- Thing
range: date

```
</details></div>
