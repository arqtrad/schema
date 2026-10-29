---
search:
  boost: 2.0
---


# Enum: EventPlaceType 




_Para eventos que implicam a deslocação do bem, indica se o local se refere ao descobrimento, à origem ou ao destino da obra._



<div data-search-exclude markdown="1">

URI: [wasth:EventPlaceType](https://tradicional.arq.br/schema/EventPlaceType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| discovery | term:lido01037 |  |
| origin | term:lido00220 |  |
| destination | term:lido00221 |  |




## Slots

| Name | Description |
| ---  | --- |
| [event_place_type](event_place_type.md) | Se relevante para a ação, indicar se se trata do local de descobrimento do ob... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: EventPlaceType
description: Para eventos que implicam a deslocação do bem, indica se o local se refere
  ao descobrimento, à origem ou ao destino da obra.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  discovery:
    text: discovery
    meaning: term:lido01037
  origin:
    text: origin
    meaning: term:lido00220
  destination:
    text: destination
    meaning: term:lido00221

```
</details>

</div>