---
search:
  boost: 10.0
---

# Class: BroaderConceptReference 


_Relações hierárquicas._



<div data-search-exclude markdown="1">



URI: [wasth:BroaderConceptReference](https://tradicional.arq.br/schema/BroaderConceptReference)





```mermaid
 classDiagram
    class BroaderConceptReference
    click BroaderConceptReference href "../BroaderConceptReference/"
      ConceptReference <|-- BroaderConceptReference
        click ConceptReference href "../ConceptReference/"
      
      BroaderConceptReference : bibliographic_citation
        
          
    
        
        
        BroaderConceptReference --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"
    

        
      BroaderConceptReference : concept
        
          
    
        
        
        BroaderConceptReference --> "1" Concept : concept
        click Concept href "../Concept/"
    

        
      BroaderConceptReference : description
        
      BroaderConceptReference : match
        
          
    
        
        
        BroaderConceptReference --> "1" SkosBroaderRelation : match
        click SkosBroaderRelation href "../SkosBroaderRelation/"
    

        
      
```





## Inheritance
* [ConceptReference](ConceptReference.md)
    * **BroaderConceptReference**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [match](match.md) | 1 <br/> [SkosBroaderRelation](SkosBroaderRelation.md) | Tipo da relação | direct |
| [concept](concept.md) | 1 <br/> [Concept](Concept.md) |  | [ConceptReference](ConceptReference.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [ConceptReference](ConceptReference.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | 📚  Cadastro de uma referência bibliográfica | [ConceptReference](ConceptReference.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [broader](broader.md) | range | [BroaderConceptReference](BroaderConceptReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:BroaderConceptReference |
| native | wasth:BroaderConceptReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BroaderConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    domain_of:
    - BroaderConceptReference
    - NarrowerConceptReference
    - MappingConceptReference
    range: SkosBroaderRelation
    required: true

```
</details>

### Induced

<details>
```yaml
name: BroaderConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    rank: 1000
    owner: BroaderConceptReference
    domain_of:
    - BroaderConceptReference
    - NarrowerConceptReference
    - MappingConceptReference
    range: SkosBroaderRelation
    required: true
  concept:
    name: concept
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: name
    owner: BroaderConceptReference
    domain_of:
    - ConceptReference
    - Topic
    range: Concept
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
    owner: BroaderConceptReference
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
  bibliographic_citation:
    name: bibliographic_citation
    description: '📚  Cadastro de uma referência bibliográfica.

      O campo `refid` deve conter a chave de citação (citation key) que consta do
      registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero,
      começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação,
      mas pode ser diferente.

      Se necessário, incluir no campo `note` uma especificação adicional, como o número
      da página da referência bibliográfica de onde a informação foi extraída.

      Usar o campo `description` para formatar a referência, caso a formatação automática
      do Zotero não for satisfatória.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: BroaderConceptReference
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