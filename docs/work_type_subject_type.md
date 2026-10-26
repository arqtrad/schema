---
search:
  boost: 5.0
---

# Slot: work_type_subject_type


_Descriptors for objects that are distinguishable by their topics, themes, or other content of the work. If an object is identified by what it is of or about, then it is qualified by subject._

_Based on [AAT "subjects"](http://vocab.getty.edu/page/aat/300404126)_

_Nos Documentários da Arquitetura Tradicional, é o único bloco opcional desta seção : ele indica, se houver, uma classificação iconográfica mais específica do que `form` ou `function`._



<div data-search-exclude markdown="1">



URI: [term:lido00768](http://terminology.lido-schema.org/lido00768)
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
| Slot URI | [term:lido00768](http://terminology.lido-schema.org/lido00768) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
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
| self | term:lido00768 |
| native | wasth:work_type_subject_type |




## LinkML Source

<details>
```yaml
name: work_type_subject_type
description: 'Descriptors for objects that are distinguishable by their topics, themes,
  or other content of the work. If an object is identified by what it is of or about,
  then it is qualified by subject.

  Based on [AAT "subjects"](http://vocab.getty.edu/page/aat/300404126)

  Nos Documentários da Arquitetura Tradicional, é o único bloco opcional desta seção :
  ele indica, se houver, uma classificação iconográfica mais específica do que `form`
  ou `function`.'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido00768
owner: Work
domain_of:
- Work
range: ConceptReference
recommended: true
multivalued: true
inlined_as_list: false

```
</details></div>
