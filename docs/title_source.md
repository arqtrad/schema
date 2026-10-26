---
search:
  boost: 5.0
---

# Slot: title_source


_📚 A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen)._

_Se a fonte for cadastrada, o campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente._

_Se necessário, incluir no campo note uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída._

_Todos os campos source no restante da ficha devem ser preenchidos do mesmo modo. (Equivalente DublinCore: bibliographiCitation)._



<div data-search-exclude markdown="1">



URI: [wasth:title_source](https://tradicional.arq.br/schema/title_source)
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
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BibliographicCitation](BibliographicCitation.md) |
| Domain Of | [Thing](Thing.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


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
| self | wasth:title_source |
| native | wasth:title_source |




## LinkML Source

<details>
```yaml
name: title_source
description: '📚 A fonte do título title_source é opcional ; um título pode ser atestado
  em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa
  com um hífen).

  Se a fonte for cadastrada, o campo `refid` deve conter a chave de citação (citation
  key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa
  no Zotero. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode
  ser diferente.

  Se necessário, incluir no campo note uma especificação adicional, como o número
  da página da referência bibliográfica de onde a informação foi extraída.

  Todos os campos source no restante da ficha devem ser preenchidos do mesmo modo.
  (Equivalente DublinCore: bibliographiCitation).'
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: BibliographicCitation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
