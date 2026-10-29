---
search:
  boost: 5.0
---

# Slot: work_type_condition 


_Descreve o estado físico da edificação quanto à sua aparência de completude, deterioração ou capacidade de desempenhar sua função._

_Atende aos campos do [SICG](https://sicg.iphan.gov.br/sicg/manual/manual.html) "estado de preservação" e "estado de conservação"._

_---------------------------------------------------------------------_

_Descriptors for objects that are distinguishable by their overall state such as appearance, level of damage, completeness, or quality. If an object is identified by its prevailing physical state, then it is qualified by condition._

_Based on [AAT "conditions"](http://vocab.getty.edu/page/aat/300389724) and [CIDOC CRM "E3 Condition State"](http://cidoc-crm.org/html/cidoc_crm_v7.1.1_with_translations.html#E3)_



<div data-search-exclude markdown="1">



URI: [term:lido00937](http://terminology.lido-schema.org/lido00937)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConceptReference](ConceptReference.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [term:lido00937](http://terminology.lido-schema.org/lido00937) |
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
| self | term:lido00937 |
| native | wasth:work_type_condition |




## LinkML Source

<details>
```yaml
name: work_type_condition
description: 'Descreve o estado físico da edificação quanto à sua aparência de completude,
  deterioração ou capacidade de desempenhar sua função.

  Atende aos campos do [SICG](https://sicg.iphan.gov.br/sicg/manual/manual.html) "estado
  de preservação" e "estado de conservação".

  ---------------------------------------------------------------------

  Descriptors for objects that are distinguishable by their overall state such as
  appearance, level of damage, completeness, or quality. If an object is identified
  by its prevailing physical state, then it is qualified by condition.

  Based on [AAT "conditions"](http://vocab.getty.edu/page/aat/300389724) and [CIDOC
  CRM "E3 Condition State"](http://cidoc-crm.org/html/cidoc_crm_v7.1.1_with_translations.html#E3)'
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: term:lido00937
owner: Work
domain_of:
- Work
range: ConceptReference
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>