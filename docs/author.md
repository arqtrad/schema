---
search:
  boost: 5.0
---

# Slot: author


_ORCID iD of the record author or maintainer._



<div data-search-exclude markdown="1">



URI: [dcterms:creator](http://purl.org/dc/terms/creator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OrcidId](OrcidId.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:creator](http://purl.org/dc/terms/creator) |
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
| self | dcterms:creator |
| native | wasth:author |




## LinkML Source

<details>
```yaml
name: author
description: ORCID iD of the record author or maintainer.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:creator
owner: Thing
domain_of:
- Thing
range: OrcidId

```
</details></div>
