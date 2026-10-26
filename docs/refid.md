---
search:
  boost: 5.0
---

# Slot: refid


_Local or external identifier._



<div data-search-exclude markdown="1">



URI: [dcterm:identifier](dcterm:identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |  no  |
| [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [BibliographicCitation](BibliographicCitation.md), [TypedReference](TypedReference.md) |
| Slot URI | [dcterm:identifier](dcterm:identifier) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Key | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:identifier |
| native | wasth:refid |
| exact | schema:identifier |




## LinkML Source

<details>
```yaml
name: refid
description: Local or external identifier.
from_schema: https://tradicional.arq.br/schema
exact_mappings:
- schema:identifier
rank: 1000
slot_uri: dcterm:identifier
key: true
domain_of:
- BibliographicCitation
- TypedReference
range: uriorcurie
required: true

```
</details></div>
