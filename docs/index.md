# wasth_schema

Esquemas LinkML para os Documentários da Arquitetura Tradicional.

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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialTech](MaterialTech.md) | Usar discernimento para identificar sistemas, materiais e técnicas que |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StylePeriod](StylePeriod.md) |  |
| [Container](Container.md) | Todos os elementos do documentário |
| [DateRange](DateRange.md) |  |
| [EventDate](EventDate.md) | A wrapper for the expression of a date by providing a set of years as |
| [EventPlace](EventPlace.md) |  |
| [GeographicExtent](GeographicExtent.md) | Coordenadas do polígono que define o sítio |
| [GeographicPoint](GeographicPoint.md) | Coordenadas do ponto que situa o sítio na visualização do mapa |
| [Header](Header.md) | Presentation metadata for the WASTH interface |
| [HistoricPlace](HistoricPlace.md) | Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a loc... |
| [Inscription](Inscription.md) | A descrição da inscrição informa local, dimensões e características |
| [LegalBody](LegalBody.md) | Personal, corporate, family, or other responsible body |
| [Measurements](Measurements.md) | O campo `description` permite uma representação textual das medidas da |
| [Media](Media.md) | Descrição e referência a um único arquivo de mídia |
| [RelatedConceptReference](RelatedConceptReference.md) | Relações hierárquicas |
| [RelatedEvent](RelatedEvent.md) |  |
| [RelatedObject](RelatedObject.md) | As formas mais comuns de relação no nosso projeto são : |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelatedWork](RelatedWork.md) | A wrapper for identifying information about an object or work, including coll... |
| [Right](Right.md) | Rights statement associated with a record, resource, or note |
| [Thing](Thing.md) | This class comprises all things in the universe of discourse of the CIDOC |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Concept](Concept.md) | A SKOS concept can be viewed as an idea or notion; a unit of thought |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Event](Event.md) | This class comprises distinct, delimited and coherent processes and |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Place](Place.md) | Entities that have a somewhat fixed, physical extension |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Work](Work.md) | An historical landmark or building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Repository](Repository.md) | Entidade com existência jurídica e espacial |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Resource](Resource.md) | This class comprises identifiable immaterial items that make propositions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Site](Site.md) | This class comprises 4-dimensional point sets (volumes) in physical |
| [Topic](Topic.md) | Subject or iconographic topic |
| [TypedReference](TypedReference.md) | Reference to a local record, IRI, URI, or LIDO terminology term |



## Slots

| Slot | Description |
| --- | --- |
| [actor_extent](actor_extent.md) |  |
| [actor_name](actor_name.md) |  |
| [actor_qualifier](actor_qualifier.md) | For the Attribution Qualifier Actor element choose a concept URI from |
| [actor_role](actor_role.md) |  |
| [actor_type](actor_type.md) |  |
| [alt](alt.md) | Altitude em metros (separador decimal: ponto) |
| [alt_name](alt_name.md) | O bloco `alt_name` permite cadastrar outros nomes pelos quais a edificação |
| [author](author.md) | ORCID iD of the record author or maintainer |
| [bibliographic_citation](bibliographic_citation.md) |  |
| [broader](broader.md) | Um conceito de significação mais genérica |
| [caption](caption.md) | Legenda descritiva ou explicativa |
| [category](category.md) | The LIDO Category Vocabulary is a structured controlled list of terms recomme... |
| [classification_genre](classification_genre.md) | A broad category for grouping objects on the basis of shared intrinsic |
| [classification_local](classification_local.md) | A classification scheme for grouping objects on the basis of locally defined ... |
| [classification_special](classification_special.md) | A classification scheme for grouping objects on the basis of criteria defined... |
| [classification_subject](classification_subject.md) | A broad category for grouping objects or works on the basis of a topical asso... |
| [collection](collection.md) | Collections or aggregations to which the object belongs |
| [concept](concept.md) |  |
| [concepts](concepts.md) |  |
| [content](content.md) | Deixe uma linha em branco após o fechamento dos metadados e inclua aqui |
| [coordinates](coordinates.md) | No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do |
| [credit](credit.md) | Informação sobre autoria ou responsabilidade |
| [culture](culture.md) | An index element for the cultural context from which the object/work in focus... |
| [date_type](date_type.md) |  |
| [date_value](date_value.md) |  |
| [description](description.md) | A human-readable description for a thing |
| [earliest_date](earliest_date.md) |  |
| [end_date](end_date.md) |  |
| [event_date](event_date.md) |  |
| [extent](extent.md) | Polygonal, multipolygonal, or linear geographic extent associated with the pl... |
| [format](format.md) | Campo disciplinado pela especificação [DublinCore] no campo |
| [format_extent](format_extent.md) | Indica a parte do objeto que está sendo medida — por |
| [former_site](former_site.md) | Indica que a edificação não se encontra mais no local indicado, seja porque f... |
| [geometry_type](geometry_type.md) | Tipo da geometria descrita pelas coordenadas |
| [href](href.md) | Um hyperlink simples |
| [id](id.md) | Unique identifier for this object |
| [identifiers](identifiers.md) | Published or external identifiers for the object |
| [inscriptions](inscriptions.md) | Marcas, símbolos ou textos gravados na edificação, especialmente aqueles refe... |
| [intended_site](intended_site.md) | Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser c... |
| [lat](lat.md) | Latitude em graus decimais (separador decimal: ponto) |
| [latest_date](latest_date.md) |  |
| [legal_body](legal_body.md) |  |
| [legal_body_name](legal_body_name.md) |  |
| [legal_body_type](legal_body_type.md) |  |
| [location](location.md) | Representative point location for the place, normally in EPSG:4326 (WGS 84) |
| [location_historic](location_historic.md) | Antigas jurisdições ou designações para o lugar onde o objeto se encontra |
| [lon](lon.md) | Longitude em graus decimais (separador decimal: ponto) |
| [match](match.md) | Tipo da relação |
| [material](material.md) |  |
| [material_tech_type](material_tech_type.md) |  |
| [measurements](measurements.md) |  |
| [media](media.md) |  |
| [media_alt](media_alt.md) | Texto alternativo para leitores de tela ou outras formas de acessibilidade |
| [method](method.md) | An index element for the method by which the event is or was carried out |
| [name](name.md) | Identificador do termo referido |
| [narrower](narrower.md) | Um conceito de significação mais específica |
| [note](note.md) | Se necessário, incluir no campo `note` uma especificação adicional, |
| [object_type](object_type.md) | Usar um vocabulário controlado para identificar o tipo de representação, |
| [other_site](other_site.md) | Para casos não contemplados em nenhuma das categorias acima |
| [overlay_image](overlay_image.md) |  |
| [part_of](part_of.md) | A set of structured information about a place that is the broader context for... |
| [perspective](perspective.md) | Tipo de vista do desenho |
| [place](place.md) | A set of structured information indicating the place or location where an obj... |
| [places](places.md) |  |
| [preview_image](preview_image.md) | Uma única miniatura da imagem original |
| [provided_3d](provided_3d.md) | Modelo tridimensional ou IFC da edificação |
| [provided_image](provided_image.md) | Lista de versões ampliadas ou originais da imagem, vetorial ou bitmap |
| [qualifier](qualifier.md) | Indica que as medidas são aproximadas : usar um |
| [record_date](record_date.md) | Date the record was created or last substantively revised |
| [record_rights](record_rights.md) |  |
| [reference_type](reference_type.md) |  |
| [refid](refid.md) | Local or external identifier |
| [related_events](related_events.md) | A set of structured information about an event related to the event in focus,... |
| [related_object](related_object.md) |  |
| [related_work](related_work.md) |  |
| [relation](relation.md) | Um conceito com o qual existe um relacionamento semântico associativo |
| [relation_type](relation_type.md) | Usamos os tipos de relação previstos pelo [VRA Core] |
| [repository](repository.md) |  |
| [resource](resource.md) | Os desenhos ou modelos da edificação são apresentados online por meio de |
| [resource_service](resource_service.md) | Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal... |
| [right_concept](right_concept.md) |  |
| [right_holder](right_holder.md) |  |
| [right_temporal](right_temporal.md) |  |
| [right_type](right_type.md) |  |
| [rights](rights.md) |  |
| [role_in_event](role_in_event.md) |  |
| [scale](scale.md) | Número inverso da escala da imagem, se ela tiver uma resolução ou tamanho de ... |
| [shape](shape.md) | caso relevante, indicar a forma do elemento medido |
| [site](site.md) | A localização real, atual da edificação — é o que será usado em quase todos o... |
| [source](source.md) |  |
| [srs_name](srs_name.md) | Names the coordinate reference system (CRS) that defines the semantics of the... |
| [start_date](start_date.md) |  |
| [style_period](style_period.md) | An index element for the period in which the event happened, |
| [subject](subject.md) | Recomenda-se articular o tema em três níveis : descrição, identificação e |
| [tags](tags.md) | Provisional uncontrolled keywords |
| [teaser](teaser.md) |  |
| [technique](technique.md) |  |
| [temporal](temporal.md) | Temporalidade do objeto |
| [term](term.md) | LIDO terminology term |
| [things_present](things_present.md) | A set of structured information for a related object or work that is or was p... |
| [title](title.md) | The preferred human-readable label for a Thing |
| [title_preference](title_preference.md) | Indica se o nome em questão deve ser oculto ou não, se é uma versão alternati... |
| [title_source](title_source.md) | 📚 A fonte do título title_source é opcional ; um título pode ser atestado em ... |
| [title_type](title_type.md) | Indica se o título é um nome próprio, descritivo, etc |
| [type](type.md) | designa a natureza da medida : largura, altura, |
| [unit](unit.md) | Unidade de medida usada no dimensionamento da representação, |
| [value](value.md) | Valor numérico, usar ponto como separador decimal |
| [work_rights](work_rights.md) |  |
| [work_type_condition](work_type_condition.md) | Descriptors for objects that are distinguishable by their overall state such ... |
| [work_type_context](work_type_context.md) | Descriptors for objects that are distinguishable by their use or application ... |
| [work_type_form](work_type_form.md) | Descriptors for objects that are distinguishable by their physical form or by... |
| [work_type_function](work_type_function.md) | Objects that are distinguishable by the particular purpose for which they are... |
| [work_type_material_tech](work_type_material_tech.md) | Descriptors for objects that are distinguishable by their materials encorpora... |
| [work_type_subject_type](work_type_subject_type.md) | Descriptors for objects that are distinguishable by their topics, themes, or ... |
| [work_type_use](work_type_use.md) | Descriptors for objects that are distinguishable by the way they are employed... |
| [works](works.md) |  |
| [zoom](zoom.md) | Usado para visualizar o mapa mais de longe se a precisão das |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AgentType](AgentType.md) | LIDO actor type |
| [DateQualifier](DateQualifier.md) | Exatidão da data indicada |
| [EventPlaceType](EventPlaceType.md) | The type attribute qualifies the place according to its role or function in t... |
| [EventType](EventType.md) | The particular kind of event the object/work participated in or was |
| [GeometryType](GeometryType.md) | geoJSON types of area geometry |
| [InscriptionType](InscriptionType.md) | VRA Core types for inscriptions |
| [LabelType](LabelType.md) | SKOS label types |
| [MaterialTechType](MaterialTechType.md) | The physical matter or substance from which an object is made, including |
| [MeasurementType](MeasurementType.md) | The type attribute qualifies whether the measurements given are features of t... |
| [ObjectType](ObjectType.md) | The LIDO Object Type Vocabulary is a structured controlled list of terms reco... |
| [PeriodNameType](PeriodNameType.md) | The LIDO Period/Style Type-Vocabulary is a controlled list of terms |
| [ReferenceType](ReferenceType.md) | Tipos de referências a objetos externos previstos no LIDO |
| [RelationType](RelationType.md) | Os tipos de relação entre objetos são definidos pelo VRA Core |
| [RepositoryType](RepositoryType.md) | Type of repository or legal body |
| [RightsType](RightsType.md) | LIDO expressions for rights types |
| [RoleType](RoleType.md) | Contribuições de um agente a um evento |
| [SkosHierarchicalRelation](SkosHierarchicalRelation.md) | SKOS-THES hierarchical relation type |
| [SkosMappingRelation](SkosMappingRelation.md) | SKOS mapping properties |
| [SubjectType](SubjectType.md) | The type attribute indicates the kind of subject information, whether it |
| [TitleType](TitleType.md) | VRA Core title types |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [CslCitekey](CslCitekey.md) | Citation Style Language citekey, beginning with '@' |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [GeoJSONCoordinateArray](GeoJSONCoordinateArray.md) | JSON array of GeoJSON positions |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Latitude](Latitude.md) | Latitude in decimal degrees |
| [Longitude](Longitude.md) | Longitude in decimal degrees |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [OlcPlusCode11](OlcPlusCode11.md) | Open Location Code (Plus Code) with a resolution of 11 digits |
| [OrcidId](OrcidId.md) | Bare ORCID iD, without the https://orcid |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
