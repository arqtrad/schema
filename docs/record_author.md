---
search:
  boost: 5.0
---

# Slot: record_author 


_ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita._

__



<div data-search-exclude markdown="1">



URI: [dcterms:contributor](http://purl.org/dc/terms/contributor)
Alias: author

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |  no  |
| [Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |  no  |
| [Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |  no  |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |  no  |
| [Repository](Repository.md) | Entidade com existência jurídica e espacial |  no  |
| [Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |  no  |
| [Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OrcidId](OrcidId.md) |
| Domain Of | [Thing](Thing.md) |
| Slot URI | [dcterms:contributor](http://purl.org/dc/terms/contributor) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Thing](Thing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:contributor |
| native | wasth:record_author |




## LinkML Source

<details>
```yaml
name: record_author
description: 'ORCID iD da pessoa que escreveu a versão original da ficha. Alterar
  apenas no caso de a ficha ter sido substancialmente reescrita.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
slot_uri: dcterms:contributor
alias: author
owner: Thing
domain_of:
- Thing
range: OrcidId

```
</details></div>