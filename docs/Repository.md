---
search:
  boost: 10.0
---

# Class: Repository


_Entidade com existência jurídica e espacial._



<div data-search-exclude markdown="1">



URI: [schema:Organization](http://schema.org/Organization)





```mermaid
 classDiagram
    class Repository
    click Repository href "../Repository/"
      Thing <|-- Repository
        click Thing href "../Thing/"

      Repository : alt_name





        Repository --> "*" Appellation : alt_name
        click Appellation href "../Appellation/"



      Repository : author

      Repository : bibliographic_citation





        Repository --> "* _recommended_" BibliographicCitation : bibliographic_citation
        click BibliographicCitation href "../BibliographicCitation/"



      Repository : category

      Repository : collection





        Repository --> "*" TypedReference : collection
        click TypedReference href "../TypedReference/"



      Repository : content

      Repository : description

      Repository : id

      Repository : identifiers





        Repository --> "*" TypedReference : identifiers
        click TypedReference href "../TypedReference/"



      Repository : legal_body





        Repository --> "1" LegalBody : legal_body
        click LegalBody href "../LegalBody/"



      Repository : record_date

      Repository : record_rights





        Repository --> "1..*" Right : record_rights
        click Right href "../Right/"



      Repository : repositories





        Repository --> "*" Repository : repositories
        click Repository href "../Repository/"



      Repository : site





        Repository --> "1" Site : site
        click Site href "../Site/"



      Repository : tags

      Repository : temporal





        Repository --> "*" Event : temporal
        click Event href "../Event/"



      Repository : title

      Repository : title_source





        Repository --> "*" BibliographicCitation : title_source
        click BibliographicCitation href "../BibliographicCitation/"



      Repository : title_type





        Repository --> "1" TitleType : title_type
        click TitleType href "../TitleType/"




```





## Inheritance
* [Thing](Thing.md)
    * **Repository**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [schema:Organization](http://schema.org/Organization) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [site](site.md) | 1 <br/> [Site](Site.md) | A localização real, atual da edificação — é o que será usado em quase todos o... | direct |
| [legal_body](legal_body.md) | 1 <br/> [LegalBody](LegalBody.md) |  | direct |
| [description](description.md) | 1 <br/> [String](String.md) | A human-readable description for a thing | [Thing](Thing.md) |
| [title_type](title_type.md) | 1 <br/> [TitleType](TitleType.md) | Indica se o título é um nome próprio, descritivo, etc | [Thing](Thing.md) |
| [bibliographic_citation](bibliographic_citation.md) | * _recommended_ <br/> [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica | [Thing](Thing.md) |
| [content](content.md) | 0..1 _recommended_ <br/> [String](String.md) | Deixe uma linha em branco após o fechamento dos metadados e inclua aqui uma d... | [Thing](Thing.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Unique identifier for this object | [Thing](Thing.md) |
| [author](author.md) | 0..1 <br/> [OrcidId](OrcidId.md) | ORCID iD of the record author or maintainer | [Thing](Thing.md) |
| [record_date](record_date.md) | 0..1 <br/> [Date](Date.md) | Date the record was created or last substantively revised | [Thing](Thing.md) |
| [title](title.md) | 1 <br/> [String](String.md) | The preferred human-readable label for a Thing | [Thing](Thing.md) |
| [title_source](title_source.md) | * <br/> [BibliographicCitation](BibliographicCitation.md) | 📚 A fonte do título title_source é opcional ; um título pode ser atestado em ... | [Thing](Thing.md) |
| [alt_name](alt_name.md) | * <br/> [Appellation](Appellation.md) | O bloco `alt_name` permite cadastrar outros nomes pelos quais a edificação se... | [Thing](Thing.md) |
| [category](category.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | The LIDO Category Vocabulary is a structured controlled list of terms recomme... | [Thing](Thing.md) |
| [identifiers](identifiers.md) | * <br/> [TypedReference](TypedReference.md) | Published or external identifiers for the object | [Thing](Thing.md) |
| [tags](tags.md) | * <br/> [String](String.md) | Provisional uncontrolled keywords | [Thing](Thing.md) |
| [temporal](temporal.md) | * <br/> [Event](Event.md) | Temporalidade do objeto | [Thing](Thing.md) |
| [collection](collection.md) | * <br/> [TypedReference](TypedReference.md) | Collections or aggregations to which the object belongs | [Thing](Thing.md) |
| [repositories](repositories.md) | * <br/> [Repository](Repository.md) | A set of elements for the identification, name and location of the repository... | [Thing](Thing.md) |
| [record_rights](record_rights.md) | 1..* <br/> [Right](Right.md) | A set of structured information about rights regarding the content provided i... | [Thing](Thing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Resource](Resource.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Event](Event.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Thing](Thing.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Repository](Repository.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Work](Work.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |
| [Site](Site.md) | [repositories](repositories.md) | range | [Repository](Repository.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:Organization |
| native | wasth:Repository |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Repository
description: Entidade com existência jurídica e espacial.
from_schema: https://tradicional.arq.br/schema
is_a: Thing
slots:
- site
- legal_body
class_uri: schema:Organization

```
</details>

### Induced

<details>
```yaml
name: Repository
description: Entidade com existência jurídica e espacial.
from_schema: https://tradicional.arq.br/schema
is_a: Thing
attributes:
  site:
    name: site
    description: A localização real, atual da edificação — é o que será usado em quase
      todos os casos.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Repository
    domain_of:
    - Repository
    - Work
    range: Site
    required: true
    inlined: true
  legal_body:
    name: legal_body
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    owner: Repository
    domain_of:
    - Repository
    range: LegalBody
    required: true
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://tradicional.arq.br/schema
    exact_mappings:
    - schema:description
    rank: 1000
    slot_uri: dcterms:description
    alias: display
    owner: Repository
    domain_of:
    - ConceptReference
    - BibliographicCitation
    - RelatedObject
    - MediaObject
    - Measurement
    - EventDate
    - EventPlace
    - RelatedEvent
    - Thing
    - Appellation
    - Inscription
    - Topic
    range: string
    required: true
  title_type:
    name: title_type
    description: Indica se o título é um nome próprio, descritivo, etc.
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    alias: type
    owner: Repository
    domain_of:
    - Thing
    - Appellation
    range: TitleType
    required: true
  bibliographic_citation:
    name: bibliographic_citation
    description: 'Cadastro de uma referência bibliográfica.

      Usar o campo `description` para formatar a referência, caso a formatação automática
      do Zotero não for satisfatória.

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: dcterms:bibliographicCitation
    owner: Repository
    domain_of:
    - ConceptReference
    - RelatedObject
    - MediaObject
    - TypedReference
    - Measurement
    - Actor
    - Thing
    - Appellation
    - GeographicPoint
    - GeographicExtent
    - Inscription
    range: BibliographicCitation
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  content:
    name: content
    description: 'Deixe uma linha em branco após o fechamento dos metadados e inclua
      aqui uma descrição morfológica e histórica da edificação com texto livre, usando
      formatação Markdown.

      Poderá incluir um segundo bloco de metadados para indicar as referências bibliográficas
      da descrição textual, no campo `nocite`. O formato é uma lista de chaves de
      citação do Zotero (cada uma começando com `@`) separadas por vírgulas:

      ```yaml Conteúdo textual em formato *Markdown* com citações [@citekey].

      --- nocite: "@*" --- ```

      '
    from_schema: https://tradicional.arq.br/schema
    rank: 1000
    slot_uri: skos:scopeNote
    owner: Repository
    domain_of:
    - Thing
    - Inscription
    range: string
    recommended: true
  id:
    name: id
    description: Unique identifier for this object.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    owner: Repository
    domain_of:
    - Thing
    range: uriorcurie
    required: true
  author:
    name: author
    description: ORCID iD of the record author or maintainer.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    slot_uri: dcterms:creator
    owner: Repository
    domain_of:
    - Thing
    range: OrcidId
  record_date:
    name: record_date
    description: Date the record was created or last substantively revised.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    slot_uri: dcterms:created
    owner: Repository
    domain_of:
    - Thing
    range: date
  title:
    name: title
    description: The preferred human-readable label for a Thing.
    from_schema: https://tradicional.arq.br/schema/thing
    exact_mappings:
    - schema:name
    rank: 1000
    slot_uri: dcterms:title
    owner: Repository
    domain_of:
    - Thing
    range: string
    required: true
  title_source:
    name: title_source
    description: '📚 A fonte do título title_source é opcional ; um título pode ser
      atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada
      item começa com um hífen).

      Se a fonte for cadastrada, o campo `refid` deve conter a chave de citação (citation
      key) que consta do registro bibliográfico na biblioteca do nosso projeto de
      pesquisa no Zotero. Em geral, a chave de citação é o DOI ou ISBN da publicação,
      mas pode ser diferente.

      Se necessário, incluir no campo note uma especificação adicional, como o número
      da página da referência bibliográfica de onde a informação foi extraída.

      Todos os campos source no restante da ficha devem ser preenchidos do mesmo modo.
      (Equivalente DublinCore: bibliographiCitation).'
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: BibliographicCitation
    multivalued: true
    inlined: true
    inlined_as_list: true
  alt_name:
    name: alt_name
    description: 'O bloco `alt_name` permite cadastrar outros nomes pelos quais a
      edificação será eventualmente conhecida. É uma lista opcional de itens, e se
      existir, os campos de cada item da lista devem ser preenchidos como os do título
      principal.

      O campo `description` de cada item contém o texto do título (nome).

      Este bloco pode ser omitido por completo se não houver títulos alternativos.

      '
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: Appellation
    multivalued: true
    inlined: true
    inlined_as_list: true
  category:
    name: category
    description: 'The LIDO Category Vocabulary is a structured controlled list of
      terms recommended to use as values in the LIDO Category element.

      Examples are human-made object or natural object.

      Nos documentários de edificações, preencher este campo obrigatoriamente com
      `term:lido00096`'
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    slot_uri: term:lidoCategory
    designates_type: true
    owner: Repository
    domain_of:
    - Thing
    range: uriorcurie
    required: true
  identifiers:
    name: identifiers
    description: Published or external identifiers for the object.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: TypedReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  tags:
    name: tags
    description: Provisional uncontrolled keywords. Prefer `classifications` or `subject`
      for curated vocabulary terms.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: string
    multivalued: true
  temporal:
    name: temporal
    description: Temporalidade do objeto.
    from_schema: https://tradicional.arq.br/schema/thing
    owner: Repository
    domain_of:
    - Right
    - Thing
    range: Event
    multivalued: true
    inlined: true
    inlined_as_list: true
  collection:
    name: collection
    description: Collections or aggregations to which the object belongs.
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    - Work
    range: TypedReference
    multivalued: true
    inlined: true
    inlined_as_list: true
  repositories:
    name: repositories
    description: 'A set of elements for the identification, name and location of the
      repository that is responsible for the object/work in focus.

      Repeated if there are several designations known, or if former repositories
      or geographic places should be listed.

      ---------------------------------------------------------------------

      Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar
      a inclusão da edificação em perímetros de sítios do patrimônio cultural, etc.

      Os repositórios devem ser cadastrados de modo semelhante às informações de georreferenciamento,
      usando o tipo `other`.

      '
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: Repository
    multivalued: true
    inlined: true
    inlined_as_list: true
  record_rights:
    name: record_rights
    description: 'A set of structured information about rights regarding the content
      provided in this LIDO record.

      ---------------------------------------------------------------------

      :warning: Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre
      os direitos incidentes sobre o objeto descrito.

      '
    from_schema: https://tradicional.arq.br/schema/thing
    rank: 1000
    owner: Repository
    domain_of:
    - Thing
    range: Right
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: schema:Organization

```
</details></div>
