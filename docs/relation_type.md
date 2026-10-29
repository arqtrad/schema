---
search:
  boost: 5.0
---

# Slot: relation_type 


_Usamos os tipos de relação previstos pelo [VRA Core]. Provavelmente necessitamos apenas de :_

_- `planFor` : desenho técnico bidimensional de levantamento_

_  (padrão, pode ser omitido) ;_

__

_- `modelFor` : modelo tridimensional, com ou sem informações construtivas_

_  associadas (BIM) ;_

__

_- `imageOf` : outras representações em duas dimensões da edificação ;_

_- `preparatoryFor` : representação técnica de projeto para intervenções a_

_  serem realizadas (ou já realizadas) na edificação._

__



<div data-search-exclude markdown="1">



URI: [wasth:relation_type](https://tradicional.arq.br/schema/relation_type)
Alias: rel_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [RelatedWork](RelatedWork.md) | As formas mais comuns de relação no nosso projeto são : |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RelationType](RelationType.md) |
| Domain Of | [RelatedObject](RelatedObject.md), [Resource](Resource.md) |
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
| self | wasth:relation_type |
| native | wasth:relation_type |




## LinkML Source

<details>
```yaml
name: relation_type
description: "Usamos os tipos de relação previstos pelo [VRA Core]. Provavelmente\
  \ necessitamos apenas de :\n- `planFor` : desenho técnico bidimensional de levantamento\n\
  \  (padrão, pode ser omitido) ;\n\n- `modelFor` : modelo tridimensional, com ou\
  \ sem informações construtivas\n  associadas (BIM) ;\n\n- `imageOf` : outras representações\
  \ em duas dimensões da edificação ;\n- `preparatoryFor` : representação técnica\
  \ de projeto para intervenções a\n  serem realizadas (ou já realizadas) na edificação.\n"
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: rel_type
domain_of:
- RelatedObject
- Resource
range: RelationType
required: true

```
</details></div>