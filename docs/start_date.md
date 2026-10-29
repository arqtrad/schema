---
search:
  boost: 5.0
---

# Slot: start_date 


_Data inicial do evento ou mais antiga data presumida para o seu decurso. Omitir se desconhecida._

_Por ora, é responsabilidade de quem preenche a ficha assegurar que `start_date` e `end_date` ocorram em ordem cronológica. Não dispomos de validação automática para tanto._

__



<div data-search-exclude markdown="1">



URI: [wasth:start_date](https://tradicional.arq.br/schema/start_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EventDate](EventDate.md) |
| Domain Of | [Event](Event.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 0 |
| Maximum Cardinality | 2 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Event](Event.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:start_date |
| native | wasth:start_date |




## LinkML Source

<details>
```yaml
name: start_date
description: 'Data inicial do evento ou mais antiga data presumida para o seu decurso.
  Omitir se desconhecida.

  Por ora, é responsabilidade de quem preenche a ficha assegurar que `start_date`
  e `end_date` ocorram em ordem cronológica. Não dispomos de validação automática
  para tanto.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Event
domain_of:
- Event
range: EventDate
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 0
maximum_cardinality: 2

```
</details></div>