---
search:
  boost: 5.0
---

# Slot: bibliographic_citation


_Cadastro de uma referência bibliográfica._

_Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória._

__



<div data-search-exclude markdown="1">



URI: [dcterms:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |  no  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |
| [Actor](Actor.md) | Agent and role in an event |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Appellation](Appellation.md) |  |  no  |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
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
| Range | [BibliographicCitation](BibliographicCitation.md) |
| Domain Of | [ConceptReference](ConceptReference.md), [RelatedObject](RelatedObject.md), [MediaObject](MediaObject.md), [TypedReference](TypedReference.md), [Measurement](Measurement.md), [Actor](Actor.md), [Thing](Thing.md), [Appellation](Appellation.md), [GeographicPoint](GeographicPoint.md), [GeographicExtent](GeographicExtent.md), [Inscription](Inscription.md) |
| Slot URI | [dcterms:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:bibliographicCitation |
| native | wasth:bibliographic_citation |




## LinkML Source

<details>
```yaml
name: bibliographic_citation
description: 'Cadastro de uma referência bibliográfica.

  Usar o campo `description` para formatar a referência, caso a formatação automática
  do Zotero não for satisfatória.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:bibliographicCitation
domain_of:
- ConceptReference
- RelatedObject
- MediaObject
- TypedReference
- Measurement
- Actor
- Thing
- Appellation
- GeographicPoint
- GeographicExtent
- Inscription
range: BibliographicCitation
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
