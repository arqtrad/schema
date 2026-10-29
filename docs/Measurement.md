---
search:
  boost: 10.0
---

# Class: Measurement 


_Informações estruturadas sobre as dimensões do objeto ou requisitos de condicionamento ambiental no espaço que ele ocupa. Para edificações, é recomendável cadastrar ao menos a área útil, testada e a altura de coroamento._

_Se a modulação original for conhecida ou puder ser deduzida por um estudo metrológico, é interessante cadastrar também as medidas históricas utilizadas (por exemplo, dimensões em palmos)._

_O campo `description` permite uma representação textual das medidas da edificação, caso não seja viável cadastrar medidas individuais com precisão, ou seja preciso maior flexibilidade para explicar as dimensões._

__



<div data-search-exclude markdown="1">



URI: [crm:E16_Measurement](http://www.cidoc-crm.org/cidoc-crm/E16_Measurement)





```mermaid
 classDiagram
    class Measurement
    click Measurement href "../Measurement/"
      Measurement : bibliographic_citation
        
          
    
        
        
        Measurement --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"
    

        
      Measurement : description
        
      Measurement : format_extent
        
          
    
        
        
        Measurement --> "0..1" TypedReference : format_extent
        click TypedReference href "../TypedReference/"
    

        
      Measurement : measurement_event
        
          
    
        
        
        Measurement --> "0..1" Event : measurement_event
        click Event href "../Event/"
    

        
      Measurement : measurement_qualifier
        
          
    
        
        
        Measurement --> "0..1" MeasurementQualifier : measurement_qualifier
        click MeasurementQualifier href "../MeasurementQualifier/"
    

        
      Measurement : measurement_shape
        
          
    
        
        
        Measurement --> "0..1" TypedReference : measurement_shape
        click TypedReference href "../TypedReference/"
    

        
      Measurement : measurement_type
        
          
    
        
        
        Measurement --> "0..1" MeasurementType : measurement_type
        click MeasurementType href "../MeasurementType/"
    

        
      Measurement : measurement_value
        
      Measurement : unit
        
          
    
        
        
        Measurement --> "1" TypedReference : unit
        click TypedReference href "../TypedReference/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [crm:E16_Measurement](http://www.cidoc-crm.org/cidoc-crm/E16_Measurement) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [unit](unit.md) | 1 <br/> [TypedReference](TypedReference.md) | Unidade de medida usada no dimensionamento do objeto ou da representação, por... | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | direct |
| [format_extent](format_extent.md) | 0..1 <br/> [TypedReference](TypedReference.md) | Indica a parte do objeto que está sendo medida — por exemplo, se a altura é a... | direct |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | 📚  Cadastro de uma referência bibliográfica | direct |
| [measurement_type](measurement_type.md) | 0..1 <br/> [MeasurementType](MeasurementType.md) | designa a natureza da medida : largura, altura, área, etc | direct |
| [measurement_value](measurement_value.md) | 1 <br/> [Float](Float.md) | Valor numérico, usar ponto como separador decimal | direct |
| [measurement_qualifier](measurement_qualifier.md) | 0..1 <br/> [MeasurementQualifier](MeasurementQualifier.md) | Indica que as medidas são aproximadas | direct |
| [measurement_shape](measurement_shape.md) | 0..1 <br/> [TypedReference](TypedReference.md) | caso relevante, indicar a forma do elemento medido usando a [lista de formas ... | direct |
| [measurement_event](measurement_event.md) | 0..1 <br/> [Event](Event.md) | Descreve a ocasião em que as medidas foram aferidas, caso essa informação sej... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MediaObject](MediaObject.md) | [measurements](measurements.md) | range | [Measurement](Measurement.md) |
| [Event](Event.md) | [measurements](measurements.md) | range | [Measurement](Measurement.md) |
| [Work](Work.md) | [measurements](measurements.md) | range | [Measurement](Measurement.md) |










## Notes

* This class comprises actions measuring physical properties and other values that can be determined by a systematic, objective procedure of direct observation of particular states of physical reality.
* An instance of E16 Measurement may use simple counting or tools, such as yardsticks or radiation detection devices. The interest is in the method and care applied, so that the reliability of the result may be judged at a later stage, or research continued on the associated documents. The date of the event is important for dimensions, which may change value over time, such as the length of an object subject to shrinkage. Methods and devices employed should be associated with instances of E16 Measurement by properties such as: *P33 used specific technique*: E29 Design or Procedure, *P125 used object of type*: E55 Type, *P16 used specific object (was used for)*: E70 Thing, whereas basic techniques such as "carbon-14 dating" should be encoded using *P2 has type (is type of)*: E55 Type. Details of methods and devices reused or reusable in other instances of E16 Measurement should be documented for these entities rather than the measurements themselves, whereas details of particular execution may be documented by free text or by instantiating adequate sub-activities, if the detail may be of interest for an overarching query.
* Regardless whether a measurement is made by an instrument or by human senses, it represents the initial transition from physical reality to information without any other documented information object in between within the reasoning chain that would represent the result of the interaction of the observer or device with reality. Therefore, determining properties of an instance of E90 Symbolic Object is regarded as an instance of E13 Attribute Assignment, which may be inferred from observing and measuring representative carriers. In the case that the carrier can be named, the property *P16 used specific object (was used for)* should be used to indicate the instance(s) of E18 Physical Thing that was used as the empirical basis for the attribute assignment. For instance, inferring properties of depicted items using image material, such as satellite images, is not regarded as an instance of E16 Measurement, but as a subsequent instance of E13 Attribute Assignment. Rather, only the production of the images, understood as arrays of radiation intensities, is regarded as an instance of E16 Measurement. The same reasoning holds for other sensor data.



## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | crm:E16_Measurement |
| native | wasth:Measurement |
| related | dcterms:format |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Measurement
description: 'Informações estruturadas sobre as dimensões do objeto ou requisitos
  de condicionamento ambiental no espaço que ele ocupa. Para edificações, é recomendável
  cadastrar ao menos a área útil, testada e a altura de coroamento.

  Se a modulação original for conhecida ou puder ser deduzida por um estudo metrológico,
  é interessante cadastrar também as medidas históricas utilizadas (por exemplo, dimensões
  em palmos).

  O campo `description` permite uma representação textual das medidas da edificação,
  caso não seja viável cadastrar medidas individuais com precisão, ou seja preciso
  maior flexibilidade para explicar as dimensões.

  '
notes:
- This class comprises actions measuring physical properties and other values that
  can be determined by a systematic, objective procedure of direct observation of
  particular states of physical reality.
- 'An instance of E16 Measurement may use simple counting or tools, such as yardsticks
  or radiation detection devices. The interest is in the method and care applied,
  so that the reliability of the result may be judged at a later stage, or research
  continued on the associated documents. The date of the event is important for dimensions,
  which may change value over time, such as the length of an object subject to shrinkage.
  Methods and devices employed should be associated with instances of E16 Measurement
  by properties such as: *P33 used specific technique*: E29 Design or Procedure, *P125
  used object of type*: E55 Type, *P16 used specific object (was used for)*: E70 Thing,
  whereas basic techniques such as "carbon-14 dating" should be encoded using *P2
  has type (is type of)*: E55 Type. Details of methods and devices reused or reusable
  in other instances of E16 Measurement should be documented for these entities rather
  than the measurements themselves, whereas details of particular execution may be
  documented by free text or by instantiating adequate sub-activities, if the detail
  may be of interest for an overarching query.'
- Regardless whether a measurement is made by an instrument or by human senses, it
  represents the initial transition from physical reality to information without any
  other documented information object in between within the reasoning chain that would
  represent the result of the interaction of the observer or device with reality.
  Therefore, determining properties of an instance of E90 Symbolic Object is regarded
  as an instance of E13 Attribute Assignment, which may be inferred from observing
  and measuring representative carriers. In the case that the carrier can be named,
  the property *P16 used specific object (was used for)* should be used to indicate
  the instance(s) of E18 Physical Thing that was used as the empirical basis for the
  attribute assignment. For instance, inferring properties of depicted items using
  image material, such as satellite images, is not regarded as an instance of E16
  Measurement, but as a subsequent instance of E13 Attribute Assignment. Rather, only
  the production of the images, understood as arrays of radiation intensities, is
  regarded as an instance of E16 Measurement. The same reasoning holds for other sensor
  data.
from_schema: https://tradicional.arq.br/schema
related_mappings:
- dcterms:format
slots:
- unit
- description
- format_extent
- bibliographic_citation
slot_usage:
  unit:
    name: unit
    required: true
attributes:
  measurement_type:
    name: measurement_type
    description: 'designa a natureza da medida : largura, altura, área, etc. — usar
      um dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820)
      do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos
      um vocabulário controlado próprio.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    ifabsent: MeasurementType(proper)
    alias: type
    domain_of:
    - Measurement
    range: MeasurementType
  measurement_value:
    name: measurement_value
    description: Valor numérico, usar ponto como separador decimal.
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: value
    domain_of:
    - Measurement
    range: float
    required: true
    minimum_value: 0
  measurement_qualifier:
    name: measurement_qualifier
    description: 'Indica que as medidas são aproximadas.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    ifabsent: MeasurementQualifier(2)
    alias: qualifier
    domain_of:
    - Measurement
    range: MeasurementQualifier
  measurement_shape:
    name: measurement_shape
    description: 'caso relevante, indicar a forma do elemento medido usando a [lista
      de formas do AAT](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300056273),
      enquanto não tivermos um vocabulário controlado próprio.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: shape
    domain_of:
    - Measurement
    range: TypedReference
  measurement_event:
    name: measurement_event
    description: 'Descreve a ocasião em que as medidas foram aferidas, caso essa informação
      seja relevante (por exemplo, no âmbito de um levantamento prévio a intervenções
      que alteraram as dimensões da edificação).

      Referencia um evento cadastrado em `temporal` pelo seu `id`.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: event
    domain_of:
    - Measurement
    range: Event
    inlined: false
class_uri: crm:E16_Measurement

```
</details>

### Induced

<details>
```yaml
name: Measurement
description: 'Informações estruturadas sobre as dimensões do objeto ou requisitos
  de condicionamento ambiental no espaço que ele ocupa. Para edificações, é recomendável
  cadastrar ao menos a área útil, testada e a altura de coroamento.

  Se a modulação original for conhecida ou puder ser deduzida por um estudo metrológico,
  é interessante cadastrar também as medidas históricas utilizadas (por exemplo, dimensões
  em palmos).

  O campo `description` permite uma representação textual das medidas da edificação,
  caso não seja viável cadastrar medidas individuais com precisão, ou seja preciso
  maior flexibilidade para explicar as dimensões.

  '
notes:
- This class comprises actions measuring physical properties and other values that
  can be determined by a systematic, objective procedure of direct observation of
  particular states of physical reality.
- 'An instance of E16 Measurement may use simple counting or tools, such as yardsticks
  or radiation detection devices. The interest is in the method and care applied,
  so that the reliability of the result may be judged at a later stage, or research
  continued on the associated documents. The date of the event is important for dimensions,
  which may change value over time, such as the length of an object subject to shrinkage.
  Methods and devices employed should be associated with instances of E16 Measurement
  by properties such as: *P33 used specific technique*: E29 Design or Procedure, *P125
  used object of type*: E55 Type, *P16 used specific object (was used for)*: E70 Thing,
  whereas basic techniques such as "carbon-14 dating" should be encoded using *P2
  has type (is type of)*: E55 Type. Details of methods and devices reused or reusable
  in other instances of E16 Measurement should be documented for these entities rather
  than the measurements themselves, whereas details of particular execution may be
  documented by free text or by instantiating adequate sub-activities, if the detail
  may be of interest for an overarching query.'
- Regardless whether a measurement is made by an instrument or by human senses, it
  represents the initial transition from physical reality to information without any
  other documented information object in between within the reasoning chain that would
  represent the result of the interaction of the observer or device with reality.
  Therefore, determining properties of an instance of E90 Symbolic Object is regarded
  as an instance of E13 Attribute Assignment, which may be inferred from observing
  and measuring representative carriers. In the case that the carrier can be named,
  the property *P16 used specific object (was used for)* should be used to indicate
  the instance(s) of E18 Physical Thing that was used as the empirical basis for the
  attribute assignment. For instance, inferring properties of depicted items using
  image material, such as satellite images, is not regarded as an instance of E16
  Measurement, but as a subsequent instance of E13 Attribute Assignment. Rather, only
  the production of the images, understood as arrays of radiation intensities, is
  regarded as an instance of E16 Measurement. The same reasoning holds for other sensor
  data.
from_schema: https://tradicional.arq.br/schema
related_mappings:
- dcterms:format
slot_usage:
  unit:
    name: unit
    required: true
attributes:
  measurement_type:
    name: measurement_type
    description: 'designa a natureza da medida : largura, altura, área, etc. — usar
      um dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820)
      do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos
      um vocabulário controlado próprio.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    ifabsent: MeasurementType(proper)
    alias: type
    owner: Measurement
    domain_of:
    - Measurement
    range: MeasurementType
  measurement_value:
    name: measurement_value
    description: Valor numérico, usar ponto como separador decimal.
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: value
    owner: Measurement
    domain_of:
    - Measurement
    range: float
    required: true
    minimum_value: 0
  measurement_qualifier:
    name: measurement_qualifier
    description: 'Indica que as medidas são aproximadas.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    ifabsent: MeasurementQualifier(2)
    alias: qualifier
    owner: Measurement
    domain_of:
    - Measurement
    range: MeasurementQualifier
  measurement_shape:
    name: measurement_shape
    description: 'caso relevante, indicar a forma do elemento medido usando a [lista
      de formas do AAT](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300056273),
      enquanto não tivermos um vocabulário controlado próprio.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: shape
    owner: Measurement
    domain_of:
    - Measurement
    range: TypedReference
  measurement_event:
    name: measurement_event
    description: 'Descreve a ocasião em que as medidas foram aferidas, caso essa informação
      seja relevante (por exemplo, no âmbito de um levantamento prévio a intervenções
      que alteraram as dimensões da edificação).

      Referencia um evento cadastrado em `temporal` pelo seu `id`.

      '
    from_schema: https://tradicional.arq.br/schema/shared
    rank: 1000
    alias: event
    owner: Measurement
    domain_of:
    - Measurement
    range: Event
    inlined: false
  unit:
    name: unit
    description: 'Unidade de medida usada no dimensionamento do objeto ou da representação,
      por exemplo metros, milímetros ou palmos. Usar a [hierarquia de unidades de
      medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096)
      do AAT, ou do nosso próprio [vocabulário controlado].

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Measurement
    domain_of:
    - Resource
    - Measurement
    range: TypedReference
    required: true
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
    owner: Measurement
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
  format_extent:
    name: format_extent
    description: 'Indica a parte do objeto que está sendo medida — por exemplo, se
      a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri`
      de um vocabulário controlado.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: extent
    owner: Measurement
    domain_of:
    - Measurement
    - Inscription
    - Topic
    range: TypedReference
    inlined: true
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
    owner: Measurement
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
class_uri: crm:E16_Measurement

```
</details></div>