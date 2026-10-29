---
search:
  boost: 5.0
---

# Slot: refid 


_Local or external identifier._



<div data-search-exclude markdown="1">



URI: [dcterms:identifier](http://purl.org/dc/terms/identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |  yes  |
| [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [BibliographicCitation](BibliographicCitation.md), [TypedReference](TypedReference.md) |
| Slot URI | [dcterms:identifier](http://purl.org/dc/terms/identifier) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:identifier |
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
slot_uri: dcterms:identifier
domain_of:
- BibliographicCitation
- TypedReference
range: uriorcurie

```
</details></div>