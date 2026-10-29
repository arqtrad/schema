---
search:
  boost: 5.0
---

# Slot: source 

<div data-search-exclude markdown="1">



URI: [wasth:source](https://tradicional.arq.br/schema/source)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |  no  |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |
| [RelatedWork](RelatedWork.md) | As formas mais comuns de relação no nosso projeto são : |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LegalBody](LegalBody.md) |
| Domain Of | [RelatedObject](RelatedObject.md), [MediaObject](MediaObject.md), [TypedReference](TypedReference.md), [GeographicPoint](GeographicPoint.md), [GeographicExtent](GeographicExtent.md) |
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
| self | wasth:source |
| native | wasth:source |




## LinkML Source

<details>
```yaml
name: source
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- RelatedObject
- MediaObject
- TypedReference
- GeographicPoint
- GeographicExtent
range: LegalBody
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>