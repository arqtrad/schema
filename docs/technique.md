---
search:
  boost: 5.0
---

# Slot: technique


_The production or manufacturing processes, techniques, and methods incorporated in the fabrication or alteration of the work or image._

__



<div data-search-exclude markdown="1">



URI: [vra:Technique](http://purl.org/vra/Technique)
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
| Slot URI | [vra:Technique](http://purl.org/vra/Technique) |
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
| self | vra:Technique |
| native | wasth:technique |
| close | crm:E55_Type |




## LinkML Source

<details>
```yaml
name: technique
description: 'The production or manufacturing processes, techniques, and methods incorporated
  in the fabrication or alteration of the work or image.

  '
from_schema: https://tradicional.arq.br/schema
close_mappings:
- crm:E55_Type
rank: 1000
slot_uri: vra:Technique
domain_of:
- Event
- Work
range: MaterialTech
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
