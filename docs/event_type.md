---
search:
  boost: 5.0
---

# Slot: event_type 


_Categoriza o evento segundo os vários tipos de ações, de processos, ou de resultados (início ou fim da existência, transformação)._

__



<div data-search-exclude markdown="1">



URI: [wasth:event_type](https://tradicional.arq.br/schema/event_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EventType](EventType.md) |
| Domain Of | [Event](Event.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | wasth:event_type |
| native | wasth:event_type |




## LinkML Source

<details>
```yaml
name: event_type
description: 'Categoriza o evento segundo os vários tipos de ações, de processos,
  ou de resultados (início ou fim da existência, transformação).

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: type
owner: Event
domain_of:
- Event
range: EventType
required: true

```
</details></div>