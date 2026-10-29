---
search:
  boost: 5.0
---

# Slot: culture 


_Designa o contexto cultural ou étnico no qual o objeto foi afetado pelo evento em questão, desde que as características de tal contexto estejam refletidas no objeto. O preenchimento do contexto cultural é especialmente relevante quando os agentes envolvidos na produção ou alteração do objeto são desconhecidos._

_---------------------------------------------------------------------_

_An index element for the cultural context from which the object/work in focus originated. Used if the creator or producer is unknown, or if the cultural context is of particular interest. Examples may include the name of a culture, a nation, or an ethnic group._



<div data-search-exclude markdown="1">



URI: [wasth:culture](https://tradicional.arq.br/schema/culture)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Event](Event.md), [Work](Work.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:culture |
| native | wasth:culture |




## LinkML Source

<details>
```yaml
name: culture
description: 'Designa o contexto cultural ou étnico no qual o objeto foi afetado pelo
  evento em questão, desde que as características de tal contexto estejam refletidas
  no objeto. O preenchimento do contexto cultural é especialmente relevante quando
  os agentes envolvidos na produção ou alteração do objeto são desconhecidos.

  ---------------------------------------------------------------------

  An index element for the cultural context from which the object/work in focus originated.
  Used if the creator or producer is unknown, or if the cultural context is of particular
  interest. Examples may include the name of a culture, a nation, or an ethnic group.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Event
- Work
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>