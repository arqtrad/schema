---
search:
  boost: 10.0
---

# Class: NarrowerConceptReference 


_Relações hierárquicas._



<div data-search-exclude markdown="1">



URI: [wasth:NarrowerConceptReference](https://tradicional.arq.br/schema/NarrowerConceptReference)





```mermaid
 classDiagram
    class NarrowerConceptReference
    click NarrowerConceptReference href "../NarrowerConceptReference/"
      ConceptReference <|-- NarrowerConceptReference
        click ConceptReference href "../ConceptReference/"
      
      NarrowerConceptReference : bibliographic_citation
        
          
    
        
        
        NarrowerConceptReference --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"
    

        
      NarrowerConceptReference : concept
        
          
    
        
        
        NarrowerConceptReference --> "1" Concept : concept
        click Concept href "../Concept/"
    

        
      NarrowerConceptReference : description
        
      NarrowerConceptReference : match
        
          
    
        
        
        NarrowerConceptReference --> "1" SkosNarrowerRelation : match
        click SkosNarrowerRelation href "../SkosNarrowerRelation/"
    

        
      
```





## Inheritance
* [ConceptReference](ConceptReference.md)
    * **NarrowerConceptReference**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [match](match.md) | 1 <br/> [SkosNarrowerRelation](SkosNarrowerRelation.md) | Tipo da relação | direct |
| [concept](concept.md) | 1 <br/> [Concept](Concept.md) |  | [ConceptReference](ConceptReference.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [ConceptReference](ConceptReference.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | 📚  Cadastro de uma referência bibliográfica | [ConceptReference](ConceptReference.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [narrower](narrower.md) | range | [NarrowerConceptReference](NarrowerConceptReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:NarrowerConceptReference |
| native | wasth:NarrowerConceptReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NarrowerConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    domain_of:
    - BroaderConceptReference
    - NarrowerConceptReference
    - MappingConceptReference
    range: SkosNarrowerRelation
    required: true

```
</details>

### Induced

<details>
```yaml
name: NarrowerConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
is_a: ConceptReference
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    owner: NarrowerConceptReference
    domain_of:
    - BroaderConceptReference
    - NarrowerConceptReference
    - MappingConceptReference
    range: SkosNarrowerRelation
    required: true
  concept:
    name: concept
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: name
    owner: NarrowerConceptReference
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
    owner: NarrowerConceptReference
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
    owner: NarrowerConceptReference
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