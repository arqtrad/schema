---
search:
  boost: 10.0
---

# Class: RelatedConceptReference


_Relações hierárquicas._



<div data-search-exclude markdown="1">



URI: [wasth:RelatedConceptReference](https://tradicional.arq.br/schema/RelatedConceptReference)





```mermaid
 classDiagram
    class RelatedConceptReference
    click RelatedConceptReference href "../RelatedConceptReference/"
      RelatedConceptReference : match





        RelatedConceptReference --> "0..1" SkosMappingRelation : match
        click SkosMappingRelation href "../SkosMappingRelation/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [match](match.md) | 0..1 <br/> [SkosMappingRelation](SkosMappingRelation.md) | Tipo da relação | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [relation](relation.md) | range | [RelatedConceptReference](RelatedConceptReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:RelatedConceptReference |
| native | wasth:RelatedConceptReference |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RelatedConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    domain_of:
    - BroaderConceptReference
    - RelatedConceptReference
    range: SkosMappingRelation

```
</details>

### Induced

<details>
```yaml
name: RelatedConceptReference
description: Relações hierárquicas.
from_schema: https://tradicional.arq.br/schema
attributes:
  match:
    name: match
    description: Tipo da relação.
    from_schema: https://tradicional.arq.br/schema/concept
    owner: RelatedConceptReference
    domain_of:
    - BroaderConceptReference
    - RelatedConceptReference
    range: SkosMappingRelation

```
</details></div>
