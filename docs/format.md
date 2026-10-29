---
search:
  boost: 5.0
---

# Slot: format 


_Campo disciplinado pela especificação [DublinCore] no campo [format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/). Esta especificação sugere a [lista de tipos de mídia IANA]._

__



<div data-search-exclude markdown="1">



URI: [dcterms:format](http://purl.org/dc/terms/format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [MediaObject](MediaObject.md) |
| Slot URI | [dcterms:format](http://purl.org/dc/terms/format) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:format |
| native | wasth:format |




## LinkML Source

<details>
```yaml
name: format
description: 'Campo disciplinado pela especificação [DublinCore] no campo [format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/).
  Esta especificação sugere a [lista de tipos de mídia IANA].

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:format
domain_of:
- MediaObject
range: TypedReference
required: true
inlined: true

```
</details></div>