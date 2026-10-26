---
search:
  boost: 10.0
---

# Class: HistoricPlace


_Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a localização original de uma construção fisicamente deslocada (para tanto, cadastrar outra localização do tipo `former_site`). Preencher apenas caso a nomenclatura seja relevante, por exemplo para nomear as antigas províncias de Portugal ou o Oeste da Bahia, que originalmente pertencia a Pernambuco, ou ainda se for relevante informar uma região física._



<div data-search-exclude markdown="1">



URI: [wasth:HistoricPlace](https://tradicional.arq.br/schema/HistoricPlace)





```mermaid
 classDiagram
    class HistoricPlace
    click HistoricPlace href "../HistoricPlace/"
      HistoricPlace : name





        HistoricPlace --> "1" TypedReference : name
        click TypedReference href "../TypedReference/"



      HistoricPlace : type





        HistoricPlace --> "1" RepositoryType : type
        click RepositoryType href "../RepositoryType/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1 <br/> [RepositoryType](RepositoryType.md) |  | direct |
| [name](name.md) | 1 <br/> [TypedReference](TypedReference.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Work](Work.md) | [location_historic](location_historic.md) | range | [HistoricPlace](HistoricPlace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:HistoricPlace |
| native | wasth:HistoricPlace |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HistoricPlace
description: Designações alternativas ou jurisdições antigas para o mesmo local, NÃO
  a localização original de uma construção fisicamente deslocada (para tanto, cadastrar
  outra localização do tipo `former_site`). Preencher apenas caso a nomenclatura seja
  relevante, por exemplo para nomear as antigas províncias de Portugal ou o Oeste
  da Bahia, que originalmente pertencia a Pernambuco, ou ainda se for relevante informar
  uma região física.
from_schema: https://tradicional.arq.br/schema
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/work
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
    range: RepositoryType
    required: true
  name:
    name: name
    from_schema: https://tradicional.arq.br/schema/work
    domain_of:
    - ConceptReference
    - LegalBody
    - RelatedEvent
    - HistoricPlace
    range: TypedReference
    required: true
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: HistoricPlace
description: Designações alternativas ou jurisdições antigas para o mesmo local, NÃO
  a localização original de uma construção fisicamente deslocada (para tanto, cadastrar
  outra localização do tipo `former_site`). Preencher apenas caso a nomenclatura seja
  relevante, por exemplo para nomear as antigas províncias de Portugal ou o Oeste
  da Bahia, que originalmente pertencia a Pernambuco, ou ainda se for relevante informar
  uma região física.
from_schema: https://tradicional.arq.br/schema
attributes:
  type:
    name: type
    from_schema: https://tradicional.arq.br/schema/work
    owner: HistoricPlace
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
    range: RepositoryType
    required: true
  name:
    name: name
    from_schema: https://tradicional.arq.br/schema/work
    owner: HistoricPlace
    domain_of:
    - ConceptReference
    - LegalBody
    - RelatedEvent
    - HistoricPlace
    range: TypedReference
    required: true
    inlined: true

```
</details></div>
