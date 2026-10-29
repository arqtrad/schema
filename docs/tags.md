---
search:
  boost: 5.0
---

# Slot: tags 


_Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:_

_- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional._

_---------------------------------------------------------------------_

_Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms._



<div data-search-exclude markdown="1">



URI: [wasth:tags](https://tradicional.arq.br/schema/tags)
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
| Range | [String](String.md) |
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
| self | wasth:tags |
| native | wasth:tags |




## LinkML Source

<details>
```yaml
name: tags
description: 'Lista de palavras-chave que caracterizam o objeto, de modo não estruturado.
  Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:

  - Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; -
  Temático ou tipológico ; - Funcional.

  ---------------------------------------------------------------------

  Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated
  vocabulary terms.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: string
multivalued: true

```
</details></div>