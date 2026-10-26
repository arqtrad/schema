---
search:
  boost: 10.0
---

# Class: Container


_Todos os elementos do documentário._



<div data-search-exclude markdown="1">



URI: [wasth:Container](https://tradicional.arq.br/schema/Container)





```mermaid
 classDiagram
    class Container
    click Container href "../Container/"
      Container : concepts





        Container --> "*" Concept : concepts
        click Concept href "../Concept/"



      Container : places





        Container --> "*" Place : places
        click Place href "../Place/"



      Container : works





        Container --> "*" Work : works
        click Work href "../Work/"




```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [works](works.md) | * <br/> [Work](Work.md) | Todas as edificações documentadas | direct |
| [places](places.md) | * <br/> [Place](Place.md) | Todos os lugares cadastrados | direct |
| [concepts](concepts.md) | * <br/> [Concept](Concept.md) | Todos os termos de vocabulário controlado | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:Container |
| native | wasth:Container |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
description: Todos os elementos do documentário.
from_schema: https://tradicional.arq.br/schema
attributes:
  works:
    name: works
    description: Todas as edificações documentadas.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    domain_of:
    - Container
    range: Work
    multivalued: true
    inlined_as_list: true
  places:
    name: places
    description: Todos os lugares cadastrados.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    domain_of:
    - Container
    - EventPlace
    range: Place
    multivalued: true
    inlined_as_list: true
  concepts:
    name: concepts
    description: Todos os termos de vocabulário controlado.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    domain_of:
    - Container
    range: Concept
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
description: Todos os elementos do documentário.
from_schema: https://tradicional.arq.br/schema
attributes:
  works:
    name: works
    description: Todas as edificações documentadas.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Container
    domain_of:
    - Container
    range: Work
    multivalued: true
    inlined: true
    inlined_as_list: true
  places:
    name: places
    description: Todos os lugares cadastrados.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Container
    domain_of:
    - Container
    - EventPlace
    range: Place
    multivalued: true
    inlined: true
    inlined_as_list: true
  concepts:
    name: concepts
    description: Todos os termos de vocabulário controlado.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Container
    domain_of:
    - Container
    range: Concept
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>
