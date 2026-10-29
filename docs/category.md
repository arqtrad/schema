---
search:
  boost: 5.0
---

# Slot: category 


_Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO._

_Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` ("Objeto manufaturado")._

_No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` ("Objeto conceitual")._

_---------------------------------------------------------------------_

_The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element._

_Examples are human-made object or natural object._



<div data-search-exclude markdown="1">



URI: [term:lidoCategory](http://terminology.lido-schema.org/lidoCategory)
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
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [term:lidoCategory](http://terminology.lido-schema.org/lidoCategory) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Designates Type | Yes |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | term:lidoCategory |
| native | wasth:category |




## LinkML Source

<details>
```yaml
name: category
description: 'Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário
  controlado do LIDO.

  Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096`
  ("Objeto manufaturado").

  No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193`
  ("Objeto conceitual").

  ---------------------------------------------------------------------

  The LIDO Category Vocabulary is a structured controlled list of terms recommended
  to use as values in the LIDO Category element.

  Examples are human-made object or natural object.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lidoCategory
designates_type: true
owner: Thing
domain_of:
- Thing
range: uriorcurie
required: true

```
</details></div>