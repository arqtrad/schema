---
search:
  boost: 5.0
---

# Slot: category


_The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element._

_Examples are human-made object or natural object._

_Nos documentários de edificações, preencher este campo obrigatoriamente com `term:lido00096`_



<div data-search-exclude markdown="1">



URI: [term:lidoCategory](http://terminology.lido-schema.org/lidoCategory)
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
| [Work](Work.md) | An historical landmark or building |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [term:lidoCategory](http://terminology.lido-schema.org/lidoCategory) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Designates Type | Yes |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | term:lidoCategory |
| native | wasth:category |




## LinkML Source

<details>
```yaml
name: category
description: 'The LIDO Category Vocabulary is a structured controlled list of terms
  recommended to use as values in the LIDO Category element.

  Examples are human-made object or natural object.

  Nos documentários de edificações, preencher este campo obrigatoriamente com `term:lido00096`'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lidoCategory
designates_type: true
owner: Thing
domain_of:
- Thing
range: uriorcurie
required: true

```
</details></div>
