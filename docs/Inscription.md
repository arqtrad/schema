---
search:
  boost: 10.0
---

# Class: Inscription


_A descrição da inscrição informa local, dimensões e características. Os tipos de descrição podem ser extraídos da hierarquia Getty: <http://vocab.getty.edu/page/aat/300220469>._

_Os itens das listas de `material` e `technique` DEVEM usar o nosso [vocabulário controlado](https://vocabulario.tradicional.arq.br)._

_Essa distinção é especialmente relevante no caso de revestimentos, como estuques, azulejos ou pinturas decorativas, por oposição à base sobre a qual eles são aplicados._



<div data-search-exclude markdown="1">



URI: [wasth:Inscription](https://tradicional.arq.br/schema/Inscription)





```mermaid
 classDiagram
    class Inscription
    click Inscription href "../Inscription/"
      Inscription : bibliographic_citation





        Inscription --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      Inscription : content

      Inscription : description

      Inscription : format_extent





        Inscription --> "0..1" TypedReference : format_extent
        click TypedReference href "../TypedReference/"



      Inscription : type





        Inscription --> "1" InscriptionType : type
        click InscriptionType href "../InscriptionType/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [format_extent](format_extent.md) | 0..1 <br/> [TypedReference](TypedReference.md) | Indica a parte do objeto que está sendo medida — por exemplo, se a altura é a... | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | direct |
| [content](content.md) | 0..1 _recommended_ <br/> [String](String.md) | Deixe uma linha em branco após o fechamento dos metadados e inclua aqui uma d... | direct |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica | direct |
| [type](type.md) | 1 <br/> [InscriptionType](InscriptionType.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Work](Work.md) | [inscriptions](inscriptions.md) | range | [Inscription](Inscription.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:Inscription |
| native | wasth:Inscription |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Inscription
description: 'A descrição da inscrição informa local, dimensões e características.
  Os tipos de descrição podem ser extraídos da hierarquia Getty: <http://vocab.getty.edu/page/aat/300220469>.

  Os itens das listas de `material` e `technique` DEVEM usar o nosso [vocabulário
  controlado](https://vocabulario.tradicional.arq.br).

  Essa distinção é especialmente relevante no caso de revestimentos, como estuques,
  azulejos ou pinturas decorativas, por oposição à base sobre a qual eles são aplicados.'
from_schema: https://tradicional.arq.br/schema
slots:
- format_extent
- description
- content
- bibliographic_citation
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/work
    ifabsent: string(text)
    domain_of:
    - Measurement
    - Right
    - LegalBody
    - Event
    - StylePeriod
    - EventPlace
    - Inscription
    - Topic
    - HistoricPlace
    range: InscriptionType
    required: true

```
</details>

### Induced

<details>
```yaml
name: Inscription
description: 'A descrição da inscrição informa local, dimensões e características.
  Os tipos de descrição podem ser extraídos da hierarquia Getty: <http://vocab.getty.edu/page/aat/300220469>.

  Os itens das listas de `material` e `technique` DEVEM usar o nosso [vocabulário
  controlado](https://vocabulario.tradicional.arq.br).

  Essa distinção é especialmente relevante no caso de revestimentos, como estuques,
  azulejos ou pinturas decorativas, por oposição à base sobre a qual eles são aplicados.'
from_schema: https://tradicional.arq.br/schema
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/work
    ifabsent: string(text)
    owner: Inscription
    domain_of:
    - Measurement
    - Right
    - LegalBody
    - Event
    - StylePeriod
    - EventPlace
    - Inscription
    - Topic
    - HistoricPlace
    range: InscriptionType
    required: true
  format_extent:
    name: format_extent
    description: 'Indica a parte do objeto que está sendo medida — por exemplo, se
      a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri`
      de um vocabulário controlado.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: extent
    owner: Inscription
    domain_of:
    - Measurement
    - Inscription
    - Topic
    range: TypedReference
    inlined: true
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://tradicional.arq.br/schema
    exact_mappings:
    - schema:description
    rank: 1000
    slot_uri: dcterms:description
    alias: display
    owner: Inscription
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
  content:
    name: content
    description: 'Deixe uma linha em branco após o fechamento dos metadados e inclua
      aqui uma descrição morfológica e histórica da edificação com texto livre, usando
      formatação Markdown.

      Poderá incluir um segundo bloco de metadados para indicar as referências bibliográficas
      da descrição textual, no campo `nocite`. O formato é uma lista de chaves de
      citação do Zotero (cada uma começando com `@`) separadas por vírgulas:

      ```yaml Conteúdo textual em formato *Markdown* com citações [@citekey].

      --- nocite: "@*" --- ```

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: skos:scopeNote
    owner: Inscription
    domain_of:
    - Thing
    - Inscription
    range: string
    recommended: true
  bibliographic_citation:
    name: bibliographic_citation
    description: 'Cadastro de uma referência bibliográfica.

      Usar o campo `description` para formatar a referência, caso a formatação automática
      do Zotero não for satisfatória.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: Inscription
    domain_of:
    - ConceptReference
    - GeographicPoint
    - GeographicExtent
    - RelatedObject
    - MediaObject
    - TypedReference
    - Measurement
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
