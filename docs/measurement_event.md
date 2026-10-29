---
search:
  boost: 5.0
---

# Slot: measurement_event 


_Descreve a ocasião em que as medidas foram aferidas, caso essa informação seja relevante (por exemplo, no âmbito de um levantamento prévio a intervenções que alteraram as dimensões da edificação)._

_Referencia um evento cadastrado em `temporal` pelo seu `id`._

__



<div data-search-exclude markdown="1">



URI: [wasth:measurement_event](https://tradicional.arq.br/schema/measurement_event)
Alias: event

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Event](Event.md) |
| Domain Of | [Measurement](Measurement.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Measurement](Measurement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:measurement_event |
| native | wasth:measurement_event |




## LinkML Source

<details>
```yaml
name: measurement_event
description: 'Descreve a ocasião em que as medidas foram aferidas, caso essa informação
  seja relevante (por exemplo, no âmbito de um levantamento prévio a intervenções
  que alteraram as dimensões da edificação).

  Referencia um evento cadastrado em `temporal` pelo seu `id`.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: event
owner: Measurement
domain_of:
- Measurement
range: Event
inlined: false

```
</details></div>