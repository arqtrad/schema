---
search:
  boost: 5.0
---

# Slot: related_works 


_A wrapper for identifying information about an object or work, including collections, related to the object/work in focus. May include a weblink._

_As formas mais comuns de relação no nosso projeto são :_

__

_  - depicted in: A edificação é representada numa pintura ou desenho_

_    artístico;_

__

_  - documented by: Informações sobre a edificação estão publicadas numa_

_    referência bibliográfica, processo administrativo ou outro documento_

_    textual impresso, manuscrito ou eletrônico;_

__

_  - has plan / has floor plan / has section / has elevation / has_

_    rendering: Essas relações mostram a existência de desenhos técnicos_

_    da edificação, sejam eles históricos ou recentes, compilados de_

_    fontes externas a este projeto de pesquisa._

__

_  - has construction drawing / has design / has sketch: Essas relações se_

_    referem a desenhos históricos (fontes primárias) que atestam o_

_    processo de projeto da edificação._

__

_ATENÇÃO : OS DESENHOS PRODUZIDOS POR ESTE PROJETO DE PESQUISA DEVEM SER CADASTRADOS NO GRUPO resource, MAIS ABAIXO._

_O grupo relation é destinado unicamente a cadastrar relações desta edificação com objetos autônomos, tais como outras edificações, conjuntos urbanos, obras de artes visuais, referências bibliográficas ou acervos arquivísticos._



<div data-search-exclude markdown="1">



URI: [dcterms:related](http://purl.org/dc/terms/related)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelatedWork](RelatedWork.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [dcterms:related](http://purl.org/dc/terms/related) |
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
| self | dcterms:related |
| native | wasth:related_works |




## LinkML Source

<details>
```yaml
name: related_works
description: "A wrapper for identifying information about an object or work, including\
  \ collections, related to the object/work in focus. May include a weblink.\nAs formas\
  \ mais comuns de relação no nosso projeto são :\n\n  - depicted in: A edificação\
  \ é representada numa pintura ou desenho\n    artístico;\n\n  - documented by: Informações\
  \ sobre a edificação estão publicadas numa\n    referência bibliográfica, processo\
  \ administrativo ou outro documento\n    textual impresso, manuscrito ou eletrônico;\n\
  \n  - has plan / has floor plan / has section / has elevation / has\n    rendering:\
  \ Essas relações mostram a existência de desenhos técnicos\n    da edificação, sejam\
  \ eles históricos ou recentes, compilados de\n    fontes externas a este projeto\
  \ de pesquisa.\n\n  - has construction drawing / has design / has sketch: Essas\
  \ relações se\n    referem a desenhos históricos (fontes primárias) que atestam\
  \ o\n    processo de projeto da edificação.\n\nATENÇÃO : OS DESENHOS PRODUZIDOS\
  \ POR ESTE PROJETO DE PESQUISA DEVEM SER CADASTRADOS NO GRUPO resource, MAIS ABAIXO.\n\
  O grupo relation é destinado unicamente a cadastrar relações desta edificação com\
  \ objetos autônomos, tais como outras edificações, conjuntos urbanos, obras de artes\
  \ visuais, referências bibliográficas ou acervos arquivísticos."
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:related
domain_of:
- Work
range: RelatedWork
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>