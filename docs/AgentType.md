---
search:
  boost: 2.0
---


# Enum: AgentType




_LIDO actor type._



<div data-search-exclude markdown="1">

URI: [wasth:AgentType](https://tradicional.arq.br/schema/AgentType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| personal | term:lido00163 |  |
| corporate | term:lido00413 |  |
| family | term:lido00166 |  |
| other | term:lido00165 |  |




## Slots

| Name | Description |
| ---  | --- |
| [actor_type](actor_type.md) | Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: AgentType
description: LIDO actor type.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  personal:
    text: personal
    meaning: term:lido00163
  corporate:
    text: corporate
    meaning: term:lido00413
  family:
    text: family
    meaning: term:lido00166
  other:
    text: other
    meaning: term:lido00165

```
</details>

</div>
