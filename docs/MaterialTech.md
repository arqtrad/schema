---
search:
  boost: 10.0
---

# Class: MaterialTech


_Usar discernimento para identificar sistemas, materiais e técnicas que_

_interessam ao conhecimento da edificação no seu conjunto, não a partes_

_menos extensas ou pouco importantes._

__



<div data-search-exclude markdown="1">



URI: [wasth:MaterialTech](https://tradicional.arq.br/schema/MaterialTech)





```mermaid
 classDiagram
    class MaterialTech
    click MaterialTech href "../MaterialTech/"
      ConceptReference <|-- MaterialTech
        click ConceptReference href "../ConceptReference/"

      MaterialTech : bibliographic_citation





        MaterialTech --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      MaterialTech : description

      MaterialTech : material_tech_type





        MaterialTech --> "1" MaterialTechType : material_tech_type
        click MaterialTechType href "../MaterialTechType/"



      MaterialTech : name





        MaterialTech --> "0..1" Concept : name
        click Concept href "../Concept/"




```





## Inheritance
* [ConceptReference](ConceptReference.md)
    * **MaterialTech**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [material_tech_type](material_tech_type.md) | 1 <br/> [MaterialTechType](MaterialTechType.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [ConceptReference](ConceptReference.md) |
| [name](name.md) | 0..1 <br/> [Concept](Concept.md) | Identificador do termo referido | [ConceptReference](ConceptReference.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) |  | [ConceptReference](ConceptReference.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [material](material.md) | range | [MaterialTech](MaterialTech.md) |
| [Event](Event.md) | [technique](technique.md) | range | [MaterialTech](MaterialTech.md) |
| [Work](Work.md) | [material](material.md) | range | [MaterialTech](MaterialTech.md) |
| [Work](Work.md) | [technique](technique.md) | range | [MaterialTech](MaterialTech.md) |
| [Work](Work.md) | [work_type_material_tech](work_type_material_tech.md) | range | [MaterialTech](MaterialTech.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:MaterialTech |
| native | wasth:MaterialTech |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialTech
description: 'Usar discernimento para identificar sistemas, materiais e técnicas que

  interessam ao conhecimento da edificação no seu conjunto, não a partes

  menos extensas ou pouco importantes.

  '
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  material_tech_type:
    name: material_tech_type
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: type
    domain_of:
    - MaterialTech
    range: MaterialTechType
    required: true

```
</details>

### Induced

<details>
```yaml
name: MaterialTech
description: 'Usar discernimento para identificar sistemas, materiais e técnicas que

  interessam ao conhecimento da edificação no seu conjunto, não a partes

  menos extensas ou pouco importantes.

  '
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  material_tech_type:
    name: material_tech_type
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: type
    owner: MaterialTech
    domain_of:
    - MaterialTech
    range: MaterialTechType
    required: true
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:description
    alias: display
    owner: MaterialTech
    domain_of:
    - ConceptReference
    - Measurements
    - BibliographicCitation
    - RelatedObject
    - Media
    - EventDate
    - EventPlace
    - RelatedEvent
    - Thing
    - Appellation
    - Inscription
    - Topic
    range: string
  name:
    name: name
    description: Identificador do termo referido.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    owner: MaterialTech
    domain_of:
    - ConceptReference
    - RelatedEvent
    - HistoricPlace
    range: Concept
  bibliographic_citation:
    name: bibliographic_citation
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: MaterialTech
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
