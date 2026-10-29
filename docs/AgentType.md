---
search:
  boost: 2.0
---


# Enum: AgentType 




_Tipo de agente na terminologia LIDO._



<div data-search-exclude markdown="1">

URI: [wasth:AgentType](https://tradicional.arq.br/schema/AgentType)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| personal | term:lido00163 |  | Title: individual<br>|
| corporate | term:lido00413 | Uma entidade coletiva tal como uma oficina, escola (no sentido de um grupo de... | Title: coletivo<br>|
| family | term:lido00166 | Coletivo de agentes caracterizado por laços familiares, incluindo parentesco ... | Title: familiar<br>|
| other | term:lido00165 |  | Title: outro<br>|




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
description: Tipo de agente na terminologia LIDO.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  personal:
    text: personal
    meaning: term:lido00163
    title: individual
  corporate:
    text: corporate
    description: 'Uma entidade coletiva tal como uma oficina, escola (no sentido de
      um grupo de artistas que partilham um estilo semelhante), empresa, corporação
      de ofício, grupo étnico-cultural, ou outra agremiação na qual é impossível ou
      irrelevante delimitar as contribuições individuais.

      '
    meaning: term:lido00413
    title: coletivo
  family:
    text: family
    description: 'Coletivo de agentes caracterizado por laços familiares, incluindo
      parentesco consanguíneo, por matrimônio, adotivo ou outras relações familiares
      socialmente sancionadas no seu contexto de origem.

      '
    meaning: term:lido00166
    title: familiar
  other:
    text: other
    meaning: term:lido00165
    title: outro

```
</details>

</div>