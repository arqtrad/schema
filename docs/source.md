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
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |  no  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |  no  |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Media](Media.md) | Descrição e referência a um único arquivo de mídia |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LegalBody](LegalBody.md) |
| Domain Of | [GeographicPoint](GeographicPoint.md), [GeographicExtent](GeographicExtent.md), [TypedReference](TypedReference.md), [RelatedObject](RelatedObject.md), [Media](Media.md) |
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
- GeographicPoint
- GeographicExtent
- TypedReference
- RelatedObject
- Media
range: LegalBody
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
