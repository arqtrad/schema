---
search:
  boost: 10.0
---

# Class: ConceptReference


_Atribuição de vocabulário controlado com citação de apoio._



<div data-search-exclude markdown="1">



URI: [wasth:ConceptReference](https://tradicional.arq.br/schema/ConceptReference)





```mermaid
 classDiagram
    class ConceptReference
    click ConceptReference href "../ConceptReference/"
      ConceptReference <|-- MaterialTech
        click MaterialTech href "../MaterialTech/"
      ConceptReference <|-- StylePeriod
        click StylePeriod href "../StylePeriod/"

      ConceptReference : bibliographic_citation





        ConceptReference --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      ConceptReference : description

      ConceptReference : name





        ConceptReference --> "0..1" Concept : name
        click Concept href "../Concept/"




```





## Inheritance
* **ConceptReference**
    * [MaterialTech](MaterialTech.md)
    * [StylePeriod](StylePeriod.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | direct |
| [name](name.md) | 0..1 <br/> [Concept](Concept.md) | Identificador do termo referido | direct |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) |  | direct |
| [name](name.md) | 0..1 <br/> [Concept](Concept.md) | Identificador do termo referido | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [narrower](narrower.md) | range | [ConceptReference](ConceptReference.md) |
| [Place](Place.md) | [work_type_function](work_type_function.md) | range | [ConceptReference](ConceptReference.md) |
| [Place](Place.md) | [work_type_context](work_type_context.md) | range | [ConceptReference](ConceptReference.md) |
| [Event](Event.md) | [method](method.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_condition](work_type_condition.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_form](work_type_form.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_subject_type](work_type_subject_type.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_use](work_type_use.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [classification_genre](classification_genre.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [classification_subject](classification_subject.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [classification_local](classification_local.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [classification_special](classification_special.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_function](work_type_function.md) | range | [ConceptReference](ConceptReference.md) |
| [Work](Work.md) | [work_type_context](work_type_context.md) | range | [ConceptReference](ConceptReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:ConceptReference |
| native | wasth:ConceptReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConceptReference
description: Atribuição de vocabulário controlado com citação de apoio.
from_schema: https://tradicional.arq.br/schema
slots:
- description
- name
- bibliographic_citation
attributes:
  name:
    name: name
    description: Identificador do termo referido.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    domain_of:
    - ConceptReference
    - LegalBody
    - RelatedEvent
    - HistoricPlace
    range: Concept

```
</details>

### Induced

<details>
```yaml
name: ConceptReference
description: Atribuição de vocabulário controlado com citação de apoio.
from_schema: https://tradicional.arq.br/schema
attributes:
  name:
    name: name
    description: Identificador do termo referido.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    owner: ConceptReference
    domain_of:
    - ConceptReference
    - LegalBody
    - RelatedEvent
    - HistoricPlace
    range: Concept
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:description
    alias: display
    owner: ConceptReference
    domain_of:
    - ConceptReference
    - Measurement
    - BibliographicCitation
    - RelatedObject
    - MediaObject
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
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: ConceptReference
    domain_of:
    - ConceptReference
    - GeographicPoint
    - GeographicExtent
    - TypedReference
    - Measurement
    - RelatedObject
    - MediaObject
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
