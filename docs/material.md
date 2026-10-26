---
search:
  boost: 5.0
---

# Slot: material


_This class is a specialization of E55 Type and comprises the concepts of materials._

_Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing)._

_This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E57 Material, e.g. “instances of gold”._

_It is recommended that internationally or nationally agreed codes and terminology should be used._

__



<div data-search-exclude markdown="1">



URI: [crm:E57_Material](http://www.cidoc-crm.org/cidoc-crm/E57_Material)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [Work](Work.md) | An historical landmark or building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MaterialTech](MaterialTech.md) |
| Domain Of | [Event](Event.md), [Work](Work.md) |
| Slot URI | [crm:E57_Material](http://www.cidoc-crm.org/cidoc-crm/E57_Material) |
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
| self | crm:E57_Material |
| native | wasth:material |
| exact | vra:Material |




## LinkML Source

<details>
```yaml
name: material
description: 'This class is a specialization of E55 Type and comprises the concepts
  of materials.

  Instances of E57 Material may denote properties of matter before its use, during
  its use, and as incorporated in an object, such as ultramarine powder, tempera paste,
  reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks,
  sheets of fabric, pieces of metal, should be modelled individually in the same way
  as other objects. Discrete used or processed pieces, such as the stones from Nefer
  Titi''s temple, should be modelled as parts (cf. P46 is composed of (forms part
  of): E18 Physical Thing).

  This type is used categorically in the model without reference to instances of it,
  i.e. the Model does not foresee the description of instances of instances of E57
  Material, e.g. “instances of gold”.

  It is recommended that internationally or nationally agreed codes and terminology
  should be used.

  '
from_schema: https://tradicional.arq.br/schema
exact_mappings:
- vra:Material
rank: 1000
slot_uri: crm:E57_Material
domain_of:
- Event
- Work
range: MaterialTech
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
