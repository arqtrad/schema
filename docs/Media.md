---
search:
  boost: 5.0
---

# Slot: media


_Representações iconográficas deste objeto._

_No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo._

_(A FAZER) Ver [Instruções para carregar imagens e desenhos]._

__



<div data-search-exclude markdown="1">



URI: [wasth:media](https://tradicional.arq.br/schema/media)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |
| [RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaObject](MediaObject.md) |
| Domain Of | [RelatedObject](RelatedObject.md), [Event](Event.md), [Work](Work.md) |
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
| self | wasth:media |
| native | wasth:media |




## LinkML Source

<details>
```yaml
name: media
description: 'Representações iconográficas deste objeto.

  No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente
  o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o
  link deve remeter a uma página web que forneça a respetiva API ou as informações
  acerca do modelo.

  (A FAZER) Ver [Instruções para carregar imagens e desenhos].

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- RelatedObject
- Event
- Work
range: MediaObject
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
