---
search:
  boost: 5.0
---

# Slot: date_value 


_Usar o formato ISO-8601 (AAAA-MM-DD). Para datas imprecisas, usar o PRIMEIRO ou o ÚLTIMO dia, mês ou ano do período delimitado, conforme se tratar de uma data de corte inicial ou final para o evento, e descrever verbalmente o período no campo `display_date`._

__



<div data-search-exclude markdown="1">



URI: [wasth:date_value](https://tradicional.arq.br/schema/date_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EventDate](EventDate.md) | Expressão complexa de uma data que pode se referir ao começo ou ao término de... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [EventDate](EventDate.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EventDate](EventDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:date_value |
| native | wasth:date_value |




## LinkML Source

<details>
```yaml
name: date_value
description: 'Usar o formato ISO-8601 (AAAA-MM-DD). Para datas imprecisas, usar o
  PRIMEIRO ou o ÚLTIMO dia, mês ou ano do período delimitado, conforme se tratar de
  uma data de corte inicial ou final para o evento, e descrever verbalmente o período
  no campo `display_date`.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: EventDate
domain_of:
- EventDate
range: date

```
</details></div>