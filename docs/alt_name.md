---
search:
  boost: 5.0
---

# Slot: alt_name 


_O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal._

_O campo `label` ou `description` de cada item contém o texto do título (nome)._

_Este bloco pode ser omitido por completo se não houver títulos alternativos._

__



<div data-search-exclude markdown="1">



URI: [wasth:alt_name](https://tradicional.arq.br/schema/alt_name)
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
| Range | [Appellation](Appellation.md) |
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
| self | wasth:alt_name |
| native | wasth:alt_name |




## LinkML Source

<details>
```yaml
name: alt_name
description: 'O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto
  ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir,
  os campos de cada item da lista devem ser preenchidos como os do título principal.

  O campo `label` ou `description` de cada item contém o texto do título (nome).

  Este bloco pode ser omitido por completo se não houver títulos alternativos.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: Appellation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>