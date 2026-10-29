---
search:
  boost: 5.0
---

# Slot: id 


_Identificador globalmente único para este objeto ou recurso._

__



<div data-search-exclude markdown="1">



URI: [dcterms:identifier](http://purl.org/dc/terms/identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  yes  |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:identifier](http://purl.org/dc/terms/identifier) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:identifier |
| native | wasth:id |




## LinkML Source

<details>
```yaml
name: id
description: 'Identificador globalmente único para este objeto ou recurso.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:identifier
identifier: true
owner: Thing
domain_of:
- Thing
range: uriorcurie
required: true

```
</details></div>