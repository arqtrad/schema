---
search:
  boost: 5.0
---

# Slot: repositories


_A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus._

_Repeated if there are several designations known, or if former repositories or geographic places should be listed._

_---------------------------------------------------------------------_

_Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios do patrimônio cultural, etc._

_Os repositórios devem ser cadastrados de modo semelhante às informações de georreferenciamento, usando o tipo `other`._

__



<div data-search-exclude markdown="1">



URI: [wasth:repositories](https://tradicional.arq.br/schema/repositories)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






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
description: 'A set of elements for the identification, name and location of the repository
  that is responsible for the object/work in focus.

  Repeated if there are several designations known, or if former repositories or geographic
  places should be listed.

  ---------------------------------------------------------------------

  Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a
  inclusão da edificação em perímetros de sítios do patrimônio cultural, etc.

  Os repositórios devem ser cadastrados de modo semelhante às informações de georreferenciamento,
  usando o tipo `other`.

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
