---
search:
  boost: 5.0
---

# Slot: bibliographic_citation 


_📚  Cadastro de uma referência bibliográfica._

_O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente._

_Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída._

_Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória._

__



<div data-search-exclude markdown="1">



URI: [dcterms:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |  no  |
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |  no  |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |  no  |
| [Actor](Actor.md) | Agent and role in an event |  no  |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  no  |
| [Appellation](Appellation.md) |  |  no  |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
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
description: '📚  Cadastro de uma referência bibliográfica.

  O campo `refid` deve conter a chave de citação (citation key) que consta do registro
  bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com
  arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser
  diferente.

  Se necessário, incluir no campo `note` uma especificação adicional, como o número
  da página da referência bibliográfica de onde a informação foi extraída.

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