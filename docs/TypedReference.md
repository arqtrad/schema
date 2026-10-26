---
search:
  boost: 10.0
---

# Class: TypedReference


_Reference to a local record, IRI, URI, or LIDO terminology term._



<div data-search-exclude markdown="1">



URI: [wasth:TypedReference](https://tradicional.arq.br/schema/TypedReference)





```mermaid
 classDiagram
    class TypedReference
    click TypedReference href "../TypedReference/"
      TypedReference : bibliographic_citation





        TypedReference --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      TypedReference : reference_type





        TypedReference --> "0..1" ReferenceType : reference_type
        click ReferenceType href "../ReferenceType/"



      TypedReference : refid

      TypedReference : source





        TypedReference --> "*" LegalBody : source
        click LegalBody href "../LegalBody/"



      TypedReference : term


```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [reference_type](reference_type.md) | 0..1 <br/> [ReferenceType](ReferenceType.md) |  | direct |
| [term](term.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | LIDO terminology term | direct |
| [refid](refid.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Local or external identifier | direct |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) |  | direct |
| [source](source.md) | * <br/> [LegalBody](LegalBody.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Concept](Concept.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Place](Place.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Place](Place.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Site](Site.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Site](Site.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Resource](Resource.md) | [resource_service](resource_service.md) | range | [TypedReference](TypedReference.md) |
| [Resource](Resource.md) | [unit](unit.md) | range | [TypedReference](TypedReference.md) |
| [Resource](Resource.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Resource](Resource.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [MediaObject](MediaObject.md) | [format](format.md) | range | [TypedReference](TypedReference.md) |
| [MediaObject](MediaObject.md) | [resource_service](resource_service.md) | range | [TypedReference](TypedReference.md) |
| [Measurement](Measurement.md) | [format_extent](format_extent.md) | range | [TypedReference](TypedReference.md) |
| [Measurement](Measurement.md) | [unit](unit.md) | range | [TypedReference](TypedReference.md) |
| [Right](Right.md) | [type](type.md) | range | [TypedReference](TypedReference.md) |
| [LegalBody](LegalBody.md) | [name](name.md) | range | [TypedReference](TypedReference.md) |
| [Event](Event.md) | [culture](culture.md) | range | [TypedReference](TypedReference.md) |
| [Event](Event.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Event](Event.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Actor](Actor.md) | [actor_name](actor_name.md) | range | [TypedReference](TypedReference.md) |
| [Actor](Actor.md) | [actor_qualifier](actor_qualifier.md) | range | [TypedReference](TypedReference.md) |
| [Actor](Actor.md) | [actor_extent](actor_extent.md) | range | [TypedReference](TypedReference.md) |
| [Thing](Thing.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Thing](Thing.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Repository](Repository.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Repository](Repository.md) | [collection](collection.md) | range | [TypedReference](TypedReference.md) |
| [Work](Work.md) | [identifiers](identifiers.md) | range | [TypedReference](TypedReference.md) |
| [Inscription](Inscription.md) | [format_extent](format_extent.md) | range | [TypedReference](TypedReference.md) |
| [Topic](Topic.md) | [format_extent](format_extent.md) | range | [TypedReference](TypedReference.md) |
| [HistoricPlace](HistoricPlace.md) | [name](name.md) | range | [TypedReference](TypedReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:TypedReference |
| native | wasth:TypedReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TypedReference
description: Reference to a local record, IRI, URI, or LIDO terminology term.
from_schema: https://tradicional.arq.br/schema
slots:
- reference_type
- term
- refid
- bibliographic_citation
- source

```
</details>

### Induced

<details>
```yaml
name: TypedReference
description: Reference to a local record, IRI, URI, or LIDO terminology term.
from_schema: https://tradicional.arq.br/schema
attributes:
  reference_type:
    name: reference_type
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    ifabsent: string(uri)
    alias: type
    owner: TypedReference
    domain_of:
    - TypedReference
    range: ReferenceType
  term:
    name: term
    description: LIDO terminology term.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: TypedReference
    domain_of:
    - TypedReference
    range: uriorcurie
    pattern: ^http://terminology\.lido-schema\.org/lido[0-9]{5}$
  refid:
    name: refid
    description: Local or external identifier.
    from_schema: https://tradicional.arq.br/schema
    exact_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dcterm:identifier
    key: true
    owner: TypedReference
    domain_of:
    - BibliographicCitation
    - TypedReference
    range: uriorcurie
    required: true
  bibliographic_citation:
    name: bibliographic_citation
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: TypedReference
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
  source:
    name: source
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: TypedReference
    domain_of:
    - GeographicPoint
    - GeographicExtent
    - RelatedObject
    - MediaObject
    - TypedReference
    range: LegalBody
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>
