---
search:
  boost: 5.0
---

# Slot: record_rights


_A set of structured information about rights regarding the content provided in this LIDO record._

_---------------------------------------------------------------------_

_:warning: Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito._

__



<div data-search-exclude markdown="1">



URI: [wasth:record_rights](https://tradicional.arq.br/schema/record_rights)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Right](Right.md) |
| Domain Of | [Thing](Thing.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
description: 'A set of structured information about rights regarding the content provided
  in this LIDO record.

  ---------------------------------------------------------------------

  :warning: Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre
  os direitos incidentes sobre o objeto descrito.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: Right
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
