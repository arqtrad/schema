---
search:
  boost: 5.0
---

# Slot: classification_genre


_A broad category for grouping objects on the basis of shared intrinsic_

_characteristics. The relationship between an object/work and the object_

_genre is a generic is-a-relation rather than a membership based on_

_ascription to a subject group._

__

_Note that the_

_[AAT Object Genres](http://vocab.getty.edu/page/aat/300185711) hierarchy_

_differs in its scope from Object genre here in that the AAT includes more_

_specific terms grouped by various aspects. In general, AAT descriptors_

_are not intended to be used as indexing terms for classification._

__

_❓ Ainda não implementamos o bloco `objectClassification` do LIDO._

_Talvez ele não seja relevante para o documentário de arquitetura_

_doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação_

_para arquitetura._

__



<div data-search-exclude markdown="1">



URI: [term:lido00853](http://terminology.lido-schema.org/lido00853)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [term:lido00853](http://terminology.lido-schema.org/lido00853) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Work](Work.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | term:lido00853 |
| native | wasth:classification_genre |




## LinkML Source

<details>
```yaml
name: classification_genre
description: 'A broad category for grouping objects on the basis of shared intrinsic

  characteristics. The relationship between an object/work and the object

  genre is a generic is-a-relation rather than a membership based on

  ascription to a subject group.


  Note that the

  [AAT Object Genres](http://vocab.getty.edu/page/aat/300185711) hierarchy

  differs in its scope from Object genre here in that the AAT includes more

  specific terms grouped by various aspects. In general, AAT descriptors

  are not intended to be used as indexing terms for classification.


  ❓ Ainda não implementamos o bloco `objectClassification` do LIDO.

  Talvez ele não seja relevante para o documentário de arquitetura

  doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação

  para arquitetura.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido00853
owner: Work
domain_of:
- Work
range: ConceptReference
multivalued: true
inlined_as_list: false

```
</details></div>
