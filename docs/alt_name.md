---
search:
  boost: 5.0
---

# Slot: alt_name


_O bloco `alt_name` permite cadastrar outros nomes pelos quais a edificação_

_será eventualmente conhecida. É uma lista opcional de itens, e se_

_existir, os campos de cada item da lista devem ser preenchidos como os do_

_título principal._

__

_O campo `description` de cada item contém o texto do título (nome)._

__

_Este bloco pode ser omitido por completo se não houver títulos_

_alternativos._

__



<div data-search-exclude markdown="1">



URI: [wasth:alt_name](https://tradicional.arq.br/schema/alt_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |  no  |
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
| Range | [Appellation](Appellation.md) |
| Domain Of | [Thing](Thing.md) |
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
| self | wasth:alt_name |
| native | wasth:alt_name |




## LinkML Source

<details>
```yaml
name: alt_name
description: 'O bloco `alt_name` permite cadastrar outros nomes pelos quais a edificação

  será eventualmente conhecida. É uma lista opcional de itens, e se

  existir, os campos de cada item da lista devem ser preenchidos como os do

  título principal.


  O campo `description` de cada item contém o texto do título (nome).


  Este bloco pode ser omitido por completo se não houver títulos

  alternativos.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
domain_of:
- Thing
range: Appellation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
