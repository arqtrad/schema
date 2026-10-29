---
search:
  boost: 5.0
---

# Slot: concept 

<div data-search-exclude markdown="1">



URI: [wasth:concept](https://tradicional.arq.br/schema/concept)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |  no  |
| [Topic](Topic.md) | Subject or iconographic topic |  yes  |
| [BroaderConceptReference](BroaderConceptReference.md) | Relações hierárquicas |  no  |
| [NarrowerConceptReference](NarrowerConceptReference.md) | Relações hierárquicas |  no  |
| [MappingConceptReference](MappingConceptReference.md) | Relações semânticas |  no  |
| [MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |  no  |
| [StylePeriod](StylePeriod.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md) |
| Domain Of | [ConceptReference](ConceptReference.md), [Topic](Topic.md) |
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
| self | wasth:concept |
| native | wasth:concept |




## LinkML Source

<details>
```yaml
name: concept
from_schema: https://tradicional.arq.br/schema
rank: 1000
alias: name
domain_of:
- ConceptReference
- Topic
range: Concept
required: true

```
</details></div>