---
search:
  boost: 5.0
---

# Slot: title_source 


_A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen)._



<div data-search-exclude markdown="1">



URI: [wasth:title_source](https://tradicional.arq.br/schema/title_source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BibliographicCitation](BibliographicCitation.md) |
| Domain Of | [Thing](Thing.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:title_source |
| native | wasth:title_source |




## LinkML Source

<details>
```yaml
name: title_source
description: A fonte do título title_source é opcional ; um título pode ser atestado
  em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa
  com um hífen).
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: BibliographicCitation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>