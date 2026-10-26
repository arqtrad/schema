---
search:
  boost: 5.0
---

# Slot: bibliographic_citation

<div data-search-exclude markdown="1">



URI: [dcterms:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |  no  |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |
| [Measurements](Measurements.md) | O campo `description` permite uma representação textual das medidas da |  no  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Media](Media.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [Actor](Actor.md) | Agent and role in an event |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |  no  |
| [Appellation](Appellation.md) |  |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |  no  |
| [MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |
| [StylePeriod](StylePeriod.md) |  |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BibliographicCitation](BibliographicCitation.md) |
| Domain Of | [ConceptReference](ConceptReference.md), [GeographicPoint](GeographicPoint.md), [GeographicExtent](GeographicExtent.md), [TypedReference](TypedReference.md), [Measurements](Measurements.md), [RelatedObject](RelatedObject.md), [Media](Media.md), [Actor](Actor.md), [Thing](Thing.md), [Appellation](Appellation.md), [Inscription](Inscription.md) |
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
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:bibliographicCitation
domain_of:
- ConceptReference
- GeographicPoint
- GeographicExtent
- TypedReference
- Measurements
- RelatedObject
- Media
- Actor
- Thing
- Appellation
- Inscription
range: BibliographicCitation
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
