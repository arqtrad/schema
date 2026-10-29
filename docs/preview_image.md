---
search:
  boost: 5.0
---

# Slot: preview_image 


_Uma única miniatura da imagem original._

_Obs.: não usamos a opção `placeholder`, ela será preenchida automaticamente em caso de ausência da miniatura, nem outros tipos de miniaturas que não imagens. A especificação LIDO admite listar mais de uma miniatura, mas tampouco prevemos essa hipótese._

__



<div data-search-exclude markdown="1">



URI: [wasth:preview_image](https://tradicional.arq.br/schema/preview_image)
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
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Resource](Resource.md), [MediaObject](MediaObject.md) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:preview_image |
| native | wasth:preview_image |




## LinkML Source

<details>
```yaml
name: preview_image
description: 'Uma única miniatura da imagem original.

  Obs.: não usamos a opção `placeholder`, ela será preenchida automaticamente em caso
  de ausência da miniatura, nem outros tipos de miniaturas que não imagens. A especificação
  LIDO admite listar mais de uma miniatura, mas tampouco prevemos essa hipótese.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Resource
- MediaObject
range: uriorcurie

```
</details></div>