---
search:
  boost: 10.0
---

# Class: LegalBody


_Personal, corporate, family, or other responsible body._



<div data-search-exclude markdown="1">



URI: [wasth:LegalBody](https://tradicional.arq.br/schema/LegalBody)





```mermaid
 classDiagram
    class LegalBody
    click LegalBody href "../LegalBody/"
      LegalBody : legal_body_name





        LegalBody --> "0..1" TypedReference : legal_body_name
        click TypedReference href "../TypedReference/"



      LegalBody : legal_body_type





        LegalBody --> "0..1" RepositoryType : legal_body_type
        click RepositoryType href "../RepositoryType/"




```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [legal_body_type](legal_body_type.md) | 0..1 <br/> [RepositoryType](RepositoryType.md) |  | direct |
| [legal_body_name](legal_body_name.md) | 0..1 <br/> [TypedReference](TypedReference.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeographicPoint](GeographicPoint.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [GeographicExtent](GeographicExtent.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [TypedReference](TypedReference.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [Right](Right.md) | [right_holder](right_holder.md) | range | [LegalBody](LegalBody.md) |
| [RelatedObject](RelatedObject.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [RelatedWork](RelatedWork.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [Media](Media.md) | [source](source.md) | range | [LegalBody](LegalBody.md) |
| [Repository](Repository.md) | [legal_body](legal_body.md) | range | [LegalBody](LegalBody.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:LegalBody |
| native | wasth:LegalBody |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalBody
description: Personal, corporate, family, or other responsible body.
from_schema: https://tradicional.arq.br/schema
slots:
- legal_body_type
- legal_body_name

```
</details>

### Induced

<details>
```yaml
name: LegalBody
description: Personal, corporate, family, or other responsible body.
from_schema: https://tradicional.arq.br/schema
attributes:
  legal_body_type:
    name: legal_body_type
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    ifabsent: string(corporate)
    alias: type
    owner: LegalBody
    domain_of:
    - LegalBody
    range: RepositoryType
  legal_body_name:
    name: legal_body_name
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: name
    owner: LegalBody
    domain_of:
    - LegalBody
    range: TypedReference
    inlined: true

```
</details></div>
