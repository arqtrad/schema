---
search:
  boost: 5.0
---

# Slot: title 


_Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`._

__



<div data-search-exclude markdown="1">



URI: [dcterms:title](http://purl.org/dc/terms/title)
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
| Slot URI | [dcterms:title](http://purl.org/dc/terms/title) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | dcterms:title |
| native | wasth:title |
| exact | schema:name |




## LinkML Source

<details>
```yaml
name: title
description: 'Nome pelo qual este item é mais comumente conhecido. Outros nomes podem
  ser cadastrados em `alt_name`.

  '
from_schema: https://tradicional.arq.br/schema
exact_mappings:
- schema:name
rank: 1000
slot_uri: dcterms:title
owner: Thing
domain_of:
- Thing
range: string
required: true

```
</details></div>