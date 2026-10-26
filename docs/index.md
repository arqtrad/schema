# Esquema de dados do WASTH (Web App para Sítios Tradicionais e Históricos)

## Orientações gerais

Todas as fichas dos projetos dos Documentários da arquitetura tradicional são
arquivos de texto sem formatação, que podem ser criados e editados em
programas como o Notepad++, Sublime Text, ou Zettlr, entre muitos outros.
Elas podem, também, ser criadas e editadas diretamente online no repositório
do GitHub.

> :warning: As fichas **não** devem ser criadas nem editadas em processadores
> de texto formatado, tais como Microsoft Word, Google Docs, ou LibreOffice.

A ficha se divide em dois blocos :
um bloco de metadados delimitado por linhas contendo apenas três hífens `---` e
um bloco de conteúdo com texto livre.

Os metadados são formatados segundo a especificação [YAML].
O conteúdo é formatado segundo a especificação [Markdown],
e pode incluir formatação específica do [Pandoc].

Quanto às informações que devem ser inseridas na ficha,
(quase) todos os campos são definidos pela especificação [LIDO] e,
na medida do possível, têm uma equivalência com o [DublinCore].

Na medida do possível, buscamos também adequar o conteúdo das fichas às
normas de preenchimento das fichas de Cadastro (M301, M302) do
Sistema Integrado de Conhecimento e Gestão ([SICG]) do
Instituto do Patrimônio Histórico e Artístico Nacional (IPHAN).

[YAML]: https://www.yaml.info/learn/index.html

[Markdown]: https://programminghistorian.org/pt/licoes/introducao-ao-markdown

[Pandoc]: https://programminghistorian.org/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown

[LIDO]: https://icom-documentation.mini.icom.museum/working-groups/lido/lido-overview/

[DublinCore]: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/

[SICG]: https://sicg.iphan.gov.br/sicg/manual/manual.html


## Antes de começar

Para contribuir com os Documentários da Arquitetura Tradicional, você ou
o seu grupo de pesquisa precisa ter sua própria versão dos repositórios.

Comece aprendendo um pouco sobre como trabalhar com controle de versão no Git e
no GitHub, estudando
[estes tutoriais em português](https://programminghistorian.org/pt/licoes/git-ferramenta-metodologica-projetos-historia-1)
no site [Programming Historian].
Em Windows ou MacOS, o jeito mais fácil de trabalhar com repositórios de dados
no GitHub é instalando o [GitHub Desktop].
No Linux, há outras opções, como o [SmartGit]
(também disponível para Windows e MacOS).

Em seguida, precisa **bifurcar** (fork) o repositório no qual vai trabalhar,
provavelmente à partida o repositório da
[Casa tradicional](https://github.com/arqtrad/casa/),
usando o botão `Fork 🔽` como ilustrado abaixo :

<img alt="Captura de tela" src="https://github.com/user-attachments/assets/6c22dcec-b8e1-4688-a504-d9ea640bdc43" />

A partir daí, pode trabalhar livremente na sua própria cópia do repositório,
usando as ferramentas `🔄 Sync fork` e  `⤴️ Contribute` para, respectivamente,
obter periodicamente atualizações *vindas do* repositório principal e
propor as suas contribuições *para o* repositório principal.

<img alt="Captura de tela" src="https://github.com/user-attachments/assets/25905e40-99ef-4b23-b33e-cfe586c41001" />

<img alt="Captura de tela" src="https://github.com/user-attachments/assets/b5f6ef50-c122-4f01-8ec9-b16207a9b63d" />

Poderá então abrir uma solicitação de integração das suas alterações
ao repositório principal (**pull request**):

<img alt="Captura de tela" src="https://github.com/user-attachments/assets/56de1236-6fa0-47f3-9e94-06218dace0a8" />

Se não estiver à vontade para manipular diretamente os repositórios do GitHub,
sempre pode contribuir informações, sugestões ou desejos no
[Fórum de discussão] deste projeto de pesquisa.
Se tiver contribuições pontuais sobre fichas específicas, formatos ou lacunas,
pode também abrir uma [*issue* no repositório da Casa].


## Por onde começo ?

Leia a especificação da ficha [Work](Work/) para saber como preencher as
fichas de edificações dos Documentários da Arquitetura Tradicional.


[Programming Historian]: https://programminghistorian.org/pt/

[GitHub Desktop]: https://github.com/apps/desktop?locale=pt-br

[SmartGit]: https://www.smartgit.dev/

[Fórum de discussão]: https://github.com/orgs/arqtrad/discussions

[*issue* no repositório da Casa]: https://github.com/arqtrad/casa/issues

[Zotero]: https://www.zotero.org/groups/2495935/arquitetura_tradicional_luso-brasileira/

[Global Building Atlas]: https://github.com/zhu-xlab/GlobalBuildingAtlas

[QGIS]: https://qgis.org/

[ORCiD]: https://orcid.org/

[SIPA]: https://monumentos.gov.pt/

[HPIP]: https://hpip.org/

[iPatrimonio]: https://ipatrimonio.org/

[VRA Core]: https://www.loc.gov/standards/vracore/

[ULAN]: https://www.getty.edu/research/tools/vocabularies/ulan

[IIIF]: https://iiif.io/

[lista de tipos de mídia IANA]: https://www.iana.org/assignments/media-types


URI: https://tradicional.arq.br/schema

Name: wasth_schema



## Classes

| Class | Description |
| --- | --- |
| [Actor](Actor.md) | Agent and role in an event |
| [Appellation](Appellation.md) |  |
| [BibliographicCitation](BibliographicCitation.md) | Cadastro de uma referência bibliográfica |
| [BroaderConceptReference](BroaderConceptReference.md) | Relações hierárquicas |
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StylePeriod](StylePeriod.md) |  |
| [Container](Container.md) | Todos os elementos do documentário |
| [DateRange](DateRange.md) |  |
| [EventDate](EventDate.md) | A wrapper for the expression of a date by providing a set of years as earlies... |
| [EventPlace](EventPlace.md) |  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |
| [Header](Header.md) | Presentation metadata for the WASTH interface |
| [HistoricPlace](HistoricPlace.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |
| [LegalBody](LegalBody.md) | Personal, corporate, family, or other responsible body |
| [Measurement](Measurement.md) | This class comprises actions measuring physical properties and other values t... |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |
| [RelatedConceptReference](RelatedConceptReference.md) | Relações hierárquicas |
| [RelatedEvent](RelatedEvent.md) |  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos direitos ou ... |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC Con... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Event](Event.md) | This class comprises distinct, delimited and coherent processes and interacti... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Place](Place.md) | Entities that have a somewhat fixed, physical extension |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Work](Work.md) | An historical landmark or building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Repository](Repository.md) | Entidade com existência jurídica e espacial |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical spacetime... |
| [Topic](Topic.md) | Subject or iconographic topic |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |



## Slots

| Slot | Description |
| --- | --- |
| [actor_extent](actor_extent.md) | Parte da obra sobre a qual o agente interveio |
| [actor_name](actor_name.md) | Nome do agente extraído de um vocabulário controlado |
| [actor_qualifier](actor_qualifier.md) | For the Attribution Qualifier Actor element choose a concept URI from the [at... |
| [actor_role](actor_role.md) | Identificação de um agente e do seu papel no evento |
| [actor_type](actor_type.md) | Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, ... |
| [alt](alt.md) | Altitude em metros (separador decimal: ponto) |
| [alt_name](alt_name.md) | O bloco `alt_name` permite cadastrar outros nomes pelos quais a edificação se... |
| [author](author.md) | ORCID iD of the record author or maintainer |
| [bibliographic_citation](bibliographic_citation.md) |  |
| [broader](broader.md) | Um conceito de significação mais genérica |
| [caption](caption.md) | Legenda descritiva ou explicativa |
| [category](category.md) | The LIDO Category Vocabulary is a structured controlled list of terms recomme... |
| [classification_genre](classification_genre.md) | A broad category for grouping objects on the basis of shared intrinsic charac... |
| [classification_local](classification_local.md) | A classification scheme for grouping objects on the basis of locally defined ... |
| [classification_special](classification_special.md) | A classification scheme for grouping objects on the basis of criteria defined... |
| [classification_subject](classification_subject.md) | A broad category for grouping objects or works on the basis of a topical asso... |
| [collection](collection.md) | Collections or aggregations to which the object belongs |
| [concept](concept.md) |  |
| [concepts](concepts.md) | Todos os termos de vocabulário controlado |
| [content](content.md) | Deixe uma linha em branco após o fechamento dos metadados e inclua aqui uma d... |
| [coordinates](coordinates.md) | No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do polígono (`... |
| [credit](credit.md) | Informação sobre autoria ou responsabilidade |
| [culture](culture.md) | An index element for the cultural context from which the object/work in focus... |
| [date_type](date_type.md) | An attribute for the kind of latest date, whether it is, for instance, exact ... |
| [date_value](date_value.md) | Usar o formato ISO-8601 (por exemplo, 2026-03-17) |
| [description](description.md) | A human-readable description for a thing |
| [earliest_date](earliest_date.md) | An index element for the expression of an exact or estimated date, for instan... |
| [end_date](end_date.md) | Data final do evento ou mais tardia data presumida para o seu decurso |
| [event_date](event_date.md) | Conjunto de datas em que decorreu o evento |
| [extent](extent.md) | Polygonal, multipolygonal, or linear geographic extent associated with the pl... |
| [format](format.md) | Campo disciplinado pela especificação [DublinCore] no campo [format](https://... |
| [format_extent](format_extent.md) | Indica a parte do objeto que está sendo medida — por exemplo, se a altura é a... |
| [former_site](former_site.md) | Indica que a edificação não se encontra mais no local indicado, seja porque f... |
| [geometry_type](geometry_type.md) | Tipo da geometria descrita pelas coordenadas |
| [holder](holder.md) | A set of elements identifying the person or the group of persons holding the ... |
| [href](href.md) | Um hyperlink simples |
| [id](id.md) | Unique identifier for this object |
| [identifiers](identifiers.md) | Published or external identifiers for the object |
| [inscriptions](inscriptions.md) | Marcas, símbolos ou textos gravados na edificação, especialmente aqueles refe... |
| [intended_site](intended_site.md) | Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser c... |
| [lat](lat.md) | Latitude em graus decimais (separador decimal: ponto) |
| [latest_date](latest_date.md) | An index element for the expression of the exact or approximate date, for ins... |
| [legal_body](legal_body.md) |  |
| [location](location.md) | Representative point location for the place, normally in EPSG:4326 (WGS 84) |
| [location_historic](location_historic.md) | Antigas jurisdições ou designações para o lugar onde o objeto se encontra |
| [lon](lon.md) | Longitude em graus decimais (separador decimal: ponto) |
| [match](match.md) | Tipo da relação |
| [material](material.md) | This class is a specialization of E55 Type and comprises the concepts of mate... |
| [material_tech_type](material_tech_type.md) | Tipo da referência a um material ou técnica usado na obra: material de constr... |
| [measurements](measurements.md) |  |
| [media](media.md) |  |
| [media_alt](media_alt.md) | Texto alternativo para leitores de tela ou outras formas de acessibilidade |
| [method](method.md) | An index element for the method by which the event is or was carried out |
| [name](name.md) | Identificador do termo referido |
| [narrower](narrower.md) | Um conceito de significação mais específica |
| [note](note.md) | Se necessário, incluir no campo `note` uma especificação adicional, como o nú... |
| [object_type](object_type.md) | Usar um vocabulário controlado para identificar o tipo de representação, por ... |
| [other_site](other_site.md) | Para casos não contemplados em nenhuma das categorias acima |
| [overlay_image](overlay_image.md) |  |
| [part_of](part_of.md) | A set of structured information about a place that is the broader context for... |
| [perspective](perspective.md) | Tipo de vista do desenho |
| [place](place.md) | A set of structured information indicating the place or location where an obj... |
| [places](places.md) | Todos os lugares cadastrados |
| [preview_image](preview_image.md) | Uma única miniatura da imagem original |
| [provided_3d](provided_3d.md) | Modelo tridimensional ou IFC da edificação |
| [provided_image](provided_image.md) | Lista de versões ampliadas ou originais da imagem, vetorial ou bitmap |
| [qualifier](qualifier.md) | Indica que as medidas são aproximadas : usar um [qualificador do AAT](https:/... |
| [record_date](record_date.md) | Date the record was created or last substantively revised |
| [record_rights](record_rights.md) | A set of structured information about rights regarding the content provided i... |
| [reference_type](reference_type.md) |  |
| [refid](refid.md) | Local or external identifier |
| [related_events](related_events.md) | A set of structured information about an event related to the event in focus,... |
| [related_object](related_object.md) |  |
| [related_works](related_works.md) |  |
| [relation](relation.md) | Um conceito com o qual existe um relacionamento semântico associativo |
| [relation_type](relation_type.md) | Usamos os tipos de relação previstos pelo [VRA Core] |
| [repositories](repositories.md) | A set of elements for the identification, name and location of the repository... |
| [resource_service](resource_service.md) | Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal... |
| [resources](resources.md) | Os desenhos ou modelos da edificação são apresentados online por meio de imag... |
| [rights](rights.md) |  |
| [role_in_event](role_in_event.md) | Ação desempenhada pelo agente no evento |
| [scale](scale.md) | Número inverso da escala da imagem, se ela tiver uma resolução ou tamanho de ... |
| [shape](shape.md) | caso relevante, indicar a forma do elemento medido usando a [lista de formas ... |
| [site](site.md) | A localização real, atual da edificação — é o que será usado em quase todos o... |
| [source](source.md) |  |
| [srs_name](srs_name.md) | Names the coordinate reference system (CRS) that defines the semantics of the... |
| [start_date](start_date.md) | Data inicial do evento ou mais antiga data presumida para o seu decurso |
| [style_period](style_period.md) | An index element for the period in which the event happened, comprising infor... |
| [subject](subject.md) | Recomenda-se articular o tema em três níveis : descrição, identificação e int... |
| [tags](tags.md) | Provisional uncontrolled keywords |
| [teaser](teaser.md) |  |
| [technique](technique.md) | The production or manufacturing processes, techniques, and methods incorporat... |
| [temporal](temporal.md) | Date on which a right is or was current |
| [term](term.md) | LIDO terminology term |
| [things_present](things_present.md) | A set of structured information for a related object or work that is or was p... |
| [title](title.md) | The preferred human-readable label for a Thing |
| [title_preference](title_preference.md) | Indica se o nome em questão deve ser oculto ou não, se é uma versão alternati... |
| [title_source](title_source.md) | 📚 A fonte do título title_source é opcional ; um título pode ser atestado em ... |
| [title_type](title_type.md) | Indica se o título é um nome próprio, descritivo, etc |
| [type](type.md) | designa a natureza da medida : largura, altura, área, etc |
| [unit](unit.md) | Unidade de medida usada no dimensionamento da representação, por exemplo metr... |
| [value](value.md) | Valor numérico, usar ponto como separador decimal |
| [work_rights](work_rights.md) | > :warning: Este bloco se refere a eventuais direitos autorais sobre A > EDIF... |
| [work_type_condition](work_type_condition.md) | Descriptors for objects that are distinguishable by their overall state such ... |
| [work_type_context](work_type_context.md) | Descriptors for objects that are distinguishable by their use or application ... |
| [work_type_form](work_type_form.md) | Descriptors for objects that are distinguishable by their physical form or by... |
| [work_type_function](work_type_function.md) | Objects that are distinguishable by the particular purpose for which they are... |
| [work_type_material_tech](work_type_material_tech.md) | Descriptors for objects that are distinguishable by their materials encorpora... |
| [work_type_subject_type](work_type_subject_type.md) | Descriptors for objects that are distinguishable by their topics, themes, or ... |
| [work_type_use](work_type_use.md) | Descriptors for objects that are distinguishable by the way they are employed... |
| [works](works.md) | Todas as edificações documentadas |
| [zoom](zoom.md) | Usado para visualizar o mapa mais de longe se a precisão das coordenadas for ... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgentType](AgentType.md) | LIDO actor type |
| [DateQualifier](DateQualifier.md) | Exatidão da data conhecida |
| [EventPlaceType](EventPlaceType.md) | The type attribute qualifies the place according to its role or function in t... |
| [EventType](EventType.md) | The particular kind of event the object/work participated in or was present a... |
| [GeometryType](GeometryType.md) | geoJSON types of area geometry |
| [InscriptionType](InscriptionType.md) | VRA Core types for inscriptions |
| [LabelType](LabelType.md) | SKOS label types |
| [MaterialTechType](MaterialTechType.md) | The physical matter or substance from which an object is made, including any ... |
| [MeasurementType](MeasurementType.md) | The type attribute qualifies whether the measurements given are features of t... |
| [ObjectType](ObjectType.md) | The LIDO Object Type Vocabulary is a structured controlled list of terms reco... |
| [PeriodNameType](PeriodNameType.md) | The LIDO Period/Style Type-Vocabulary is a controlled list of terms recommend... |
| [ReferenceType](ReferenceType.md) | Tipos de referências a objetos externos previstos no LIDO |
| [RelationType](RelationType.md) | Os tipos de relação entre objetos são definidos pelo VRA Core |
| [RepositoryType](RepositoryType.md) | Type of repository or legal body |
| [RightsType](RightsType.md) | LIDO expressions for rights types |
| [RoleType](RoleType.md) | Contribuições de um agente a um evento |
| [SkosHierarchicalRelation](SkosHierarchicalRelation.md) | SKOS-THES hierarchical relation type |
| [SkosMappingRelation](SkosMappingRelation.md) | SKOS mapping properties |
| [SubjectType](SubjectType.md) | The type attribute indicates the kind of subject information, whether it is, ... |
| [TitleType](TitleType.md) | VRA Core title types |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [CslCitekey](CslCitekey.md) | Chave de citação compatível com o Citation Style Language, começando com '@' |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [GeoJSONCoordinateArray](GeoJSONCoordinateArray.md) | JSON array of GeoJSON positions |
| [GeonamesId](GeonamesId.md) | Identificador de lugar no GeoNames, na forma de um CURIE `geonames:1234` |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Latitude](Latitude.md) | Latitude em graus decimais (separador: ponto) |
| [Longitude](Longitude.md) | Longitude em graus decimais (separador: ponto) |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [OlcPlusCode11](OlcPlusCode11.md) | Open Location Code (Plus Code) com resolução de 11 dígitos |
| [OrcidId](OrcidId.md) | ORCID iD, sem o prefixo https://orcid |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
