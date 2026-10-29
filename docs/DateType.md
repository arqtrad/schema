---
search:
  boost: 2.0
---


# Enum: DateType 




_Exatidão da data conhecida._



<div data-search-exclude markdown="1">

URI: [wasth:DateType](https://tradicional.arq.br/schema/DateType)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| exact | term:lido00528 | Designates a date that is definitely known, based on credible, documented fac... | Title: conhecida<br>|
| estimated | term:lido00529 | Designates a date that is uncertain, estimated broadly using available inform... | Title: provável<br>|




## Slots

| Name | Description |
| ---  | --- |
| [date_type](date_type.md) | Qualifica a confiabilidade da data como sendo conhecida ou estimada |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: DateType
description: Exatidão da data conhecida.
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  exact:
    text: exact
    description: 'Designates a date that is definitely known, based on credible, documented
      fact.

      Note that *exact* does not preclude the granularity of the date expression.

      '
    meaning: term:lido00528
    title: conhecida
  estimated:
    text: estimated
    description: 'Designates a date that is uncertain, estimated broadly using available
      information about the work or the artist. For example, you could estimate that
      the earliest possible date for any work by a given artist is eighteen or twenty
      years after the artist''s birth.

      Included are also dates that are inferred from known dates associated with the
      object. For instance, if the date of production is unknown, but the date when
      the object was found is known, there is evidence that the production must have
      taken place before the finding of the object.

      '
    meaning: term:lido00529
    title: provável

```
</details>

</div>