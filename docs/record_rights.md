---
search:
  boost: 5.0
---

# Slot: record_rights 


_Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha._

_⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito._

_---------------------------------------------------------------------_

_A set of structured information about rights regarding the content provided in this LIDO record._

__



<div data-search-exclude markdown="1">



URI: [wasth:record_rights](https://tradicional.arq.br/schema/record_rights)
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
| Range | [Right](Right.md) |
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
| self | wasth:record_rights |
| native | wasth:record_rights |




## LinkML Source

<details>
```yaml
name: record_rights
description: 'Informações estruturadas sobre os direitos que incidem sobre o conteúdo
  textual desta ficha.

  ⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos
  incidentes sobre o objeto descrito.

  ---------------------------------------------------------------------

  A set of structured information about rights regarding the content provided in this
  LIDO record.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: Right
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>