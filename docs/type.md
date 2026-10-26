---
search:
  boost: 5.0
---

# Slot: type

<div data-search-exclude markdown="1">



URI: [wasth:type](https://tradicional.arq.br/schema/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |  no  |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos direitos ou ... |  no  |
| [LegalBody](LegalBody.md) | Personal, corporate, family, or other responsible body |  no  |
| [Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |  no  |
| [StylePeriod](StylePeriod.md) |  |  no  |
| [EventPlace](EventPlace.md) |  |  no  |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |  no  |
| [Topic](Topic.md) | Subject or iconographic topic |  no  |
| [HistoricPlace](HistoricPlace.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Measurement](Measurement.md), [Right](Right.md), [LegalBody](LegalBody.md), [Event](Event.md), [StylePeriod](StylePeriod.md), [EventPlace](EventPlace.md), [Inscription](Inscription.md), [Topic](Topic.md), [HistoricPlace](HistoricPlace.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | wasth:type |
| native | wasth:type |




## LinkML Source

<details>
```yaml
name: type
domain_of:
- Measurement
- Right
- LegalBody
- Event
- StylePeriod
- EventPlace
- Inscription
- Topic
- HistoricPlace
range: string

```
</details></div>
