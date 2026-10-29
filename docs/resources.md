---
search:
  boost: 5.0
---

# Slot: resources 


_Os desenhos ou modelos da edificação são apresentados online por meio de imagens vetoriais ou bitmap._

_Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização, imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :_

_As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type> e são inseridas na ficha como um mapa._

__



<div data-search-exclude markdown="1">



URI: [wasth:resources](https://tradicional.arq.br/schema/resources)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |
| [RelatedWork](RelatedWork.md) | As formas mais comuns de relação no nosso projeto são : |  no  |






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
| self | wasth:resources |
| native | wasth:resources |




## LinkML Source

<details>
```yaml
name: resources
description: 'Os desenhos ou modelos da edificação são apresentados online por meio
  de imagens vetoriais ou bitmap.

  Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização,
  imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :

  As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type>
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