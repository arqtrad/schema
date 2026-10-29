---
search:
  boost: 5.0
---

# Slot: record_date 


_Data de inclusão da ficha._



<div data-search-exclude markdown="1">



URI: [dcterms:created](http://purl.org/dc/terms/created)
Alias: date

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
| Range | [Date](Date.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:created](http://purl.org/dc/terms/created) |
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
| self | dcterms:created |
| native | wasth:record_date |




## LinkML Source

<details>
```yaml
name: record_date
description: Data de inclusão da ficha.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:created
alias: date
owner: Thing
domain_of:
- Thing
range: date

```
</details></div>