---
search:
  boost: 2.0
---


# Enum: RepositoryType 




_Type of repository or legal body._



<div data-search-exclude markdown="1">

URI: [wasth:RepositoryType](https://tradicional.arq.br/schema/RepositoryType)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| corporate | None |  | Title: institucional<br>|
| geographic | None |  | Title: geográfico<br>|
| personal | None |  | Title: individual<br>|
| other | None |  | Title: outro<br>|




## Slots

| Name | Description |
| ---  | --- |
| [legal_body_type](legal_body_type.md) | Define a natureza do ente legal : pessoa jurídica, perímetro geográfico de tu... |
| [location_historic_type](location_historic_type.md) | Define se o local histórico designa uma jurisdição, um topônimo antigo, ou ou... |
| [title_type](title_type.md) |  |
| [title_type](title_type.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: RepositoryType
description: Type of repository or legal body.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  corporate:
    text: corporate
    title: institucional
  geographic:
    text: geographic
    title: geográfico
  personal:
    text: personal
    title: individual
  other:
    text: other
    title: outro

```
</details>

</div>