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
    

        
      StylePeriod : concept
        
          
    
        
        
        StylePeriod --> "1" Concept : concept
        click Concept href "../Concept/"
    

        
      StylePeriod : description
        
      StylePeriod : period_name_type
        
          
    
        
        
        StylePeriod --> "1" PeriodNameType : period_name_type
        click PeriodNameType href "../PeriodNameType/"
    

        
      
```





## Inheritance
* [ConceptReference](ConceptReference.md)
    * **StylePeriod**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [period_name_type](period_name_type.md) | 1 <br/> [PeriodNameType](PeriodNameType.md) | Designa a natureza ou origem do nome do período ou estilo indicado | direct |
| [concept](concept.md) | 1 <br/> [Concept](Concept.md) |  | [ConceptReference](ConceptReference.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [ConceptReference](ConceptReference.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | 📚  Cadastro de uma referência bibliográfica | [ConceptReference](ConceptReference.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Event](Event.md) | [style_period](style_period.md) | range | [StylePeriod](StylePeriod.md) |
| [Work](Work.md) | [style_period](style_period.md) | range | [StylePeriod](StylePeriod.md) |












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
  period_name_type:
    name: period_name_type
    description: 'Designa a natureza ou origem do nome do período ou estilo indicado.

      '
    from_schema: https://tradicional.arq.br/schema/temporal
    rank: 1000
    alias: type
    domain_of:
    - StylePeriod
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
  period_name_type:
    name: period_name_type
    description: 'Designa a natureza ou origem do nome do período ou estilo indicado.

      '
    from_schema: https://tradicional.arq.br/schema/temporal
    rank: 1000
    alias: type
    owner: StylePeriod
    domain_of:
    - StylePeriod
    range: PeriodNameType
    required: true
  concept:
    name: concept
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: name
    owner: StylePeriod
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
    owner: StylePeriod
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

```
</details></div>