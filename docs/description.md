---
search:
  boost: 5.0
---

# Slot: description


_A human-readable description for a thing_



<div data-search-exclude markdown="1">



URI: [dcterms:description](http://purl.org/dc/terms/description)
Alias: display

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |  no  |
| [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica |  no  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |
| [EventDate](EventDate.md) | A wrapper for the expression of a date by providing a set of years as earlies... |  no  |
| [EventPlace](EventPlace.md) |  |  no  |
| [RelatedEvent](RelatedEvent.md) |  |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  yes  |
| [Appellation](Appellation.md) |  |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Topic](Topic.md) | Subject or iconographic topic |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [StylePeriod](StylePeriod.md) |  |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ConceptReference](ConceptReference.md), [BibliographicCitation](BibliographicCitation.md), [RelatedObject](RelatedObject.md), [MediaObject](MediaObject.md), [Measurement](Measurement.md), [EventDate](EventDate.md), [EventPlace](EventPlace.md), [RelatedEvent](RelatedEvent.md), [Thing](Thing.md), [Appellation](Appellation.md), [Inscription](Inscription.md), [Topic](Topic.md) |
| Slot URI | [dcterms:description](http://purl.org/dc/terms/description) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:description |
| native | wasth:description |
| exact | schema:description |




## LinkML Source

<details>
```yaml
name: description
description: A human-readable description for a thing
from_schema: https://tradicional.arq.br/schema
exact_mappings:
- schema:description
rank: 1000
slot_uri: dcterms:description
alias: display
domain_of:
- ConceptReference
- BibliographicCitation
- RelatedObject
- MediaObject
- Measurement
- EventDate
- EventPlace
- RelatedEvent
- Thing
- Appellation
- Inscription
- Topic
range: string

```
</details></div>
