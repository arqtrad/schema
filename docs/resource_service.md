---
search:
  boost: 5.0
---

# Slot: resource_service 


_Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal como a especificação [IIIF]._



<div data-search-exclude markdown="1">



URI: [wasth:resource_service](https://tradicional.arq.br/schema/resource_service)
Alias: service

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Resource](Resource.md), [MediaObject](MediaObject.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:resource_service |
| native | wasth:resource_service |




## LinkML Source

<details>
```yaml
name: resource_service
description: Apenas no caso de a imagem ser fornecida como um serviço dinâmico online,
  tal como a especificação [IIIF].
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: service
domain_of:
- Resource
- MediaObject
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>