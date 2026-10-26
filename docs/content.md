---
search:
  boost: 5.0
---

# Slot: content


_Deixe uma linha em branco após o fechamento dos metadados e inclua aqui_

_uma descrição morfológica e histórica da edificação com texto livre,_

_usando formatação Markdown._

__

_Poderá incluir um segundo bloco de metadados para indicar as referências_

_bibliográficas da descrição textual, no campo `nocite`._

_O formato é uma lista de chaves de citação do Zotero_

_(cada uma começando com `@`) separadas por vírgulas._

__



<div data-search-exclude markdown="1">



URI: [skos:scopeNote](http://www.w3.org/2004/02/skos/core#scopeNote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |  no  |
| [Place](Place.md) | Entities that have a somewhat fixed, physical extension |  no  |
| [Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






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
description: 'Deixe uma linha em branco após o fechamento dos metadados e inclua aqui

  uma descrição morfológica e histórica da edificação com texto livre,

  usando formatação Markdown.


  Poderá incluir um segundo bloco de metadados para indicar as referências

  bibliográficas da descrição textual, no campo `nocite`.

  O formato é uma lista de chaves de citação do Zotero

  (cada uma começando com `@`) separadas por vírgulas.

  '
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
