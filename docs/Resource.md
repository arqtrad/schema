---
search:
  boost: 5.0
---

# Slot: resource


_Os desenhos ou modelos da edificação são apresentados online por meio de_

_imagens vetoriais ou bitmap._

__

_Cada desenho ou modelo pode ser apresentado sob várias representações,_

_como pré-visualização, imagem original, ou serviço [IIIF]._

_Essas imagens devem ser identificadas como segue :_

__

_As categorias de representação previstas no [LIDO] podem ser consultadas_

_em <http://terminology.lido-schema.org/resourceRepresentation_type>_

_e são inseridas na ficha como um mapa._

__



<div data-search-exclude markdown="1">



URI: [wasth:resource](https://tradicional.arq.br/schema/resource)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resource](Resource.md) |
| Domain Of | [RelatedObject](RelatedObject.md), [Work](Work.md) |
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
| self | wasth:resource |
| native | wasth:resource |




## LinkML Source

<details>
```yaml
name: resource
description: 'Os desenhos ou modelos da edificação são apresentados online por meio
  de

  imagens vetoriais ou bitmap.


  Cada desenho ou modelo pode ser apresentado sob várias representações,

  como pré-visualização, imagem original, ou serviço [IIIF].

  Essas imagens devem ser identificadas como segue :


  As categorias de representação previstas no [LIDO] podem ser consultadas

  em <http://terminology.lido-schema.org/resourceRepresentation_type>

  e são inseridas na ficha como um mapa.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- RelatedObject
- Work
range: Resource
multivalued: true
inlined: true
inlined_as_list: false

```
</details></div>
