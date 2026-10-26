---
search:
  boost: 5.0
---

# Slot: actor_type


_Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, uma família, etc._

__



<div data-search-exclude markdown="1">



URI: [wasth:actor_type](https://tradicional.arq.br/schema/actor_type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Actor](Actor.md) | Agent and role in an event |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AgentType](AgentType.md) |
| Domain Of | [Actor](Actor.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| If Absent | `AgentType(personal)` |
| Owner | [Actor](Actor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:actor_type |
| native | wasth:actor_type |




## LinkML Source

<details>
```yaml
name: actor_type
description: 'Define se o agente é uma pessoa, uma organização ou corporação, uma
  oficina, uma família, etc.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
ifabsent: AgentType(personal)
alias: type
owner: Actor
domain_of:
- Actor
range: AgentType

```
</details></div>
