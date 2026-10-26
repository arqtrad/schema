---
search:
  boost: 2.0
---


# Enum: MeasurementType




_The type attribute qualifies whether the measurements given are features of the object proper or object requirements for handling the object, for instance, the maximum temperature variation._



<div data-search-exclude markdown="1">

URI: [wasth:MeasurementType](https://tradicional.arq.br/schema/MeasurementType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| proper | term:lido00927 |  |
| requirement | term:lido00923 |  |




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | designa a natureza da medida : largura, altura, área, etc |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: MeasurementType
description: The type attribute qualifies whether the measurements given are features
  of the object proper or object requirements for handling the object, for instance,
  the maximum temperature variation.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  proper:
    text: proper
    meaning: term:lido00927
  requirement:
    text: requirement
    meaning: term:lido00923

```
</details>

</div>
