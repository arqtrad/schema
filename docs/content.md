---
search:
  boost: 5.0
---

# Slot: content 


_Conteúdo textual descritivo ou explicativo._



<div data-search-exclude markdown="1">



URI: [skos:scopeNote](http://www.w3.org/2004/02/skos/core#scopeNote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  yes  |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Thing](Thing.md), [Inscription](Inscription.md) |
| Slot URI | [skos:scopeNote](http://www.w3.org/2004/02/skos/core#scopeNote) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:scopeNote |
| native | wasth:content |




## LinkML Source

<details>
```yaml
name: content
description: Conteúdo textual descritivo ou explicativo.
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: skos:scopeNote
domain_of:
- Thing
- Inscription
range: string
recommended: true

```
</details></div>