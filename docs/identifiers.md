---
search:
  boost: 5.0
---

# Slot: identifiers 


_Números de inventário e demais códigos que identificam este objeto em outras bases de dados._

_Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue._

_:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :_

_* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou_

_  `local` — se estiver em dúvida, omita esta linha ;_

__

_* `refid` é obrigatório : representa o identificador do conceito no_

_  vocabulário controlado ou no repositório de origem — normalmente_

_  será uma URI (um link para a página web do cadastro) ;_

__

_* `description` deve ser usado para representar textualmente_

_  o número de inventário, código identificador ou outra informação_

_  que individualize o objeto na base externa (por exemplo, livro do_

_  tombo e número do processo de tombamento, no Brasil) ;_

__

_* `bibliographic_citation` é opcional e permite citar uma lista de_

_  referências bibliográficas que validem a inclusão deste termo._

__

_* `source` também é opcional e permite cadastrar os dados da pessoa_

_  jurídica responsável pelo registro._

__

_---------------------------------------------------------------------_

_Published or external identifiers for the object._

__



<div data-search-exclude markdown="1">



URI: [wasth:identifiers](https://tradicional.arq.br/schema/identifiers)
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
| Range | [TypedReference](TypedReference.md) |
| Domain Of | [Thing](Thing.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


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
| self | wasth:identifiers |
| native | wasth:identifiers |




## LinkML Source

<details>
```yaml
name: identifiers
description: "Números de inventário e demais códigos que identificam este objeto em\
  \ outras bases de dados.\nCaso esta edificação esteja cadastrada em outras bases\
  \ de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher\
  \ a lista `identifiers` como segue.\n:clipboard: O conteúdo de cada bloco é uma\
  \ lista recuada em dois espaços com respeito à categoria superior. Seus itens são :\n\
  * `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou\n  `local` —\
  \ se estiver em dúvida, omita esta linha ;\n\n* `refid` é obrigatório : representa\
  \ o identificador do conceito no\n  vocabulário controlado ou no repositório de\
  \ origem — normalmente\n  será uma URI (um link para a página web do cadastro) ;\n\
  \n* `description` deve ser usado para representar textualmente\n  o número de inventário,\
  \ código identificador ou outra informação\n  que individualize o objeto na base\
  \ externa (por exemplo, livro do\n  tombo e número do processo de tombamento, no\
  \ Brasil) ;\n\n* `bibliographic_citation` é opcional e permite citar uma lista de\n\
  \  referências bibliográficas que validem a inclusão deste termo.\n\n* `source`\
  \ também é opcional e permite cadastrar os dados da pessoa\n  jurídica responsável\
  \ pelo registro.\n\n---------------------------------------------------------------------\n\
  Published or external identifiers for the object.\n"
from_schema: https://tradicional.arq.br/schema
rank: 1000
owner: Thing
domain_of:
- Thing
range: TypedReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>