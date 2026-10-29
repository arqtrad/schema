---
search:
  boost: 5.0
---

# Slot: repositories 


_Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc._

_O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica._

_---------------------------------------------------------------------_

_A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus._

_Repeated if there are several designations known, or if former repositories or geographic places should be listed._

__



<div data-search-exclude markdown="1">



URI: [wasth:repositories](https://tradicional.arq.br/schema/repositories)
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
| Range | [Repository](Repository.md) |
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
| self | wasth:repositories |
| native | wasth:repositories |




## LinkML Source

<details>
```yaml
name: repositories
description: 'Nos Documentários da Arquitetura Tradicional, usamos repositórios para
  indicar a inclusão da edificação em perímetros de sítios tombados/classificados
  do patrimônio, áreas de interesse histórico-cultural, etc.

  O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.

  ---------------------------------------------------------------------

  A set of elements for the identification, name and location of the repository that
  is responsible for the object/work in focus.

  Repeated if there are several designations known, or if former repositories or geographic
  places should be listed.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: Repository
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>