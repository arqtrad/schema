---
search:
  boost: 2.0
---


# Enum: SubjectType 




_The type attribute indicates the kind of subject information, whether it is, for instance, a description of a generic subject, an identification of a named individual, or an interpretation of the theme._

_Note that "Iconclass notations" are distinguished from other index terms for subject type in order to consider the impact of the type of indexing vocabulary with respect to information retrieval facilities._

__



<div data-search-exclude markdown="1">

URI: [wasth:SubjectType](https://tradicional.arq.br/schema/SubjectType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| descriptive | term:lido00525 |  |
| iconographic | term:lido00745 |  |
| concept | term:lido00524 |  |
| other | term:lido00136 |  |




## Slots

| Name | Description |
| ---  | --- |
| [topic_type](topic_type.md) | Categoriza o nível descritivo ou interpretativo do tema |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: SubjectType
description: 'The type attribute indicates the kind of subject information, whether
  it is, for instance, a description of a generic subject, an identification of a
  named individual, or an interpretation of the theme.

  Note that "Iconclass notations" are distinguished from other index terms for subject
  type in order to consider the impact of the type of indexing vocabulary with respect
  to information retrieval facilities.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  descriptive:
    text: descriptive
    meaning: term:lido00525
  iconographic:
    text: iconographic
    meaning: term:lido00745
  concept:
    text: concept
    meaning: term:lido00524
  other:
    text: other
    meaning: term:lido00136

```
</details>

</div>