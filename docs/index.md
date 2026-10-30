# Esquema de dados do WASTH (Web App para Sítios Tradicionais e Históricos)

## Orientações gerais

Todas as fichas dos projetos dos Documentários da arquitetura tradicional são
arquivos de texto sem formatação, que podem ser criados e editados em
programas como o Notepad++, Sublime Text, ou Zettlr, entre muitos outros.
Elas podem, também, ser criadas e editadas diretamente online no repositório
do GitHub.

> ⚠️ As fichas **não** devem ser criadas nem editadas em processadores
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
| [ConceptReference](ConceptReference.md) | Atribuição de vocabulário controlado com citação de apoio |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BroaderConceptReference](BroaderConceptReference.md) | Relações hierárquicas |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MappingConceptReference](MappingConceptReference.md) | Relações semânticas |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que intere... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NarrowerConceptReference](NarrowerConceptReference.md) | Relações hierárquicas |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StylePeriod](StylePeriod.md) |  |
| [Container](Container.md) | Todos os elementos do documentário |
| [EventDate](EventDate.md) | Expressão complexa de uma data que pode se referir ao começo ou ao término de... |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |
| [LegalBody](LegalBody.md) | Referência a uma pessoa jurídica (pode ser um indivíduo detentor de direitos ... |
| [LocationHistoric](LocationHistoric.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |
| [Measurement](Measurement.md) | Informações estruturadas sobre as dimensões do objeto ou requisitos de condic... |
| [MediaObject](MediaObject.md) | Descrição e referência a um único arquivo de mídia |
| [RelatedEvent](RelatedEvent.md) |  |
| [RelatedObject](RelatedObject.md) | A wrapper for identifying information about an object or work, including coll... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelatedWork](RelatedWork.md) | As formas mais comuns de relação no nosso projeto são : |
| [Right](Right.md) | * Preencher `earliest_date` com a data de início da vigência dos |
| [Thing](Thing.md) | Esta classe compreende todas as coisas no universo do CIDOC CRM |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Concept](Concept.md) | Um conceito é uma unidade de conhecimento ou entendimento delimitada e defini... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Event](Event.md) | Um evento é um processo específico e coerente, delimitável, de interações ent... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Repository](Repository.md) | Entidade com existência jurídica e espacial |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions abo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Site](Site.md) | O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura T... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Work](Work.md) | Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastr... |
| [Topic](Topic.md) | Subject or iconographic topic |
| [TypedReference](TypedReference.md) | Permite referenciar um registro local ou externo por meio da sua URI (localiz... |



## Slots

| Slot | Description |
| --- | --- |
| [actor_extent](actor_extent.md) | Parte da obra sobre a qual o agente interveio |
| [actor_name](actor_name.md) | Nome do agente extraído de um vocabulário controlado |
| [actor_qualifier](actor_qualifier.md) | For the Attribution Qualifier Actor element choose a concept URI from the [at... |
| [actor_role](actor_role.md) | Identificação de um agente e do seu papel no evento |
| [actor_type](actor_type.md) | Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, ... |
| [alt](alt.md) | Altitude em metros (separador decimal: ponto) |
| [alt_name](alt_name.md) | O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou con... |
| [bibliographic_citation](bibliographic_citation.md) | 📚  Cadastro de uma referência bibliográfica |
| [broader](broader.md) | Um conceito de significação mais genérica |
| [category](category.md) | Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário... |
| [classification_genre](classification_genre.md) | ❓ Ainda não implementamos o bloco `objectClassification` do LIDO |
| [classification_local](classification_local.md) | ❓ Ainda não implementamos o bloco `objectClassification` do LIDO |
| [classification_special](classification_special.md) | ❓ Ainda não implementamos o bloco `objectClassification` do LIDO |
| [classification_subject](classification_subject.md) | ❓ Ainda não implementamos o bloco `objectClassification` do LIDO |
| [collection](collection.md) | Descreve conjuntos conceituais nos quais a edificação foi incluída, por exemp... |
| [concept_name](concept_name.md) |  |
| [concept_type](concept_type.md) |  |
| [concepts](concepts.md) | Todos os termos de vocabulário controlado |
| [content](content.md) | Conteúdo textual descritivo ou explicativo |
| [coordinates](coordinates.md) | No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do polígono (`... |
| [credit](credit.md) | Informação sobre autoria ou responsabilidade |
| [culture](culture.md) | Designa o contexto cultural ou étnico no qual o objeto foi afetado pelo event... |
| [date_type](date_type.md) | Qualifica a confiabilidade da data como sendo conhecida ou estimada |
| [date_value](date_value.md) | Usar o formato ISO-8601 (AAAA-MM-DD) |
| [description](description.md) | A human-readable description for a thing |
| [display_date](display_date.md) | Permite a expressão descritiva das datas de início e fim do evento, para cont... |
| [end_date](end_date.md) | Data final do evento ou mais tardia data presumida para o seu decurso |
| [event_name](event_name.md) | Identifica o evento ralacionado |
| [event_place](event_place.md) | Lugares associados ao evento, sem incluir o próprio local no qual se situa a ... |
| [event_place_type](event_place_type.md) | Se relevante para a ação, indicar se se trata do local de descobrimento do ob... |
| [event_type](event_type.md) | Categoriza o evento segundo os vários tipos de ações, de processos, ou de res... |
| [extent](extent.md) | Área da implantação da edificação ou sítio cadastrado |
| [format](format.md) | Campo disciplinado pela especificação [DublinCore] no campo [format](https://... |
| [format_extent](format_extent.md) | Indica a parte do objeto que está sendo medida — por exemplo, se a altura é a... |
| [former_site](former_site.md) | Indica que a edificação não se encontra mais no local indicado, seja porque f... |
| [geometry_type](geometry_type.md) | Tipo da geometria descrita pelas coordenadas |
| [holder](holder.md) | A set of elements identifying the person or the group of persons holding the ... |
| [id](id.md) | Identificador globalmente único para este objeto ou recurso |
| [identifiers](identifiers.md) | Números de inventário e demais códigos que identificam este objeto em outras ... |
| [inscription_type](inscription_type.md) | Determina a natureza da inscrição |
| [inscriptions](inscriptions.md) | Marcas, símbolos ou textos gravados na edificação, especialmente aqueles refe... |
| [intended_site](intended_site.md) | Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser c... |
| [label](label.md) | Nome ou título (texto sem formatação) |
| [lat](lat.md) | Latitude em graus decimais (separador decimal: ponto) |
| [legal_body](legal_body.md) | Informações estruturadas sobre a pessoa jurídica |
| [legal_body_name](legal_body_name.md) | Referencia a identidade do ente legal num vocabulário controlado ou repositór... |
| [legal_body_type](legal_body_type.md) | Define a natureza do ente legal : pessoa jurídica, perímetro geográfico de tu... |
| [lido_term](lido_term.md) | LIDO terminology term |
| [location](location.md) | Coordenadas geográficas do ponto que permite situar a edificação no mapa para... |
| [location_historic](location_historic.md) | Antigas jurisdições ou designações para o lugar onde o objeto se encontra |
| [location_historic_name](location_historic_name.md) | Identificação do local com referência a um vocabulário controlado ou repositó... |
| [location_historic_type](location_historic_type.md) | Define se o local histórico designa uma jurisdição, um topônimo antigo, ou ou... |
| [lon](lon.md) | Longitude em graus decimais (separador decimal: ponto) |
| [mapping](mapping.md) | Um conceito com o qual existe um relacionamento semântico associativo |
| [match](match.md) | Tipo da relação |
| [material](material.md) | Descreve a natureza do material empregado na edificação, no elemento ou no ev... |
| [material_tech_type](material_tech_type.md) | Tipo da referência a um material ou técnica usado na obra: material de constr... |
| [measurement_event](measurement_event.md) | Descreve a ocasião em que as medidas foram aferidas, caso essa informação sej... |
| [measurement_qualifier](measurement_qualifier.md) | Indica que as medidas são aproximadas |
| [measurement_shape](measurement_shape.md) | caso relevante, indicar a forma do elemento medido usando a [lista de formas ... |
| [measurement_type](measurement_type.md) | designa a natureza da medida : largura, altura, área, etc |
| [measurement_value](measurement_value.md) | Valor numérico, usar ponto como separador decimal |
| [measurements](measurements.md) | A wrapper for information about the dimensions, or other measurements, of the... |
| [media](media.md) | Representações iconográficas deste objeto |
| [media_alt](media_alt.md) | Texto alternativo para leitores de tela ou outras formas de acessibilidade |
| [method](method.md) | An index element for the method by which the event is or was carried out |
| [narrower](narrower.md) | Um conceito de significação mais específica |
| [note](note.md) | Se necessário, incluir no campo `note` uma especificação adicional, como o nú... |
| [object_type](object_type.md) | Usar um vocabulário controlado para identificar o tipo de representação, por ... |
| [other_site](other_site.md) | Para casos de implantação não contemplados em nenhuma das categorias acima |
| [part_of](part_of.md) | Permite identificar o contexto geográfico ou administrativo ao qual a edifica... |
| [period_name_type](period_name_type.md) | Designa a natureza ou origem do nome do período ou estilo indicado |
| [perspective](perspective.md) | Tipo de vista do desenho |
| [preview_image](preview_image.md) | Uma única miniatura da imagem original |
| [provided_3d](provided_3d.md) | Modelo tridimensional ou IFC da edificação |
| [provided_image](provided_image.md) | Lista de versões ampliadas ou originais da imagem, vetorial ou bitmap |
| [record_author](record_author.md) | ORCID iD da pessoa que escreveu a versão original da ficha |
| [record_date](record_date.md) | Data de inclusão da ficha |
| [record_rights](record_rights.md) | Informações estruturadas sobre os direitos que incidem sobre o conteúdo textu... |
| [reference_type](reference_type.md) |  |
| [refid](refid.md) | Local or external identifier |
| [related_events](related_events.md) | A set of structured information about an event related to the event in focus,... |
| [related_object](related_object.md) |  |
| [related_works](related_works.md) | A wrapper for identifying information about an object or work, including coll... |
| [relation](relation.md) | Um conceito com o qual existe um relacionamento semântico associativo |
| [relation_type](relation_type.md) | Usamos os tipos de relação previstos pelo [VRA Core] |
| [repositories](repositories.md) | Nos Documentários da Arquitetura Tradicional, usamos repositórios para indica... |
| [repository_type](repository_type.md) |  |
| [resource_service](resource_service.md) | Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal... |
| [resources](resources.md) | Os desenhos ou modelos da edificação são apresentados online por meio de imag... |
| [rights](rights.md) |  |
| [rights_statement](rights_statement.md) | Referencia, preferencialmente por meio de uma URI, as informações específicas... |
| [rights_type](rights_type.md) | Determina se os direitos ora descritos são uma licença específica (padrão) ou... |
| [role_in_event](role_in_event.md) | Ação desempenhada pelo agente no evento |
| [scale](scale.md) | Número inverso da escala da imagem, se ela tiver uma resolução ou tamanho de ... |
| [site](site.md) | A localização real, atual da edificação — é o que será usado em quase todos o... |
| [site_type](site_type.md) |  |
| [source](source.md) |  |
| [srs_name](srs_name.md) | Names the coordinate reference system (CRS) that defines the semantics of the... |
| [start_date](start_date.md) | Data inicial do evento ou mais antiga data presumida para o seu decurso |
| [style_period](style_period.md) | Denomina o(s) período(s) em que o evento decorreu, em qualquer escala relevan... |
| [subject](subject.md) | Recomenda-se articular o tema em três níveis : descrição, identificação e int... |
| [tags](tags.md) | Lista de palavras-chave que caracterizam o objeto, de modo não estruturado |
| [technique](technique.md) | Processos, técnicas, métodos e saberes postos em prática no conjunto da edifi... |
| [temporal](temporal.md) | Date on which a right is or was current |
| [things_present](things_present.md) | A set of structured information for a related object or work that is or was p... |
| [title](title.md) | Nome pelo qual este item é mais comumente conhecido |
| [title_preference](title_preference.md) | Indica se o nome em questão deve ser oculto ou não, se é uma versão alternati... |
| [title_source](title_source.md) | A fonte do título title_source é opcional ; um título pode ser atestado em ma... |
| [title_type](title_type.md) |  |
| [topic_type](topic_type.md) | Categoriza o nível descritivo ou interpretativo do tema |
| [unit](unit.md) | Unidade de medida usada no dimensionamento do objeto ou da representação, por... |
| [work_rights](work_rights.md) | ⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobr... |
| [work_type_condition](work_type_condition.md) | Descreve o estado físico da edificação quanto à sua aparência de completude, ... |
| [work_type_context](work_type_context.md) | Nos Documentários de edificações, designa sobretudo o contexto imediato de im... |
| [work_type_form](work_type_form.md) | Nos Documentários da Arquitetura Tradicional, designa uma tipologia formal |
| [work_type_function](work_type_function.md) | Nos Documentários de edificações, designa um dos sete tipos de propósitos con... |
| [work_type_material_tech](work_type_material_tech.md) | Nos Documentários da Arquitetura Tradicional, refere-se à caracterização cons... |
| [work_type_subject_type](work_type_subject_type.md) | Nos Documentários da Arquitetura Tradicional, indica, se houver, uma classifi... |
| [work_type_use](work_type_use.md) | Nos Documentários da Arquitetura Tradicional, designa propriamente a(s) class... |
| [works](works.md) | Todas as edificações documentadas |
| [zoom](zoom.md) | Usado para visualizar o mapa mais de longe se a precisão das coordenadas for ... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgentType](AgentType.md) | Tipo de agente na terminologia LIDO |
| [ConceptType](ConceptType.md) | Tipos de termos de vocabulário baseados no Getty AAT |
| [DateType](DateType.md) | Exatidão da data conhecida |
| [EventPlaceType](EventPlaceType.md) | Para eventos que implicam a deslocação do bem, indica se o local se refere ao... |
| [EventType](EventType.md) | O tipo de incidência sobre a edificação que o evento descreve |
| [GeometryType](GeometryType.md) | Tipos de geometria do objeto geoJSON |
| [InscriptionType](InscriptionType.md) | Tipos de inscrições previstos no VRA Core |
| [LabelType](LabelType.md) | No SKOS, caracteriza se cada termo deve ser considerado preferencial ou alter... |
| [MaterialTechType](MaterialTechType.md) | A materialidade e as técnicas de produção ou intervenção na edificação devem ... |
| [MeasurementQualifier](MeasurementQualifier.md) | Qualifica a confiabilidade das medidas aferidas |
| [MeasurementType](MeasurementType.md) | The type attribute qualifies whether the measurements given are features of t... |
| [ObjectType](ObjectType.md) | The LIDO Object Type Vocabulary is a structured controlled list of terms reco... |
| [PeriodNameType](PeriodNameType.md) | O vocabulário de tipos de período/estilo do LIDO é uma lista controlada estru... |
| [ReferenceType](ReferenceType.md) | Tipos de referências a objetos externos previstos no LIDO |
| [RelationType](RelationType.md) | Os tipos de relação entre objetos são definidos pelo VRA Core |
| [RepositoryType](RepositoryType.md) | Type of repository or legal body |
| [RightsType](RightsType.md) | LIDO expressions for rights types |
| [RoleType](RoleType.md) | Contribuições de um agente a um evento |
| [SkosBroaderRelation](SkosBroaderRelation.md) | SKOS-THES broader relation type |
| [SkosMappingRelation](SkosMappingRelation.md) | SKOS mapping properties |
| [SkosNarrowerRelation](SkosNarrowerRelation.md) | SKOS-THES narrower relation type |
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
