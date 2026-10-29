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
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |  no  |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |  no  |
| [RelatedEvent](RelatedEvent.md) |  |  no  |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  yes  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Topic](Topic.md) | Subject or iconographic topic |  no  |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |
| [BroaderConceptReference](BroaderConceptReference.md) | Relações hierárquicas |  no  |
| [NarrowerConceptReference](NarrowerConceptReference.md) | Relações hierárquicas |  no  |
| [MappingConceptReference](MappingConceptReference.md) | Relações semânticas |  no  |
| [RelatedWork](RelatedWork.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |  no  |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [StylePeriod](StylePeriod.md) |  |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ConceptReference](ConceptReference.md), [BibliographicCitation](BibliographicCitation.md), [RelatedObject](RelatedObject.md), [MediaObject](MediaObject.md), [TypedReference](TypedReference.md), [Measurement](Measurement.md), [RelatedEvent](RelatedEvent.md), [Thing](Thing.md), [Inscription](Inscription.md), [Topic](Topic.md) |
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
- TypedReference
- Measurement
- RelatedEvent
- Thing
- Inscription
- Topic
range: string

```
</details></div>