---
search:
  boost: 10.0
---

# Class: StylePeriod

<div data-search-exclude markdown="1">



URI: [wasth:StylePeriod](https://tradicional.arq.br/schema/StylePeriod)





```mermaid
 classDiagram
    class StylePeriod
    click StylePeriod href "../StylePeriod/"
      ConceptReference <|-- StylePeriod
        click ConceptReference href "../ConceptReference/"

      StylePeriod : bibliographic_citation





        StylePeriod --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      StylePeriod : description

      StylePeriod : name





        StylePeriod --> "0..1" Concept : name
        click Concept href "../Concept/"



      StylePeriod : type





        StylePeriod --> "1" PeriodNameType : type
        click PeriodNameType href "../PeriodNameType/"




```





## Inheritance
* [ConceptReference](ConceptReference.md)
    * **StylePeriod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [PeriodNameType](PeriodNameType.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [ConceptReference](ConceptReference.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica | [ConceptReference](ConceptReference.md) |
| [name](name.md) | 0..1 <br/> [Concept](Concept.md) | Identificador do termo referido | [ConceptReference](ConceptReference.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [style_period](style_period.md) | range | [StylePeriod](StylePeriod.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:StylePeriod |
| native | wasth:StylePeriod |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StylePeriod
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/temporal
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
    range: PeriodNameType
    required: true

```
</details>

### Induced

<details>
```yaml
name: StylePeriod
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/temporal
    owner: StylePeriod
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
    range: PeriodNameType
    required: true
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://tradicional.arq.br/schema
    exact_mappings:
    - schema:description
    rank: 1000
    slot_uri: dcterms:description
    alias: display
    owner: StylePeriod
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
  bibliographic_citation:
    name: bibliographic_citation
    description: 'Cadastro de uma referência bibliográfica.

      Usar o campo `description` para formatar a referência, caso a formatação automática
      do Zotero não for satisfatória.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: StylePeriod
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
  name:
    name: name
    description: Identificador do termo referido.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    owner: StylePeriod
    domain_of:
    - ConceptReference
    - LegalBody
    - RelatedEvent
    - HistoricPlace
    range: Concept

```
</details></div>
