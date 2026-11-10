# Auto generated from arqtrad_schema.yaml by pythongen.py version: 0.0.1
# Schema: arqtrad_schema
#
# id: https://tradicional.arq.br/schema
# description: ## Orientações gerais
#
#   Todas as fichas dos projetos dos Documentários da arquitetura tradicional são
#   arquivos de texto sem formatação, que podem ser criados e editados em
#   programas como o Notepad++, Sublime Text, ou Zettlr, entre muitos outros.
#   Elas podem, também, ser criadas e editadas diretamente online no repositório
#   do GitHub.
#
#   > ⚠️ As fichas **não** devem ser criadas nem editadas em processadores
#   > de texto formatado, tais como Microsoft Word, Google Docs, ou LibreOffice.
#
#   A ficha se divide em dois blocos :
#   um bloco de metadados delimitado por linhas contendo apenas três hífens `---` e
#   um bloco de conteúdo com texto livre.
#
#   Os metadados são formatados segundo a especificação [YAML].
#   O conteúdo é formatado segundo a especificação [Markdown],
#   e pode incluir formatação específica do [Pandoc].
#
#   Quanto às informações que devem ser inseridas na ficha,
#   (quase) todos os campos são definidos pela especificação [LIDO] e,
#   na medida do possível, têm uma equivalência com o [DublinCore].
#
#   Na medida do possível, buscamos também adequar o conteúdo das fichas às
#   normas de preenchimento das fichas de Cadastro (M301, M302) do
#   Sistema Integrado de Conhecimento e Gestão ([SICG]) do
#   Instituto do Patrimônio Histórico e Artístico Nacional (IPHAN).
#
#   [YAML]: https://www.yaml.info/learn/index.html
#
#   [Markdown]: https://programminghistorian.org/pt/licoes/introducao-ao-markdown
#
#   [Pandoc]: https://programminghistorian.org/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown
#
#   [LIDO]: https://icom-documentation.mini.icom.museum/working-groups/lido/lido-overview/
#
#   [DublinCore]: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
#
#   [SICG]: https://sicg.iphan.gov.br/sicg/manual/manual.html
#
#
#   ## Antes de começar
#
#   Para contribuir com os Documentários da Arquitetura Tradicional, você ou
#   o seu grupo de pesquisa precisa ter sua própria versão dos repositórios.
#
#   Comece aprendendo um pouco sobre como trabalhar com controle de versão no Git e
#   no GitHub, estudando [estes tutoriais em
#   português](https://programminghistorian.org/pt/licoes/git-ferramenta-metodologica-projetos-historia-1)
#   no site [Programming Historian].
#   Em Windows ou MacOS, o jeito mais fácil de trabalhar com repositórios de dados
#   no GitHub é instalando o [GitHub Desktop].
#   No Linux, há outras opções, como o [SmartGit]
#   (também disponível para Windows e MacOS).
#
#   Em seguida, precisa **bifurcar** (fork) o repositório no qual vai trabalhar,
#   provavelmente à partida o repositório da
#   [Casa tradicional](https://github.com/arqtrad/casa/),
#   usando o botão `Fork 🔽` como ilustrado abaixo :
#
#   <img alt="Captura de tela"
#    src="https://github.com/user-attachments/assets/6c22dcec-b8e1-4688-a504-d9ea640bdc43"
#   />
#
#   A partir daí, pode trabalhar livremente na sua própria cópia do repositório,
#   usando as ferramentas `🔄 Sync fork` e  `⤴️ Contribute` para, respectivamente,
#   obter periodicamente atualizações *vindas do* repositório principal e
#   propor as suas contribuições *para o* repositório principal.
#
#   <img alt="Captura de tela"
#    src="https://github.com/user-attachments/assets/25905e40-99ef-4b23-b33e-cfe586c41001"
#   />
#
#   <img alt="Captura de tela"
#    src="https://github.com/user-attachments/assets/b5f6ef50-c122-4f01-8ec9-b16207a9b63d"
#   />
#
#   Poderá então abrir uma solicitação de integração das suas alterações
#   ao repositório principal (**pull request**):
#
#   <img alt="Captura de tela"
#    src="https://github.com/user-attachments/assets/56de1236-6fa0-47f3-9e94-06218dace0a8"
#   />
#
#   Se não estiver à vontade para manipular diretamente os repositórios do GitHub,
#   sempre pode contribuir informações, sugestões ou desejos no
#   [Fórum de discussão] deste projeto de pesquisa.
#   Se tiver contribuições pontuais sobre fichas específicas, formatos ou lacunas,
#   pode também abrir uma [*issue* no repositório da Casa].
#
#
#   ## Por onde começo ?
#
#   > Leia a especificação da ficha **[Work](Work/)** para saber como preencher
#   > as fichas de edificações dos Documentários da Arquitetura Tradicional.
#
#
#   [Programming Historian]: https://programminghistorian.org/pt/
#
#   [GitHub Desktop]: https://github.com/apps/desktop?locale=pt-br
#
#   [SmartGit]: https://www.smartgit.dev/
#
#   [Fórum de discussão]: https://github.com/orgs/arqtrad/discussions
#
#   [*issue* no repositório da Casa]: https://github.com/arqtrad/casa/issues
#
#   [Zotero]: https://www.zotero.org/groups/2495935/arquitetura_tradicional_luso-brasileira/
#
#   [Global Building Atlas]: https://github.com/zhu-xlab/GlobalBuildingAtlas
#
#   [QGIS]: https://qgis.org/
#
#   [ORCiD]: https://orcid.org/
#
#   [SIPA]: https://monumentos.gov.pt/
#
#   [HPIP]: https://hpip.org/
#
#   [iPatrimonio]: https://ipatrimonio.org/
#
#   [VRA Core]: https://www.loc.gov/standards/vracore/
#
#   [ULAN]: https://www.getty.edu/research/tools/vocabularies/ulan
#
#   [IIIF]: https://iiif.io/
#
#   [lista de tipos de mídia IANA]: https://www.iana.org/assignments/media-types
#
# license: MIT

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_int
from rdflib import URIRef

from linkml_runtime.linkml_model.types import Double, String
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.12.0"
version = None

# Namespaces
EPSG = CurieNamespace("EPSG", "http://www.opengis.net/def/crs/EPSG/0/")
AAT = CurieNamespace("aat", "http://vocab.getty.edu/aat/")
CRM = CurieNamespace("crm", "http://www.cidoc-crm.org/cidoc-crm/")
DCTERMS = CurieNamespace("dcterms", "http://purl.org/dc/terms/")
DCTYPES = CurieNamespace("dctypes", "http://purl.org/dc/dcmitype/")
DOI = CurieNamespace("doi", "https://doi.org/")
GEO = CurieNamespace("geo", "http://www.opengis.net/ont/geosparql#")
GEONAMES = CurieNamespace("geonames", "https://www.geonames.org/ontology#")
ISNI = CurieNamespace("isni", "https://isni.org/isni/")
ISO = CurieNamespace("iso", "http://purl.org/iso25964/skos-thes#")
LA = CurieNamespace("la", "https://linked.art/ns/terms/")
LIDO = CurieNamespace("lido", "http://www.lido-schema.org/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
RDFS = CurieNamespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
SKOS = CurieNamespace("skos", "http://www.w3.org/2004/02/skos/core#")
TERM = CurieNamespace("term", "http://terminology.lido-schema.org/")
TGN = CurieNamespace("tgn", "http://vocab.getty.edu/tgn/")
UCUM = CurieNamespace("ucum", "http://purl.oclc.org/NET/muo/ucum/")
ULAN = CurieNamespace("ulan", "http://vocab.getty.edu/ulan/")
UNESCO = CurieNamespace("unesco", "http://vocabularies.unesco.org/thesaurus/")
VRA = CurieNamespace("vra", "http://purl.org/vra/")
WASTH = CurieNamespace("wasth", "https://tradicional.arq.br/schema/")
WD = CurieNamespace("wd", "http://www.wikidata.org/entity/")
WGS84 = CurieNamespace("wgs84", "http://www.w3.org/2003/01/geo/wgs84_pos#")
XSD = CurieNamespace("xsd", "http://www.w3.org/2001/XMLSchema#")
DEFAULT_ = WASTH


# Types
class CslCitekey(String):
    """Chave de citação compatível com o Citation Style Language, começando com '@'. Obter as chaves de citação das referências bibliográficas consultando a nossa biblioteca compartilhada no Zotero."""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CslCitekey"
    type_model_uri = WASTH.CslCitekey


class GeoJSONCoordinateArray(String):
    """JSON array of GeoJSON positions. The valid nesting depends on the associated geometry type."""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "GeoJSONCoordinateArray"
    type_model_uri = WASTH.GeoJSONCoordinateArray


class Latitude(Double):
    """Latitude em graus decimais (separador: ponto)."""

    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "Latitude"
    type_model_uri = WASTH.Latitude


class Longitude(Double):
    """Longitude em graus decimais (separador: ponto)."""

    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "Longitude"
    type_model_uri = WASTH.Longitude


class OrcidId(String):
    """ORCID iD, no formato `orcid:1234-5678-9012-345X` ou
    `https://orcid.org/1234-5678-9012-345X`.
    """

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "OrcidId"
    type_model_uri = WASTH.OrcidId


class OlcPlusCode11(String):
    """Open Location Code (Plus Code) com resolução de 11 dígitos."""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "OlcPlusCode11"
    type_model_uri = WASTH.OlcPlusCode11


# Class references
class BibliographicCitationRefid(CslCitekey):
    pass


class TypedReferenceRefid(URIorCURIE):
    pass


class ResourceId(URIorCURIE):
    pass


class WorkId(OlcPlusCode11):
    pass


class GeonamesFeatureGeonameid(extended_int):
    pass


@dataclass(repr=False)
class Container(YAMLRoot):
    """
    Todos os elementos do documentário.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Container"]
    class_class_curie: ClassVar[str] = "wasth:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = WASTH.Container

    works: Optional[
        Union[dict[Union[str, WorkId], Union[dict, "Work"]], list[Union[dict, "Work"]]]
    ] = empty_dict()
    concepts: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = (
        empty_list()
    )
    places: Optional[
        Union[
            dict[Union[int, GeonamesFeatureGeonameid], Union[dict, "GeonamesFeature"]],
            list[Union[dict, "GeonamesFeature"]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="works", slot_type=Work, key_name="id", keyed=True
        )

        if not isinstance(self.concepts, list):
            self.concepts = [self.concepts] if self.concepts is not None else []
        self.concepts = [
            v if isinstance(v, Concept) else Concept(**as_dict(v))
            for v in self.concepts
        ]

        self._normalize_inlined_as_list(
            slot_name="places",
            slot_type=GeonamesFeature,
            key_name="geonameid",
            keyed=True,
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptReference(YAMLRoot):
    """
    Atribuição de vocabulário controlado com citação de apoio.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["ConceptReference"]
    class_class_curie: ClassVar[str] = "wasth:ConceptReference"
    class_name: ClassVar[str] = "ConceptReference"
    class_model_uri: ClassVar[URIRef] = WASTH.ConceptReference

    concept_name: Optional[Union[dict, "Concept"]] = None
    description: Optional[str] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, "BibliographicCitation"],
            ],
            list[Union[dict, "BibliographicCitation"]],
        ]
    ] = empty_dict()
    source: Optional[Union[dict, "LegalBody"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.concept_name is not None and not isinstance(self.concept_name, Concept):
            self.concept_name = Concept(**as_dict(self.concept_name))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.source is not None and not isinstance(self.source, LegalBody):
            self.source = LegalBody(**as_dict(self.source))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BroaderConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["BroaderConceptReference"]
    class_class_curie: ClassVar[str] = "wasth:BroaderConceptReference"
    class_name: ClassVar[str] = "BroaderConceptReference"
    class_model_uri: ClassVar[URIRef] = WASTH.BroaderConceptReference

    broader_match: Union[str, "SkosBroaderRelation"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.broader_match):
            self.MissingRequiredField("broader_match")
        if not isinstance(self.broader_match, SkosBroaderRelation):
            self.broader_match = SkosBroaderRelation(self.broader_match)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NarrowerConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["NarrowerConceptReference"]
    class_class_curie: ClassVar[str] = "wasth:NarrowerConceptReference"
    class_name: ClassVar[str] = "NarrowerConceptReference"
    class_model_uri: ClassVar[URIRef] = WASTH.NarrowerConceptReference

    narrower_match: Union[str, "SkosNarrowerRelation"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.narrower_match):
            self.MissingRequiredField("narrower_match")
        if not isinstance(self.narrower_match, SkosNarrowerRelation):
            self.narrower_match = SkosNarrowerRelation(self.narrower_match)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingConceptReference(ConceptReference):
    """
    Relações semânticas.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["MappingConceptReference"]
    class_class_curie: ClassVar[str] = "wasth:MappingConceptReference"
    class_name: ClassVar[str] = "MappingConceptReference"
    class_model_uri: ClassVar[URIRef] = WASTH.MappingConceptReference

    mapping_match: Union[str, "SkosMappingRelation"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mapping_match):
            self.MissingRequiredField("mapping_match")
        if not isinstance(self.mapping_match, SkosMappingRelation):
            self.mapping_match = SkosMappingRelation(self.mapping_match)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BibliographicCitation(YAMLRoot):
    """
    Cadastro de uma referência bibliográfica.
    Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["BibliographicCitation"]
    class_class_curie: ClassVar[str] = "dcterms:BibliographicCitation"
    class_name: ClassVar[str] = "BibliographicCitation"
    class_model_uri: ClassVar[URIRef] = WASTH.BibliographicCitation

    refid: Union[str, BibliographicCitationRefid] = None
    description: Optional[str] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.refid):
            self.MissingRequiredField("refid")
        if not isinstance(self.refid, BibliographicCitationRefid):
            self.refid = BibliographicCitationRefid(self.refid)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TypedReference(YAMLRoot):
    """
    Permite referenciar um registro local ou externo por meio da sua URI (localizador universal, como um link da
    internet, por padrão), IRI ou código na base local (não recomendado).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["TypedReference"]
    class_class_curie: ClassVar[str] = "wasth:TypedReference"
    class_name: ClassVar[str] = "TypedReference"
    class_model_uri: ClassVar[URIRef] = WASTH.TypedReference

    refid: Union[str, TypedReferenceRefid] = None
    refid_type: Optional[Union[str, "ReferenceType"]] = "uri"
    title: Optional[str] = None
    description: Optional[str] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    source: Optional[Union[dict, "LegalBody"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.refid):
            self.MissingRequiredField("refid")
        if not isinstance(self.refid, TypedReferenceRefid):
            self.refid = TypedReferenceRefid(self.refid)

        if self.refid_type is not None and not isinstance(
            self.refid_type, ReferenceType
        ):
            self.refid_type = ReferenceType(self.refid_type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.source is not None and not isinstance(self.source, LegalBody):
            self.source = LegalBody(**as_dict(self.source))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(YAMLRoot):
    """
    Informações estruturadas sobre as dimensões do objeto ou requisitos de condicionamento ambiental no espaço que ele
    ocupa. Para edificações, é recomendável cadastrar ao menos a área útil, testada e a altura de coroamento.
    Se a modulação original for conhecida ou puder ser deduzida por um estudo metrológico, é interessante cadastrar
    também as medidas históricas utilizadas (por exemplo, dimensões em palmos).
    O campo `description` permite uma representação textual das medidas da edificação, caso não seja viável cadastrar
    medidas individuais com precisão, ou seja preciso maior flexibilidade para explicar as dimensões.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E16_Measurement"]
    class_class_curie: ClassVar[str] = "crm:E16_Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = WASTH.Measurement

    unit: Union[dict, TypedReference] = None
    measurement_value: float = None
    description: Optional[str] = None
    format_extent: Optional[Union[dict, TypedReference]] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    related_events: Optional[
        Union[Union[dict, "RelatedEvent"], list[Union[dict, "RelatedEvent"]]]
    ] = empty_list()
    measurement_type: Optional[Union[str, "MeasurementType"]] = "proper"
    measurement_extent: Optional[Union[dict, TypedReference]] = None
    measurement_qualifier: Optional[Union[str, "MeasurementQualifier"]] = "derived"
    measurement_shape: Optional[Union[str, TypedReferenceRefid]] = None
    measurement_event: Optional[Union[dict, "Event"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TypedReference):
            self.unit = TypedReference(**as_dict(self.unit))

        if self._is_empty(self.measurement_value):
            self.MissingRequiredField("measurement_value")
        if not isinstance(self.measurement_value, float):
            self.measurement_value = float(self.measurement_value)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.format_extent is not None and not isinstance(
            self.format_extent, TypedReference
        ):
            self.format_extent = TypedReference(**as_dict(self.format_extent))

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if not isinstance(self.related_events, list):
            self.related_events = (
                [self.related_events] if self.related_events is not None else []
            )
        self.related_events = [
            v if isinstance(v, RelatedEvent) else RelatedEvent(**as_dict(v))
            for v in self.related_events
        ]

        if self.measurement_type is not None and not isinstance(
            self.measurement_type, MeasurementType
        ):
            self.measurement_type = MeasurementType(self.measurement_type)

        if self.measurement_extent is not None and not isinstance(
            self.measurement_extent, TypedReference
        ):
            self.measurement_extent = TypedReference(**as_dict(self.measurement_extent))

        if self.measurement_qualifier is not None and not isinstance(
            self.measurement_qualifier, MeasurementQualifier
        ):
            self.measurement_qualifier = MeasurementQualifier(
                self.measurement_qualifier
            )

        if self.measurement_shape is not None and not isinstance(
            self.measurement_shape, TypedReferenceRefid
        ):
            self.measurement_shape = TypedReferenceRefid(self.measurement_shape)

        if self.measurement_event is not None and not isinstance(
            self.measurement_event, Event
        ):
            self.measurement_event = Event(**as_dict(self.measurement_event))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialTech(ConceptReference):
    """
    Usar discernimento para identificar sistemas, materiais e técnicas que interessam ao conhecimento da edificação no
    seu conjunto, não a partes menos extensas ou pouco importantes.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["MaterialTech"]
    class_class_curie: ClassVar[str] = "wasth:MaterialTech"
    class_name: ClassVar[str] = "MaterialTech"
    class_model_uri: ClassVar[URIRef] = WASTH.MaterialTech

    material_tech_type: Union[str, "MaterialTechType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.material_tech_type):
            self.MissingRequiredField("material_tech_type")
        if not isinstance(self.material_tech_type, MaterialTechType):
            self.material_tech_type = MaterialTechType(self.material_tech_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Right(YAMLRoot):
    """
    * Preencher `earliest_date` com a data de início da vigência dos
    direitos ou a data do preenchimento da ficha.

    * `latest_date` pode ser omitido se não houver fim da vigência.
    * `holder` pode ser omitido se a obra estiver no domínio público.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E30_Right"]
    class_class_curie: ClassVar[str] = "crm:E30_Right"
    class_name: ClassVar[str] = "Right"
    class_model_uri: ClassVar[URIRef] = WASTH.Right

    rights_type: Union[str, "RightsType"] = None
    statement: Union[dict, TypedReference] = None
    earliest_date: Optional[Union[dict, "EventDate"]] = None
    latest_date: Optional[Union[dict, "EventDate"]] = None
    holder: Optional[Union[dict, "LegalBody"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rights_type):
            self.MissingRequiredField("rights_type")
        if not isinstance(self.rights_type, RightsType):
            self.rights_type = RightsType(self.rights_type)

        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, TypedReference):
            self.statement = TypedReference(**as_dict(self.statement))

        if self.earliest_date is not None and not isinstance(
            self.earliest_date, EventDate
        ):
            self.earliest_date = EventDate(**as_dict(self.earliest_date))

        if self.latest_date is not None and not isinstance(self.latest_date, EventDate):
            self.latest_date = EventDate(**as_dict(self.latest_date))

        if self.holder is not None and not isinstance(self.holder, LegalBody):
            self.holder = LegalBody(**as_dict(self.holder))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Actor(YAMLRoot):
    """
    Agent and role in an event.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Actor"]
    class_class_curie: ClassVar[str] = "wasth:Actor"
    class_name: ClassVar[str] = "Actor"
    class_model_uri: ClassVar[URIRef] = WASTH.Actor

    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    actor_type: Optional[Union[str, "AgentType"]] = "personal"
    actor_name: Optional[Union[dict, TypedReference]] = None
    role_in_event: Optional[Union[str, "RoleType"]] = None
    actor_qualifier: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()
    actor_extent: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.actor_type is not None and not isinstance(self.actor_type, AgentType):
            self.actor_type = AgentType(self.actor_type)

        if self.actor_name is not None and not isinstance(
            self.actor_name, TypedReference
        ):
            self.actor_name = TypedReference(**as_dict(self.actor_name))

        if self.role_in_event is not None and not isinstance(
            self.role_in_event, RoleType
        ):
            self.role_in_event = RoleType(self.role_in_event)

        self._normalize_inlined_as_list(
            slot_name="actor_qualifier",
            slot_type=TypedReference,
            key_name="refid",
            keyed=True,
        )

        self._normalize_inlined_as_list(
            slot_name="actor_extent",
            slot_type=TypedReference,
            key_name="refid",
            keyed=True,
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventDate(YAMLRoot):
    """
    Expressão complexa de uma data que pode se referir ao começo ou ao término de um evento pontual ou de uma
    decorrência prolongada. Permite expressar as datas de corte inicial e final, cada uma com seus respetivos graus de
    confiabilidade e de precisão.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["EventDate"]
    class_class_curie: ClassVar[str] = "wasth:EventDate"
    class_name: ClassVar[str] = "EventDate"
    class_model_uri: ClassVar[URIRef] = WASTH.EventDate

    date_type: Union[str, "DateType"] = None
    date_value: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.date_type):
            self.MissingRequiredField("date_type")
        if not isinstance(self.date_type, DateType):
            self.date_type = DateType(self.date_type)

        if self.date_value is not None and not isinstance(self.date_value, XSDDate):
            self.date_value = XSDDate(self.date_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StylePeriod(ConceptReference):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["StylePeriod"]
    class_class_curie: ClassVar[str] = "wasth:StylePeriod"
    class_name: ClassVar[str] = "StylePeriod"
    class_model_uri: ClassVar[URIRef] = WASTH.StylePeriod

    period_name_type: Union[str, "PeriodNameType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.period_name_type):
            self.MissingRequiredField("period_name_type")
        if not isinstance(self.period_name_type, PeriodNameType):
            self.period_name_type = PeriodNameType(self.period_name_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedEvent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["RelatedEvent"]
    class_class_curie: ClassVar[str] = "wasth:RelatedEvent"
    class_name: ClassVar[str] = "RelatedEvent"
    class_model_uri: ClassVar[URIRef] = WASTH.RelatedEvent

    event_name: Union[Union[dict, "Event"], list[Union[dict, "Event"]]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_name):
            self.MissingRequiredField("event_name")
        self._normalize_inlined_as_dict(
            slot_name="event_name", slot_type=Event, key_name="event_type", keyed=False
        )

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    Esta classe compreende todas as coisas no universo do CIDOC CRM. É um conceito abstrato que prevê três
    propriedades gerais:
    - Identificação por nome ou título, em particular por um identificador
    preferencial.
    - Classificação por tipo, permitindo o refinamento da subclasse
    específica à qual a instância pertence.
    - Atribuição de texto livre e de outros dados não estruturados, para
    expressar informações não capturadas por propriedades formais.

    Todas as demais classes do CIDOC CRM são especializações diretas ou indiretas de E1 CRM Entity.
    -------------------------------------------------------------------------
    This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.
    It is an abstract concept providing for three general properties:
    - Identification by name or appellation, and in particular by a preferred
    identifier.

    - Classification by type, allowing further refinement of the specific
    subclass to which an instance belongs.

    - Attachment of free text and other unstructured data for the expression
    of anything not captured by formal properties.

    All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E1_CRM_Entity"]
    class_class_curie: ClassVar[str] = "crm:E1_CRM_Entity"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = WASTH.Thing

    title: Optional[str] = None
    id: Optional[Union[str, URIorCURIE]] = None
    author: Optional[Union[str, OrcidId]] = None
    authors: Optional[Union[Union[str, OrcidId], list[Union[str, OrcidId]]]] = (
        empty_list()
    )
    record_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None
    category: Optional[Union[str, URIorCURIE]] = None
    identifiers: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    content: Optional[str] = None
    title_source: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    alt_name: Optional[
        Union[Union[dict, "Appellation"], list[Union[dict, "Appellation"]]]
    ] = empty_list()
    tags: Optional[Union[str, list[str]]] = empty_list()
    temporal: Optional[Union[Union[dict, "Event"], list[Union[dict, "Event"]]]] = (
        empty_list()
    )
    repositories: Optional[
        Union[Union[dict, "Repository"], list[Union[dict, "Repository"]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.id is not None and not isinstance(self.id, URIorCURIE):
            self.id = URIorCURIE(self.id)

        if self.author is not None and not isinstance(self.author, OrcidId):
            self.author = OrcidId(self.author)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [
            v if isinstance(v, OrcidId) else OrcidId(v) for v in self.authors
        ]

        if self.record_date is not None and not isinstance(self.record_date, XSDDate):
            self.record_date = XSDDate(self.record_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )

        self._normalize_inlined_as_list(
            slot_name="identifiers",
            slot_type=TypedReference,
            key_name="refid",
            keyed=True,
        )

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        self._normalize_inlined_as_list(
            slot_name="title_source",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if not isinstance(self.alt_name, list):
            self.alt_name = [self.alt_name] if self.alt_name is not None else []
        self.alt_name = [
            v if isinstance(v, Appellation) else Appellation(**as_dict(v))
            for v in self.alt_name
        ]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        self._normalize_inlined_as_list(
            slot_name="temporal", slot_type=Event, key_name="event_type", keyed=False
        )

        if not isinstance(self.repositories, list):
            self.repositories = (
                [self.repositories] if self.repositories is not None else []
            )
        self.repositories = [
            v if isinstance(v, Repository) else Repository(**as_dict(v))
            for v in self.repositories
        ]

        super().__post_init__(**kwargs)

    def __new__(cls, *args, **kwargs):

        type_designator = "category"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_class_curie", type_designator_value)

            if target_cls is None:
                target_cls = cls._class_for("class_class_uri", type_designator_value)

            if target_cls is None:
                target_cls = cls._class_for("class_model_uri", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_class_curie', 'class_class_uri', 'class_model_uri']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class Concept(Thing):
    """
    Um conceito é uma unidade de conhecimento ou entendimento delimitada e definida com clareza, distinta de outros
    conceitos. Cada conceito pretende descrever um aspecto ou recorte da realidade empírica ou teórica, de modo que a
    sua definição seja amplamente conhecida e partilhada dentro do campo disciplinar ao qual ele pertence.
    Para além da clareza na definição do próprio conceito, estabelecer a sua relação com outros conceitos mais gerais
    ou mais específicos é importante ao se constituir um vocabulário controlado.
    Por isso, a definição de cada conceito DEVE se referir a bibliografia consagrada e, sempre que possível, a outros
    vocabulários controlados nacionais e estrangeiros.
    -------------------------------------------------------------------------
    A SKOS concept can be viewed as an idea or notion; a unit of thought. However, what constitutes a unit of thought
    is subjective, and this definition is meant to be suggestive, rather than restrictive.
    The notion of a SKOS concept is useful when describing the conceptual or intellectual structure of a knowledge
    organization system, and when referring to specific ideas or meanings established within a KOS.
    Note that, because SKOS is designed to be a vehicle for representing semi-formal KOS, such as thesauri and
    classification schemes, a certain amount of flexibility has been built in to the formal definition of this class.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = WASTH.Concept

    broader: Optional[
        Union[
            Union[dict, BroaderConceptReference],
            list[Union[dict, BroaderConceptReference]],
        ]
    ] = empty_list()
    narrower: Optional[
        Union[
            Union[dict, NarrowerConceptReference],
            list[Union[dict, NarrowerConceptReference]],
        ]
    ] = empty_list()
    record_rights: Optional[Union[Union[dict, Right], list[Union[dict, Right]]]] = (
        empty_list()
    )
    concept_type: Optional[Union[str, "ConceptType"]] = "concept"
    mapping: Optional[
        Union[
            Union[dict, MappingConceptReference],
            list[Union[dict, MappingConceptReference]],
        ]
    ] = empty_list()
    relation: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="broader",
            slot_type=BroaderConceptReference,
            key_name="broader_match",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="narrower",
            slot_type=NarrowerConceptReference,
            key_name="narrower_match",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="record_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        if self.concept_type is not None and not isinstance(
            self.concept_type, ConceptType
        ):
            self.concept_type = ConceptType(self.concept_type)

        self._normalize_inlined_as_list(
            slot_name="mapping",
            slot_type=MappingConceptReference,
            key_name="mapping_match",
            keyed=False,
        )

        if not isinstance(self.relation, list):
            self.relation = [self.relation] if self.relation is not None else []
        self.relation = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.relation
        ]

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class RelatedObject(Thing):
    """
    A set of structured information about an object or work, or a group of objects or works related to the object/work
    in focus, including the kind of relationship between them. May include bibliographic objects in which the
    object/work is documented or mentioned.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["RelatedObject"]
    class_class_curie: ClassVar[str] = "wasth:RelatedObject"
    class_name: ClassVar[str] = "RelatedObject"
    class_model_uri: ClassVar[URIRef] = WASTH.RelatedObject

    work_rights: Optional[Union[Union[dict, Right], list[Union[dict, Right]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="work_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class RelatedWork(RelatedObject):
    """
    As formas mais comuns de relação no nosso projeto são :

    - depicted in: A edificação é representada numa pintura ou desenho
    artístico;

    - documented by: Informações sobre a edificação estão publicadas numa
    referência bibliográfica, processo administrativo ou outro documento
    textual impresso, manuscrito ou eletrônico;

    - has plan / has floor plan / has section / has elevation / has
    rendering: Essas relações mostram a existência de desenhos técnicos
    da edificação, sejam eles históricos ou recentes, compilados de
    fontes externas a este projeto de pesquisa.

    - has construction drawing / has design / has sketch: Essas relações se
    referem a desenhos históricos (fontes primárias) que atestam o
    processo de projeto da edificação.

    ATENÇÃO : OS DESENHOS PRODUZIDOS POR ESTE PROJETO DE PESQUISA DEVEM SER CADASTRADOS NO GRUPO resource, MAIS ABAIXO.
    O grupo relation é destinado unicamente a cadastrar relações desta edificação com objetos autônomos, tais como
    outras edificações, conjuntos urbanos, obras de artes visuais, referências bibliográficas ou acervos
    arquivísticos.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["RelatedWork"]
    class_class_curie: ClassVar[str] = "wasth:RelatedWork"
    class_name: ClassVar[str] = "RelatedWork"
    class_model_uri: ClassVar[URIRef] = WASTH.RelatedWork

    relation_type: Union[str, "RelatedWorkRelType"] = None
    media: Optional[
        Union[Union[dict, "MediaObject"], list[Union[dict, "MediaObject"]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relation_type):
            self.MissingRequiredField("relation_type")
        if not isinstance(self.relation_type, RelatedWorkRelType):
            self.relation_type = RelatedWorkRelType(self.relation_type)

        self._normalize_inlined_as_list(
            slot_name="media", slot_type=MediaObject, key_name="format", keyed=False
        )

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class LargerContextReference(RelatedObject):
    """
    Tipo de relação específica entre obras a ser usado quando o objeto descrito na ficha é ou era parte integrante de
    outro objeto, físico ou intelectual.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["LargerContextReference"]
    class_class_curie: ClassVar[str] = "wasth:LargerContextReference"
    class_name: ClassVar[str] = "LargerContextReference"
    class_model_uri: ClassVar[URIRef] = WASTH.LargerContextReference

    context_type: Union[str, "LargerContextType"] = None
    media: Optional[
        Union[Union[dict, "MediaObject"], list[Union[dict, "MediaObject"]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.context_type):
            self.MissingRequiredField("context_type")
        if not isinstance(self.context_type, LargerContextType):
            self.context_type = LargerContextType(self.context_type)

        self._normalize_inlined_as_list(
            slot_name="media", slot_type=MediaObject, key_name="format", keyed=False
        )

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class Resource(Thing):
    """
    Este grupo identifica um recurso visual ou documental que fornece informações técnicas ou uma representação
    ilustrativa da obra à qual ele se relaciona.
    Recursos produzidos pela equipe dos Documentários da Arquitetura Tradicional são descritos na ficha de cada
    edificação, no grupo `resources`. Representações e documentos externos são referidos nos grupos `media` e
    `related_works`, respetivamente.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E31_Document"]
    class_class_curie: ClassVar[str] = "crm:E31_Document"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = WASTH.Resource

    id: Union[str, ResourceId] = None
    format: str = None
    resource_type: Union[str, "ResourceType"] = None
    perspective: int = None
    scale: Optional[float] = None
    unit: Optional[Union[dict, TypedReference]] = None
    preview_image: Optional[Union[str, URIorCURIE]] = None
    provided_image: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    provided_3d: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    resource_service: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    credit: Optional[str] = None
    work_rights: Optional[Union[Union[dict, Right], list[Union[dict, Right]]]] = (
        empty_list()
    )
    category: Optional[Union[str, URIorCURIE]] = TERM["lido01193"]

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.resource_type):
            self.MissingRequiredField("resource_type")
        if not isinstance(self.resource_type, ResourceType):
            self.resource_type = ResourceType(self.resource_type)

        if self._is_empty(self.perspective):
            self.MissingRequiredField("perspective")
        if not isinstance(self.perspective, int):
            self.perspective = int(self.perspective)

        if self.scale is not None and not isinstance(self.scale, float):
            self.scale = float(self.scale)

        if self.unit is not None and not isinstance(self.unit, TypedReference):
            self.unit = TypedReference(**as_dict(self.unit))

        if self.preview_image is not None and not isinstance(
            self.preview_image, URIorCURIE
        ):
            self.preview_image = URIorCURIE(self.preview_image)

        if not isinstance(self.provided_image, list):
            self.provided_image = (
                [self.provided_image] if self.provided_image is not None else []
            )
        self.provided_image = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v)
            for v in self.provided_image
        ]

        if not isinstance(self.provided_3d, list):
            self.provided_3d = (
                [self.provided_3d] if self.provided_3d is not None else []
            )
        self.provided_3d = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.provided_3d
        ]

        if not isinstance(self.resource_service, list):
            self.resource_service = (
                [self.resource_service] if self.resource_service is not None else []
            )
        self.resource_service = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v)
            for v in self.resource_service
        ]

        if self.credit is not None and not isinstance(self.credit, str):
            self.credit = str(self.credit)

        self._normalize_inlined_as_list(
            slot_name="work_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class MediaObject(RelatedObject):
    """
    Descrição e referência a um único arquivo de mídia.
    O `id` deve ser uma URI apontando para a localização permanente da mídia, não diretamente para um arquivo de
    imagem.
    Obrigatoriamente deve conter um link para o recurso online, seja na forma de `provided_image`, `provided_3d` ou
    `resource_service`. É importante, também, fornecer o link para uma miniatura que será usada como pré-visualização,
    em `preview_image`.
    No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da
    imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva
    API ou as informações acerca do modelo.
    Por exemplo, no caso de uma imagem hospedada no Wikimedia Commons:
    ``` id: https://commons.wikimedia.org/wiki/File:BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg preview_image:
    https://thumb.wikimedia.org/wikipedia/commons/thumb/8/86/BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg/330px-BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg
    provided_image:
    - https://upload.wikimedia.org/wikipedia/commons/8/86/BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg
    resource_service:
    -
    https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&format=json&titles=File:BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg
    ```
    Não armazenamos imagens ou outros arquivos de mídia nos sites dos Documentários da Arquitetura Tradicional.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["MediaObject"]
    class_class_curie: ClassVar[str] = "schema:MediaObject"
    class_name: ClassVar[str] = "MediaObject"
    class_model_uri: ClassVar[URIRef] = WASTH.MediaObject

    format: str = None
    depiction_type: Union[str, "DepictionType"] = None
    title: str = None
    description: str = None
    work_rights: Union[Union[dict, Right], list[Union[dict, Right]]] = None
    scale: Optional[float] = None
    unit: Optional[Union[dict, TypedReference]] = None
    preview_image: Optional[Union[str, URIorCURIE]] = None
    provided_image: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    provided_3d: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    resource_service: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    measurements: Optional[
        Union[Union[dict, Measurement], list[Union[dict, Measurement]]]
    ] = empty_list()
    credit: Optional[str] = None
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.depiction_type):
            self.MissingRequiredField("depiction_type")
        if not isinstance(self.depiction_type, DepictionType):
            self.depiction_type = DepictionType(self.depiction_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.work_rights):
            self.MissingRequiredField("work_rights")
        self._normalize_inlined_as_list(
            slot_name="work_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        if self.scale is not None and not isinstance(self.scale, float):
            self.scale = float(self.scale)

        if self.unit is not None and not isinstance(self.unit, TypedReference):
            self.unit = TypedReference(**as_dict(self.unit))

        if self.preview_image is not None and not isinstance(
            self.preview_image, URIorCURIE
        ):
            self.preview_image = URIorCURIE(self.preview_image)

        if not isinstance(self.provided_image, list):
            self.provided_image = (
                [self.provided_image] if self.provided_image is not None else []
            )
        self.provided_image = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v)
            for v in self.provided_image
        ]

        if not isinstance(self.provided_3d, list):
            self.provided_3d = (
                [self.provided_3d] if self.provided_3d is not None else []
            )
        self.provided_3d = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.provided_3d
        ]

        if not isinstance(self.resource_service, list):
            self.resource_service = (
                [self.resource_service] if self.resource_service is not None else []
            )
        self.resource_service = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v)
            for v in self.resource_service
        ]

        self._normalize_inlined_as_list(
            slot_name="measurements",
            slot_type=Measurement,
            key_name="measurement_value",
            keyed=False,
        )

        if self.credit is not None and not isinstance(self.credit, str):
            self.credit = str(self.credit)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class LegalBody(Thing):
    """
    Referência a uma pessoa jurídica (pode ser um indivíduo detentor de direitos jurídicos específicos que se queira
    referenciar) ou entidade coletiva histórica.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "LegalBody"
    class_model_uri: ClassVar[URIRef] = WASTH.LegalBody

    legal_body_type: Optional[Union[str, "RepositoryType"]] = "corporate"
    weblink: Optional[Union[str, URIorCURIE]] = None
    identifiers: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()
    category: Optional[Union[str, URIorCURIE]] = TERM["lido00413"]

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.legal_body_type is not None and not isinstance(
            self.legal_body_type, RepositoryType
        ):
            self.legal_body_type = RepositoryType(self.legal_body_type)

        if self.weblink is not None and not isinstance(self.weblink, URIorCURIE):
            self.weblink = URIorCURIE(self.weblink)

        self._normalize_inlined_as_list(
            slot_name="identifiers",
            slot_type=TypedReference,
            key_name="refid",
            keyed=True,
        )

        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class Event(Thing):
    """
    Um evento é um processo específico e coerente, delimitável, de interações entre fatores materiais, humanos e
    físico-ambientais, que afetam objetos de modo característico ao tipo de processo em jogo. Pode tratar-se de uma
    ação ou um conjunto articulado de ações intencionais, de consequências imprevistas de ações intencionais, ou de
    processos naturais sem intervenção humana.
    -------------------------------------------------------------------------
    This class comprises distinct, delimited and coherent processes and interactions of a material nature, in
    cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way
    characteristic of the kind of process. Typical examples are meetings, births, deaths, actions of decision taking,
    making or inventing things, but also more complex and extended ones such as conferences, elections, building of a
    castle, or battles.
    While the continuous growth of a tree lacks the limits characteristic of an event, its germination from a seed
    does qualify as an event. Similarly, the blowing of the wind lacks the distinctness and limits of an event, but a
    hurricane, flood or earthquake would qualify as an event. Mental processes are considered as events, in cases
    where they are connected with the material externalization of their results; for example, the creation of a poem,
    a performance or a change of intention that becomes obvious from subsequent actions or declarations.
    The effects of an instance of E5 Event may not lead to relevant permanent changes of properties or relations of
    the items involved in it, for example an unrecorded performance. Of course, in order to be documented, some kind
    of evidence for an event must exist, be it witnesses, traces or products of the event.
    While instances of E4 Period always require some form of coherence between its constituent phenomena, in addition,
    the essential constituents of instances of E5 Event should contribute to an overall effect; for example, the
    statements made during a meeting and the listening of the audience.
    Viewed at a coarse level of detail, an instance of E5 Event may appear as if it had an ‘instantaneous’ overall
    effect, but any process or interaction of material nature in reality have an extent in time and space. At a fine
    level, instances of E5 Event may be analysed into component phenomena and phases within a space and timeframe, and
    as such can be seen as a period, regardless of the size of the phenomena. The reverse is not necessarily the case:
    not all instances of E4 Period give rise to a noteworthy overall effect and are thus not instances of E5 Event.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E5_Event"]
    class_class_curie: ClassVar[str] = "crm:E5_Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = WASTH.Event

    event_type: Union[str, "EventType"] = None
    style_period: Optional[
        Union[Union[dict, StylePeriod], list[Union[dict, StylePeriod]]]
    ] = empty_list()
    culture: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()
    measurements: Optional[
        Union[Union[dict, Measurement], list[Union[dict, Measurement]]]
    ] = empty_list()
    material: Optional[
        Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]
    ] = empty_list()
    technique: Optional[
        Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]
    ] = empty_list()
    media: Optional[Union[Union[dict, MediaObject], list[Union[dict, MediaObject]]]] = (
        empty_list()
    )
    related_events: Optional[
        Union[Union[dict, RelatedEvent], list[Union[dict, RelatedEvent]]]
    ] = empty_list()
    actor_role: Optional[Union[Union[dict, Actor], list[Union[dict, Actor]]]] = (
        empty_list()
    )
    start_date: Optional[
        Union[Union[dict, EventDate], list[Union[dict, EventDate]]]
    ] = empty_list()
    end_date: Optional[Union[Union[dict, EventDate], list[Union[dict, EventDate]]]] = (
        empty_list()
    )
    event_place: Optional[Union[Union[dict, "Site"], list[Union[dict, "Site"]]]] = (
        empty_list()
    )
    method: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    things_present: Optional[
        Union[Union[dict, RelatedWork], list[Union[dict, RelatedWork]]]
    ] = empty_list()
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_type):
            self.MissingRequiredField("event_type")
        if not isinstance(self.event_type, EventType):
            self.event_type = EventType(self.event_type)

        self._normalize_inlined_as_list(
            slot_name="style_period",
            slot_type=StylePeriod,
            key_name="period_name_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="culture", slot_type=TypedReference, key_name="refid", keyed=True
        )

        self._normalize_inlined_as_list(
            slot_name="measurements",
            slot_type=Measurement,
            key_name="measurement_value",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="material",
            slot_type=MaterialTech,
            key_name="material_tech_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="technique",
            slot_type=MaterialTech,
            key_name="material_tech_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="media", slot_type=MediaObject, key_name="format", keyed=False
        )

        if not isinstance(self.related_events, list):
            self.related_events = (
                [self.related_events] if self.related_events is not None else []
            )
        self.related_events = [
            v if isinstance(v, RelatedEvent) else RelatedEvent(**as_dict(v))
            for v in self.related_events
        ]

        if not isinstance(self.actor_role, list):
            self.actor_role = [self.actor_role] if self.actor_role is not None else []
        self.actor_role = [
            v if isinstance(v, Actor) else Actor(**as_dict(v)) for v in self.actor_role
        ]

        self._normalize_inlined_as_list(
            slot_name="start_date",
            slot_type=EventDate,
            key_name="date_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="end_date", slot_type=EventDate, key_name="date_type", keyed=False
        )

        if not isinstance(self.event_place, list):
            self.event_place = (
                [self.event_place] if self.event_place is not None else []
            )
        self.event_place = [
            v if isinstance(v, Site) else Site(**as_dict(v)) for v in self.event_place
        ]

        if not isinstance(self.method, list):
            self.method = [self.method] if self.method is not None else []
        self.method = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.method
        ]

        self._normalize_inlined_as_list(
            slot_name="things_present",
            slot_type=RelatedWork,
            key_name="relation_type",
            keyed=False,
        )

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class Appellation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Appellation"]
    class_class_curie: ClassVar[str] = "wasth:Appellation"
    class_name: ClassVar[str] = "Appellation"
    class_model_uri: ClassVar[URIRef] = WASTH.Appellation

    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    label: Optional[str] = None
    appellation_preference: Optional[Union[str, "LabelType"]] = "alternative"
    title_type: Optional[Union[str, "TitleType"]] = "descriptive"

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.appellation_preference is not None and not isinstance(
            self.appellation_preference, LabelType
        ):
            self.appellation_preference = LabelType(self.appellation_preference)

        if self.title_type is not None and not isinstance(self.title_type, TitleType):
            self.title_type = TitleType(self.title_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Repository(Thing):
    """
    Entidade com existência jurídica e espacial.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Repository"
    class_model_uri: ClassVar[URIRef] = WASTH.Repository

    site: Union[dict, "Site"] = None
    legal_body: Union[dict, LegalBody] = None
    repository_type: Optional[Union[str, "RepositoryType"]] = "corporate"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, Site):
            self.site = Site(**as_dict(self.site))

        if self._is_empty(self.legal_body):
            self.MissingRequiredField("legal_body")
        if not isinstance(self.legal_body, LegalBody):
            self.legal_body = LegalBody(**as_dict(self.legal_body))

        if self.repository_type is not None and not isinstance(
            self.repository_type, RepositoryType
        ):
            self.repository_type = RepositoryType(self.repository_type)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class Work(Thing):
    """
    Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastrar uma edificação, um conjunto
    arquitetônico, ou ainda uma parte significativa de uma edificação.
    <h3>Especificação e modelo de preenchimento</h3>
    As instruções de preeenchimento para cada elemento da ficha se encontram na seção [Slots](#slots).
    Observe como exemplo de ficha (quase) completamente preenchida a [Casa dos Sete
    Candeeiros](https://github.com/arqtrad/casa/blob/main/br-ba-salvador-casa_7_candeeiros.md?plain=1).
    Em caso de dúvidas quanto à formatação da ficha, observe as informações acerca da especificação
    [YAML](https://www.yaml.info/learn/index.html).
    Todos os grupos que começam com um hífen `-` são listas que podem conter qualquer número de linhas ou blocos.
    A ordem dos blocos não é importante, mas a hierarquia dentro de cada bloco e a indentação de dois espaços por
    nível hierárquico, sim.
    O caractere `#` indica o início de um comentário, que prossegue até o final da linha. Os comentários e as linhas
    que contêm apenas comentários devem ser apagados das fichas preenchidas.
    Campos não preenchidos também devem ser apagadas das fichas.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["LandmarksOrHistoricalBuildings"]
    class_class_curie: ClassVar[str] = "schema:LandmarksOrHistoricalBuildings"
    class_name: ClassVar[str] = "Work"
    class_model_uri: ClassVar[URIRef] = WASTH.Work

    id: Union[str, WorkId] = None
    site: Union[dict, "Site"] = None
    work_rights: Union[Union[dict, Right], list[Union[dict, Right]]] = None
    record_rights: Union[Union[dict, Right], list[Union[dict, Right]]] = None
    title_type: Union[str, "TitleType"] = None
    title: str = None
    record_date: Union[str, XSDDate] = None
    description: str = None
    measurements: Optional[
        Union[Union[dict, Measurement], list[Union[dict, Measurement]]]
    ] = empty_list()
    material: Optional[
        Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]
    ] = empty_list()
    technique: Optional[
        Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]
    ] = empty_list()
    style_period: Optional[
        Union[Union[dict, StylePeriod], list[Union[dict, StylePeriod]]]
    ] = empty_list()
    culture: Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ] = empty_dict()
    resources: Optional[
        Union[
            dict[Union[str, ResourceId], Union[dict, Resource]],
            list[Union[dict, Resource]],
        ]
    ] = empty_dict()
    media: Optional[Union[Union[dict, MediaObject], list[Union[dict, MediaObject]]]] = (
        empty_list()
    )
    work_type_condition: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    work_type_form: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    work_type_function: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    work_type_context: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    work_type_material_tech: Optional[
        Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]
    ] = empty_list()
    work_type_subject: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    work_type_use: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    classification_genre: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    classification_subject: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    classification_local: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    classification_special: Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ] = empty_list()
    part_of: Optional[
        Union[
            Union[dict, LargerContextReference],
            list[Union[dict, LargerContextReference]],
        ]
    ] = empty_list()
    former_site: Optional[Union[Union[dict, "Site"], list[Union[dict, "Site"]]]] = (
        empty_list()
    )
    intended_site: Optional[Union[Union[dict, "Site"], list[Union[dict, "Site"]]]] = (
        empty_list()
    )
    other_site: Optional[Union[Union[dict, "Site"], list[Union[dict, "Site"]]]] = (
        empty_list()
    )
    location_historic: Optional[
        Union[Union[dict, LegalBody], list[Union[dict, LegalBody]]]
    ] = empty_list()
    inscriptions: Optional[
        Union[Union[dict, "Inscription"], list[Union[dict, "Inscription"]]]
    ] = empty_list()
    collection: Optional[
        Union[Union[dict, "Collection"], list[Union[dict, "Collection"]]]
    ] = empty_list()
    related_works: Optional[
        Union[Union[dict, RelatedWork], list[Union[dict, RelatedWork]]]
    ] = empty_list()
    subject: Optional[Union[Union[dict, "Topic"], list[Union[dict, "Topic"]]]] = (
        empty_list()
    )
    category: Optional[Union[str, URIorCURIE]] = TERM["lido00096"]
    content: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkId):
            self.id = WorkId(self.id)

        if self._is_empty(self.site):
            self.MissingRequiredField("site")
        if not isinstance(self.site, Site):
            self.site = Site(**as_dict(self.site))

        if self._is_empty(self.work_rights):
            self.MissingRequiredField("work_rights")
        self._normalize_inlined_as_list(
            slot_name="work_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        if self._is_empty(self.record_rights):
            self.MissingRequiredField("record_rights")
        self._normalize_inlined_as_list(
            slot_name="record_rights",
            slot_type=Right,
            key_name="rights_type",
            keyed=False,
        )

        if self._is_empty(self.title_type):
            self.MissingRequiredField("title_type")
        if not isinstance(self.title_type, TitleType):
            self.title_type = TitleType(self.title_type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.record_date):
            self.MissingRequiredField("record_date")
        if not isinstance(self.record_date, XSDDate):
            self.record_date = XSDDate(self.record_date)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(
            slot_name="measurements",
            slot_type=Measurement,
            key_name="measurement_value",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="material",
            slot_type=MaterialTech,
            key_name="material_tech_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="technique",
            slot_type=MaterialTech,
            key_name="material_tech_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="style_period",
            slot_type=StylePeriod,
            key_name="period_name_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="culture", slot_type=TypedReference, key_name="refid", keyed=True
        )

        self._normalize_inlined_as_list(
            slot_name="resources", slot_type=Resource, key_name="id", keyed=True
        )

        self._normalize_inlined_as_list(
            slot_name="media", slot_type=MediaObject, key_name="format", keyed=False
        )

        if not isinstance(self.work_type_condition, list):
            self.work_type_condition = (
                [self.work_type_condition]
                if self.work_type_condition is not None
                else []
            )
        self.work_type_condition = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_condition
        ]

        if not isinstance(self.work_type_form, list):
            self.work_type_form = (
                [self.work_type_form] if self.work_type_form is not None else []
            )
        self.work_type_form = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_form
        ]

        if not isinstance(self.work_type_function, list):
            self.work_type_function = (
                [self.work_type_function] if self.work_type_function is not None else []
            )
        self.work_type_function = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_function
        ]

        if not isinstance(self.work_type_context, list):
            self.work_type_context = (
                [self.work_type_context] if self.work_type_context is not None else []
            )
        self.work_type_context = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_context
        ]

        self._normalize_inlined_as_list(
            slot_name="work_type_material_tech",
            slot_type=MaterialTech,
            key_name="material_tech_type",
            keyed=False,
        )

        if not isinstance(self.work_type_subject, list):
            self.work_type_subject = (
                [self.work_type_subject] if self.work_type_subject is not None else []
            )
        self.work_type_subject = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_subject
        ]

        if not isinstance(self.work_type_use, list):
            self.work_type_use = (
                [self.work_type_use] if self.work_type_use is not None else []
            )
        self.work_type_use = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.work_type_use
        ]

        if not isinstance(self.classification_genre, list):
            self.classification_genre = (
                [self.classification_genre]
                if self.classification_genre is not None
                else []
            )
        self.classification_genre = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.classification_genre
        ]

        if not isinstance(self.classification_subject, list):
            self.classification_subject = (
                [self.classification_subject]
                if self.classification_subject is not None
                else []
            )
        self.classification_subject = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.classification_subject
        ]

        if not isinstance(self.classification_local, list):
            self.classification_local = (
                [self.classification_local]
                if self.classification_local is not None
                else []
            )
        self.classification_local = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.classification_local
        ]

        if not isinstance(self.classification_special, list):
            self.classification_special = (
                [self.classification_special]
                if self.classification_special is not None
                else []
            )
        self.classification_special = [
            v if isinstance(v, ConceptReference) else ConceptReference(**as_dict(v))
            for v in self.classification_special
        ]

        self._normalize_inlined_as_list(
            slot_name="part_of",
            slot_type=LargerContextReference,
            key_name="context_type",
            keyed=False,
        )

        if not isinstance(self.former_site, list):
            self.former_site = (
                [self.former_site] if self.former_site is not None else []
            )
        self.former_site = [
            v if isinstance(v, Site) else Site(**as_dict(v)) for v in self.former_site
        ]

        if not isinstance(self.intended_site, list):
            self.intended_site = (
                [self.intended_site] if self.intended_site is not None else []
            )
        self.intended_site = [
            v if isinstance(v, Site) else Site(**as_dict(v)) for v in self.intended_site
        ]

        if not isinstance(self.other_site, list):
            self.other_site = [self.other_site] if self.other_site is not None else []
        self.other_site = [
            v if isinstance(v, Site) else Site(**as_dict(v)) for v in self.other_site
        ]

        if not isinstance(self.location_historic, list):
            self.location_historic = (
                [self.location_historic] if self.location_historic is not None else []
            )
        self.location_historic = [
            v if isinstance(v, LegalBody) else LegalBody(**as_dict(v))
            for v in self.location_historic
        ]

        self._normalize_inlined_as_list(
            slot_name="inscriptions",
            slot_type=Inscription,
            key_name="inscription_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="collection",
            slot_type=Collection,
            key_name="collection_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="related_works",
            slot_type=RelatedWork,
            key_name="relation_type",
            keyed=False,
        )

        self._normalize_inlined_as_list(
            slot_name="subject", slot_type=Topic, key_name="topic_type", keyed=False
        )

        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class Site(Thing):
    """
    O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura Tradicional. Ele permite investigar a
    distribuição geográfica das características construtivas e morfológicas das edificações cadastradas.
    As instruções de preenchimento específicas se encontram na documentação das classes que fornecem os dados para o
    sítio. Consulte também o [Tutorial de
    georreferenciamento](https://github.com/arqtrad/.github/wiki/Tutorial-de-georreferenciamento) para saber como
    localizar edificações não cadastradas nas bases de dados do patrimônio cultural (SICG ou SIPA).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CRM["E92_Spacetime_Volume"]
    class_class_curie: ClassVar[str] = "crm:E92_Spacetime_Volume"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = WASTH.Site

    location: Union[dict, "GeographicPoint"] = None
    name: Optional[Union[dict, "GeonamesFeature"]] = None
    site_type: Optional[Union[str, "RepositoryType"]] = "geographic"
    extent: Optional[Union[dict, "GeographicExtent"]] = None
    event_place_type: Optional[Union[str, "EventPlaceType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, GeographicPoint):
            self.location = GeographicPoint(**as_dict(self.location))

        if self.name is not None and not isinstance(self.name, GeonamesFeature):
            self.name = GeonamesFeature(**as_dict(self.name))

        if self.site_type is not None and not isinstance(
            self.site_type, RepositoryType
        ):
            self.site_type = RepositoryType(self.site_type)

        if self.extent is not None and not isinstance(self.extent, GeographicExtent):
            self.extent = GeographicExtent(**as_dict(self.extent))

        if self.event_place_type is not None and not isinstance(
            self.event_place_type, EventPlaceType
        ):
            self.event_place_type = EventPlaceType(self.event_place_type)

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class GeographicPoint(YAMLRoot):
    """
    Coordenadas do ponto que situa o sítio na visualização do mapa.
    A fonte preferencial de autoridade para o georreferenciamento é um órgão público, por exemplo o IPHAN no Brasil
    (usando as coordenadas informadas no [SICG]) ou a DGMN em Portugal (usando as coordenadas informadas no [SIPA]).
    Caso não haja georreferenciamento oficial, usar uma planta cadastral municipal georreferenciada ou, na falta
    desta, o [Global Building Atlas]. Nesses casos, para se obter as coordenadas de georreferenciamento, é preciso
    usar um Sistema de Informações Geográficas da sua preferência.
    Como exemplo, no [QGIS], isso pode ser feito seguindo as instruções abaixo :
    1. Sempre projetar o mapa usando EPSG:4326 (WGS84) ;
    2. Selecionar o polígono da edificação na camada da planta cadastral ou
    do Global Building Atlas ;

    3. Rodar o comando do menu `Vector > Geometry Tools > Centroids` para
    obter as coordenadas do ponto (`location`) — ele vai criar uma camada
    temporária com o ponto no centróide do polígono selecionado ;

    4. Usar novamente a ferramenta `Get WKT` para visualizar as coordenadas,
    copiar os valores e colar na ficha com o grau de precisão (casas
    decimais) desejado.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["GeographicPoint"]
    class_class_curie: ClassVar[str] = "wasth:GeographicPoint"
    class_name: ClassVar[str] = "GeographicPoint"
    class_model_uri: ClassVar[URIRef] = WASTH.GeographicPoint

    lat: Union[float, Latitude] = None
    lon: Union[float, Longitude] = None
    srs_name: Optional[Union[str, URIorCURIE]] = None
    source: Optional[Union[dict, LegalBody]] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()
    alt: Optional[float] = None
    zoom: Optional[int] = 13

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lat):
            self.MissingRequiredField("lat")
        if not isinstance(self.lat, Latitude):
            self.lat = Latitude(self.lat)

        if self._is_empty(self.lon):
            self.MissingRequiredField("lon")
        if not isinstance(self.lon, Longitude):
            self.lon = Longitude(self.lon)

        if self.srs_name is not None and not isinstance(self.srs_name, URIorCURIE):
            self.srs_name = URIorCURIE(self.srs_name)

        if self.source is not None and not isinstance(self.source, LegalBody):
            self.source = LegalBody(**as_dict(self.source))

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        if self.alt is not None and not isinstance(self.alt, float):
            self.alt = float(self.alt)

        if self.zoom is not None and not isinstance(self.zoom, int):
            self.zoom = int(self.zoom)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeographicExtent(YAMLRoot):
    """
    Coordenadas do polígono que define o sítio.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["GeographicExtent"]
    class_class_curie: ClassVar[str] = "wasth:GeographicExtent"
    class_name: ClassVar[str] = "GeographicExtent"
    class_model_uri: ClassVar[URIRef] = WASTH.GeographicExtent

    geometry_type: Union[str, "GeometryType"] = None
    coordinates: Union[str, GeoJSONCoordinateArray] = None
    srs_name: Optional[Union[str, URIorCURIE]] = None
    source: Optional[Union[dict, LegalBody]] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.geometry_type):
            self.MissingRequiredField("geometry_type")
        if not isinstance(self.geometry_type, GeometryType):
            self.geometry_type = GeometryType(self.geometry_type)

        if self._is_empty(self.coordinates):
            self.MissingRequiredField("coordinates")
        if not isinstance(self.coordinates, GeoJSONCoordinateArray):
            self.coordinates = GeoJSONCoordinateArray(self.coordinates)

        if self.srs_name is not None and not isinstance(self.srs_name, URIorCURIE):
            self.srs_name = URIorCURIE(self.srs_name)

        if self.source is not None and not isinstance(self.source, LegalBody):
            self.source = LegalBody(**as_dict(self.source))

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Inscription(YAMLRoot):
    """
    A descrição da inscrição informa local, dimensões e características. Os tipos de descrição podem ser extraídos da
    hierarquia Getty: <http://vocab.getty.edu/page/aat/300220469>.
    Os itens das listas de `material` e `technique` DEVEM usar o nosso [vocabulário
    controlado](https://vocabulario.tradicional.arq.br).
    Essa distinção é especialmente relevante no caso de revestimentos, como estuques, azulejos ou pinturas
    decorativas, por oposição à base sobre a qual eles são aplicados.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Inscription"]
    class_class_curie: ClassVar[str] = "wasth:Inscription"
    class_name: ClassVar[str] = "Inscription"
    class_model_uri: ClassVar[URIRef] = WASTH.Inscription

    inscription_type: Union[str, "InscriptionType"] = "text"
    format_extent: Optional[Union[dict, TypedReference]] = None
    description: Optional[str] = None
    content: Optional[str] = None
    bibliographic_citation: Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.inscription_type):
            self.MissingRequiredField("inscription_type")
        if not isinstance(self.inscription_type, InscriptionType):
            self.inscription_type = InscriptionType(self.inscription_type)

        if self.format_extent is not None and not isinstance(
            self.format_extent, TypedReference
        ):
            self.format_extent = TypedReference(**as_dict(self.format_extent))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.content is not None and not isinstance(self.content, str):
            self.content = str(self.content)

        self._normalize_inlined_as_list(
            slot_name="bibliographic_citation",
            slot_type=BibliographicCitation,
            key_name="refid",
            keyed=True,
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Topic(YAMLRoot):
    """
    Subject or iconographic topic.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Topic"]
    class_class_curie: ClassVar[str] = "wasth:Topic"
    class_name: ClassVar[str] = "Topic"
    class_model_uri: ClassVar[URIRef] = WASTH.Topic

    concept_name: Union[dict, Concept] = None
    topic_type: Union[str, "SubjectType"] = None
    description: Optional[str] = None
    format_extent: Optional[Union[dict, TypedReference]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_name):
            self.MissingRequiredField("concept_name")
        if not isinstance(self.concept_name, Concept):
            self.concept_name = Concept(**as_dict(self.concept_name))

        if self._is_empty(self.topic_type):
            self.MissingRequiredField("topic_type")
        if not isinstance(self.topic_type, SubjectType):
            self.topic_type = SubjectType(self.topic_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.format_extent is not None and not isinstance(
            self.format_extent, TypedReference
        ):
            self.format_extent = TypedReference(**as_dict(self.format_extent))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Collection(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = WASTH["Collection"]
    class_class_curie: ClassVar[str] = "wasth:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = WASTH.Collection

    collection_type: Union[str, "CollectionType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        self.category = str(
            self.class_class_curie
            if self.class_class_curie is not None
            else self.class_class_uri
        )


@dataclass(repr=False)
class GeonamesFeature(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEONAMES["Feature"]
    class_class_curie: ClassVar[str] = "geonames:Feature"
    class_name: ClassVar[str] = "GeonamesFeature"
    class_model_uri: ClassVar[URIRef] = WASTH.GeonamesFeature

    geonameid: Union[int, GeonamesFeatureGeonameid] = None
    name: Optional[str] = None
    asciiname: Optional[str] = None
    alternatenames: Optional[str] = None
    latitude: Optional[Union[float, Latitude]] = None
    longitude: Optional[Union[float, Longitude]] = None
    feature_class: Optional[Union[str, "FeatureClassEnum"]] = None
    feature_code: Optional[Union[str, "FeatureCodeEnum"]] = None
    country_code: Optional[Union[str, "CountryCodeEnum"]] = None
    cc2: Optional[str] = None
    admin1_code: Optional[int] = None
    admin2_code: Optional[int] = None
    admin3_code: Optional[int] = None
    admin4_code: Optional[str] = None
    population: Optional[int] = None
    elevation: Optional[int] = None
    dem: Optional[int] = None
    timezone: Optional[Union[str, "TimezoneEnum"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.geonameid):
            self.MissingRequiredField("geonameid")
        if not isinstance(self.geonameid, GeonamesFeatureGeonameid):
            self.geonameid = GeonamesFeatureGeonameid(self.geonameid)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.asciiname is not None and not isinstance(self.asciiname, str):
            self.asciiname = str(self.asciiname)

        if self.alternatenames is not None and not isinstance(self.alternatenames, str):
            self.alternatenames = str(self.alternatenames)

        if self.latitude is not None and not isinstance(self.latitude, Latitude):
            self.latitude = Latitude(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Longitude):
            self.longitude = Longitude(self.longitude)

        if self.feature_class is not None and not isinstance(
            self.feature_class, FeatureClassEnum
        ):
            self.feature_class = FeatureClassEnum(self.feature_class)

        if self.feature_code is not None and not isinstance(
            self.feature_code, FeatureCodeEnum
        ):
            self.feature_code = FeatureCodeEnum(self.feature_code)

        if self.country_code is not None and not isinstance(
            self.country_code, CountryCodeEnum
        ):
            self.country_code = CountryCodeEnum(self.country_code)

        if self.cc2 is not None and not isinstance(self.cc2, str):
            self.cc2 = str(self.cc2)

        if self.admin1_code is not None and not isinstance(self.admin1_code, int):
            self.admin1_code = int(self.admin1_code)

        if self.admin2_code is not None and not isinstance(self.admin2_code, int):
            self.admin2_code = int(self.admin2_code)

        if self.admin3_code is not None and not isinstance(self.admin3_code, int):
            self.admin3_code = int(self.admin3_code)

        if self.admin4_code is not None and not isinstance(self.admin4_code, str):
            self.admin4_code = str(self.admin4_code)

        if self.population is not None and not isinstance(self.population, int):
            self.population = int(self.population)

        if self.elevation is not None and not isinstance(self.elevation, int):
            self.elevation = int(self.elevation)

        if self.dem is not None and not isinstance(self.dem, int):
            self.dem = int(self.dem)

        if self.timezone is not None and not isinstance(self.timezone, TimezoneEnum):
            self.timezone = TimezoneEnum(self.timezone)

        if self.modification_date is not None and not isinstance(
            self.modification_date, XSDDate
        ):
            self.modification_date = XSDDate(self.modification_date)

        super().__post_init__(**kwargs)


# Enumerations
class AgentType(EnumDefinitionImpl):
    """
    Tipo de agente na terminologia LIDO.
    """

    personal = PermissibleValue(
        text="personal", title="individual", meaning=TERM["lido00163"]
    )
    corporate = PermissibleValue(
        text="corporate",
        title="coletivo",
        description="""Uma entidade coletiva tal como uma oficina, escola (no sentido de um grupo de artistas que partilham um estilo semelhante), empresa, corporação de ofício, grupo étnico-cultural, ou outra agremiação na qual é impossível ou irrelevante delimitar as contribuições individuais.""",
        meaning=TERM["lido00413"],
    )
    family = PermissibleValue(
        text="family",
        title="familiar",
        description="""Coletivo de agentes caracterizado por laços familiares, incluindo parentesco consanguíneo, por matrimônio, adotivo ou outras relações familiares socialmente sancionadas no seu contexto de origem.""",
        meaning=TERM["lido00166"],
    )
    other = PermissibleValue(text="other", title="outro", meaning=TERM["lido00165"])

    _defn = EnumDefinition(
        name="AgentType",
        description="Tipo de agente na terminologia LIDO.",
    )


class CollectionType(EnumDefinitionImpl):
    """
    The LIDO Object Type Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO
    Object Type element, specifying the particular kind of object being in some way associated with the object/work
    that is the focus of the record.
    """

    _defn = EnumDefinition(
        name="CollectionType",
        description="""The LIDO Object Type Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Object Type element, specifying the particular kind of object being in some way associated with the object/work that is the focus of the record.""",
    )


class ConceptType(EnumDefinitionImpl):
    """
    Tipos de termos de vocabulário baseados no Getty AAT.
    """

    concept = PermissibleValue(text="concept", title="conceitos")
    hierarchy_name = PermissibleValue(
        text="hierarchy_name", title="(nome de hierarquia)"
    )
    guide_term = PermissibleValue(text="guide_term", title="<termo guia>")
    facet = PermissibleValue(text="facet", title="Faceta")

    _defn = EnumDefinition(
        name="ConceptType",
        description="""Tipos de termos de vocabulário baseados no Getty AAT.""",
    )


class DateType(EnumDefinitionImpl):
    """
    Exatidão da data conhecida.
    """

    exact = PermissibleValue(
        text="exact",
        title="conhecida",
        description="""Designates a date that is definitely known, based on credible, documented fact.
Note that *exact* does not preclude the granularity of the date expression.""",
        meaning=TERM["lido00528"],
    )
    estimated = PermissibleValue(
        text="estimated",
        title="provável",
        description="""Designates a date that is uncertain, estimated broadly using available information about the work or the artist. For example, you could estimate that the earliest possible date for any work by a given artist is eighteen or twenty years after the artist's birth.
Included are also dates that are inferred from known dates associated with the object. For instance, if the date of production is unknown, but the date when the object was found is known, there is evidence that the production must have taken place before the finding of the object.""",
        meaning=TERM["lido00529"],
    )

    _defn = EnumDefinition(
        name="DateType",
        description="Exatidão da data conhecida.",
    )


class DepictionType(EnumDefinitionImpl):
    """
    Designa a relação que a edificação descrita na ficha tem com a mídia relacionada.
    """

    depictedIn = PermissibleValue(
        text="depictedIn",
        title="representado em",
        description="""A obra descrita na ficha está representada na mídia relacionada, que será geralmente uma obra de arte ou fotografia depositada num repositório externo (catálogo de museu, Wikimedia Commons, etc.).""",
        meaning=TERM["lido00998"],
    )

    _defn = EnumDefinition(
        name="DepictionType",
        description="""Designa a relação que a edificação descrita na ficha tem com a mídia relacionada.""",
    )


class EventType(EnumDefinitionImpl):
    """
    O tipo de incidência sobre a edificação que o evento descreve. Usa a terminologia do LIDO em
    <http://terminology.lido-schema.org/eventType>.
    """

    creation = PermissibleValue(
        text="creation",
        title="criação",
        description="""Designa um acontecimento que leva à conceção de itens ou produtos de natureza imaterial, como obras literárias ou imagens. Não usar para a produção de bens materiais. Quando a conceção desses bens, como uma edificação, passa por um processo de criação intelectual atestada, usar para tanto o termo `designing` (\"projeto\").""",
        meaning=TERM["lido0001"],
    )
    designing = PermissibleValue(
        text="designing",
        title="projeto",
        description="""O projeto, na classificação de tipos de eventos do LIDO, designa a criação de um arcabouço conceitual para a organização da aparência de objetos tridimensionais, obras visuais, obras de arquitetura, ou sistemas técnicos.""",
        meaning=TERM["lido00224"],
    )
    production = PermissibleValue(
        text="production",
        title="produção",
        description="""Designa ações que levam à existência de novos objetos, compreendendo ações como projeto e execução.""",
        meaning=TERM["lido00007"],
    )
    item_production = PermissibleValue(
        text="item_production",
        title="produção de um exemplar",
        description="""No caso de construções seriadas (por exemplo, casas idênticas numa vila operária), designa a produção de um exemplar singular dentro do conjunto. Usar quando for relevante individualizar a produção desses exemplares no âmbito da descrição do seu conjunto, mas não quando cada exemplar for indexado separadamente.""",
        meaning=TERM["lido01096"],
    )
    completion = PermissibleValue(
        text="completion",
        title="conclusão",
        description="""Processo que completa um objeto ou uma campanha de obras.""",
        meaning=TERM["lido00025"],
    )
    execution = PermissibleValue(
        text="execution",
        title="execução do projeto",
        description="""Ação de produzir um objeto com base num projeto, por oposição ao processo de projeto.""",
        meaning=TERM["lido00031"],
    )
    transformation = PermissibleValue(
        text="transformation",
        title="transformação",
        description="""Ação que destrói um objeto e, usando substancialmente a mesma matéria, produz outro que mantém características reconhecíveis do objeto anterior mas é essencialmente distinto deste por sua natureza e identidade. Esta categoria pode ser usada tanto para designar a destruição do objeto antigo quanto a produção do objeto novo.
Exemplos de transformação incluem o uso de espólios ou ruínas para produzir uma nova construção. Não deve ser confundido com `reconstruction` (\"reconstrução\"), que implica seja uma mudança de lugar, seja a reprodução da identidade visual e espacial da edificação anterior.""",
        meaning=TERM["lido00029"],
    )
    reconstruction = PermissibleValue(
        text="reconstruction",
        title="reconstrução",
        description="""Ato de construir uma nova estrutura que substitui e se parece com uma construção anterior que já não subsiste, baseada em evidências históricas, arqueológicas, gráficas, literárias ou outras. A semelhança visual e, eventualmente, funcional é a característica principal de uma reconstrução, e ela pode ou não usar materiais sobrestantes da edificação anterior.
A edificação destruída e a edificação reconstruída devem ser cadastradas em fichas distintas e relacionadas entre si.""",
        meaning=LIDO["lido00723"],
    )
    translocation = PermissibleValue(
        text="translocation",
        title="remoção",
        description="""A remoção designa o ato de se desmantelar uma edificação no seu local de origem para reconstruí-la em outro sítio. Para construções deslocadas sem serem desmanteladas, usar o tipo de evento `move` (\"deslocação\").
Exemplos de remoção são aquela do templo de Abu Simbel, no Egito, ou ainda aquela da casa Erbo Stenzel em Curitiba do seu lote original para o parque São Lourenço (onde foi posteriormente destruída num incêndio).""",
        meaning=LIDO["lido01159"],
    )
    modification_activity = PermissibleValue(
        text="modification_activity",
        title="alteração",
        description="""Ação intencional que cria, altera ou modifica um objeto ou obra em um ou mais dos seus aspectos mas não em outros. Usar para ações que não possam ser definidas como tipos mais específicos de alteração.""",
        meaning=TERM["lido00006"],
    )
    conservation = PermissibleValue(
        text="conservation",
        title="conservação",
        description="""Ação ou processo realizado visando à estabilidade e salvaguarda do objeto no longo prazo, incluindo a sua proteção contra danos ou deterioração e a prevenção da deterioração natural da sua matéria. No nosso vocabulário, a conservação é diferente da preservação e da restauração.""",
        meaning=TERM["lido00402"],
    )
    conversion = PermissibleValue(
        text="conversion",
        title="reforma",
        description="""Intervenção significativa na materialidade e espacialidade de uma edificação, usando materiais e técnicas construtivas. Frequentemente resulta na alteração de uso ou de aparência da edificação, mas sem comprometer a sua identidade anterior.
Sempre que possível, preferir designações mais específicas, tais como `addition`, `removal`, `adaptive_reuse`, `renewal`.""",
        meaning=TERM["lido01178"],
    )
    dismantling = PermissibleValue(
        text="dismantling",
        title="desmantelamento",
        description="""Ato de desmontar ou remover partes significativas de um objeto, especialmente com a intenção de reduzir ou desbilitar o seu uso. Particularmente, refere-se à desmontagem cuidadosa de modo a evitar danos ao material removido, visando à sua reutilização, reciclagem ou gestão de resíduos.""",
        meaning=TERM["lido01179"],
    )
    addition = PermissibleValue(
        text="addition",
        title="acréscimo",
        description="""Acréscimo a uma edificação existente, sem lhe alterar fundamentalmente a identidade, por meio da ampliação ou do acréscimo de elementos. O conjunto resultante continuará a ser identificado como a mesma obra anterior ao acréscimo.""",
        meaning=TERM["lido00008"],
    )
    removal = PermissibleValue(
        text="removal",
        title="eliminação parcial",
        description="""Envolve a redução de uma edificação devida à eliminação de parte(s). Pode incluir a eliminação de anexos, de elementos construtivos, ou a exclusão de uma obra de um conjunto designado.""",
        meaning=TERM["lido00021"],
    )
    partial_destruction_activity = PermissibleValue(
        text="partial_destruction_activity",
        title="destruição parcial",
        description="""Ação intencional de destruir ou danificar partes de uma obra, sem lhe comprometer a identatidade enquanto objeto de documentação.""",
        meaning=TERM["lido01187"],
    )
    remediation = PermissibleValue(
        text="remediation",
        title="reconstituição",
        description="""Atividades construtivas ou de gestão que têm por objetivo restituir uma obra a um estado anterior conhecido ou presumido, sobretudo após perdas catastróficas de materialidade ou integridade.""",
        meaning=TERM["lido01180"],
    )
    renewal = PermissibleValue(
        text="renewal",
        title="renovação",
        description="""Ação que altera uma edificação de modo a recuperar a sua estrutura, atualizar a sua aparência, permitir a adequação a novos usos, aprimorar a sua eficiência energética, ou outras finalidades não relacionadas à preservação do patrimônio cultural ou que não tenham considerações patrimoniais como prioridade.""",
        meaning=TERM["lido01183"],
    )
    restoration = PermissibleValue(
        text="restoration",
        title="restauração",
        description="""Alterações a um objeto que têm por objetivo restabelecer um estado original ou anterior conhecido ou presumido (usar em vez de `part_removal` --- \"eliminação parcial\" se a intenção dominante da eliminação tiver sido a restauração a um estado anterior).""",
        meaning=TERM["lido00034"],
    )
    modification_process = PermissibleValue(
        text="modification_process",
        title="alteração",
        description="""Processo não deliberado de alteração nas características, aparência ou desempenho dos materiais que constituem um objeto. Por exemplo, corrosão, formação de cristais salinos, etc.""",
        meaning=TERM["lido01155"],
    )
    partial_destruction_process = PermissibleValue(
        text="partial_destruction_process",
        title="perda parcial",
        description="""Processo não intencional de degradação material, destruindo ou danificando partes de um objeto sem descaracterizar a sua identidade (por exemplo, sem convertê-lo numa ruína). Pode ser causado por condições ambientais continuadas ou por desastres naturais.""",
        meaning=TERM["lido01157"],
    )
    deterioration = PermissibleValue(
        text="deterioration",
        title="deterioração",
        description="""Processo de perda parcial de matéria, desempenho, ou funcionalidade de um objeto sem intervenção ou atuação deliberada. Geralmente causado por condições ambientais continuadas, mas pode ser agravado por desastres naturais. A deterioração pode levar ao `destruction_process` (\"arruinamento\") da edificação.""",
        meaning=TERM["lido01160"],
    )
    adaptive_reuse = PermissibleValue(
        text="adaptive_reuse",
        title="reutilização adaptada",
        description="""Ação de converter ou adaptar uma edificação, em geral com valor histórico-cultural reconhecido, para novos usos ou aplicação em contexto distinto do original. Distinguir eventos de reutilização adaptativa de eventos que envolvem as intervenções físicas necessárias ou preparatórias a essa reutilização, usando o termo `conversion` (\"reforma\").""",
        meaning=TERM["lido01161"],
    )
    opening = PermissibleValue(
        text="opening",
        title="inauguração",
        description="""Ato pelo qual um objeto é declarado operacional, geralmente por meio de uma cerimônia, mas não necessariamente.""",
        meaning=TERM["lido01169"],
    )
    decommissioning = PermissibleValue(
        text="decommissioning",
        title="desafetação",
        description="""Ação que acompanha ou sinaliza o encerramento da utilização de um objeto, geralmente associado à interdição física da edificação.""",
        meaning=TERM["lido01170"],
    )
    attribute_assignment = PermissibleValue(text="attribute_assignment")
    assignment_to_curated_holding = PermissibleValue(
        text="assignment_to_curated_holding"
    )
    condition_assessment = PermissibleValue(
        text="condition_assessment",
        title="levantamento e avaliação do estado de conservação",
        description="""Ação que analisa as características físicas do objeto, seu estado de conservação e integridade formal.""",
        meaning=TERM["lido00931"],
    )
    cultural_context_assignment = PermissibleValue(text="cultural_context_assignment")
    designation = PermissibleValue(text="designation")
    deciphering = PermissibleValue(text="deciphering")
    meaning_assignment = PermissibleValue(text="meaning_assignment")
    name_assignment = PermissibleValue(text="name_assignment")
    type_assignment = PermissibleValue(text="type_assignment")
    ceremony = PermissibleValue(text="ceremony")
    cornerstone = PermissibleValue(text="cornerstone")
    groundbreaking = PermissibleValue(text="groundbreaking")
    consecration = PermissibleValue(text="consecration")
    deconsecration = PermissibleValue(text="deconsecration")
    change_control_or_title = PermissibleValue(text="change_control_or_title")
    change_control_and_title = PermissibleValue(text="change_control_and_title")
    change_legal_title = PermissibleValue(text="change_legal_title")
    restitution = PermissibleValue(text="restitution")
    change_physical_control = PermissibleValue(text="change_physical_control")
    collecting = PermissibleValue(text="collecting")
    loss = PermissibleValue(text="loss")
    commissioning = PermissibleValue(text="commissioning")
    excavation = PermissibleValue(text="excavation")
    exhibition = PermissibleValue(text="exhibition")
    finding = PermissibleValue(text="finding")
    marketing = PermissibleValue(text="marketing")
    move = PermissibleValue(text="move")
    req_assess = PermissibleValue(text="req_assess")
    display_assess = PermissibleValue(text="display_assess")
    move_assess = PermissibleValue(text="move_assess")
    performance = PermissibleValue(text="performance")
    planning = PermissibleValue(text="planning")
    protection = PermissibleValue(text="protection")
    publishing = PermissibleValue(text="publishing")
    use = PermissibleValue(text="use")
    end_existence = PermissibleValue(text="end_existence")
    destruction = PermissibleValue(text="destruction")
    destruction_activity = PermissibleValue(text="destruction_activity")
    destruction_process = PermissibleValue(text="destruction_process")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="EventType",
        description="""O tipo de incidência sobre a edificação que o evento descreve. Usa a terminologia do LIDO em <http://terminology.lido-schema.org/eventType>.""",
    )


class EventPlaceType(EnumDefinitionImpl):
    """
    Para eventos que implicam a deslocação do bem, indica se o local se refere ao descobrimento, à origem ou ao
    destino da obra.
    """

    discovery = PermissibleValue(text="discovery", meaning=TERM["lido01037"])
    origin = PermissibleValue(text="origin", meaning=TERM["lido00220"])
    destination = PermissibleValue(text="destination", meaning=TERM["lido00221"])

    _defn = EnumDefinition(
        name="EventPlaceType",
        description="""Para eventos que implicam a deslocação do bem, indica se o local se refere ao descobrimento, à origem ou ao destino da obra.""",
    )


class PeriodNameType(EnumDefinitionImpl):
    """
    O vocabulário de tipos de período/estilo do LIDO é uma lista controlada estruturada de termos recomendada para uso
    como valores do atributo de tipo do elemento Período/Estilo.
    O atributo de tipo qualifica o tipo particular de informação de período/estilo, como estilo, período ou movimento.
    Exemplos podem ser “neolítico” para um período, “impressionista” para um estilo ou “cubismo” para um movimento.
    Baseado na categoria do [CDWA
    "Styles/Periods/Groups/Movements"](http://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)
    """

    period = PermissibleValue(
        text="period",
        description="""A distinct named historical or cultural portion or division of time during which something runs its course, characterized by some prevalent or distinguishing condition, circumstance, or occurrence, or by the rule of a particular government.""",
        meaning=TERM["lido00731"],
    )
    style = PermissibleValue(
        text="style",
        description="""A distinct configuration of artistic elements that together constitute a named manner of expression peculiar to a certain epoch, people, or to a visual appearance, technique, or visual language adopted by particular adherents of that language.""",
        meaning=TERM["lido00732"],
    )
    group = PermissibleValue(
        text="group",
        description="""A cultural group, which includes societies or groups of people characterized by common ideas, customs, social behavior, products, or way of life within a particular nation, people, or period.""",
        meaning=TERM["lido00735"],
    )
    movement = PermissibleValue(
        text="movement",
        description="""The state or process in which events or conditions transpire, a tendency, or a trend evident at a particular time or in a particular sphere, particularly a course or series of actions and endeavours on the part of a group of people working towards a shared goal or to advance a shared political, social, or artistic objective.""",
        meaning=TERM["lido00733"],
    )
    dynasty = PermissibleValue(
        text="dynasty",
        description="""The succession of rulers from the same family, line, stock, or group, during a particular period of time; extended to include all the people and culture surrounding this succession of rulers.""",
        meaning=TERM["lido00734"],
    )

    _defn = EnumDefinition(
        name="PeriodNameType",
        description="""O vocabulário de tipos de período/estilo do LIDO é uma lista controlada estruturada de termos recomendada para uso como valores do atributo de tipo do elemento Período/Estilo.
O atributo de tipo qualifica o tipo particular de informação de período/estilo, como estilo, período ou movimento. Exemplos podem ser “neolítico” para um período, “impressionista” para um estilo ou “cubismo” para um movimento.
Baseado na categoria do [CDWA \"Styles/Periods/Groups/Movements\"](http://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)""",
    )


class GeometryType(EnumDefinitionImpl):
    """
    Tipos de geometria do objeto geoJSON
    """

    Polygon = PermissibleValue(text="Polygon")
    MultiPolygon = PermissibleValue(text="MultiPolygon")

    _defn = EnumDefinition(
        name="GeometryType",
        description="Tipos de geometria do objeto geoJSON",
    )


class InscriptionType(EnumDefinitionImpl):
    """
    Tipos de inscrições previstos no VRA Core.
    """

    signature = PermissibleValue(text="signature")
    mark = PermissibleValue(text="mark")
    caption = PermissibleValue(text="caption")
    date = PermissibleValue(text="date")
    text = PermissibleValue(text="text")
    translation = PermissibleValue(text="translation")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="InscriptionType",
        description="Tipos de inscrições previstos no VRA Core.",
    )


class LabelType(EnumDefinitionImpl):
    """
    No SKOS, caracteriza se cada termo deve ser considerado preferencial ou alternativo, usado para indexação, oculto
    da visualização (usado apenas para buscas), etc.
    """

    alternative = PermissibleValue(
        text="alternative",
        description="""Abreviações, abreviaturas, variantes lexicais e formas irregulares de singular ou plural podem ser incluídas como termos ou títulos alternativos para um conceito ou objeto. No caso de edificações ou conjuntos que são conhecidos por mais de um nome (por exemplo, pela sua função atual ou antiga, ou pelo endereço), selecionar `alternative` e indicar o tipo de título.""",
        meaning=SKOS["altLabel"],
    )
    display = PermissibleValue(
        text="display",
        description="Nome a ser apresentado na interfaz pública, incluindo artigos se for o caso.",
        meaning=TERM["lido00526"],
    )
    hidden = PermissibleValue(
        text="hidden",
        description="""Uma variante do nome com erros comuns de grafia ou imprecisões lexicais, mas que seja relevante para buscas dos usuários. Deve ficar oculto da interfaz pública.""",
        meaning=SKOS["hiddenLabel"],
    )
    indexing = PermissibleValue(
        text="indexing",
        description="""Nome, termo ou identificador a ser usado em indexação, por exemplo removendo artigos ou partículas iniciais, invertendo a ordem do nome e do sobrenome, etc.""",
        meaning=TERM["lido00961"],
    )
    preferred = PermissibleValue(
        text="preferred",
        description="""O nome, termo ou título preferencial. Normalmente não usaremos esta opção pois o campo `title` já contempla a opção preferencial.""",
        meaning=SKOS["prefLabel"],
    )

    _defn = EnumDefinition(
        name="LabelType",
        description="""No SKOS, caracteriza se cada termo deve ser considerado preferencial ou alternativo, usado para indexação, oculto da visualização (usado apenas para buscas), etc.""",
    )


class LargerContextType(EnumDefinitionImpl):
    """
    Tipos de relações entre partes e todo previstas no vocabulário controlado
    do LIDO. Inclui as categorias de relações hierárquicas e de relações
    associativas de parte ao todo.

    Ver <http://terminology.lido-schema.org/relatedWorkRelType>
    """

    physical_part_of = PermissibleValue(
        text="physical_part_of",
        title="fisicamente contido em",
        description="""Usar quando um objeto físico fizer parte integrante de um objeto ou complexo físico maior. Se o conjunto mais amplo for um construto interpretativo, usar a relação `has_borader_conceptual_context`.""",
        meaning=TERM["lido00255"],
    )
    conceptual_part_of = PermissibleValue(
        text="conceptual_part_of",
        title="parte conceitual de",
        description="""Usar quando um objeto intelectual for parte de uma entidade conceitual maior ou mais ampla.""",
        meaning=TERM["lido00572"],
    )
    has_borader_conceptual_context = PermissibleValue(
        text="has_borader_conceptual_context",
        title="tem contexto conceitual mais amplo",
        description="""Usar quando um objeto físico for incluído segundo critérios interpretativos num conjunto conceitual mais amplo. Se o conjunto mais amplo for uma extensão física que compreende inequivocamente o objeto, usar a relação `physical_part_of`.""",
        meaning=TERM["lido00575"],
    )
    example_of = PermissibleValue(
        text="example_of",
        title="exemplar de",
        description="""Usar quando o objeto construído é a manifestação física de um conteúdo intelectual, podendo abarcar desde instâncias específicas de um projeto seriado (por exemplo, um exemplar das casas da SHIS — Sociedade de Habitações de Interesse Social — produzidas em Brasília a partir de 1969) até a realização edificada de um programa teórico específico (por exemplo, a Cité Radieuse de Marselha como exemplo da unité d'habitation de Le Corbusier).
Vinculações teóricas ou conceituais com maior distância interpretativa (por exemplo, o Jardim América como exemplar de cidade–jardim) devem ser cadastradas no grupo `subject`.""",
        meaning=TERM["lido00627"],
    )
    has_arch_context = PermissibleValue(
        text="has_arch_context",
        title="tem como contexto arquitetônico",
        description="""O objeto em causa foi concebido para integrar ou está situado no referido conjunto edificado, ou integra o contexto funcional deste.""",
        meaning=TERM["lido00616"],
    )
    had_arch_context = PermissibleValue(
        text="had_arch_context",
        title="tinha como contexto arquitetônico",
        description="""O objeto em causa foi concebido para integrar ou esteve situado no referido conjunto edificado, mas não tem mais esse contexto por ter sido trasladado ou removido, ou porque o contexto foi destruído ou descaracterizado.""",
        meaning=TERM["lido01051"],
    )
    in_conceptual_whole_with = PermissibleValue(
        text="in_conceptual_whole_with",
        title="pertence ao mesmo contexto conceitual que",
        description="""Relação simétrica entre dois objetos que pertencem ao mesmo contexto conceitual. Usar apenas nos casos em que o conjunto conceitual maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.""",
        meaning=TERM["lido00578"],
    )
    in_physical_whole_with = PermissibleValue(
        text="in_physical_whole_with",
        title="pertence ao mesmo contexto material que",
        description="""Relação simétrica entre dois objetos que pertencem ao mesmo contexto material ou espacial. Usar apenas nos casos em que o conjunto arquitetônico maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.""",
        meaning=TERM["lido00577"],
    )
    was_part_of_whole_with = PermissibleValue(
        text="was_part_of_whole_with",
        title="pertenceu ao mesmo contexto que",
        description="""Relação simétrica entre dois objetos que pertenceram ao mesmo contexto conceitual, material ou espacial, mas já não pertencem devido a remoção, traslado, destruição ou reclassificação. Usar apenas nos casos em que o conjunto maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.""",
        meaning=TERM["lido01059"],
    )
    was_antedated = PermissibleValue(
        text="was_antedated",
        title="foi precedido no mesmo sítio por",
        meaning=TERM["lido01189"],
    )
    is_part_of = PermissibleValue(
        text="is_part_of",
        title="faz parte de",
        description="""Relação genérica entre parte e todo. Sempre que possível, usar os tipos de relação mais específicos.""",
        meaning=TERM["lido00574"],
    )
    formerly_part_of = PermissibleValue(
        text="formerly_part_of",
        title="anteriormente parte de",
        description="""O objeto físico em questão era anteriormente compreendido num conjunto edificado maior que não mais existe, seja porque o conjunto foi parcialmente demolido ou descaracterizado, ou porque suas outras partes foram trasladadas ou removidas.""",
        meaning=TERM["lido01085"],
    )
    is_was_part_of = PermissibleValue(
        text="is_was_part_of",
        title="parte de",
        description="""O objeto faz ou fazia parte de um conjunto físico maior, mas não é possível determinar se esse conjunto ainda existe ou não.""",
        meaning=TERM["lido01088"],
    )

    _defn = EnumDefinition(
        name="LargerContextType",
        description="""Tipos de relações entre partes e todo previstas no vocabulário controlado
do LIDO. Inclui as categorias de relações hierárquicas e de relações
associativas de parte ao todo.

Ver <http://terminology.lido-schema.org/relatedWorkRelType>""",
    )


class MaterialTechType(EnumDefinitionImpl):
    """
    A materialidade e as técnicas de produção ou intervenção na edificação devem ser categorizadas segundo esta
    classificação.
    """

    material = PermissibleValue(text="material", meaning=TERM["lido00132"])
    medium = PermissibleValue(text="medium", meaning=TERM["lido00513"])
    support = PermissibleValue(text="support", meaning=TERM["lido00514"])
    color_name = PermissibleValue(text="color_name", meaning=TERM["lido00479"])
    implement = PermissibleValue(text="implement", meaning=TERM["lido00248"])
    technique = PermissibleValue(text="technique", meaning=TERM["lido00131"])
    watermark = PermissibleValue(text="watermark", meaning=TERM["lido00427"])
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="MaterialTechType",
        description="""A materialidade e as técnicas de produção ou intervenção na edificação devem ser categorizadas segundo esta classificação.""",
    )


class MeasurementQualifier(EnumDefinitionImpl):
    """
    Qualifica a confiabilidade das medidas aferidas.
    """

    interpreted = PermissibleValue(
        text="interpreted",
        title="interpretativa",
        description="Metrologia interpretativa ou citação textual.",
    )
    estimated = PermissibleValue(
        text="estimated",
        title="estimativa visual",
        description="""Estimativa obtida por comparação com uma escala gráfica, com medidas adjacentes conhecidas, ou por caminhamento, partes do corpo, etc.""",
    )
    derived = PermissibleValue(
        text="derived",
        title="extrapolada",
        description="Extrapolado de um desenho ou modelo.",
    )
    measured = PermissibleValue(
        text="measured",
        title="medida no local",
        description="""Medida obtida no local por meio de instrumentos manuais ou eletrônicos (trena, teodolito, etc.).""",
    )
    scanned = PermissibleValue(
        text="scanned",
        title="escaneada digitalmente",
        description="""Medida extraída de um escaneamento a laser de alta precisão ou de uma estação topográfica digital.""",
    )

    _defn = EnumDefinition(
        name="MeasurementQualifier",
        description="""Qualifica a confiabilidade das medidas aferidas.""",
    )


class MeasurementType(EnumDefinitionImpl):
    """
    The type attribute qualifies whether the measurements given are features of the object proper or object
    requirements for handling the object, for instance, the maximum temperature variation.
    """

    proper = PermissibleValue(text="proper", meaning=TERM["lido00927"])
    requirement = PermissibleValue(text="requirement", meaning=TERM["lido00923"])

    _defn = EnumDefinition(
        name="MeasurementType",
        description="""The type attribute qualifies whether the measurements given are features of the object proper or object requirements for handling the object, for instance, the maximum temperature variation.""",
    )


class ReferenceType(EnumDefinitionImpl):
    """
    Tipos de referências a objetos externos previstos no LIDO.
    """

    uri = PermissibleValue(text="uri", title="URI", meaning=TERM["lido00099"])
    iri = PermissibleValue(text="iri", title="IRI", meaning=TERM["lido00510"])
    local = PermissibleValue(
        text="local", title="Identificador local", meaning=TERM["lido00100"]
    )

    _defn = EnumDefinition(
        name="ReferenceType",
        description="""Tipos de referências a objetos externos previstos no LIDO.""",
    )


class RelatedWorkRelType(EnumDefinitionImpl):
    """
    Relações associativas entre objetos físicos ou criações intelectuais,
    definidas segundo o vocabulário do LIDO.
    Compreende as relações associativas, exceto aquelas de partes com o todo.

    Ver <http://terminology.lido-schema.org/relatedWorkRelType>
    """

    documentedIn = PermissibleValue(
        text="documentedIn",
        title="documentado em",
        description="""A obra descrita na ficha está documentada, discutida ou descrita na mídia relacionada, que em geral será um texto.""",
        meaning=TERM["lido00617"],
    )
    complements = PermissibleValue(
        text="complements",
        title="complementa",
        description="""Relação entre obras criadas independentemente uma da outra, mas que mais tarde passaram a ser consideradas ou usadas conjuntamente.""",
        meaning=TERM["lido00580"],
    )
    complemented = PermissibleValue(
        text="complemented",
        title="complementava",
        description="""Relação entre obras criadas independentemente uma da outra, mas que mais tarde passaram a ser consideradas ou usadas conjuntamente, sendo essa associação posteriormente desfeita.""",
        meaning=TERM["lido01095"],
    )
    derivedFrom = PermissibleValue(
        text="derivedFrom",
        title="derivado de",
        description="""A obra descrita é derivada ou sensivelmente influenciada pelo objeto relacionado.
Preferir outras expressões de relação mais específicas sempre que possível. A relação `derivedFrom` deve ser reservada para casos em que a relação seja de variações e influências. Essas relações devem ser fundamentadas em interpretação bibliográfica.""",
        meaning=TERM["lido00603"],
    )
    positionedNear = PermissibleValue(
        text="positionedNear",
        title="próximo a",
        description="""Relação simétrica entre dois objetos situados em proximidade espacial, quando esta proximidade for significativa por razões compositivas, históricas ou funcionais.""",
        meaning=TERM["lido01136"],
    )

    _defn = EnumDefinition(
        name="RelatedWorkRelType",
        description="""Relações associativas entre objetos físicos ou criações intelectuais,
definidas segundo o vocabulário do LIDO.
Compreende as relações associativas, exceto aquelas de partes com o todo.

Ver <http://terminology.lido-schema.org/relatedWorkRelType>""",
    )


class ResourceType(EnumDefinitionImpl):
    """
    Relações associativas entre objetos físicos ou criações intelectuais, definidas segundo o vocabulário do LIDO.
    Compreende as relações de documentação técnica das edificações.
    Ver <http://terminology.lido-schema.org/relatedWorkRelType>
    """

    architecturalSurvey = PermissibleValue(text="architecturalSurvey")
    planFor = PermissibleValue(text="planFor")

    _defn = EnumDefinition(
        name="ResourceType",
        description="""Relações associativas entre objetos físicos ou criações intelectuais, definidas segundo o vocabulário do LIDO. Compreende as relações de documentação técnica das edificações.
Ver <http://terminology.lido-schema.org/relatedWorkRelType>""",
    )


class RepositoryType(EnumDefinitionImpl):
    """
    Type of repository or legal body.
    """

    corporate = PermissibleValue(text="corporate", title="institucional")
    geographic = PermissibleValue(text="geographic", title="geográfico")
    personal = PermissibleValue(text="personal", title="individual")
    other = PermissibleValue(text="other", title="outro")

    _defn = EnumDefinition(
        name="RepositoryType",
        description="Type of repository or legal body.",
    )


class RightsType(EnumDefinitionImpl):
    """
    LIDO expressions for rights types.
    """

    generic = PermissibleValue(text="generic", meaning=TERM["lido00920"])
    specific = PermissibleValue(text="specific", meaning=TERM["lido00921"])

    _defn = EnumDefinition(
        name="RightsType",
        description="LIDO expressions for rights types.",
    )


class RoleType(EnumDefinitionImpl):
    """
    Contribuições de um agente a um evento.
    """

    author = PermissibleValue(text="author", meaning=VRA["author"])
    builder = PermissibleValue(text="builder", meaning=VRA["builder"])
    collector = PermissibleValue(text="collector", meaning=VRA["collector"])
    commissioner = PermissibleValue(text="commissioner", meaning=VRA["commissioner"])
    composer = PermissibleValue(text="composer", meaning=VRA["composer"])
    contractor = PermissibleValue(text="contractor", meaning=VRA["contractor"])
    creator = PermissibleValue(text="creator", meaning=VRA["creator"])
    dealer = PermissibleValue(text="dealer", meaning=VRA["dealer"])
    decorator = PermissibleValue(text="decorator", meaning=VRA["decorator"])
    designer = PermissibleValue(text="designer", meaning=VRA["designer"])
    developer = PermissibleValue(text="developer", meaning=VRA["developer"])
    director = PermissibleValue(text="director", meaning=VRA["director"])
    donator = PermissibleValue(text="donator", meaning=VRA["donator"])
    drafter = PermissibleValue(text="drafter", meaning=VRA["drafter"])
    drawer = PermissibleValue(text="drawer", meaning=VRA["drawer"])
    editor = PermissibleValue(text="editor", meaning=VRA["editor"])
    engineer = PermissibleValue(text="engineer", meaning=VRA["engineer"])
    financier = PermissibleValue(text="financier", meaning=VRA["financier"])
    formerOwner = PermissibleValue(text="formerOwner", meaning=VRA["formerOwner"])
    manufacturer = PermissibleValue(text="manufacturer", meaning=VRA["manufacturer"])
    owner = PermissibleValue(text="owner", meaning=VRA["owner"])
    painter = PermissibleValue(text="painter", meaning=VRA["painter"])
    partnerInSetWith = PermissibleValue(
        text="partnerInSetWith", meaning=VRA["partnerInSetWith"]
    )
    performer = PermissibleValue(text="performer", meaning=VRA["performer"])
    photographer = PermissibleValue(text="photographer", meaning=VRA["photographer"])
    printer = PermissibleValue(text="printer", meaning=VRA["printer"])
    producer = PermissibleValue(text="producer", meaning=VRA["producer"])
    programmer = PermissibleValue(text="programmer", meaning=VRA["programmer"])
    restorer = PermissibleValue(text="restorer", meaning=VRA["restorer"])
    writer = PermissibleValue(text="writer", meaning=VRA["writer"])

    _defn = EnumDefinition(
        name="RoleType",
        description="Contribuições de um agente a um evento.",
    )


class SkosMappingRelation(EnumDefinitionImpl):
    """
    SKOS mapping properties.
    """

    close = PermissibleValue(text="close", meaning=SKOS["closeMatch"])
    exact = PermissibleValue(text="exact", meaning=SKOS["exactMatch"])
    broad = PermissibleValue(text="broad", meaning=SKOS["broadMatch"])
    narrow = PermissibleValue(text="narrow", meaning=SKOS["narrowMatch"])
    related = PermissibleValue(text="related", meaning=SKOS["relatedMatch"])

    _defn = EnumDefinition(
        name="SkosMappingRelation",
        description="SKOS mapping properties.",
    )


class SkosBroaderRelation(EnumDefinitionImpl):
    """
    SKOS-THES broader relation type.
    """

    broader = PermissibleValue(text="broader", meaning=SKOS["broader"])
    transitive = PermissibleValue(text="transitive", meaning=SKOS["broaderTransitive"])
    generic = PermissibleValue(text="generic", meaning=SKOS["broaderGeneric"])
    instantial = PermissibleValue(text="instantial", meaning=SKOS["broaderInstantial"])
    partitive = PermissibleValue(text="partitive", meaning=SKOS["broaderPartitive"])

    _defn = EnumDefinition(
        name="SkosBroaderRelation",
        description="SKOS-THES broader relation type.",
    )


class SkosNarrowerRelation(EnumDefinitionImpl):
    """
    SKOS-THES narrower relation type.
    """

    broader = PermissibleValue(text="broader", meaning=SKOS["narrower"])
    transitive = PermissibleValue(text="transitive", meaning=SKOS["narrowerTransitive"])
    generic = PermissibleValue(text="generic", meaning=SKOS["narrowerGeneric"])
    instantial = PermissibleValue(text="instantial", meaning=SKOS["narrowerInstantial"])
    partitive = PermissibleValue(text="partitive", meaning=SKOS["narrowerPartitive"])

    _defn = EnumDefinition(
        name="SkosNarrowerRelation",
        description="SKOS-THES narrower relation type.",
    )


class TitleType(EnumDefinitionImpl):
    """
    VRA Core title types.
    """

    brandName = PermissibleValue(text="brandName")
    cited = PermissibleValue(text="cited")
    creator = PermissibleValue(text="creator")
    descriptive = PermissibleValue(text="descriptive")
    former = PermissibleValue(text="former")
    inscribed = PermissibleValue(text="inscribed")
    owner = PermissibleValue(text="owner")
    popular = PermissibleValue(text="popular")
    repository = PermissibleValue(text="repository")
    translated = PermissibleValue(text="translated")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="TitleType",
        description="VRA Core title types.",
    )


class SubjectType(EnumDefinitionImpl):
    """
    The type attribute indicates the kind of subject information, whether it is, for instance, a description of a
    generic subject, an identification of a named individual, or an interpretation of the theme.
    Note that "Iconclass notations" are distinguished from other index terms for subject type in order to consider the
    impact of the type of indexing vocabulary with respect to information retrieval facilities.
    """

    descriptive = PermissibleValue(text="descriptive", meaning=TERM["lido00525"])
    iconographic = PermissibleValue(text="iconographic", meaning=TERM["lido00745"])
    concept = PermissibleValue(text="concept", meaning=TERM["lido00524"])
    other = PermissibleValue(text="other", meaning=TERM["lido00136"])

    _defn = EnumDefinition(
        name="SubjectType",
        description="""The type attribute indicates the kind of subject information, whether it is, for instance, a description of a generic subject, an identification of a named individual, or an interpretation of the theme.
Note that \"Iconclass notations\" are distinguished from other index terms for subject type in order to consider the impact of the type of indexing vocabulary with respect to information retrieval facilities.""",
    )


class FeatureClassEnum(EnumDefinitionImpl):
    A = PermissibleValue(
        text="A", title="administrativo", description="country, state, region,..."
    )
    H = PermissibleValue(text="H", title="hidrografia", description="stream, lake, ...")
    L = PermissibleValue(text="L", title="paisagem", description="parks, area, ...")
    P = PermissibleValue(text="P", title="povoações", description="city, village,...")
    R = PermissibleValue(text="R", title="estradas", description="road, railroad")
    S = PermissibleValue(
        text="S", title="construções", description="spot, building, farm"
    )
    T = PermissibleValue(
        text="T", title="topografia", description="mountain,hill,rock,..."
    )
    U = PermissibleValue(text="U", title="batimetria", description="undersea")
    V = PermissibleValue(text="V", title="vegetação", description="forest,heath,...")

    _defn = EnumDefinition(
        name="FeatureClassEnum",
    )


class FeatureCodeEnum(EnumDefinitionImpl):
    ADM1 = PermissibleValue(
        text="ADM1",
        title="first-order administrative division",
        description="a primary administrative division of a country, such as a state in the United States",
    )
    ADM1H = PermissibleValue(
        text="ADM1H",
        title="historical first-order administrative division",
        description="a former first-order administrative division",
    )
    ADM2 = PermissibleValue(
        text="ADM2",
        title="second-order administrative division",
        description="a subdivision of a first-order administrative division",
    )
    ADM2H = PermissibleValue(
        text="ADM2H",
        title="historical second-order administrative division",
        description="a former second-order administrative division",
    )
    ADM3 = PermissibleValue(
        text="ADM3",
        title="third-order administrative division",
        description="a subdivision of a second-order administrative division",
    )
    ADM3H = PermissibleValue(
        text="ADM3H",
        title="historical third-order administrative division",
        description="a former third-order administrative division",
    )
    ADM4 = PermissibleValue(
        text="ADM4",
        title="fourth-order administrative division",
        description="a subdivision of a third-order administrative division",
    )
    ADM4H = PermissibleValue(
        text="ADM4H",
        title="historical fourth-order administrative division",
        description="a former fourth-order administrative division",
    )
    ADM5 = PermissibleValue(
        text="ADM5",
        title="fifth-order administrative division",
        description="a subdivision of a fourth-order administrative division",
    )
    ADM5H = PermissibleValue(
        text="ADM5H",
        title="historical fifth-order administrative division",
        description="a former fifth-order administrative division",
    )
    ADMD = PermissibleValue(
        text="ADMD",
        title="administrative division",
        description="an administrative division of a country, undifferentiated as to administrative level",
    )
    ADMDH = PermissibleValue(
        text="ADMDH",
        title="historical administrative division",
        description="""a former administrative division of a political entity, undifferentiated as to administrative level""",
    )
    ADMS = PermissibleValue(
        text="ADMS", title="school district", description="school district"
    )
    LTER = PermissibleValue(
        text="LTER",
        title="leased area",
        description="a tract of land leased to another country, usually for military installations",
    )
    PCL = PermissibleValue(text="PCL", title="political entity")
    PCLD = PermissibleValue(text="PCLD", title="dependent political entity")
    PCLF = PermissibleValue(text="PCLF", title="freely associated state")
    PCLH = PermissibleValue(
        text="PCLH",
        title="historical political entity",
        description="a former political entity",
    )
    PCLI = PermissibleValue(text="PCLI", title="independent political entity")
    PCLIX = PermissibleValue(
        text="PCLIX", title="section of independent political entity"
    )
    PCLS = PermissibleValue(text="PCLS", title="semi-independent political entity")
    PRSH = PermissibleValue(
        text="PRSH", title="parish", description="an ecclesiastical district"
    )
    TERR = PermissibleValue(text="TERR", title="territory")
    ZN = PermissibleValue(text="ZN", title="zone")
    ZNB = PermissibleValue(
        text="ZNB",
        title="buffer zone",
        description="""a zone recognized as a buffer between two nations in which military presence is minimal or absent""",
    )
    AIRS = PermissibleValue(
        text="AIRS",
        title="seaplane landing area",
        description="a place on a waterbody where floatplanes land and take off",
    )
    ANCH = PermissibleValue(
        text="ANCH", title="anchorage", description="an area where vessels may anchor"
    )
    BAY = PermissibleValue(
        text="BAY",
        title="bay",
        description="""a coastal indentation between two capes or headlands, larger than a cove but smaller than a gulf""",
    )
    BAYS = PermissibleValue(
        text="BAYS",
        title="bays",
        description="""coastal indentations between two capes or headlands, larger than a cove but smaller than a gulf""",
    )
    BGHT = PermissibleValue(
        text="BGHT",
        title="bight(s)",
        description="an open body of water forming a slight recession in a coastline",
    )
    BNK = PermissibleValue(
        text="BNK",
        title="bank(s)",
        description="""an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for most surface navigation""",
    )
    BNKR = PermissibleValue(
        text="BNKR",
        title="stream bank",
        description="a sloping margin of a stream channel which normally confines the stream to its channel on land",
    )
    BNKX = PermissibleValue(text="BNKX", title="section of bank")
    BOG = PermissibleValue(
        text="BOG",
        title="bog(s)",
        description="a wetland characterized by peat forming sphagnum moss, sedge, and other acid-water plants",
    )
    CAPG = PermissibleValue(
        text="CAPG",
        title="icecap",
        description="""a dome-shaped mass of glacial ice covering an area of mountain summits or other high lands; smaller than an ice sheet""",
    )
    CHN = PermissibleValue(
        text="CHN",
        title="channel",
        description="the deepest part of a stream, bay, lagoon, or strait, through which the main current flows",
    )
    CHNL = PermissibleValue(
        text="CHNL",
        title="lake channel(s)",
        description="that part of a lake having water deep enough for navigation between islands, shoals, etc.",
    )
    CHNM = PermissibleValue(
        text="CHNM",
        title="marine channel",
        description="that part of a body of water deep enough for navigation through an area otherwise not suitable",
    )
    CHNN = PermissibleValue(
        text="CHNN",
        title="navigation channel",
        description="a buoyed channel of sufficient depth for the safe navigation of vessels",
    )
    CNFL = PermissibleValue(
        text="CNFL",
        title="confluence",
        description="a place where two or more streams or intermittent streams flow together",
    )
    CNL = PermissibleValue(
        text="CNL", title="canal", description="an artificial watercourse"
    )
    CNLA = PermissibleValue(
        text="CNLA", title="aqueduct", description="a conduit used to carry water"
    )
    CNLB = PermissibleValue(
        text="CNLB",
        title="canal bend",
        description="a conspicuously curved or bent section of a canal",
    )
    CNLD = PermissibleValue(
        text="CNLD",
        title="drainage canal",
        description="an artificial waterway carrying water away from a wetland or from drainage ditches",
    )
    CNLI = PermissibleValue(
        text="CNLI",
        title="irrigation canal",
        description="a canal which serves as a main conduit for irrigation water",
    )
    CNLN = PermissibleValue(
        text="CNLN",
        title="navigation canal(s)",
        description="a watercourse constructed for navigation of vessels",
    )
    CNLQ = PermissibleValue(text="CNLQ", title="abandoned canal")
    CNLSB = PermissibleValue(
        text="CNLSB",
        title="underground irrigation canal(s)",
        description="a gently inclined underground tunnel bringing water for irrigation from aquifers",
    )
    CNLX = PermissibleValue(text="CNLX", title="section of canal")
    COVE = PermissibleValue(
        text="COVE",
        title="cove(s)",
        description="a small coastal indentation, smaller than a bay",
    )
    CRKT = PermissibleValue(
        text="CRKT",
        title="tidal creek(s)",
        description="a meandering channel in a coastal wetland subject to bi-directional tidal currents",
    )
    CRNT = PermissibleValue(
        text="CRNT",
        title="current",
        description="a horizontal flow of water in a given direction with uniform velocity",
    )
    CUTF = PermissibleValue(
        text="CUTF",
        title="cutoff",
        description="a channel formed as a result of a stream cutting through a meander neck",
    )
    DCK = PermissibleValue(
        text="DCK",
        title="dock(s)",
        description="a waterway between two piers, or cut into the land for the berthing of ships",
    )
    DCKB = PermissibleValue(
        text="DCKB",
        title="docking basin",
        description="a part of a harbor where ships dock",
    )
    DOMG = PermissibleValue(
        text="DOMG",
        title="icecap dome",
        description="a comparatively elevated area on an icecap",
    )
    DPRG = PermissibleValue(
        text="DPRG",
        title="icecap depression",
        description="a comparatively depressed area on an icecap",
    )
    DTCH = PermissibleValue(
        text="DTCH",
        title="ditch",
        description="a small artificial watercourse dug for draining or irrigating the land",
    )
    DTCHD = PermissibleValue(
        text="DTCHD",
        title="drainage ditch",
        description="a ditch which serves to drain the land",
    )
    DTCHI = PermissibleValue(
        text="DTCHI",
        title="irrigation ditch",
        description="a ditch which serves to distribute irrigation water",
    )
    DTCHM = PermissibleValue(
        text="DTCHM",
        title="ditch mouth(s)",
        description="an area where a drainage ditch enters a lagoon, lake or bay",
    )
    ESTY = PermissibleValue(
        text="ESTY",
        title="estuary",
        description="""a funnel-shaped stream mouth or embayment where fresh water mixes with sea water under tidal influences""",
    )
    FISH = PermissibleValue(
        text="FISH",
        title="fishing area",
        description="a fishing ground, bank or area where fishermen go to catch fish",
    )
    FJD = PermissibleValue(
        text="FJD",
        title="fjord",
        description="""a long, narrow, steep-walled, deep-water arm of the sea at high latitudes, usually along mountainous coasts""",
    )
    FJDS = PermissibleValue(
        text="FJDS",
        title="fjords",
        description="""long, narrow, steep-walled, deep-water arms of the sea at high latitudes, usually along mountainous coasts""",
    )
    FLLS = PermissibleValue(
        text="FLLS",
        title="waterfall(s)",
        description="a perpendicular or very steep descent of the water of a stream",
    )
    FLLSX = PermissibleValue(text="FLLSX", title="section of waterfall(s)")
    FLTM = PermissibleValue(
        text="FLTM",
        title="mud flat(s)",
        description="a relatively level area of mud either between high and low tide lines, or subject to flooding",
    )
    FLTT = PermissibleValue(
        text="FLTT",
        title="tidal flat(s)",
        description="""a large flat area of mud or sand attached to the shore and alternately covered and uncovered by the tide""",
    )
    GLCR = PermissibleValue(
        text="GLCR",
        title="glacier(s)",
        description="""a mass of ice, usually at high latitudes or high elevations, with sufficient thickness to flow away from the source area in lobes, tongues, or masses""",
    )
    GULF = PermissibleValue(
        text="GULF",
        title="gulf",
        description="a large recess in the coastline, larger than a bay",
    )
    GYSR = PermissibleValue(
        text="GYSR",
        title="geyser",
        description="a type of hot spring with intermittent eruptions of jets of hot water and steam",
    )
    HBR = PermissibleValue(
        text="HBR",
        title="harbor(s)",
        description="""a haven or space of deep water so sheltered by the adjacent land as to afford a safe anchorage for ships""",
    )
    HBRX = PermissibleValue(text="HBRX", title="section of harbor")
    INLT = PermissibleValue(
        text="INLT",
        title="inlet",
        description="""a narrow waterway extending into the land, or connecting a bay or lagoon with a larger body of water""",
    )
    INLTQ = PermissibleValue(
        text="INLTQ",
        title="former inlet",
        description="an inlet which has been filled in, or blocked by deposits",
    )
    LBED = PermissibleValue(
        text="LBED",
        title="lake bed(s)",
        description="a dried up or drained area of a former lake",
    )
    LGN = PermissibleValue(
        text="LGN",
        title="lagoon",
        description="""a shallow coastal waterbody, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature""",
    )
    LGNS = PermissibleValue(
        text="LGNS",
        title="lagoons",
        description="""shallow coastal waterbodies, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature""",
    )
    LGNX = PermissibleValue(text="LGNX", title="section of lagoon")
    LK = PermissibleValue(
        text="LK", title="lake", description="a large inland body of standing water"
    )
    LKC = PermissibleValue(
        text="LKC", title="crater lake", description="a lake in a crater or caldera"
    )
    LKI = PermissibleValue(text="LKI", title="intermittent lake")
    LKN = PermissibleValue(
        text="LKN",
        title="salt lake",
        description="an inland body of salt water with no outlet",
    )
    LKNI = PermissibleValue(text="LKNI", title="intermittent salt lake")
    LKO = PermissibleValue(
        text="LKO",
        title="oxbow lake",
        description="a crescent-shaped lake commonly found adjacent to meandering streams",
    )
    LKOI = PermissibleValue(text="LKOI", title="intermittent oxbow lake")
    LKS = PermissibleValue(
        text="LKS", title="lakes", description="large inland bodies of standing water"
    )
    LKSB = PermissibleValue(
        text="LKSB",
        title="underground lake",
        description="a standing body of water in a cave",
    )
    LKSC = PermissibleValue(
        text="LKSC", title="crater lakes", description="lakes in a crater or caldera"
    )
    LKSI = PermissibleValue(text="LKSI", title="intermittent lakes")
    LKSN = PermissibleValue(
        text="LKSN",
        title="salt lakes",
        description="inland bodies of salt water with no outlet",
    )
    LKSNI = PermissibleValue(text="LKSNI", title="intermittent salt lakes")
    LKX = PermissibleValue(text="LKX", title="section of lake")
    MFGN = PermissibleValue(
        text="MFGN",
        title="salt evaporation ponds",
        description="diked salt ponds used in the production of solar evaporated salt",
    )
    MGV = PermissibleValue(
        text="MGV",
        title="mangrove swamp",
        description="a tropical tidal mud flat characterized by mangrove vegetation",
    )
    MOOR = PermissibleValue(
        text="MOOR",
        title="moor(s)",
        description="an area of open ground overlaid with wet peaty soils",
    )
    MRSH = PermissibleValue(
        text="MRSH",
        title="marsh(es)",
        description="a wetland dominated by grass-like vegetation",
    )
    MRSHN = PermissibleValue(
        text="MRSHN",
        title="salt marsh",
        description="""a flat area, subject to periodic salt water inundation, dominated by grassy salt-tolerant plants""",
    )
    NRWS = PermissibleValue(
        text="NRWS",
        title="narrows",
        description="a navigable narrow part of a bay, strait, river, etc.",
    )
    OCN = PermissibleValue(
        text="OCN",
        title="ocean",
        description="one of the major divisions of the vast expanse of salt water covering part of the earth",
    )
    OVF = PermissibleValue(
        text="OVF",
        title="overfalls",
        description="""an area of breaking waves caused by the meeting of currents or by waves moving against the current""",
    )
    PND = PermissibleValue(
        text="PND", title="pond", description="a small standing waterbody"
    )
    PNDI = PermissibleValue(text="PNDI", title="intermittent pond")
    PNDN = PermissibleValue(
        text="PNDN",
        title="salt pond",
        description="a small standing body of salt water often in a marsh or swamp, usually along a seacoast",
    )
    PNDNI = PermissibleValue(text="PNDNI", title="intermittent salt pond(s)")
    PNDS = PermissibleValue(
        text="PNDS", title="ponds", description="small standing waterbodies"
    )
    PNDSF = PermissibleValue(
        text="PNDSF",
        title="fishponds",
        description="ponds or enclosures in which fish are kept or raised",
    )
    PNDSI = PermissibleValue(text="PNDSI", title="intermittent ponds")
    PNDSN = PermissibleValue(
        text="PNDSN",
        title="salt ponds",
        description="small standing bodies of salt water often in a marsh or swamp, usually along a seacoast",
    )
    POOL = PermissibleValue(
        text="POOL",
        title="pool(s)",
        description="""a small and comparatively still, deep part of a larger body of water such as a stream or harbor; or a small body of standing water""",
    )
    POOLI = PermissibleValue(text="POOLI", title="intermittent pool")
    RCH = PermissibleValue(
        text="RCH",
        title="reach",
        description="a straight section of a navigable stream or channel between two bends",
    )
    RDGG = PermissibleValue(
        text="RDGG", title="icecap ridge", description="a linear elevation on an icecap"
    )
    RDST = PermissibleValue(
        text="RDST",
        title="roadstead",
        description="an open anchorage affording less protection than a harbor",
    )
    RF = PermissibleValue(
        text="RF",
        title="reef(s)",
        description="a surface-navigation hazard composed of consolidated material",
    )
    RFC = PermissibleValue(
        text="RFC",
        title="coral reef(s)",
        description="a surface-navigation hazard composed of coral",
    )
    RFX = PermissibleValue(text="RFX", title="section of reef")
    RPDS = PermissibleValue(
        text="RPDS",
        title="rapids",
        description="a turbulent section of a stream associated with a steep, irregular stream bed",
    )
    RSV = PermissibleValue(
        text="RSV", title="reservoir(s)", description="an artificial pond or lake"
    )
    RSVI = PermissibleValue(text="RSVI", title="intermittent reservoir")
    RSVT = PermissibleValue(
        text="RSVT",
        title="water tank",
        description="a contained pool or tank of water at, below, or above ground level",
    )
    RVN = PermissibleValue(
        text="RVN",
        title="ravine(s)",
        description="a small, narrow, deep, steep-sided stream channel, smaller than a gorge",
    )
    SBKH = PermissibleValue(
        text="SBKH",
        title="sabkha(s)",
        description="a salt flat or salt encrusted plain subject to periodic inundation from flooding or high tides",
    )
    SD = PermissibleValue(
        text="SD",
        title="sound",
        description="""a long arm of the sea forming a channel between the mainland and an island or islands; or connecting two larger bodies of water""",
    )
    SEA = PermissibleValue(
        text="SEA",
        title="sea",
        description="""a large body of salt water more or less confined by continuous land or chains of islands forming a subdivision of an ocean""",
    )
    SHOL = PermissibleValue(
        text="SHOL",
        title="shoal(s)",
        description="a surface-navigation hazard composed of unconsolidated material",
    )
    SILL = PermissibleValue(
        text="SILL",
        title="sill",
        description="""the low part of an underwater gap or saddle separating basins, including a similar feature at the mouth of a fjord""",
    )
    SPNG = PermissibleValue(
        text="SPNG",
        title="spring(s)",
        description="a place where ground water flows naturally out of the ground",
    )
    SPNS = PermissibleValue(
        text="SPNS",
        title="sulphur spring(s)",
        description="a place where sulphur ground water flows naturally out of the ground",
    )
    SPNT = PermissibleValue(
        text="SPNT",
        title="hot spring(s)",
        description="a place where hot ground water flows naturally out of the ground",
    )
    STM = PermissibleValue(
        text="STM",
        title="stream",
        description="a body of running water moving to a lower level in a channel on land",
    )
    STMA = PermissibleValue(
        text="STMA",
        title="anabranch",
        description="a diverging branch flowing out of a main stream and rejoining it downstream",
    )
    STMB = PermissibleValue(
        text="STMB",
        title="stream bend",
        description="a conspicuously curved or bent segment of a stream",
    )
    STMC = PermissibleValue(
        text="STMC",
        title="canalized stream",
        description="a stream that has been substantially ditched, diked, or straightened",
    )
    STMD = PermissibleValue(
        text="STMD",
        title="distributary(-ies)",
        description="a branch which flows away from the main stream, as in a delta or irrigation canal",
    )
    STMH = PermissibleValue(
        text="STMH",
        title="headwaters",
        description="the source and upper part of a stream, including the upper drainage basin",
    )
    STMI = PermissibleValue(text="STMI", title="intermittent stream")
    STMIX = PermissibleValue(text="STMIX", title="section of intermittent stream")
    STMM = PermissibleValue(
        text="STMM",
        title="stream mouth(s)",
        description="a place where a stream discharges into a lagoon, lake, or the sea",
    )
    STMQ = PermissibleValue(
        text="STMQ",
        title="abandoned watercourse",
        description="""a former stream or distributary no longer carrying flowing water, but still evident due to lakes, wetland, topographic or vegetation patterns""",
    )
    STMS = PermissibleValue(
        text="STMS",
        title="streams",
        description="bodies of running water moving to a lower level in a channel on land",
    )
    STMSB = PermissibleValue(
        text="STMSB",
        title="lost river",
        description="a surface stream that disappears into an underground channel, or dries up in an arid area",
    )
    STMX = PermissibleValue(text="STMX", title="section of stream")
    STRT = PermissibleValue(
        text="STRT",
        title="strait",
        description="""a relatively narrow waterway, usually narrower and less extensive than a sound, connecting two larger bodies of water""",
    )
    SWMP = PermissibleValue(
        text="SWMP", title="swamp", description="a wetland dominated by tree vegetation"
    )
    SYSI = PermissibleValue(
        text="SYSI",
        title="irrigation system",
        description="""a network of ditches and one or more of the following elements: water supply, reservoir, canal, pump, well, drain, etc.""",
    )
    TNLC = PermissibleValue(
        text="TNLC",
        title="canal tunnel",
        description="a tunnel through which a canal passes",
    )
    WAD = PermissibleValue(
        text="WAD",
        title="wadi",
        description="""a valley or ravine, bounded by relatively steep banks, which in the rainy season becomes a watercourse; found primarily in North Africa and the Middle East""",
    )
    WADB = PermissibleValue(
        text="WADB",
        title="wadi bend",
        description="a conspicuously curved or bent segment of a wadi",
    )
    WADJ = PermissibleValue(
        text="WADJ",
        title="wadi junction",
        description="a place where two or more wadies join",
    )
    WADM = PermissibleValue(
        text="WADM",
        title="wadi mouth",
        description="""the lower terminus of a wadi where it widens into an adjoining floodplain, depression, or waterbody""",
    )
    WADS = PermissibleValue(
        text="WADS",
        title="wadies",
        description="""valleys or ravines, bounded by relatively steep banks, which in the rainy season become watercourses; found primarily in North Africa and the Middle East""",
    )
    WADX = PermissibleValue(text="WADX", title="section of wadi")
    WHRL = PermissibleValue(
        text="WHRL",
        title="whirlpool",
        description="a turbulent, rotating movement of water in a stream",
    )
    WLL = PermissibleValue(
        text="WLL",
        title="well",
        description="""a cylindrical hole, pit, or tunnel drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface""",
    )
    WLLQ = PermissibleValue(text="WLLQ", title="abandoned well")
    WLLS = PermissibleValue(
        text="WLLS",
        title="wells",
        description="""cylindrical holes, pits, or tunnels drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface""",
    )
    WTLD = PermissibleValue(
        text="WTLD",
        title="wetland",
        description="an area subject to inundation, usually characterized by bog, marsh, or swamp vegetation",
    )
    WTLDI = PermissibleValue(text="WTLDI", title="intermittent wetland")
    WTRC = PermissibleValue(
        text="WTRC",
        title="watercourse",
        description="""a natural, well-defined channel produced by flowing water, or an artificial channel designed to carry flowing water""",
    )
    WTRH = PermissibleValue(
        text="WTRH",
        title="waterhole(s)",
        description="""a natural hole, hollow, or small depression that contains water, used by man and animals, especially in arid areas""",
    )
    AGRC = PermissibleValue(
        text="AGRC",
        title="agricultural colony",
        description="a tract of land set aside for agricultural settlement",
    )
    AMUS = PermissibleValue(
        text="AMUS",
        title="amusement park",
        description="""Amusement Park are theme parks, adventure parks offering entertainment, similar to funfairs but with a fix location""",
    )
    AREA = PermissibleValue(
        text="AREA",
        title="area",
        description="a tract of land without homogeneous character or boundaries",
    )
    BSND = PermissibleValue(
        text="BSND", title="drainage basin", description="an area drained by a stream"
    )
    BSNP = PermissibleValue(
        text="BSNP",
        title="petroleum basin",
        description="an area underlain by an oil-rich structural basin",
    )
    BTL = PermissibleValue(
        text="BTL",
        title="battlefield",
        description="a site of a land battle of historical importance",
    )
    CLG = PermissibleValue(
        text="CLG",
        title="clearing",
        description="an area in a forest with trees removed",
    )
    CMN = PermissibleValue(
        text="CMN", title="common", description="a park or pasture for community use"
    )
    CNS = PermissibleValue(
        text="CNS",
        title="concession area",
        description="a lease of land by a government for economic development, e.g., mining, forestry",
    )
    COLF = PermissibleValue(
        text="COLF",
        title="coalfield",
        description="a region in which coal deposits of possible economic value occur",
    )
    CONT = PermissibleValue(
        text="CONT",
        title="continent",
        description="continent: Europe, Africa, Asia, North America, South America, Oceania, Antarctica",
    )
    CST = PermissibleValue(
        text="CST",
        title="coast",
        description="a zone of variable width straddling the shoreline",
    )
    CTRB = PermissibleValue(
        text="CTRB",
        title="business center",
        description="a place where a number of businesses are located",
    )
    DEVH = PermissibleValue(
        text="DEVH",
        title="housing development",
        description="""a tract of land on which many houses of similar design are built according to a development plan""",
    )
    FLD = PermissibleValue(
        text="FLD", title="field(s)", description="an open as opposed to wooded area"
    )
    FLDI = PermissibleValue(
        text="FLDI",
        title="irrigated field(s)",
        description="a tract of level or terraced land which is irrigated",
    )
    GASF = PermissibleValue(
        text="GASF",
        title="gasfield",
        description="an area containing a subterranean store of natural gas of economic value",
    )
    GRAZ = PermissibleValue(
        text="GRAZ",
        title="grazing area",
        description="an area of grasses and shrubs used for grazing",
    )
    GVL = PermissibleValue(
        text="GVL", title="gravel area", description="an area covered with gravel"
    )
    INDS = PermissibleValue(
        text="INDS",
        title="industrial area",
        description="an area characterized by industrial activity",
    )
    LAND = PermissibleValue(
        text="LAND", title="arctic land", description="a tract of land in the Arctic"
    )
    LCTY = PermissibleValue(
        text="LCTY",
        title="locality",
        description="a minor area or place of unspecified or mixed character and indefinite boundaries",
    )
    MILB = PermissibleValue(
        text="MILB",
        title="military base",
        description="""a place used by an army or other armed service for storing arms and supplies, and for accommodating and training troops, a base from which operations can be initiated""",
    )
    MNA = PermissibleValue(
        text="MNA",
        title="mining area",
        description="an area of mine sites where minerals and ores are extracted",
    )
    MVA = PermissibleValue(
        text="MVA",
        title="maneuver area",
        description="a tract of land where military field exercises are carried out",
    )
    NVB = PermissibleValue(
        text="NVB",
        title="naval base",
        description="""an area used to store supplies, provide barracks for troops and naval personnel, a port for naval vessels, and from which operations are initiated""",
    )
    OAS = PermissibleValue(
        text="OAS",
        title="oasis(-es)",
        description="an area in a desert made productive by the availability of water",
    )
    OILF = PermissibleValue(
        text="OILF",
        title="oilfield",
        description="an area containing a subterranean store of petroleum of economic value",
    )
    PEAT = PermissibleValue(
        text="PEAT",
        title="peat cutting area",
        description="an area where peat is harvested",
    )
    PRK = PermissibleValue(
        text="PRK",
        title="park",
        description="an area, often of forested land, maintained as a place of beauty, or for recreation",
    )
    PRT = PermissibleValue(
        text="PRT",
        title="port",
        description="""a place provided with terminal and transfer facilities for loading and discharging waterborne cargo or passengers, usually located in a harbor""",
    )
    QCKS = PermissibleValue(
        text="QCKS",
        title="quicksand",
        description="""an area where loose sand with water moving through it may become unstable when heavy objects are placed at the surface, causing them to sink""",
    )
    RES = PermissibleValue(
        text="RES",
        title="reserve",
        description="a tract of public land reserved for future use or restricted as to use",
    )
    RESA = PermissibleValue(
        text="RESA",
        title="agricultural reserve",
        description="a tract of land reserved for agricultural reclamation and/or development",
    )
    RESF = PermissibleValue(
        text="RESF",
        title="forest reserve",
        description="a forested area set aside for preservation or controlled use",
    )
    RESH = PermissibleValue(
        text="RESH",
        title="hunting reserve",
        description="a tract of land used primarily for hunting",
    )
    RESN = PermissibleValue(
        text="RESN",
        title="nature reserve",
        description="an area reserved for the maintenance of a natural habitat",
    )
    RESP = PermissibleValue(
        text="RESP",
        title="palm tree reserve",
        description="an area of palm trees where use is controlled",
    )
    RESV = PermissibleValue(
        text="RESV",
        title="reservation",
        description="a tract of land set aside for aboriginal, tribal, or native populations",
    )
    RESW = PermissibleValue(
        text="RESW",
        title="wildlife reserve",
        description="a tract of public land reserved for the preservation of wildlife",
    )
    RGN = PermissibleValue(
        text="RGN",
        title="region",
        description="an area distinguished by one or more observable physical or cultural characteristics",
    )
    RGNE = PermissibleValue(
        text="RGNE",
        title="economic region",
        description="a region of a country established for economic development or for statistical purposes",
    )
    RGNH = PermissibleValue(
        text="RGNH",
        title="historical region",
        description="""a former historic area distinguished by one or more observable physical or cultural characteristics""",
    )
    RGNL = PermissibleValue(
        text="RGNL",
        title="lake region",
        description="a tract of land distinguished by numerous lakes",
    )
    RNGA = PermissibleValue(
        text="RNGA",
        title="artillery range",
        description="a tract of land used for artillery firing practice",
    )
    SALT = PermissibleValue(
        text="SALT",
        title="salt area",
        description="a shallow basin or flat where salt accumulates after periodic inundation",
    )
    SNOW = PermissibleValue(
        text="SNOW",
        title="snowfield",
        description="an area of permanent snow and ice forming the accumulation area of a glacier",
    )
    TRB = PermissibleValue(
        text="TRB",
        title="tribal area",
        description="a tract of land used by nomadic or other tribes",
    )
    PPL = PermissibleValue(
        text="PPL",
        title="populated place",
        description="a city, town, village, or other agglomeration of buildings where people live and work",
    )
    PPLA = PermissibleValue(
        text="PPLA",
        title="seat of a first-order administrative division",
        description="seat of a first-order administrative division (PPLC takes precedence over PPLA)",
    )
    PPLA2 = PermissibleValue(
        text="PPLA2", title="seat of a second-order administrative division"
    )
    PPLA3 = PermissibleValue(
        text="PPLA3", title="seat of a third-order administrative division"
    )
    PPLA4 = PermissibleValue(
        text="PPLA4", title="seat of a fourth-order administrative division"
    )
    PPLA5 = PermissibleValue(
        text="PPLA5", title="seat of a fifth-order administrative division"
    )
    PPLC = PermissibleValue(
        text="PPLC",
        title="capital of a political entity",
        description="capital of a political entity designated as an independent state",
    )
    PPLCD = PermissibleValue(
        text="PPLCD",
        title="capital of a dependency or special area",
        description="""capital or administrative center of a dependent political territory or area of special sovereignty""",
    )
    PPLCH = PermissibleValue(
        text="PPLCH",
        title="historical capital of a political entity",
        description="a former capital of a political entity",
    )
    PPLF = PermissibleValue(
        text="PPLF",
        title="farm village",
        description="a populated place where the population is largely engaged in agricultural activities",
    )
    PPLG = PermissibleValue(
        text="PPLG", title="seat of government of a political entity"
    )
    PPLH = PermissibleValue(
        text="PPLH",
        title="historical populated place",
        description="a populated place that no longer exists",
    )
    PPLL = PermissibleValue(
        text="PPLL",
        title="populated locality",
        description="an area similar to a locality but with a small group of dwellings or other buildings",
    )
    PPLQ = PermissibleValue(text="PPLQ", title="abandoned populated place")
    PPLR = PermissibleValue(
        text="PPLR",
        title="religious populated place",
        description="a populated place whose population is largely engaged in religious occupations",
    )
    PPLS = PermissibleValue(
        text="PPLS",
        title="populated places",
        description="cities, towns, villages, or other agglomerations of buildings where people live and work",
    )
    PPLW = PermissibleValue(
        text="PPLW",
        title="destroyed populated place",
        description="a village, town or city destroyed by a natural disaster, or by war",
    )
    PPLX = PermissibleValue(text="PPLX", title="section of populated place")
    STLMT = PermissibleValue(text="STLMT", title="israeli settlement")
    CSWY = PermissibleValue(
        text="CSWY",
        title="causeway",
        description="a raised roadway across wet ground or shallow water",
    )
    OILP = PermissibleValue(
        text="OILP",
        title="oil pipeline",
        description="a pipeline used for transporting oil",
    )
    PRMN = PermissibleValue(
        text="PRMN",
        title="promenade",
        description="a place for public walking, usually along a beach front",
    )
    PTGE = PermissibleValue(
        text="PTGE",
        title="portage",
        description="a place where boats, goods, etc., are carried overland between navigable waters",
    )
    RD = PermissibleValue(
        text="RD",
        title="road",
        description="an open way with improved surface for transportation of animals, people and vehicles",
    )
    RDA = PermissibleValue(
        text="RDA",
        title="ancient road",
        description="the remains of a road used by ancient cultures",
    )
    RDB = PermissibleValue(
        text="RDB",
        title="road bend",
        description="a conspicuously curved or bent section of a road",
    )
    RDCUT = PermissibleValue(
        text="RDCUT",
        title="road cut",
        description="an excavation cut through a hill or ridge for a road",
    )
    RDJCT = PermissibleValue(
        text="RDJCT",
        title="road junction",
        description="a place where two or more roads join",
    )
    RJCT = PermissibleValue(
        text="RJCT",
        title="railroad junction",
        description="a place where two or more railroad tracks join",
    )
    RR = PermissibleValue(
        text="RR",
        title="railroad",
        description="a permanent twin steel-rail track on which freight and passenger cars move long distances",
    )
    RRQ = PermissibleValue(text="RRQ", title="abandoned railroad")
    RTE = PermissibleValue(
        text="RTE", title="caravan route", description="the route taken by caravans"
    )
    RYD = PermissibleValue(
        text="RYD",
        title="railroad yard",
        description="a system of tracks used for the making up of trains, and switching and storing freight cars",
    )
    ST = PermissibleValue(
        text="ST", title="street", description="a paved urban thoroughfare"
    )
    STKR = PermissibleValue(
        text="STKR", title="stock route", description="a route taken by livestock herds"
    )
    TNL = PermissibleValue(
        text="TNL",
        title="tunnel",
        description="a subterranean passageway for transportation",
    )
    TNLN = PermissibleValue(
        text="TNLN",
        title="natural tunnel",
        description="a cave that is open at both ends",
    )
    TNLRD = PermissibleValue(
        text="TNLRD",
        title="road tunnel",
        description="a tunnel through which a road passes",
    )
    TNLRR = PermissibleValue(
        text="TNLRR",
        title="railroad tunnel",
        description="a tunnel through which a railroad passes",
    )
    TNLS = PermissibleValue(
        text="TNLS",
        title="tunnels",
        description="subterranean passageways for transportation",
    )
    TRL = PermissibleValue(
        text="TRL",
        title="trail",
        description="a path, track, or route used by pedestrians, animals, or off-road vehicles",
    )
    ADMF = PermissibleValue(
        text="ADMF",
        title="administrative facility",
        description="a government building",
    )
    AGRF = PermissibleValue(
        text="AGRF",
        title="agricultural facility",
        description="a building and/or tract of land used for improving agriculture",
    )
    AIRB = PermissibleValue(
        text="AIRB",
        title="airbase",
        description="""an area used to store supplies, provide barracks for air force personnel, hangars and runways for aircraft, and from which operations are initiated""",
    )
    AIRF = PermissibleValue(
        text="AIRF",
        title="airfield",
        description="""a place on land where aircraft land and take off; no facilities provided for the commercial handling of passengers and cargo""",
    )
    AIRH = PermissibleValue(
        text="AIRH",
        title="heliport",
        description="a place where helicopters land and take off",
    )
    AIRP = PermissibleValue(
        text="AIRP",
        title="airport",
        description="""a place where aircraft regularly land and take off, with runways, navigational aids, and major facilities for the commercial handling of passengers and cargo""",
    )
    AIRQ = PermissibleValue(text="AIRQ", title="abandoned airfield")
    AIRT = PermissibleValue(
        text="AIRT",
        title="terminal",
        description="airport facilities for the handling of freight and passengers",
    )
    AMTH = PermissibleValue(
        text="AMTH",
        title="amphitheater",
        description="an oval or circular structure with rising tiers of seats about a stage or open space",
    )
    ANS = PermissibleValue(
        text="ANS",
        title="archaeological/prehistoric site",
        description="a place where archeological remains, old structures, or cultural artifacts are located",
    )
    AQC = PermissibleValue(
        text="AQC",
        title="aquaculture facility",
        description="""facility or area for the cultivation of aquatic animals and plants, especially fish, shellfish, and seaweed, in natural or controlled marine or freshwater environments; underwater agriculture""",
    )
    ARCH = PermissibleValue(
        text="ARCH",
        title="arch",
        description="a natural or man-made structure in the form of an arch",
    )
    ARCHV = PermissibleValue(
        text="ARCHV",
        title="archive",
        description="a place or institution where documents are preserved",
    )
    ART = PermissibleValue(
        text="ART",
        title="piece of art",
        description="""a piece of art, like a sculpture, painting. In contrast to monument (MNMT) it is not commemorative.""",
    )
    ASTR = PermissibleValue(
        text="ASTR",
        title="astronomical station",
        description="a point on the earth whose position has been determined by observations of celestial bodies",
    )
    ASYL = PermissibleValue(
        text="ASYL",
        title="asylum",
        description="a facility where the insane are cared for and protected",
    )
    ATHF = PermissibleValue(
        text="ATHF",
        title="athletic field",
        description="a tract of land used for playing team sports, and athletic track and field events",
    )
    ATM = PermissibleValue(
        text="ATM",
        title="automatic teller machine",
        description="""An unattended electronic machine in a public place, connected to a data system and related equipment and activated by a bank customer to obtain cash withdrawals and other banking services.""",
    )
    BANK = PermissibleValue(
        text="BANK",
        title="bank",
        description="""A business establishment in which money is kept for saving or commercial purposes or is invested, supplied for loans, or exchanged.""",
    )
    BCN = PermissibleValue(
        text="BCN", title="beacon", description="a fixed artificial navigation mark"
    )
    BDG = PermissibleValue(
        text="BDG",
        title="bridge",
        description="""a structure erected across an obstacle such as a stream, road, etc., in order to carry roads, railroads, and pedestrians across""",
    )
    BDGQ = PermissibleValue(
        text="BDGQ",
        title="ruined bridge",
        description="a destroyed or decayed bridge which is no longer functional",
    )
    BLDA = PermissibleValue(
        text="BLDA",
        title="apartment building",
        description="a building containing several individual apartments",
    )
    BLDG = PermissibleValue(
        text="BLDG",
        title="building(s)",
        description="a structure built for permanent use, as a house, factory, etc.",
    )
    BLDO = PermissibleValue(
        text="BLDO",
        title="office building",
        description="commercial building where business and/or services are conducted",
    )
    BP = PermissibleValue(
        text="BP",
        title="boundary marker",
        description="a fixture marking a point along a boundary",
    )
    BRKS = PermissibleValue(
        text="BRKS",
        title="barracks",
        description="a building for lodging military personnel",
    )
    BRKW = PermissibleValue(
        text="BRKW",
        title="breakwater",
        description="a structure erected to break the force of waves at the entrance to a harbor or port",
    )
    BSTN = PermissibleValue(
        text="BSTN",
        title="baling station",
        description="a facility for baling agricultural products",
    )
    BTYD = PermissibleValue(
        text="BTYD",
        title="boatyard",
        description="a waterside facility for servicing, repairing, and building small vessels",
    )
    BUR = PermissibleValue(
        text="BUR", title="burial cave(s)", description="a cave used for human burials"
    )
    BUSTN = PermissibleValue(
        text="BUSTN",
        title="bus station",
        description="a facility comprising ticket office, platforms, etc. for loading and unloading passengers",
    )
    BUSTP = PermissibleValue(
        text="BUSTP", title="bus stop", description="a place lacking station facilities"
    )
    CARN = PermissibleValue(
        text="CARN",
        title="cairn",
        description="a heap of stones erected as a landmark or for other purposes",
    )
    CAVE = PermissibleValue(
        text="CAVE",
        title="cave(s)",
        description="an underground passageway or chamber, or cavity on the side of a cliff",
    )
    CH = PermissibleValue(
        text="CH", title="church", description="a building for public Christian worship"
    )
    CMP = PermissibleValue(
        text="CMP",
        title="camp(s)",
        description="a site occupied by tents, huts, or other shelters for temporary use",
    )
    CMPL = PermissibleValue(
        text="CMPL", title="logging camp", description="a camp used by loggers"
    )
    CMPLA = PermissibleValue(
        text="CMPLA",
        title="labor camp",
        description="a camp used by migrant or temporary laborers",
    )
    CMPMN = PermissibleValue(
        text="CMPMN", title="mining camp", description="a camp used by miners"
    )
    CMPO = PermissibleValue(
        text="CMPO", title="oil camp", description="a camp used by oilfield workers"
    )
    CMPQ = PermissibleValue(text="CMPQ", title="abandoned camp")
    CMPRF = PermissibleValue(
        text="CMPRF", title="refugee camp", description="a camp used by refugees"
    )
    CMTY = PermissibleValue(
        text="CMTY", title="cemetery", description="a burial place or ground"
    )
    COMC = PermissibleValue(
        text="COMC",
        title="communication center",
        description="""a facility, including buildings, antennae, towers and electronic equipment for receiving and transmitting information""",
    )
    CRRL = PermissibleValue(
        text="CRRL",
        title="corral(s)",
        description="a pen or enclosure for confining or capturing animals",
    )
    CSNO = PermissibleValue(
        text="CSNO",
        title="casino",
        description="a building used for entertainment, especially gambling",
    )
    CSTL = PermissibleValue(
        text="CSTL",
        title="castle",
        description="a large fortified building or set of buildings",
    )
    CSTM = PermissibleValue(
        text="CSTM",
        title="customs house",
        description="""a building in a port where customs and duties are paid, and where vessels are entered and cleared""",
    )
    CTHSE = PermissibleValue(
        text="CTHSE",
        title="courthouse",
        description="a building in which courts of law are held",
    )
    CTRA = PermissibleValue(
        text="CTRA",
        title="atomic center",
        description="a facility where atomic research is carried out",
    )
    CTRCM = PermissibleValue(
        text="CTRCM",
        title="community center",
        description="a facility for community recreation and other activities",
    )
    CTRF = PermissibleValue(
        text="CTRF",
        title="facility center",
        description="a place where more than one facility is situated",
    )
    CTRM = PermissibleValue(
        text="CTRM",
        title="medical center",
        description="""a complex of health care buildings including two or more of the following: hospital, medical school, clinic, pharmacy, doctor's offices, etc.""",
    )
    CTRR = PermissibleValue(
        text="CTRR",
        title="religious center",
        description="""a facility where more than one religious activity is carried out, e.g., retreat, school, monastery, worship""",
    )
    CTRS = PermissibleValue(
        text="CTRS",
        title="space center",
        description="a facility for launching, tracking, or controlling satellites and space vehicles",
    )
    CTYD = PermissibleValue(
        text="CTYD",
        title="courtyard",
        description="an area surrounded by a building or complex and open to the sky",
    )
    CVNT = PermissibleValue(
        text="CVNT",
        title="convent",
        description="a building where a community of nuns lives in seclusion",
    )
    DAM = PermissibleValue(
        text="DAM",
        title="dam",
        description="a barrier constructed across a stream to impound water",
    )
    DAMQ = PermissibleValue(
        text="DAMQ",
        title="ruined dam",
        description="a destroyed or decayed dam which is no longer functional",
    )
    DAMSB = PermissibleValue(
        text="DAMSB",
        title="sub-surface dam",
        description="a dam put down to bedrock in a sand river",
    )
    DARY = PermissibleValue(
        text="DARY",
        title="dairy",
        description="a facility for the processing, sale and distribution of milk or milk products",
    )
    DCKD = PermissibleValue(
        text="DCKD",
        title="dry dock",
        description="""a dock providing support for a vessel, and means for removing the water so that the bottom of the vessel can be exposed""",
    )
    DCKY = PermissibleValue(
        text="DCKY",
        title="dockyard",
        description="a facility for servicing, building, or repairing ships",
    )
    DIKE = PermissibleValue(
        text="DIKE",
        title="dike",
        description="an earth or stone embankment usually constructed for flood or stream control",
    )
    DIP = PermissibleValue(
        text="DIP",
        title="diplomatic facility",
        description="""office, residence, or facility of a foreign government, which may include an embassy, consulate, chancery, office of charge d'affaires, or other diplomatic, economic, military, or cultural mission""",
    )
    DPOF = PermissibleValue(
        text="DPOF", title="fuel depot", description="an area where fuel is stored"
    )
    EST = PermissibleValue(
        text="EST",
        title="estate(s)",
        description="a large commercialized agricultural landholding with associated buildings and other facilities",
    )
    ESTO = PermissibleValue(
        text="ESTO",
        title="oil palm plantation",
        description="an estate specializing in the cultivation of oil palm trees",
    )
    ESTR = PermissibleValue(
        text="ESTR",
        title="rubber plantation",
        description="an estate which specializes in growing and tapping rubber trees",
    )
    ESTSG = PermissibleValue(
        text="ESTSG",
        title="sugar plantation",
        description="an estate that specializes in growing sugar cane",
    )
    ESTT = PermissibleValue(
        text="ESTT",
        title="tea plantation",
        description="an estate which specializes in growing tea bushes",
    )
    ESTX = PermissibleValue(text="ESTX", title="section of estate")
    FCL = PermissibleValue(
        text="FCL",
        title="facility",
        description="""a building or buildings housing a center, institute, foundation, hospital, prison, mission, courthouse, etc.""",
    )
    FIRE = PermissibleValue(
        text="FIRE",
        title="fire station",
        description="building housing firefighters and/or fire fighting equipment",
    )
    FNDY = PermissibleValue(
        text="FNDY",
        title="foundry",
        description="a building or works where metal casting is carried out",
    )
    FRM = PermissibleValue(
        text="FRM",
        title="farm",
        description="a tract of land with associated buildings devoted to agriculture",
    )
    FRMQ = PermissibleValue(text="FRMQ", title="abandoned farm")
    FRMS = PermissibleValue(
        text="FRMS",
        title="farms",
        description="tracts of land with associated buildings devoted to agriculture",
    )
    FRMT = PermissibleValue(
        text="FRMT",
        title="farmstead",
        description="the buildings and adjacent service areas of a farm",
    )
    FT = PermissibleValue(
        text="FT", title="fort", description="a defensive structure or earthworks"
    )
    FY = PermissibleValue(
        text="FY",
        title="ferry",
        description="""a boat or other floating conveyance and terminal facilities regularly used to transport people and vehicles across a waterbody""",
    )
    FYT = PermissibleValue(
        text="FYT",
        title="ferry terminal",
        description="a place where ferries pick-up and discharge passengers, vehicles and or cargo",
    )
    GATE = PermissibleValue(
        text="GATE", title="gate", description="a controlled access entrance or exit"
    )
    GDN = PermissibleValue(
        text="GDN",
        title="garden(s)",
        description="an enclosure for displaying selected plant or animal life",
    )
    GHAT = PermissibleValue(
        text="GHAT",
        title="ghat",
        description="""a set of steps leading to a river, which are of religious significance, and at their base is usually a platform for bathing""",
    )
    GHSE = PermissibleValue(
        text="GHSE",
        title="guest house",
        description="a house used to provide lodging for paying guests",
    )
    GOSP = PermissibleValue(
        text="GOSP",
        title="gas-oil separator plant",
        description="a facility for separating gas from oil",
    )
    GOVL = PermissibleValue(
        text="GOVL",
        title="local government office",
        description="a facility housing local governmental offices, usually a city, town, or village hall",
    )
    GRVE = PermissibleValue(text="GRVE", title="grave", description="a burial site")
    HERM = PermissibleValue(
        text="HERM",
        title="hermitage",
        description="a secluded residence, usually for religious sects",
    )
    HLT = PermissibleValue(
        text="HLT",
        title="halting place",
        description="a place where caravans stop for rest",
    )
    HMSD = PermissibleValue(
        text="HMSD",
        title="homestead",
        description="""a residence, owner's or manager's, on a sheep or cattle station, woolshed, outcamp, or Aboriginal outstation, specific to Australia and New Zealand""",
    )
    HSE = PermissibleValue(
        text="HSE",
        title="house(s)",
        description="a building used as a human habitation",
    )
    HSEC = PermissibleValue(
        text="HSEC",
        title="country house",
        description="a large house, mansion, or chateau, on a large estate",
    )
    HSP = PermissibleValue(
        text="HSP",
        title="hospital",
        description="a building in which sick or injured, especially those confined to bed, are medically treated",
    )
    HSPC = PermissibleValue(
        text="HSPC",
        title="clinic",
        description="a medical facility associated with a hospital for outpatients",
    )
    HSPD = PermissibleValue(
        text="HSPD",
        title="dispensary",
        description="a building where medical or dental aid is dispensed",
    )
    HSPL = PermissibleValue(
        text="HSPL", title="leprosarium", description="an asylum or hospital for lepers"
    )
    HSTS = PermissibleValue(
        text="HSTS",
        title="historical site",
        description="a place of historical importance",
    )
    HTL = PermissibleValue(
        text="HTL",
        title="hotel",
        description="a building providing lodging and/or meals for the public",
    )
    HUT = PermissibleValue(
        text="HUT", title="hut", description="a small primitive house"
    )
    HUTS = PermissibleValue(
        text="HUTS", title="huts", description="small primitive houses"
    )
    INSM = PermissibleValue(
        text="INSM",
        title="military installation",
        description="a facility for use of and control by armed forces",
    )
    ITTR = PermissibleValue(
        text="ITTR",
        title="research institute",
        description="a facility where research is carried out",
    )
    JTY = PermissibleValue(
        text="JTY",
        title="jetty",
        description="""a structure built out into the water at a river mouth or harbor entrance to regulate currents and silting""",
    )
    LDNG = PermissibleValue(
        text="LDNG",
        title="landing",
        description="""a place where boats receive or discharge passengers and freight, but lacking most port facilities""",
    )
    LEPC = PermissibleValue(
        text="LEPC",
        title="leper colony",
        description="a settled area inhabited by lepers in relative isolation",
    )
    LIBR = PermissibleValue(
        text="LIBR",
        title="library",
        description="""A place in which information resources such as books are kept for reading, reference, or lending.""",
    )
    LNDF = PermissibleValue(
        text="LNDF",
        title="landfill",
        description="""a place for trash and garbage disposal in which the waste is buried between layers of earth to build up low-lying land""",
    )
    LOCK = PermissibleValue(
        text="LOCK",
        title="lock(s)",
        description="""a basin in a waterway with gates at each end by means of which vessels are passed from one water level to another""",
    )
    LTHSE = PermissibleValue(
        text="LTHSE",
        title="lighthouse",
        description="a distinctive structure exhibiting a major navigation light",
    )
    MALL = PermissibleValue(
        text="MALL",
        title="mall",
        description="""A large, often enclosed shopping complex containing various stores, businesses, and restaurants usually accessible by common passageways.""",
    )
    MAR = PermissibleValue(
        text="MAR",
        title="marina",
        description="a harbor facility for small boats, yachts, etc.",
    )
    MFG = PermissibleValue(
        text="MFG",
        title="factory",
        description="one or more buildings where goods are manufactured, processed or fabricated",
    )
    MFGB = PermissibleValue(
        text="MFGB",
        title="brewery",
        description="one or more buildings where beer is brewed",
    )
    MFGC = PermissibleValue(
        text="MFGC",
        title="cannery",
        description="a building where food items are canned",
    )
    MFGCU = PermissibleValue(
        text="MFGCU",
        title="copper works",
        description="a facility for processing copper ore",
    )
    MFGLM = PermissibleValue(
        text="MFGLM",
        title="limekiln",
        description="a furnace in which limestone is reduced to lime",
    )
    MFGM = PermissibleValue(
        text="MFGM",
        title="munitions plant",
        description="a factory where ammunition is made",
    )
    MFGPH = PermissibleValue(
        text="MFGPH",
        title="phosphate works",
        description="a facility for producing fertilizer",
    )
    MFGQ = PermissibleValue(text="MFGQ", title="abandoned factory")
    MFGSG = PermissibleValue(
        text="MFGSG",
        title="sugar refinery",
        description="a facility for converting raw sugar into refined sugar",
    )
    MKT = PermissibleValue(
        text="MKT",
        title="market",
        description="a place where goods are bought and sold at regular intervals",
    )
    ML = PermissibleValue(
        text="ML",
        title="mill(s)",
        description="""a building housing machines for transforming, shaping, finishing, grinding, or extracting products""",
    )
    MLM = PermissibleValue(
        text="MLM",
        title="ore treatment plant",
        description="a facility for improving the metal content of ore by concentration",
    )
    MLO = PermissibleValue(
        text="MLO",
        title="olive oil mill",
        description="a mill where oil is extracted from olives",
    )
    MLSG = PermissibleValue(
        text="MLSG",
        title="sugar mill",
        description="a facility where sugar cane is processed into raw sugar",
    )
    MLSGQ = PermissibleValue(
        text="MLSGQ",
        title="former sugar mill",
        description="a sugar mill no longer used as a sugar mill",
    )
    MLSW = PermissibleValue(
        text="MLSW",
        title="sawmill",
        description="a mill where logs or lumber are sawn to specified shapes and sizes",
    )
    MLWND = PermissibleValue(
        text="MLWND",
        title="windmill",
        description="a mill or water pump powered by wind",
    )
    MLWTR = PermissibleValue(
        text="MLWTR", title="water mill", description="a mill powered by running water"
    )
    MN = PermissibleValue(
        text="MN",
        title="mine(s)",
        description="""a site where mineral ores are extracted from the ground by excavating surface pits and subterranean passages""",
    )
    MNAU = PermissibleValue(
        text="MNAU",
        title="gold mine(s)",
        description="a mine where gold ore, or alluvial gold is extracted",
    )
    MNC = PermissibleValue(
        text="MNC", title="coal mine(s)", description="a mine where coal is extracted"
    )
    MNCR = PermissibleValue(
        text="MNCR",
        title="chrome mine(s)",
        description="a mine where chrome ore is extracted",
    )
    MNCU = PermissibleValue(
        text="MNCU",
        title="copper mine(s)",
        description="a mine where copper ore is extracted",
    )
    MNFE = PermissibleValue(
        text="MNFE",
        title="iron mine(s)",
        description="a mine where iron ore is extracted",
    )
    MNMT = PermissibleValue(
        text="MNMT", title="monument", description="a commemorative structure or statue"
    )
    MNN = PermissibleValue(
        text="MNN",
        title="salt mine(s)",
        description="a mine from which salt is extracted",
    )
    MNQ = PermissibleValue(text="MNQ", title="abandoned mine")
    MNQR = PermissibleValue(
        text="MNQR",
        title="quarry(-ies)",
        description="a surface mine where building stone or gravel and sand, etc. are extracted",
    )
    MOLE = PermissibleValue(
        text="MOLE",
        title="mole",
        description="a massive structure of masonry or large stones serving as a pier or breakwater",
    )
    MSQE = PermissibleValue(
        text="MSQE", title="mosque", description="a building for public Islamic worship"
    )
    MSSN = PermissibleValue(
        text="MSSN",
        title="mission",
        description="""a place characterized by dwellings, school, church, hospital and other facilities operated by a religious group for the purpose of providing charitable services and to propagate religion""",
    )
    MSSNQ = PermissibleValue(text="MSSNQ", title="abandoned mission")
    MSTY = PermissibleValue(
        text="MSTY",
        title="monastery",
        description="a building and grounds where a community of monks lives in seclusion",
    )
    MTRO = PermissibleValue(
        text="MTRO",
        title="metro station",
        description="metro station (Underground, Tube, or Metro)",
    )
    MUS = PermissibleValue(
        text="MUS",
        title="museum",
        description="""a building where objects of permanent interest in one or more of the arts and sciences are preserved and exhibited""",
    )
    NOV = PermissibleValue(
        text="NOV",
        title="novitiate",
        description="a religious house or school where novices are trained",
    )
    NSY = PermissibleValue(
        text="NSY",
        title="nursery(-ies)",
        description="a place where plants are propagated for transplanting or grafting",
    )
    OBPT = PermissibleValue(
        text="OBPT",
        title="observation point",
        description="a wildlife or scenic observation point",
    )
    OBS = PermissibleValue(
        text="OBS",
        title="observatory",
        description="a facility equipped for observation of atmospheric or space phenomena",
    )
    OBSR = PermissibleValue(
        text="OBSR",
        title="radio observatory",
        description="a facility equipped with an array of antennae for receiving radio waves from space",
    )
    OILJ = PermissibleValue(
        text="OILJ",
        title="oil pipeline junction",
        description="a section of an oil pipeline where two or more pipes join together",
    )
    OILQ = PermissibleValue(text="OILQ", title="abandoned oil well")
    OILR = PermissibleValue(
        text="OILR",
        title="oil refinery",
        description="a facility for converting crude oil into refined petroleum products",
    )
    OILT = PermissibleValue(
        text="OILT",
        title="tank farm",
        description="""a tract of land occupied by large, cylindrical, metal tanks in which oil or liquid petrochemicals are stored""",
    )
    OILW = PermissibleValue(
        text="OILW", title="oil well", description="a well from which oil may be pumped"
    )
    OPRA = PermissibleValue(
        text="OPRA",
        title="opera house",
        description="A theater designed chiefly for the performance of operas.",
    )
    PAL = PermissibleValue(
        text="PAL",
        title="palace",
        description="a large stately house, often a royal or presidential residence",
    )
    PGDA = PermissibleValue(
        text="PGDA",
        title="pagoda",
        description="a tower-like storied structure, usually a Buddhist shrine",
    )
    PIER = PermissibleValue(
        text="PIER",
        title="pier",
        description="""a structure built out into navigable water on piles providing berthing for ships and recreation""",
    )
    PKLT = PermissibleValue(
        text="PKLT",
        title="parking lot",
        description="an area used for parking vehicles",
    )
    PMPO = PermissibleValue(
        text="PMPO",
        title="oil pumping station",
        description="a facility for pumping oil through a pipeline",
    )
    PMPW = PermissibleValue(
        text="PMPW",
        title="water pumping station",
        description="a facility for pumping water from a major well or through a pipeline",
    )
    PO = PermissibleValue(
        text="PO",
        title="post office",
        description="a public building in which mail is received, sorted and distributed",
    )
    PP = PermissibleValue(
        text="PP",
        title="police post",
        description="a building in which police are stationed",
    )
    PPQ = PermissibleValue(text="PPQ", title="abandoned police post")
    PRKGT = PermissibleValue(
        text="PRKGT", title="park gate", description="a controlled access to a park"
    )
    PRKHQ = PermissibleValue(
        text="PRKHQ",
        title="park headquarters",
        description="a park administrative facility",
    )
    PRN = PermissibleValue(
        text="PRN", title="prison", description="a facility for confining prisoners"
    )
    PRNJ = PermissibleValue(
        text="PRNJ",
        title="reformatory",
        description="a facility for confining, training, and reforming young law offenders",
    )
    PRNQ = PermissibleValue(text="PRNQ", title="abandoned prison")
    PS = PermissibleValue(
        text="PS",
        title="power station",
        description="a facility for generating electric power",
    )
    PSH = PermissibleValue(
        text="PSH",
        title="hydroelectric power station",
        description="a building where electricity is generated from water power",
    )
    PSN = PermissibleValue(
        text="PSN", title="nuclear power station", description="nuclear power station"
    )
    PSTB = PermissibleValue(
        text="PSTB",
        title="border post",
        description="""a post or station at an international boundary for the regulation of movement of people and goods""",
    )
    PSTC = PermissibleValue(
        text="PSTC",
        title="customs post",
        description="a building at an international boundary where customs and duties are paid on goods",
    )
    PSTP = PermissibleValue(
        text="PSTP",
        title="patrol post",
        description="a post from which patrols are sent out",
    )
    PYR = PermissibleValue(
        text="PYR",
        title="pyramid",
        description="""an ancient massive structure of square ground plan with four triangular faces meeting at a point and used for enclosing tombs""",
    )
    PYRS = PermissibleValue(
        text="PYRS",
        title="pyramids",
        description="""ancient massive structures of square ground plan with four triangular faces meeting at a point and used for enclosing tombs""",
    )
    QUAY = PermissibleValue(
        text="QUAY",
        title="quay",
        description="""a structure of solid construction along a shore or bank which provides berthing for ships and which generally provides cargo handling facilities""",
    )
    RDCR = PermissibleValue(
        text="RDCR",
        title="traffic circle",
        description="a road junction formed around a central circle about which traffic moves in one direction only",
    )
    RDIN = PermissibleValue(
        text="RDIN",
        title="intersection",
        description="""a junction of two or more highways by a system of separate levels that permit traffic to pass from one to another without the crossing of traffic streams""",
    )
    RECG = PermissibleValue(
        text="RECG",
        title="golf course",
        description="a recreation field where golf is played",
    )
    RECR = PermissibleValue(
        text="RECR", title="racetrack", description="a track where races are held"
    )
    REST = PermissibleValue(
        text="REST",
        title="restaurant",
        description="A place where meals are served to the public",
    )
    RET = PermissibleValue(
        text="RET",
        title="store",
        description="a building where goods and/or services are offered for sale",
    )
    RHSE = PermissibleValue(
        text="RHSE",
        title="resthouse",
        description="a structure maintained for the rest and shelter of travelers",
    )
    RKRY = PermissibleValue(
        text="RKRY",
        title="rookery",
        description="a breeding place of a colony of birds or seals",
    )
    RLG = PermissibleValue(
        text="RLG",
        title="religious site",
        description="an ancient site of significant religious importance",
    )
    RLGR = PermissibleValue(
        text="RLGR",
        title="retreat",
        description="a place of temporary seclusion, especially for religious groups",
    )
    RNCH = PermissibleValue(
        text="RNCH",
        title="ranch(es)",
        description="a large farm specializing in extensive grazing of livestock",
    )
    RSD = PermissibleValue(
        text="RSD",
        title="railroad siding",
        description="a short track parallel to and joining the main track",
    )
    RSGNL = PermissibleValue(
        text="RSGNL",
        title="railroad signal",
        description="a signal at the entrance of a particular section of track governing the movement of trains",
    )
    RSRT = PermissibleValue(
        text="RSRT",
        title="resort",
        description="a specialized facility for vacation, health, or participation sports activities",
    )
    RSTN = PermissibleValue(
        text="RSTN",
        title="railroad station",
        description="""a facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight""",
    )
    RSTNQ = PermissibleValue(text="RSTNQ", title="abandoned railroad station")
    RSTP = PermissibleValue(
        text="RSTP",
        title="railroad stop",
        description="""a place lacking station facilities where trains stop to pick up and unload passengers and freight""",
    )
    RSTPQ = PermissibleValue(text="RSTPQ", title="abandoned railroad stop")
    RUIN = PermissibleValue(
        text="RUIN",
        title="ruin(s)",
        description="a destroyed or decayed structure which is no longer functional",
    )
    SCH = PermissibleValue(
        text="SCH",
        title="school",
        description="building(s) where instruction in one or more branches of knowledge takes place",
    )
    SCHA = PermissibleValue(
        text="SCHA",
        title="agricultural school",
        description="a school with a curriculum focused on agriculture",
    )
    SCHC = PermissibleValue(
        text="SCHC",
        title="college",
        description="the grounds and buildings of an institution of higher learning",
    )
    SCHL = PermissibleValue(
        text="SCHL",
        title="language school",
        description="Language Schools & Institutions",
    )
    SCHM = PermissibleValue(
        text="SCHM",
        title="military school",
        description="a school at which military science forms the core of the curriculum",
    )
    SCHN = PermissibleValue(
        text="SCHN",
        title="maritime school",
        description="a school at which maritime sciences form the core of the curriculum",
    )
    SCHT = PermissibleValue(
        text="SCHT",
        title="technical school",
        description="post-secondary school with a specifically technical or vocational curriculum",
    )
    SECP = PermissibleValue(
        text="SECP",
        title="State Exam Prep Centre",
        description="state exam preparation centres",
    )
    SHPF = PermissibleValue(
        text="SHPF",
        title="sheepfold",
        description="a fence or wall enclosure for sheep and other small herd animals",
    )
    SHRN = PermissibleValue(
        text="SHRN",
        title="shrine",
        description="a structure or place memorializing a person or religious concept",
    )
    SHSE = PermissibleValue(
        text="SHSE",
        title="storehouse",
        description="a building for storing goods, especially provisions",
    )
    SLCE = PermissibleValue(
        text="SLCE",
        title="sluice",
        description="""a conduit or passage for carrying off surplus water from a waterbody, usually regulated by means of a sluice gate""",
    )
    SNTR = PermissibleValue(
        text="SNTR",
        title="sanatorium",
        description="a facility where victims of physical or mental disorders are treated",
    )
    SPA = PermissibleValue(
        text="SPA",
        title="spa",
        description="a resort area usually developed around a medicinal spring",
    )
    SPLY = PermissibleValue(
        text="SPLY",
        title="spillway",
        description="a passage or outlet through which surplus water flows over, around or through a dam",
    )
    SQR = PermissibleValue(
        text="SQR",
        title="square",
        description="a broad, open, public area near the center of a town or city",
    )
    STBL = PermissibleValue(
        text="STBL",
        title="stable",
        description="a building for the shelter and feeding of farm animals, especially horses",
    )
    STDM = PermissibleValue(
        text="STDM",
        title="stadium",
        description="a structure with an enclosure for athletic games with tiers of seats for spectators",
    )
    STNB = PermissibleValue(
        text="STNB",
        title="scientific research base",
        description="a scientific facility used as a base from which research is carried out or monitored",
    )
    STNC = PermissibleValue(
        text="STNC",
        title="coast guard station",
        description="a facility from which the coast is guarded by armed vessels",
    )
    STNE = PermissibleValue(
        text="STNE",
        title="experiment station",
        description="a facility for carrying out experiments",
    )
    STNF = PermissibleValue(
        text="STNF",
        title="forest station",
        description="a collection of buildings and facilities for carrying out forest management",
    )
    STNI = PermissibleValue(
        text="STNI",
        title="inspection station",
        description="a station at which vehicles, goods, and people are inspected",
    )
    STNM = PermissibleValue(
        text="STNM",
        title="meteorological station",
        description="a station at which weather elements are recorded",
    )
    STNR = PermissibleValue(
        text="STNR",
        title="radio station",
        description="a facility for producing and transmitting information by radio waves",
    )
    STNS = PermissibleValue(
        text="STNS",
        title="satellite station",
        description="a facility for tracking and communicating with orbiting satellites",
    )
    STNW = PermissibleValue(
        text="STNW",
        title="whaling station",
        description="a facility for butchering whales and processing train oil",
    )
    STPS = PermissibleValue(
        text="STPS",
        title="steps",
        description="stones or slabs placed for ease in ascending or descending a steep slope",
    )
    SWT = PermissibleValue(
        text="SWT",
        title="sewage treatment plant",
        description="facility for the processing of sewage and/or wastewater",
    )
    SYG = PermissibleValue(
        text="SYG",
        title="synagogue",
        description="a place for Jewish worship and religious instruction",
    )
    THTR = PermissibleValue(
        text="THTR",
        title="theater",
        description="""a building or outdoor area used for live theatrical presentations, concerts, opera or dance productions, cinema, and/or other stage productions""",
    )
    TMB = PermissibleValue(
        text="TMB", title="tomb(s)", description="a structure for interring bodies"
    )
    TMPL = PermissibleValue(
        text="TMPL",
        title="temple(s)",
        description="an edifice dedicated to religious worship",
    )
    TNKD = PermissibleValue(
        text="TNKD",
        title="cattle dipping tank",
        description="""a small artificial pond used for immersing cattle in chemically treated water for disease control""",
    )
    TOLL = PermissibleValue(
        text="TOLL",
        title="toll gate/barrier",
        description="highway toll collection station",
    )
    TOWR = PermissibleValue(
        text="TOWR",
        title="tower",
        description="a high conspicuous structure, typically much higher than its diameter",
    )
    TRAM = PermissibleValue(
        text="TRAM",
        title="tram",
        description="rail vehicle along urban streets (also known as streetcar or trolley)",
    )
    TRANT = PermissibleValue(
        text="TRANT",
        title="transit terminal",
        description="facilities for the handling of vehicular freight and passengers",
    )
    TRIG = PermissibleValue(
        text="TRIG",
        title="triangulation station",
        description="a point on the earth whose position has been determined by triangulation",
    )
    TRMO = PermissibleValue(
        text="TRMO",
        title="oil pipeline terminal",
        description="a tank farm or loading facility at the end of an oil pipeline",
    )
    TWO = PermissibleValue(
        text="TWO", title="temp work office", description="Temporary Work Offices"
    )
    UNIP = PermissibleValue(
        text="UNIP",
        title="university prep school",
        description="University Preparation Schools & Institutions",
    )
    UNIV = PermissibleValue(
        text="UNIV",
        title="university",
        description="""An institution for higher learning with teaching and research facilities constituting a graduate school and professional schools that award master's degrees and doctorates and an undergraduate division that awards bachelor's degrees.""",
    )
    USGE = PermissibleValue(
        text="USGE",
        title="united states government establishment",
        description="a facility operated by the United States Government in Panama",
    )
    VETF = PermissibleValue(
        text="VETF",
        title="veterinary facility",
        description="a building or camp at which veterinary services are available",
    )
    WALL = PermissibleValue(
        text="WALL",
        title="wall",
        description="""a thick masonry structure, usually enclosing a field or building, or forming the side of a structure""",
    )
    WALLA = PermissibleValue(
        text="WALLA",
        title="ancient wall",
        description="the remains of a linear defensive stone structure",
    )
    WEIR = PermissibleValue(
        text="WEIR",
        title="weir(s)",
        description="""a small dam in a stream, designed to raise the water level or to divert stream flow through a desired channel""",
    )
    WHRF = PermissibleValue(
        text="WHRF",
        title="wharf(-ves)",
        description="""a structure of open rather than solid construction along a shore or a bank which provides berthing for ships and cargo-handling facilities""",
    )
    WRCK = PermissibleValue(
        text="WRCK",
        title="wreck",
        description="the site of the remains of a wrecked vessel",
    )
    WTRW = PermissibleValue(
        text="WTRW",
        title="waterworks",
        description="""a facility for supplying potable water through a water source and a system of pumps and filtration beds""",
    )
    ZNF = PermissibleValue(
        text="ZNF",
        title="free trade zone",
        description="""an area, usually a section of a port, where goods may be received and shipped free of customs duty and of most customs regulations""",
    )
    ZOO = PermissibleValue(
        text="ZOO",
        title="zoo",
        description="a zoological garden or park where wild animals are kept for exhibition",
    )
    ASPH = PermissibleValue(
        text="ASPH",
        title="asphalt lake",
        description="a small basin containing naturally occurring asphalt",
    )
    ATOL = PermissibleValue(
        text="ATOL",
        title="atoll(s)",
        description="a ring-shaped coral reef which has closely spaced islands on it encircling a lagoon",
    )
    BAR = PermissibleValue(
        text="BAR",
        title="bar",
        description="""a shallow ridge or mound of coarse unconsolidated material in a stream channel, at the mouth of a stream, estuary, or lagoon and in the wave-break zone along coasts""",
    )
    BCH = PermissibleValue(
        text="BCH",
        title="beach",
        description="""a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves""",
    )
    BCHS = PermissibleValue(
        text="BCHS",
        title="beaches",
        description="""a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves""",
    )
    BDLD = PermissibleValue(
        text="BDLD",
        title="badlands",
        description="""an area characterized by a maze of very closely spaced, deep, narrow, steep-sided ravines, and sharp crests and pinnacles""",
    )
    BLDR = PermissibleValue(
        text="BLDR",
        title="boulder field",
        description="a high altitude or high latitude bare, flat area covered with large angular rocks",
    )
    BLHL = PermissibleValue(
        text="BLHL",
        title="blowhole(s)",
        description="""a hole in coastal rock through which sea water is forced by a rising tide or waves and spurted through an outlet into the air""",
    )
    BLOW = PermissibleValue(
        text="BLOW",
        title="blowout(s)",
        description="a small depression in sandy terrain, caused by wind erosion",
    )
    BNCH = PermissibleValue(
        text="BNCH",
        title="bench",
        description="""a long, narrow bedrock platform bounded by steeper slopes above and below, usually overlooking a waterbody""",
    )
    BUTE = PermissibleValue(
        text="BUTE",
        title="butte(s)",
        description="a small, isolated, usually flat-topped hill with steep sides",
    )
    CAPE = PermissibleValue(
        text="CAPE",
        title="cape",
        description="""a land area, more prominent than a point, projecting into the sea and marking a notable change in coastal direction""",
    )
    CFT = PermissibleValue(
        text="CFT",
        title="cleft(s)",
        description="a deep narrow slot, notch, or groove in a coastal cliff",
    )
    CLDA = PermissibleValue(
        text="CLDA",
        title="caldera",
        description="a depression measuring kilometers across formed by the collapse of a volcanic mountain",
    )
    CLF = PermissibleValue(
        text="CLF",
        title="cliff(s)",
        description="a high, steep to perpendicular slope overlooking a waterbody or lower area",
    )
    CNYN = PermissibleValue(
        text="CNYN",
        title="canyon",
        description="a deep, narrow valley with steep sides cutting into a plateau or mountainous area",
    )
    CONE = PermissibleValue(
        text="CONE",
        title="cone(s)",
        description="a conical landform composed of mud or volcanic material",
    )
    CRDR = PermissibleValue(
        text="CRDR",
        title="corridor",
        description="a strip or area of land having significance as an access way",
    )
    CRQ = PermissibleValue(
        text="CRQ",
        title="cirque",
        description="""a bowl-like hollow partially surrounded by cliffs or steep slopes at the head of a glaciated valley""",
    )
    CRQS = PermissibleValue(
        text="CRQS",
        title="cirques",
        description="""bowl-like hollows partially surrounded by cliffs or steep slopes at the head of a glaciated valley""",
    )
    CRTR = PermissibleValue(
        text="CRTR",
        title="crater(s)",
        description="""a generally circular saucer or bowl-shaped depression caused by volcanic or meteorite explosive action""",
    )
    CUET = PermissibleValue(
        text="CUET",
        title="cuesta(s)",
        description="an asymmetric ridge formed on tilted strata",
    )
    DLTA = PermissibleValue(
        text="DLTA",
        title="delta",
        description="a flat plain formed by alluvial deposits at the mouth of a stream",
    )
    DPR = PermissibleValue(
        text="DPR",
        title="depression(s)",
        description="a low area surrounded by higher land and usually characterized by interior drainage",
    )
    DSRT = PermissibleValue(
        text="DSRT",
        title="desert",
        description="a large area with little or no vegetation due to extreme environmental conditions",
    )
    DUNE = PermissibleValue(
        text="DUNE",
        title="dune(s)",
        description="a wave form, ridge or star shape feature composed of sand",
    )
    DVD = PermissibleValue(
        text="DVD",
        title="divide",
        description="a line separating adjacent drainage basins",
    )
    ERG = PermissibleValue(
        text="ERG",
        title="sandy desert",
        description="an extensive tract of shifting sand and sand dunes",
    )
    FAN = PermissibleValue(
        text="FAN",
        title="fan(s)",
        description="""a fan-shaped wedge of coarse alluvium with apex merging with a mountain stream bed and the fan spreading out at a low angle slope onto an adjacent plain""",
    )
    FORD = PermissibleValue(
        text="FORD",
        title="ford",
        description="a shallow part of a stream which can be crossed on foot or by land vehicle",
    )
    FSR = PermissibleValue(
        text="FSR", title="fissure", description="a crack associated with volcanism"
    )
    GAP = PermissibleValue(
        text="GAP",
        title="gap",
        description="a low place in a ridge, not used for transportation",
    )
    GRGE = PermissibleValue(
        text="GRGE",
        title="gorge(s)",
        description="a short, narrow, steep-sided section of a stream valley",
    )
    HDLD = PermissibleValue(
        text="HDLD",
        title="headland",
        description="a high projection of land extending into a large body of water beyond the line of the coast",
    )
    HLL = PermissibleValue(
        text="HLL",
        title="hill",
        description="""a rounded elevation of limited extent rising above the surrounding land with local relief of less than 300m""",
    )
    HLLS = PermissibleValue(
        text="HLLS",
        title="hills",
        description="""rounded elevations of limited extent rising above the surrounding land with local relief of less than 300m""",
    )
    HMCK = PermissibleValue(
        text="HMCK",
        title="hammock(s)",
        description="""a patch of ground, distinct from and slightly above the surrounding plain or wetland. Often occurs in groups""",
    )
    HMDA = PermissibleValue(
        text="HMDA",
        title="rock desert",
        description="a relatively sand-free, high bedrock plateau in a hot desert, with or without a gravel veneer",
    )
    INTF = PermissibleValue(
        text="INTF",
        title="interfluve",
        description="a relatively undissected upland between adjacent stream valleys",
    )
    ISL = PermissibleValue(
        text="ISL",
        title="island",
        description="a tract of land, smaller than a continent, surrounded by water at high water",
    )
    ISLET = PermissibleValue(
        text="ISLET",
        title="islet",
        description="small island, bigger than rock, smaller than island.",
    )
    ISLF = PermissibleValue(
        text="ISLF",
        title="artificial island",
        description="an island created by landfill or diking and filling in a wetland, bay, or lagoon",
    )
    ISLM = PermissibleValue(
        text="ISLM",
        title="mangrove island",
        description="a mangrove swamp surrounded by a waterbody",
    )
    ISLS = PermissibleValue(
        text="ISLS",
        title="islands",
        description="tracts of land, smaller than a continent, surrounded by water at high water",
    )
    ISLT = PermissibleValue(
        text="ISLT",
        title="land-tied island",
        description="a coastal island connected to the mainland by barrier beaches, levees or dikes",
    )
    ISLX = PermissibleValue(text="ISLX", title="section of island")
    ISTH = PermissibleValue(
        text="ISTH",
        title="isthmus",
        description="a narrow strip of land connecting two larger land masses and bordered by water",
    )
    KRST = PermissibleValue(
        text="KRST",
        title="karst area",
        description="""a distinctive landscape developed on soluble rock such as limestone characterized by sinkholes, caves, disappearing streams, and underground drainage""",
    )
    LAVA = PermissibleValue(
        text="LAVA", title="lava area", description="an area of solidified lava"
    )
    LEV = PermissibleValue(
        text="LEV",
        title="levee",
        description="""a natural low embankment bordering a distributary or meandering stream; often built up artificially to control floods""",
    )
    MESA = PermissibleValue(
        text="MESA",
        title="mesa(s)",
        description="""a flat-topped, isolated elevation with steep slopes on all sides, less extensive than a plateau""",
    )
    MND = PermissibleValue(
        text="MND", title="mound(s)", description="a low, isolated, rounded hill"
    )
    MRN = PermissibleValue(
        text="MRN",
        title="moraine",
        description="a mound, ridge, or other accumulation of glacial till",
    )
    MT = PermissibleValue(
        text="MT",
        title="mountain",
        description="""an elevation standing high above the surrounding area with small summit area, steep slopes and local relief of 300m or more""",
    )
    MTS = PermissibleValue(
        text="MTS",
        title="mountains",
        description="a mountain range or a group of mountains or high ridges",
    )
    NKM = PermissibleValue(
        text="NKM",
        title="meander neck",
        description="a narrow strip of land between the two limbs of a meander loop at its narrowest point",
    )
    NTK = PermissibleValue(
        text="NTK",
        title="nunatak",
        description="a rock or mountain peak protruding through glacial ice",
    )
    NTKS = PermissibleValue(
        text="NTKS",
        title="nunataks",
        description="rocks or mountain peaks protruding through glacial ice",
    )
    PAN = PermissibleValue(
        text="PAN",
        title="pan",
        description="""a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool""",
    )
    PANS = PermissibleValue(
        text="PANS",
        title="pans",
        description="""a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool""",
    )
    PASS = PermissibleValue(
        text="PASS",
        title="pass",
        description="""a break in a mountain range or other high obstruction, used for transportation from one side to the other [See also gap]""",
    )
    PEN = PermissibleValue(
        text="PEN",
        title="peninsula",
        description="an elongate area of land projecting into a body of water and nearly surrounded by water",
    )
    PENX = PermissibleValue(text="PENX", title="section of peninsula")
    PK = PermissibleValue(
        text="PK",
        title="peak",
        description="a pointed elevation atop a mountain, ridge, or other hypsographic feature",
    )
    PKS = PermissibleValue(
        text="PKS",
        title="peaks",
        description="pointed elevations atop a mountain, ridge, or other hypsographic features",
    )
    PLAT = PermissibleValue(
        text="PLAT",
        title="plateau",
        description="an elevated plain with steep slopes on one or more sides, and often with incised streams",
    )
    PLATX = PermissibleValue(text="PLATX", title="section of plateau")
    PLDR = PermissibleValue(
        text="PLDR",
        title="polder",
        description="an area reclaimed from the sea by diking and draining",
    )
    PLN = PermissibleValue(
        text="PLN",
        title="plain(s)",
        description="""an extensive area of comparatively level to gently undulating land, lacking surface irregularities, and usually adjacent to a higher area""",
    )
    PLNX = PermissibleValue(text="PLNX", title="section of plain")
    PROM = PermissibleValue(
        text="PROM",
        title="promontory(-ies)",
        description="a bluff or prominent hill overlooking or projecting into a lowland",
    )
    PT = PermissibleValue(
        text="PT",
        title="point",
        description="a tapering piece of land projecting into a body of water, less prominent than a cape",
    )
    PTS = PermissibleValue(
        text="PTS",
        title="points",
        description="tapering pieces of land projecting into a body of water, less prominent than a cape",
    )
    RDGB = PermissibleValue(
        text="RDGB",
        title="beach ridge",
        description="a ridge of sand just inland and parallel to the beach, usually in series",
    )
    RDGE = PermissibleValue(
        text="RDGE",
        title="ridge(s)",
        description="a long narrow elevation with steep sides, and a more or less continuous crest",
    )
    REG = PermissibleValue(
        text="REG",
        title="stony desert",
        description="a desert plain characterized by a surface veneer of gravel and stones",
    )
    RK = PermissibleValue(
        text="RK", title="rock", description="a conspicuous, isolated rocky mass"
    )
    RKFL = PermissibleValue(
        text="RKFL",
        title="rockfall",
        description="an irregular mass of fallen rock at the base of a cliff or steep slope",
    )
    RKS = PermissibleValue(
        text="RKS", title="rocks", description="conspicuous, isolated rocky masses"
    )
    SAND = PermissibleValue(
        text="SAND", title="sand area", description="a tract of land covered with sand"
    )
    SBED = PermissibleValue(
        text="SBED",
        title="dry stream bed",
        description="a channel formerly containing the water of a stream",
    )
    SCRP = PermissibleValue(
        text="SCRP",
        title="escarpment",
        description="a long line of cliffs or steep slopes separating level surfaces above and below",
    )
    SDL = PermissibleValue(
        text="SDL",
        title="saddle",
        description="a broad, open pass crossing a ridge or between hills or mountains",
    )
    SHOR = PermissibleValue(
        text="SHOR",
        title="shore",
        description="""a narrow zone bordering a waterbody which covers and uncovers at high and low water, respectively""",
    )
    SINK = PermissibleValue(
        text="SINK",
        title="sinkhole",
        description="a small crater-shape depression in a karst area",
    )
    SLID = PermissibleValue(
        text="SLID",
        title="slide",
        description="a mound of earth material, at the base of a slope and the associated scoured area",
    )
    SLP = PermissibleValue(
        text="SLP",
        title="slope(s)",
        description="a surface with a relatively uniform slope angle",
    )
    SPIT = PermissibleValue(
        text="SPIT",
        title="spit",
        description="a narrow, straight or curved continuation of a beach into a waterbody",
    )
    SPUR = PermissibleValue(
        text="SPUR",
        title="spur(s)",
        description="a subordinate ridge projecting outward from a hill, mountain or other elevation",
    )
    TAL = PermissibleValue(
        text="TAL",
        title="talus slope",
        description="""a steep concave slope formed by an accumulation of loose rock fragments at the base of a cliff or steep slope""",
    )
    TRGD = PermissibleValue(
        text="TRGD",
        title="interdune trough(s)",
        description="a long wind-swept trough between parallel longitudinal dunes",
    )
    TRR = PermissibleValue(
        text="TRR",
        title="terrace",
        description="""a long, narrow alluvial platform bounded by steeper slopes above and below, usually overlooking a waterbody""",
    )
    UPLD = PermissibleValue(
        text="UPLD",
        title="upland",
        description="an extensive interior region of high land with low to moderate surface relief",
    )
    VAL = PermissibleValue(
        text="VAL",
        title="valley",
        description="an elongated depression usually traversed by a stream",
    )
    VALG = PermissibleValue(
        text="VALG",
        title="hanging valley",
        description="""a valley the floor of which is notably higher than the valley or shore to which it leads; most common in areas that have been glaciated""",
    )
    VALS = PermissibleValue(
        text="VALS",
        title="valleys",
        description="elongated depressions usually traversed by a stream",
    )
    VALX = PermissibleValue(text="VALX", title="section of valley")
    VLC = PermissibleValue(
        text="VLC",
        title="volcano",
        description="a conical elevation composed of volcanic materials with a crater at the top",
    )
    APNU = PermissibleValue(
        text="APNU",
        title="apron",
        description="""a gentle slope, with a generally smooth surface, particularly found around groups of islands and seamounts""",
    )
    ARCU = PermissibleValue(
        text="ARCU",
        title="arch",
        description="a low bulge around the southeastern end of the island of Hawaii",
    )
    ARRU = PermissibleValue(
        text="ARRU",
        title="arrugado",
        description="an area of subdued corrugations off Baja California",
    )
    BDLU = PermissibleValue(
        text="BDLU",
        title="borderland",
        description="""a region adjacent to a continent, normally occupied by or bordering a shelf, that is highly irregular with depths well in excess of those typical of a shelf""",
    )
    BKSU = PermissibleValue(
        text="BKSU",
        title="banks",
        description="""elevations, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation""",
    )
    BNKU = PermissibleValue(
        text="BNKU",
        title="bank",
        description="""an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation""",
    )
    BSNU = PermissibleValue(
        text="BSNU",
        title="basin",
        description="a depression more or less equidimensional in plan and of variable extent",
    )
    CDAU = PermissibleValue(
        text="CDAU",
        title="cordillera",
        description="an entire mountain system including the subordinate ranges, interior plateaus, and basins",
    )
    CNSU = PermissibleValue(
        text="CNSU",
        title="canyons",
        description="""relatively narrow, deep depressions with steep sides, the bottom of which generally has a continuous slope""",
    )
    CNYU = PermissibleValue(
        text="CNYU",
        title="canyon",
        description="""a relatively narrow, deep depression with steep sides, the bottom of which generally has a continuous slope""",
    )
    CRSU = PermissibleValue(
        text="CRSU",
        title="continental rise",
        description="a gentle slope rising from oceanic depths towards the foot of a continental slope",
    )
    DEPU = PermissibleValue(
        text="DEPU",
        title="deep",
        description="""a localized deep area within the confines of a larger feature, such as a trough, basin or trench""",
    )
    EDGU = PermissibleValue(
        text="EDGU",
        title="shelf edge",
        description="""a line along which there is a marked increase of slope at the outer margin of a continental shelf or island shelf""",
    )
    ESCU = PermissibleValue(
        text="ESCU",
        title="escarpment (or scarp)",
        description="an elongated and comparatively steep slope separating flat or gently sloping areas",
    )
    FANU = PermissibleValue(
        text="FANU",
        title="fan",
        description="""a relatively smooth feature normally sloping away from the lower termination of a canyon or canyon system""",
    )
    FLTU = PermissibleValue(
        text="FLTU", title="flat", description="a small level or nearly level area"
    )
    FRZU = PermissibleValue(
        text="FRZU",
        title="fracture zone",
        description="""an extensive linear zone of irregular topography of the sea floor, characterized by steep-sided or asymmetrical ridges, troughs, or escarpments""",
    )
    FURU = PermissibleValue(
        text="FURU",
        title="furrow",
        description="a closed, linear, narrow, shallow depression",
    )
    GAPU = PermissibleValue(
        text="GAPU", title="gap", description="a narrow break in a ridge or rise"
    )
    GLYU = PermissibleValue(
        text="GLYU", title="gully", description="a small valley-like feature"
    )
    HLLU = PermissibleValue(
        text="HLLU",
        title="hill",
        description="an elevation rising generally less than 500 meters",
    )
    HLSU = PermissibleValue(
        text="HLSU",
        title="hills",
        description="elevations rising generally less than 500 meters",
    )
    HOLU = PermissibleValue(
        text="HOLU", title="hole", description="a small depression of the sea floor"
    )
    KNLU = PermissibleValue(
        text="KNLU",
        title="knoll",
        description="""an elevation rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summit""",
    )
    KNSU = PermissibleValue(
        text="KNSU",
        title="knolls",
        description="""elevations rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summits""",
    )
    LDGU = PermissibleValue(
        text="LDGU",
        title="ledge",
        description="a rocky projection or outcrop, commonly linear and near shore",
    )
    LEVU = PermissibleValue(
        text="LEVU",
        title="levee",
        description="an embankment bordering a canyon, valley, or seachannel",
    )
    MESU = PermissibleValue(
        text="MESU",
        title="mesa",
        description="an isolated, extensive, flat-topped elevation on the shelf, with relatively steep sides",
    )
    MNDU = PermissibleValue(
        text="MNDU", title="mound", description="a low, isolated, rounded hill"
    )
    MOTU = PermissibleValue(
        text="MOTU",
        title="moat",
        description="""an annular depression that may not be continuous, located at the base of many seamounts, islands, and other isolated elevations""",
    )
    MTU = PermissibleValue(
        text="MTU",
        title="mountain",
        description="a well-delineated subdivision of a large and complex positive feature",
    )
    PKSU = PermissibleValue(
        text="PKSU",
        title="peaks",
        description="""prominent elevations, part of a larger feature, either pointed or of very limited extent across the summit""",
    )
    PKU = PermissibleValue(
        text="PKU",
        title="peak",
        description="""a prominent elevation, part of a larger feature, either pointed or of very limited extent across the summit""",
    )
    PLNU = PermissibleValue(
        text="PLNU",
        title="plain",
        description="a flat, gently sloping or nearly level region",
    )
    PLTU = PermissibleValue(
        text="PLTU",
        title="plateau",
        description="""a comparatively flat-topped feature of considerable extent, dropping off abruptly on one or more sides""",
    )
    PNLU = PermissibleValue(
        text="PNLU",
        title="pinnacle",
        description="a high tower or spire-shaped pillar of rock or coral, alone or cresting a summit",
    )
    PRVU = PermissibleValue(
        text="PRVU",
        title="province",
        description="""a region identifiable by a group of similar physiographic features whose characteristics are markedly in contrast with surrounding areas""",
    )
    RDGU = PermissibleValue(
        text="RDGU",
        title="ridge",
        description="a long narrow elevation with steep sides",
    )
    RDSU = PermissibleValue(
        text="RDSU",
        title="ridges",
        description="long narrow elevations with steep sides",
    )
    RFSU = PermissibleValue(
        text="RFSU",
        title="reefs",
        description="surface-navigation hazards composed of consolidated material",
    )
    RFU = PermissibleValue(
        text="RFU",
        title="reef",
        description="a surface-navigation hazard composed of consolidated material",
    )
    RISU = PermissibleValue(
        text="RISU",
        title="rise",
        description="a broad elevation that rises gently, and generally smoothly, from the sea floor",
    )
    SCNU = PermissibleValue(
        text="SCNU",
        title="seachannel",
        description="""a continuously sloping, elongated depression commonly found in fans or plains and customarily bordered by levees on one or two sides""",
    )
    SCSU = PermissibleValue(
        text="SCSU",
        title="seachannels",
        description="""continuously sloping, elongated depressions commonly found in fans or plains and customarily bordered by levees on one or two sides""",
    )
    SDLU = PermissibleValue(
        text="SDLU",
        title="saddle",
        description="a low part, resembling in shape a saddle, in a ridge or between contiguous seamounts",
    )
    SHFU = PermissibleValue(
        text="SHFU",
        title="shelf",
        description="""a zone adjacent to a continent (or around an island) that extends from the low water line to a depth at which there is usually a marked increase of slope towards oceanic depths""",
    )
    SHLU = PermissibleValue(
        text="SHLU",
        title="shoal",
        description="a surface-navigation hazard composed of unconsolidated material",
    )
    SHSU = PermissibleValue(
        text="SHSU",
        title="shoals",
        description="hazards to surface navigation composed of unconsolidated material",
    )
    SHVU = PermissibleValue(
        text="SHVU",
        title="shelf valley",
        description="a valley on the shelf, generally the shoreward extension of a canyon",
    )
    SILU = PermissibleValue(
        text="SILU",
        title="sill",
        description="the low part of a gap or saddle separating basins",
    )
    SLPU = PermissibleValue(
        text="SLPU",
        title="slope",
        description="""the slope seaward from the shelf edge to the beginning of a continental rise or the point where there is a general reduction in slope""",
    )
    SMSU = PermissibleValue(
        text="SMSU",
        title="seamounts",
        description="elevations rising generally more than 1,000 meters and of limited extent across the summit",
    )
    SMU = PermissibleValue(
        text="SMU",
        title="seamount",
        description="an elevation rising generally more than 1,000 meters and of limited extent across the summit",
    )
    SPRU = PermissibleValue(
        text="SPRU",
        title="spur",
        description="a subordinate elevation, ridge, or rise projecting outward from a larger feature",
    )
    TERU = PermissibleValue(
        text="TERU",
        title="terrace",
        description="""a relatively flat horizontal or gently inclined surface, sometimes long and narrow, which is bounded by a steeper ascending slope on one side and by a steep descending slope on the opposite side""",
    )
    TMSU = PermissibleValue(
        text="TMSU",
        title="tablemounts (or guyots)",
        description="seamounts having a comparatively smooth, flat top",
    )
    TMTU = PermissibleValue(
        text="TMTU",
        title="tablemount (or guyot)",
        description="a seamount having a comparatively smooth, flat top",
    )
    TNGU = PermissibleValue(
        text="TNGU",
        title="tongue",
        description="an elongate (tongue-like) extension of a flat sea floor into an adjacent higher feature",
    )
    TRGU = PermissibleValue(
        text="TRGU",
        title="trough",
        description="""a long depression of the sea floor characteristically flat bottomed and steep sided, and normally shallower than a trench""",
    )
    TRNU = PermissibleValue(
        text="TRNU",
        title="trench",
        description="""a long, narrow, characteristically very deep and asymmetrical depression of the sea floor, with relatively steep sides""",
    )
    VALU = PermissibleValue(
        text="VALU",
        title="valley",
        description="a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
    )
    VLSU = PermissibleValue(
        text="VLSU",
        title="valleys",
        description="a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
    )
    BUSH = PermissibleValue(
        text="BUSH",
        title="bush(es)",
        description="a small clump of conspicuous bushes in an otherwise bare area",
    )
    CULT = PermissibleValue(
        text="CULT", title="cultivated area", description="an area under cultivation"
    )
    FRST = PermissibleValue(
        text="FRST",
        title="forest(s)",
        description="an area dominated by tree vegetation",
    )
    FRSTF = PermissibleValue(
        text="FRSTF",
        title="fossilized forest",
        description="a forest fossilized by geologic processes and now exposed at the earth's surface",
    )
    GROVE = PermissibleValue(
        text="GROVE",
        title="grove",
        description="""a small wooded area or collection of trees growing closely together, occurring naturally or deliberately planted""",
    )
    GRSLD = PermissibleValue(
        text="GRSLD",
        title="grassland",
        description="an area dominated by grass vegetation",
    )
    GRVC = PermissibleValue(
        text="GRVC", title="coconut grove", description="a planting of coconut trees"
    )
    GRVO = PermissibleValue(
        text="GRVO", title="olive grove", description="a planting of olive trees"
    )
    GRVP = PermissibleValue(
        text="GRVP", title="palm grove", description="a planting of palm trees"
    )
    GRVPN = PermissibleValue(
        text="GRVPN", title="pine grove", description="a planting of pine trees"
    )
    HTH = PermissibleValue(
        text="HTH",
        title="heath",
        description="an upland moor or sandy area dominated by low shrubby vegetation including heather",
    )
    MDW = PermissibleValue(
        text="MDW",
        title="meadow",
        description="a small, poorly drained area dominated by grassy vegetation",
    )
    OCH = PermissibleValue(
        text="OCH", title="orchard(s)", description="a planting of fruit or nut trees"
    )
    SCRB = PermissibleValue(
        text="SCRB",
        title="scrubland",
        description="an area of low trees, bushes, and shrubs stunted by some environmental limitation",
    )
    TREE = PermissibleValue(
        text="TREE",
        title="tree(s)",
        description="a conspicuous tree used as a landmark",
    )
    TUND = PermissibleValue(
        text="TUND",
        title="tundra",
        description="""a marshy, treeless, high latitude plain, dominated by mosses, lichens, and low shrub vegetation under permafrost conditions""",
    )
    VIN = PermissibleValue(
        text="VIN", title="vineyard", description="a planting of grapevines"
    )
    VINS = PermissibleValue(
        text="VINS", title="vineyards", description="plantings of grapevines"
    )
    null = PermissibleValue(text="null", title="not available")

    _defn = EnumDefinition(
        name="FeatureCodeEnum",
    )


class CountryCodeEnum(EnumDefinitionImpl):
    AD = PermissibleValue(text="AD", title="Andorra")
    AE = PermissibleValue(text="AE", title="United Arab Emirates")
    AF = PermissibleValue(text="AF", title="Afghanistan")
    AG = PermissibleValue(text="AG", title="Antigua and Barbuda")
    AI = PermissibleValue(text="AI", title="Anguilla")
    AL = PermissibleValue(text="AL", title="Albania")
    AM = PermissibleValue(text="AM", title="Armenia")
    AO = PermissibleValue(text="AO", title="Angola")
    AQ = PermissibleValue(text="AQ", title="Antarctica")
    AR = PermissibleValue(text="AR", title="Argentina")
    AS = PermissibleValue(text="AS", title="American Samoa")
    AT = PermissibleValue(text="AT", title="Austria")
    AU = PermissibleValue(text="AU", title="Australia")
    AW = PermissibleValue(text="AW", title="Aruba")
    AX = PermissibleValue(text="AX", title="Aland Islands")
    AZ = PermissibleValue(text="AZ", title="Azerbaijan")
    BA = PermissibleValue(text="BA", title="Bosnia and Herzegovina")
    BB = PermissibleValue(text="BB", title="Barbados")
    BD = PermissibleValue(text="BD", title="Bangladesh")
    BE = PermissibleValue(text="BE", title="Belgium")
    BF = PermissibleValue(text="BF", title="Burkina Faso")
    BG = PermissibleValue(text="BG", title="Bulgaria")
    BH = PermissibleValue(text="BH", title="Bahrain")
    BI = PermissibleValue(text="BI", title="Burundi")
    BJ = PermissibleValue(text="BJ", title="Benin")
    BL = PermissibleValue(text="BL", title="Saint Barthelemy")
    BM = PermissibleValue(text="BM", title="Bermuda")
    BN = PermissibleValue(text="BN", title="Brunei")
    BO = PermissibleValue(text="BO", title="Bolivia")
    BQ = PermissibleValue(text="BQ", title="Bonaire, Saint Eustatius and Saba")
    BR = PermissibleValue(text="BR", title="Brazil")
    BS = PermissibleValue(text="BS", title="Bahamas")
    BT = PermissibleValue(text="BT", title="Bhutan")
    BV = PermissibleValue(text="BV", title="Bouvet Island")
    BW = PermissibleValue(text="BW", title="Botswana")
    BY = PermissibleValue(text="BY", title="Belarus")
    BZ = PermissibleValue(text="BZ", title="Belize")
    CA = PermissibleValue(text="CA", title="Canada")
    CC = PermissibleValue(text="CC", title="Cocos Islands")
    CD = PermissibleValue(text="CD", title="Democratic Republic of the Congo")
    CF = PermissibleValue(text="CF", title="Central African Republic")
    CG = PermissibleValue(text="CG", title="Republic of the Congo")
    CH = PermissibleValue(text="CH", title="Switzerland")
    CI = PermissibleValue(text="CI", title="Ivory Coast")
    CK = PermissibleValue(text="CK", title="Cook Islands")
    CL = PermissibleValue(text="CL", title="Chile")
    CM = PermissibleValue(text="CM", title="Cameroon")
    CN = PermissibleValue(text="CN", title="China")
    CO = PermissibleValue(text="CO", title="Colombia")
    CR = PermissibleValue(text="CR", title="Costa Rica")
    CU = PermissibleValue(text="CU", title="Cuba")
    CV = PermissibleValue(text="CV", title="Cabo Verde")
    CW = PermissibleValue(text="CW", title="Curacao")
    CX = PermissibleValue(text="CX", title="Christmas Island")
    CY = PermissibleValue(text="CY", title="Cyprus")
    CZ = PermissibleValue(text="CZ", title="Czechia")
    DE = PermissibleValue(text="DE", title="Germany")
    DJ = PermissibleValue(text="DJ", title="Djibouti")
    DK = PermissibleValue(text="DK", title="Denmark")
    DM = PermissibleValue(text="DM", title="Dominica")
    DO = PermissibleValue(text="DO", title="Dominican Republic")
    DZ = PermissibleValue(text="DZ", title="Algeria")
    EC = PermissibleValue(text="EC", title="Ecuador")
    EE = PermissibleValue(text="EE", title="Estonia")
    EG = PermissibleValue(text="EG", title="Egypt")
    EH = PermissibleValue(text="EH", title="Western Sahara")
    ER = PermissibleValue(text="ER", title="Eritrea")
    ES = PermissibleValue(text="ES", title="Spain")
    ET = PermissibleValue(text="ET", title="Ethiopia")
    FI = PermissibleValue(text="FI", title="Finland")
    FJ = PermissibleValue(text="FJ", title="Fiji")
    FK = PermissibleValue(text="FK", title="Falkland Islands")
    FM = PermissibleValue(text="FM", title="Micronesia")
    FO = PermissibleValue(text="FO", title="Faroe Islands")
    FR = PermissibleValue(text="FR", title="France")
    GA = PermissibleValue(text="GA", title="Gabon")
    GB = PermissibleValue(text="GB", title="United Kingdom")
    GD = PermissibleValue(text="GD", title="Grenada")
    GE = PermissibleValue(text="GE", title="Georgia")
    GF = PermissibleValue(text="GF", title="French Guiana")
    GG = PermissibleValue(text="GG", title="Guernsey")
    GH = PermissibleValue(text="GH", title="Ghana")
    GI = PermissibleValue(text="GI", title="Gibraltar")
    GL = PermissibleValue(text="GL", title="Greenland")
    GM = PermissibleValue(text="GM", title="Gambia")
    GN = PermissibleValue(text="GN", title="Guinea")
    GP = PermissibleValue(text="GP", title="Guadeloupe")
    GQ = PermissibleValue(text="GQ", title="Equatorial Guinea")
    GR = PermissibleValue(text="GR", title="Greece")
    GS = PermissibleValue(
        text="GS", title="South Georgia and the South Sandwich Islands"
    )
    GT = PermissibleValue(text="GT", title="Guatemala")
    GU = PermissibleValue(text="GU", title="Guam")
    GW = PermissibleValue(text="GW", title="Guinea-Bissau")
    GY = PermissibleValue(text="GY", title="Guyana")
    HK = PermissibleValue(text="HK", title="Hong Kong")
    HM = PermissibleValue(text="HM", title="Heard Island and McDonald Islands")
    HN = PermissibleValue(text="HN", title="Honduras")
    HR = PermissibleValue(text="HR", title="Croatia")
    HT = PermissibleValue(text="HT", title="Haiti")
    HU = PermissibleValue(text="HU", title="Hungary")
    ID = PermissibleValue(text="ID", title="Indonesia")
    IE = PermissibleValue(text="IE", title="Ireland")
    IL = PermissibleValue(text="IL", title="Israel")
    IM = PermissibleValue(text="IM", title="Isle of Man")
    IN = PermissibleValue(text="IN", title="India")
    IO = PermissibleValue(text="IO", title="British Indian Ocean Territory")
    IQ = PermissibleValue(text="IQ", title="Iraq")
    IR = PermissibleValue(text="IR", title="Iran")
    IS = PermissibleValue(text="IS", title="Iceland")
    IT = PermissibleValue(text="IT", title="Italy")
    JE = PermissibleValue(text="JE", title="Jersey")
    JM = PermissibleValue(text="JM", title="Jamaica")
    JO = PermissibleValue(text="JO", title="Jordan")
    JP = PermissibleValue(text="JP", title="Japan")
    KE = PermissibleValue(text="KE", title="Kenya")
    KG = PermissibleValue(text="KG", title="Kyrgyzstan")
    KH = PermissibleValue(text="KH", title="Cambodia")
    KI = PermissibleValue(text="KI", title="Kiribati")
    KM = PermissibleValue(text="KM", title="Comoros")
    KN = PermissibleValue(text="KN", title="Saint Kitts and Nevis")
    KP = PermissibleValue(text="KP", title="North Korea")
    KR = PermissibleValue(text="KR", title="South Korea")
    XK = PermissibleValue(text="XK", title="Kosovo")
    KW = PermissibleValue(text="KW", title="Kuwait")
    KY = PermissibleValue(text="KY", title="Cayman Islands")
    KZ = PermissibleValue(text="KZ", title="Kazakhstan")
    LA = PermissibleValue(text="LA", title="Laos")
    LB = PermissibleValue(text="LB", title="Lebanon")
    LC = PermissibleValue(text="LC", title="Saint Lucia")
    LI = PermissibleValue(text="LI", title="Liechtenstein")
    LK = PermissibleValue(text="LK", title="Sri Lanka")
    LR = PermissibleValue(text="LR", title="Liberia")
    LS = PermissibleValue(text="LS", title="Lesotho")
    LT = PermissibleValue(text="LT", title="Lithuania")
    LU = PermissibleValue(text="LU", title="Luxembourg")
    LV = PermissibleValue(text="LV", title="Latvia")
    LY = PermissibleValue(text="LY", title="Libya")
    MA = PermissibleValue(text="MA", title="Morocco")
    MC = PermissibleValue(text="MC", title="Monaco")
    MD = PermissibleValue(text="MD", title="Moldova")
    ME = PermissibleValue(text="ME", title="Montenegro")
    MF = PermissibleValue(text="MF", title="Saint Martin")
    MG = PermissibleValue(text="MG", title="Madagascar")
    MH = PermissibleValue(text="MH", title="Marshall Islands")
    MK = PermissibleValue(text="MK", title="North Macedonia")
    ML = PermissibleValue(text="ML", title="Mali")
    MM = PermissibleValue(text="MM", title="Myanmar")
    MN = PermissibleValue(text="MN", title="Mongolia")
    MO = PermissibleValue(text="MO", title="Macao")
    MP = PermissibleValue(text="MP", title="Northern Mariana Islands")
    MQ = PermissibleValue(text="MQ", title="Martinique")
    MR = PermissibleValue(text="MR", title="Mauritania")
    MS = PermissibleValue(text="MS", title="Montserrat")
    MT = PermissibleValue(text="MT", title="Malta")
    MU = PermissibleValue(text="MU", title="Mauritius")
    MV = PermissibleValue(text="MV", title="Maldives")
    MW = PermissibleValue(text="MW", title="Malawi")
    MX = PermissibleValue(text="MX", title="Mexico")
    MY = PermissibleValue(text="MY", title="Malaysia")
    MZ = PermissibleValue(text="MZ", title="Mozambique")
    NA = PermissibleValue(text="NA", title="Namibia")
    NC = PermissibleValue(text="NC", title="New Caledonia")
    NE = PermissibleValue(text="NE", title="Niger")
    NF = PermissibleValue(text="NF", title="Norfolk Island")
    NG = PermissibleValue(text="NG", title="Nigeria")
    NI = PermissibleValue(text="NI", title="Nicaragua")
    NL = PermissibleValue(text="NL", title="The Netherlands")
    NO = PermissibleValue(text="NO", title="Norway")
    NP = PermissibleValue(text="NP", title="Nepal")
    NR = PermissibleValue(text="NR", title="Nauru")
    NU = PermissibleValue(text="NU", title="Niue")
    NZ = PermissibleValue(text="NZ", title="New Zealand")
    OM = PermissibleValue(text="OM", title="Oman")
    PA = PermissibleValue(text="PA", title="Panama")
    PE = PermissibleValue(text="PE", title="Peru")
    PF = PermissibleValue(text="PF", title="French Polynesia")
    PG = PermissibleValue(text="PG", title="Papua New Guinea")
    PH = PermissibleValue(text="PH", title="Philippines")
    PK = PermissibleValue(text="PK", title="Pakistan")
    PL = PermissibleValue(text="PL", title="Poland")
    PM = PermissibleValue(text="PM", title="Saint Pierre and Miquelon")
    PN = PermissibleValue(text="PN", title="Pitcairn")
    PR = PermissibleValue(text="PR", title="Puerto Rico")
    PS = PermissibleValue(text="PS", title="Palestinian Territory")
    PT = PermissibleValue(text="PT", title="Portugal")
    PW = PermissibleValue(text="PW", title="Palau")
    PY = PermissibleValue(text="PY", title="Paraguay")
    QA = PermissibleValue(text="QA", title="Qatar")
    RE = PermissibleValue(text="RE", title="Reunion")
    RO = PermissibleValue(text="RO", title="Romania")
    RS = PermissibleValue(text="RS", title="Serbia")
    RU = PermissibleValue(text="RU", title="Russia")
    RW = PermissibleValue(text="RW", title="Rwanda")
    SA = PermissibleValue(text="SA", title="Saudi Arabia")
    SB = PermissibleValue(text="SB", title="Solomon Islands")
    SC = PermissibleValue(text="SC", title="Seychelles")
    SD = PermissibleValue(text="SD", title="Sudan")
    SS = PermissibleValue(text="SS", title="South Sudan")
    SE = PermissibleValue(text="SE", title="Sweden")
    SG = PermissibleValue(text="SG", title="Singapore")
    SH = PermissibleValue(text="SH", title="Saint Helena")
    SI = PermissibleValue(text="SI", title="Slovenia")
    SJ = PermissibleValue(text="SJ", title="Svalbard and Jan Mayen")
    SK = PermissibleValue(text="SK", title="Slovakia")
    SL = PermissibleValue(text="SL", title="Sierra Leone")
    SM = PermissibleValue(text="SM", title="San Marino")
    SN = PermissibleValue(text="SN", title="Senegal")
    SO = PermissibleValue(text="SO", title="Somalia")
    SR = PermissibleValue(text="SR", title="Suriname")
    ST = PermissibleValue(text="ST", title="Sao Tome and Principe")
    SV = PermissibleValue(text="SV", title="El Salvador")
    SX = PermissibleValue(text="SX", title="Sint Maarten")
    SY = PermissibleValue(text="SY", title="Syria")
    SZ = PermissibleValue(text="SZ", title="Eswatini")
    TC = PermissibleValue(text="TC", title="Turks and Caicos Islands")
    TD = PermissibleValue(text="TD", title="Chad")
    TF = PermissibleValue(text="TF", title="French Southern Territories")
    TG = PermissibleValue(text="TG", title="Togo")
    TH = PermissibleValue(text="TH", title="Thailand")
    TJ = PermissibleValue(text="TJ", title="Tajikistan")
    TK = PermissibleValue(text="TK", title="Tokelau")
    TL = PermissibleValue(text="TL", title="Timor Leste")
    TM = PermissibleValue(text="TM", title="Turkmenistan")
    TN = PermissibleValue(text="TN", title="Tunisia")
    TO = PermissibleValue(text="TO", title="Tonga")
    TR = PermissibleValue(text="TR", title="Turkey")
    TT = PermissibleValue(text="TT", title="Trinidad and Tobago")
    TV = PermissibleValue(text="TV", title="Tuvalu")
    TW = PermissibleValue(text="TW", title="Taiwan")
    TZ = PermissibleValue(text="TZ", title="Tanzania")
    UA = PermissibleValue(text="UA", title="Ukraine")
    UG = PermissibleValue(text="UG", title="Uganda")
    UM = PermissibleValue(text="UM", title="United States Minor Outlying Islands")
    US = PermissibleValue(text="US", title="United States")
    UY = PermissibleValue(text="UY", title="Uruguay")
    UZ = PermissibleValue(text="UZ", title="Uzbekistan")
    VA = PermissibleValue(text="VA", title="Vatican")
    VC = PermissibleValue(text="VC", title="Saint Vincent and the Grenadines")
    VE = PermissibleValue(text="VE", title="Venezuela")
    VG = PermissibleValue(text="VG", title="British Virgin Islands")
    VI = PermissibleValue(text="VI", title="U.S. Virgin Islands")
    VN = PermissibleValue(text="VN", title="Vietnam")
    VU = PermissibleValue(text="VU", title="Vanuatu")
    WF = PermissibleValue(text="WF", title="Wallis and Futuna")
    WS = PermissibleValue(text="WS", title="Samoa")
    YE = PermissibleValue(text="YE", title="Yemen")
    YT = PermissibleValue(text="YT", title="Mayotte")
    ZA = PermissibleValue(text="ZA", title="South Africa")
    ZM = PermissibleValue(text="ZM", title="Zambia")
    ZW = PermissibleValue(text="ZW", title="Zimbabwe")
    CS = PermissibleValue(text="CS", title="Serbia and Montenegro")
    AN = PermissibleValue(text="AN", title="Netherlands Antilles")

    _defn = EnumDefinition(
        name="CountryCodeEnum",
    )


class TimezoneEnum(EnumDefinitionImpl):
    _defn = EnumDefinition(
        name="TimezoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(
            cls,
            "America/Sao_Paulo",
            PermissibleValue(text="America/Sao_Paulo", description="America/Sao_Paulo"),
        )
        setattr(
            cls,
            "America/Caracas",
            PermissibleValue(text="America/Caracas", description="America/Caracas"),
        )
        setattr(
            cls,
            "America/Montevideo",
            PermissibleValue(
                text="America/Montevideo", description="America/Montevideo"
            ),
        )
        setattr(
            cls,
            "America/Guatemala",
            PermissibleValue(text="America/Guatemala", description="America/Guatemala"),
        )
        setattr(
            cls,
            "America/La_Paz",
            PermissibleValue(text="America/La_Paz", description="America/La_Paz"),
        )
        setattr(
            cls,
            "America/Belem",
            PermissibleValue(text="America/Belem", description="America/Belem"),
        )
        setattr(
            cls,
            "America/Araguaina",
            PermissibleValue(text="America/Araguaina", description="America/Araguaina"),
        )
        setattr(
            cls,
            "America/Bahia",
            PermissibleValue(text="America/Bahia", description="America/Bahia"),
        )
        setattr(
            cls,
            "America/Argentina/Cordoba",
            PermissibleValue(
                text="America/Argentina/Cordoba",
                description="America/Argentina/Cordoba",
            ),
        )
        setattr(
            cls,
            "America/Maceio",
            PermissibleValue(text="America/Maceio", description="America/Maceio"),
        )
        setattr(
            cls,
            "America/Fortaleza",
            PermissibleValue(text="America/Fortaleza", description="America/Fortaleza"),
        )
        setattr(
            cls,
            "America/Lima",
            PermissibleValue(text="America/Lima", description="America/Lima"),
        )
        setattr(
            cls,
            "America/Santarem",
            PermissibleValue(text="America/Santarem", description="America/Santarem"),
        )
        setattr(
            cls,
            "America/Cayenne",
            PermissibleValue(text="America/Cayenne", description="America/Cayenne"),
        )
        setattr(
            cls,
            "America/Rio_Branco",
            PermissibleValue(
                text="America/Rio_Branco", description="America/Rio_Branco"
            ),
        )
        setattr(
            cls,
            "America/Campo_Grande",
            PermissibleValue(
                text="America/Campo_Grande", description="America/Campo_Grande"
            ),
        )
        setattr(
            cls,
            "America/Noronha",
            PermissibleValue(text="America/Noronha", description="America/Noronha"),
        )
        setattr(
            cls,
            "America/Porto_Velho",
            PermissibleValue(
                text="America/Porto_Velho", description="America/Porto_Velho"
            ),
        )
        setattr(
            cls,
            "America/Guyana",
            PermissibleValue(text="America/Guyana", description="America/Guyana"),
        )
        setattr(
            cls,
            "America/Cuiaba",
            PermissibleValue(text="America/Cuiaba", description="America/Cuiaba"),
        )
        setattr(
            cls,
            "America/Manaus",
            PermissibleValue(text="America/Manaus", description="America/Manaus"),
        )
        setattr(
            cls,
            "America/Paramaribo",
            PermissibleValue(
                text="America/Paramaribo", description="America/Paramaribo"
            ),
        )
        setattr(
            cls,
            "America/Asuncion",
            PermissibleValue(text="America/Asuncion", description="America/Asuncion"),
        )
        setattr(
            cls,
            "America/Boa_Vista",
            PermissibleValue(text="America/Boa_Vista", description="America/Boa_Vista"),
        )
        setattr(
            cls,
            "America/Costa_Rica",
            PermissibleValue(
                text="America/Costa_Rica", description="America/Costa_Rica"
            ),
        )
        setattr(
            cls,
            "America/Bogota",
            PermissibleValue(text="America/Bogota", description="America/Bogota"),
        )
        setattr(
            cls,
            "America/Eirunepe",
            PermissibleValue(text="America/Eirunepe", description="America/Eirunepe"),
        )
        setattr(
            cls,
            "America/Recife",
            PermissibleValue(text="America/Recife", description="America/Recife"),
        )


# Slots
class slots:
    pass


slots.concept_name = Slot(
    uri=WASTH.concept_name,
    name="concept_name",
    curie=WASTH.curie("concept_name"),
    model_uri=WASTH.concept_name,
    domain=None,
    range=Optional[Union[dict, Concept]],
)

slots.broader = Slot(
    uri=SKOS.broader,
    name="broader",
    curie=SKOS.curie("broader"),
    model_uri=WASTH.broader,
    domain=None,
    range=Optional[
        Union[
            Union[dict, BroaderConceptReference],
            list[Union[dict, BroaderConceptReference]],
        ]
    ],
)

slots.narrower = Slot(
    uri=SKOS.narrower,
    name="narrower",
    curie=SKOS.curie("narrower"),
    model_uri=WASTH.narrower,
    domain=None,
    range=Optional[
        Union[
            Union[dict, NarrowerConceptReference],
            list[Union[dict, NarrowerConceptReference]],
        ]
    ],
)

slots.bibliographic_citation = Slot(
    uri=DCTERMS.bibliographicCitation,
    name="bibliographic_citation",
    curie=DCTERMS.curie("bibliographicCitation"),
    model_uri=WASTH.bibliographic_citation,
    domain=None,
    range=Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ],
)

slots.collection_type = Slot(
    uri=WASTH.collection_type,
    name="collection_type",
    curie=WASTH.curie("collection_type"),
    model_uri=WASTH.collection_type,
    domain=None,
    range=Optional[Union[str, "CollectionType"]],
)

slots.resources = Slot(
    uri=WASTH.resources,
    name="resources",
    curie=WASTH.curie("resources"),
    model_uri=WASTH.resources,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, ResourceId], Union[dict, Resource]],
            list[Union[dict, Resource]],
        ]
    ],
)

slots.media = Slot(
    uri=WASTH.media,
    name="media",
    curie=WASTH.curie("media"),
    model_uri=WASTH.media,
    domain=None,
    range=Optional[Union[Union[dict, MediaObject], list[Union[dict, MediaObject]]]],
)

slots.preview_image = Slot(
    uri=WASTH.preview_image,
    name="preview_image",
    curie=WASTH.curie("preview_image"),
    model_uri=WASTH.preview_image,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.provided_image = Slot(
    uri=WASTH.provided_image,
    name="provided_image",
    curie=WASTH.curie("provided_image"),
    model_uri=WASTH.provided_image,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.provided_3d = Slot(
    uri=WASTH.provided_3d,
    name="provided_3d",
    curie=WASTH.curie("provided_3d"),
    model_uri=WASTH.provided_3d,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.resource_service = Slot(
    uri=WASTH.resource_service,
    name="resource_service",
    curie=WASTH.curie("resource_service"),
    model_uri=WASTH.resource_service,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.format = Slot(
    uri=DCTERMS.format,
    name="format",
    curie=DCTERMS.curie("format"),
    model_uri=WASTH.format,
    domain=None,
    range=str,
)

slots.scale = Slot(
    uri=WASTH.scale,
    name="scale",
    curie=WASTH.curie("scale"),
    model_uri=WASTH.scale,
    domain=None,
    range=Optional[float],
)

slots.work_rights = Slot(
    uri=LIDO.rightsWorkSet,
    name="work_rights",
    curie=LIDO.curie("rightsWorkSet"),
    model_uri=WASTH.work_rights,
    domain=None,
    range=Optional[Union[Union[dict, Right], list[Union[dict, Right]]]],
)

slots.credit = Slot(
    uri=WASTH.credit,
    name="credit",
    curie=WASTH.curie("credit"),
    model_uri=WASTH.credit,
    domain=None,
    range=Optional[str],
)

slots.refid_type = Slot(
    uri=WASTH.refid_type,
    name="refid_type",
    curie=WASTH.curie("refid_type"),
    model_uri=WASTH.refid_type,
    domain=None,
    range=Optional[Union[str, "ReferenceType"]],
)

slots.refid = Slot(
    uri=DCTERMS.identifier,
    name="refid",
    curie=DCTERMS.curie("identifier"),
    model_uri=WASTH.refid,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.measurements = Slot(
    uri=WASTH.measurements,
    name="measurements",
    curie=WASTH.curie("measurements"),
    model_uri=WASTH.measurements,
    domain=None,
    range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]],
)

slots.material = Slot(
    uri=CRM.E57_Material,
    name="material",
    curie=CRM.curie("E57_Material"),
    model_uri=WASTH.material,
    domain=None,
    range=Optional[Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]],
)

slots.technique = Slot(
    uri=VRA.Technique,
    name="technique",
    curie=VRA.curie("Technique"),
    model_uri=WASTH.technique,
    domain=None,
    range=Optional[Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]],
)

slots.format_extent = Slot(
    uri=WASTH.format_extent,
    name="format_extent",
    curie=WASTH.curie("format_extent"),
    model_uri=WASTH.format_extent,
    domain=None,
    range=Optional[Union[dict, TypedReference]],
)

slots.unit = Slot(
    uri=WASTH.unit,
    name="unit",
    curie=WASTH.curie("unit"),
    model_uri=WASTH.unit,
    domain=None,
    range=Optional[Union[dict, TypedReference]],
)

slots.style_period = Slot(
    uri=WASTH.style_period,
    name="style_period",
    curie=WASTH.curie("style_period"),
    model_uri=WASTH.style_period,
    domain=None,
    range=Optional[Union[Union[dict, StylePeriod], list[Union[dict, StylePeriod]]]],
)

slots.culture = Slot(
    uri=WASTH.culture,
    name="culture",
    curie=WASTH.curie("culture"),
    model_uri=WASTH.culture,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ],
)

slots.source = Slot(
    uri=WASTH.source,
    name="source",
    curie=WASTH.curie("source"),
    model_uri=WASTH.source,
    domain=None,
    range=Optional[Union[dict, LegalBody]],
)

slots.rights = Slot(
    uri=WASTH.rights,
    name="rights",
    curie=WASTH.curie("rights"),
    model_uri=WASTH.rights,
    domain=None,
    range=Optional[Union[Union[dict, Right], list[Union[dict, Right]]]],
)

slots.related_events = Slot(
    uri=WASTH.related_events,
    name="related_events",
    curie=WASTH.curie("related_events"),
    model_uri=WASTH.related_events,
    domain=None,
    range=Optional[Union[Union[dict, RelatedEvent], list[Union[dict, RelatedEvent]]]],
)

slots.title = Slot(
    uri=DCTERMS.title,
    name="title",
    curie=DCTERMS.curie("title"),
    model_uri=WASTH.title,
    domain=None,
    range=Optional[str],
)

slots.id = Slot(
    uri=DCTERMS.identifier,
    name="id",
    curie=DCTERMS.curie("identifier"),
    model_uri=WASTH.id,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.author = Slot(
    uri=DCTERMS.contributor,
    name="author",
    curie=DCTERMS.curie("contributor"),
    model_uri=WASTH.author,
    domain=None,
    range=Optional[Union[str, OrcidId]],
)

slots.authors = Slot(
    uri=DCTERMS.contributor,
    name="authors",
    curie=DCTERMS.curie("contributor"),
    model_uri=WASTH.authors,
    domain=None,
    range=Optional[Union[Union[str, OrcidId], list[Union[str, OrcidId]]]],
)

slots.record_date = Slot(
    uri=DCTERMS.created,
    name="record_date",
    curie=DCTERMS.curie("created"),
    model_uri=WASTH.record_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.description = Slot(
    uri=DCTERMS.description,
    name="description",
    curie=DCTERMS.curie("description"),
    model_uri=WASTH.description,
    domain=None,
    range=Optional[str],
)

slots.category = Slot(
    uri=TERM.lidoCategory,
    name="category",
    curie=TERM.curie("lidoCategory"),
    model_uri=WASTH.category,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.identifiers = Slot(
    uri=WASTH.identifiers,
    name="identifiers",
    curie=WASTH.curie("identifiers"),
    model_uri=WASTH.identifiers,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ],
)

slots.record_rights = Slot(
    uri=WASTH.record_rights,
    name="record_rights",
    curie=WASTH.curie("record_rights"),
    model_uri=WASTH.record_rights,
    domain=None,
    range=Optional[Union[Union[dict, Right], list[Union[dict, Right]]]],
)

slots.legal_body = Slot(
    uri=WASTH.legal_body,
    name="legal_body",
    curie=WASTH.curie("legal_body"),
    model_uri=WASTH.legal_body,
    domain=None,
    range=Union[dict, LegalBody],
)

slots.content = Slot(
    uri=LIDO.descriptiveNoteValue,
    name="content",
    curie=LIDO.curie("descriptiveNoteValue"),
    model_uri=WASTH.content,
    domain=None,
    range=Optional[str],
)

slots.site = Slot(
    uri=WASTH.site,
    name="site",
    curie=WASTH.curie("site"),
    model_uri=WASTH.site,
    domain=None,
    range=Union[dict, Site],
)

slots.srs_name = Slot(
    uri=WASTH.srs_name,
    name="srs_name",
    curie=WASTH.curie("srs_name"),
    model_uri=WASTH.srs_name,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.geonameid = Slot(
    uri=WASTH["geonames/geonameid"],
    name="geonameid",
    curie=WASTH.curie("geonames/geonameid"),
    model_uri=WASTH.geonameid,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=GEONAMES.name,
    name="name",
    curie=GEONAMES.curie("name"),
    model_uri=WASTH.name,
    domain=None,
    range=Optional[str],
)

slots.asciiname = Slot(
    uri=WASTH["geonames/asciiname"],
    name="asciiname",
    curie=WASTH.curie("geonames/asciiname"),
    model_uri=WASTH.asciiname,
    domain=None,
    range=Optional[str],
)

slots.alternatenames = Slot(
    uri=GEONAMES.alternatenames,
    name="alternatenames",
    curie=GEONAMES.curie("alternatenames"),
    model_uri=WASTH.alternatenames,
    domain=None,
    range=Optional[str],
)

slots.latitude = Slot(
    uri=WGS84.lat,
    name="latitude",
    curie=WGS84.curie("lat"),
    model_uri=WASTH.latitude,
    domain=None,
    range=Optional[Union[float, Latitude]],
)

slots.longitude = Slot(
    uri=WGS84.long,
    name="longitude",
    curie=WGS84.curie("long"),
    model_uri=WASTH.longitude,
    domain=None,
    range=Optional[Union[float, Longitude]],
)

slots.feature_class = Slot(
    uri=GEONAMES.featureClass,
    name="feature class",
    curie=GEONAMES.curie("featureClass"),
    model_uri=WASTH.feature_class,
    domain=None,
    range=Optional[Union[str, "FeatureClassEnum"]],
)

slots.feature_code = Slot(
    uri=GEONAMES.featureCode,
    name="feature code",
    curie=GEONAMES.curie("featureCode"),
    model_uri=WASTH.feature_code,
    domain=None,
    range=Optional[Union[str, "FeatureCodeEnum"]],
)

slots.country_code = Slot(
    uri=GEONAMES.countryCode,
    name="country code",
    curie=GEONAMES.curie("countryCode"),
    model_uri=WASTH.country_code,
    domain=None,
    range=Optional[Union[str, "CountryCodeEnum"]],
)

slots.cc2 = Slot(
    uri=WASTH["geonames/cc2"],
    name="cc2",
    curie=WASTH.curie("geonames/cc2"),
    model_uri=WASTH.cc2,
    domain=None,
    range=Optional[str],
)

slots.admin1_code = Slot(
    uri=WASTH["geonames/admin1_code"],
    name="admin1 code",
    curie=WASTH.curie("geonames/admin1_code"),
    model_uri=WASTH.admin1_code,
    domain=None,
    range=Optional[int],
)

slots.admin2_code = Slot(
    uri=WASTH["geonames/admin2_code"],
    name="admin2 code",
    curie=WASTH.curie("geonames/admin2_code"),
    model_uri=WASTH.admin2_code,
    domain=None,
    range=Optional[int],
)

slots.admin3_code = Slot(
    uri=WASTH["geonames/admin3_code"],
    name="admin3 code",
    curie=WASTH.curie("geonames/admin3_code"),
    model_uri=WASTH.admin3_code,
    domain=None,
    range=Optional[int],
)

slots.admin4_code = Slot(
    uri=WASTH["geonames/admin4_code"],
    name="admin4 code",
    curie=WASTH.curie("geonames/admin4_code"),
    model_uri=WASTH.admin4_code,
    domain=None,
    range=Optional[str],
)

slots.population = Slot(
    uri=GEONAMES.population,
    name="population",
    curie=GEONAMES.curie("population"),
    model_uri=WASTH.population,
    domain=None,
    range=Optional[int],
)

slots.elevation = Slot(
    uri=WASTH["geonames/elevation"],
    name="elevation",
    curie=WASTH.curie("geonames/elevation"),
    model_uri=WASTH.elevation,
    domain=None,
    range=Optional[int],
)

slots.dem = Slot(
    uri=WASTH["geonames/dem"],
    name="dem",
    curie=WASTH.curie("geonames/dem"),
    model_uri=WASTH.dem,
    domain=None,
    range=Optional[int],
)

slots.timezone = Slot(
    uri=WASTH["geonames/timezone"],
    name="timezone",
    curie=WASTH.curie("geonames/timezone"),
    model_uri=WASTH.timezone,
    domain=None,
    range=Optional[Union[str, "TimezoneEnum"]],
)

slots.modification_date = Slot(
    uri=WASTH["geonames/modification_date"],
    name="modification date",
    curie=WASTH.curie("geonames/modification_date"),
    model_uri=WASTH.modification_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.container__works = Slot(
    uri=WASTH.works,
    name="container__works",
    curie=WASTH.curie("works"),
    model_uri=WASTH.container__works,
    domain=None,
    range=Optional[
        Union[dict[Union[str, WorkId], Union[dict, Work]], list[Union[dict, Work]]]
    ],
)

slots.container__concepts = Slot(
    uri=WASTH.concepts,
    name="container__concepts",
    curie=WASTH.curie("concepts"),
    model_uri=WASTH.container__concepts,
    domain=None,
    range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]],
)

slots.container__places = Slot(
    uri=WASTH.places,
    name="container__places",
    curie=WASTH.curie("places"),
    model_uri=WASTH.container__places,
    domain=None,
    range=Optional[
        Union[
            dict[Union[int, GeonamesFeatureGeonameid], Union[dict, GeonamesFeature]],
            list[Union[dict, GeonamesFeature]],
        ]
    ],
)

slots.concept__concept_type = Slot(
    uri=WASTH.concept_type,
    name="concept__concept_type",
    curie=WASTH.curie("concept_type"),
    model_uri=WASTH.concept__concept_type,
    domain=None,
    range=Optional[Union[str, "ConceptType"]],
)

slots.concept__mapping = Slot(
    uri=WASTH.mapping,
    name="concept__mapping",
    curie=WASTH.curie("mapping"),
    model_uri=WASTH.concept__mapping,
    domain=None,
    range=Optional[
        Union[
            Union[dict, MappingConceptReference],
            list[Union[dict, MappingConceptReference]],
        ]
    ],
)

slots.concept__relation = Slot(
    uri=SKOS.related,
    name="concept__relation",
    curie=SKOS.curie("related"),
    model_uri=WASTH.concept__relation,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.broaderConceptReference__broader_match = Slot(
    uri=WASTH.broader_match,
    name="broaderConceptReference__broader_match",
    curie=WASTH.curie("broader_match"),
    model_uri=WASTH.broaderConceptReference__broader_match,
    domain=None,
    range=Union[str, "SkosBroaderRelation"],
)

slots.narrowerConceptReference__narrower_match = Slot(
    uri=WASTH.narrower_match,
    name="narrowerConceptReference__narrower_match",
    curie=WASTH.curie("narrower_match"),
    model_uri=WASTH.narrowerConceptReference__narrower_match,
    domain=None,
    range=Union[str, "SkosNarrowerRelation"],
)

slots.mappingConceptReference__mapping_match = Slot(
    uri=WASTH.mapping_match,
    name="mappingConceptReference__mapping_match",
    curie=WASTH.curie("mapping_match"),
    model_uri=WASTH.mappingConceptReference__mapping_match,
    domain=None,
    range=Union[str, "SkosMappingRelation"],
)

slots.bibliographicCitation__citekey = Slot(
    uri=WASTH.refid,
    name="bibliographicCitation__citekey",
    curie=WASTH.curie("refid"),
    model_uri=WASTH.bibliographicCitation__citekey,
    domain=None,
    range=URIRef,
)

slots.bibliographicCitation__note = Slot(
    uri=WASTH.note,
    name="bibliographicCitation__note",
    curie=WASTH.curie("note"),
    model_uri=WASTH.bibliographicCitation__note,
    domain=None,
    range=Optional[str],
)

slots.relatedWork__relation_type = Slot(
    uri=LIDO.relatedWorkRelType,
    name="relatedWork__relation_type",
    curie=LIDO.curie("relatedWorkRelType"),
    model_uri=WASTH.relatedWork__relation_type,
    domain=None,
    range=Union[str, "RelatedWorkRelType"],
)

slots.largerContextReference__context_type = Slot(
    uri=LIDO.relatedWorkRelType,
    name="largerContextReference__context_type",
    curie=LIDO.curie("relatedWorkRelType"),
    model_uri=WASTH.largerContextReference__context_type,
    domain=None,
    range=Union[str, "LargerContextType"],
)

slots.resource__resource_type = Slot(
    uri=LIDO.relatedWorkRelType,
    name="resource__resource_type",
    curie=LIDO.curie("relatedWorkRelType"),
    model_uri=WASTH.resource__resource_type,
    domain=None,
    range=Union[str, "ResourceType"],
)

slots.resource__perspective = Slot(
    uri=WASTH.perspective,
    name="resource__perspective",
    curie=WASTH.curie("perspective"),
    model_uri=WASTH.resource__perspective,
    domain=None,
    range=int,
)

slots.mediaObject__depiction_type = Slot(
    uri=LIDO.relatedWorkRelType,
    name="mediaObject__depiction_type",
    curie=LIDO.curie("relatedWorkRelType"),
    model_uri=WASTH.mediaObject__depiction_type,
    domain=None,
    range=Union[str, "DepictionType"],
)

slots.measurement__measurement_type = Slot(
    uri=WASTH.measurement_type,
    name="measurement__measurement_type",
    curie=WASTH.curie("measurement_type"),
    model_uri=WASTH.measurement__measurement_type,
    domain=None,
    range=Optional[Union[str, "MeasurementType"]],
)

slots.measurement__measurement_extent = Slot(
    uri=WASTH.measurement_extent,
    name="measurement__measurement_extent",
    curie=WASTH.curie("measurement_extent"),
    model_uri=WASTH.measurement__measurement_extent,
    domain=None,
    range=Optional[Union[dict, TypedReference]],
)

slots.measurement__measurement_value = Slot(
    uri=WASTH.measurement_value,
    name="measurement__measurement_value",
    curie=WASTH.curie("measurement_value"),
    model_uri=WASTH.measurement__measurement_value,
    domain=None,
    range=float,
)

slots.measurement__measurement_qualifier = Slot(
    uri=WASTH.measurement_qualifier,
    name="measurement__measurement_qualifier",
    curie=WASTH.curie("measurement_qualifier"),
    model_uri=WASTH.measurement__measurement_qualifier,
    domain=None,
    range=Optional[Union[str, "MeasurementQualifier"]],
)

slots.measurement__measurement_shape = Slot(
    uri=WASTH.measurement_shape,
    name="measurement__measurement_shape",
    curie=WASTH.curie("measurement_shape"),
    model_uri=WASTH.measurement__measurement_shape,
    domain=None,
    range=Optional[Union[str, TypedReferenceRefid]],
)

slots.measurement__measurement_event = Slot(
    uri=WASTH.measurement_event,
    name="measurement__measurement_event",
    curie=WASTH.curie("measurement_event"),
    model_uri=WASTH.measurement__measurement_event,
    domain=None,
    range=Optional[Union[dict, Event]],
)

slots.materialTech__material_tech_type = Slot(
    uri=WASTH.material_tech_type,
    name="materialTech__material_tech_type",
    curie=WASTH.curie("material_tech_type"),
    model_uri=WASTH.materialTech__material_tech_type,
    domain=None,
    range=Union[str, "MaterialTechType"],
)

slots.right__rights_type = Slot(
    uri=WASTH.rights_type,
    name="right__rights_type",
    curie=WASTH.curie("rights_type"),
    model_uri=WASTH.right__rights_type,
    domain=None,
    range=Union[str, "RightsType"],
)

slots.right__statement = Slot(
    uri=WASTH.statement,
    name="right__statement",
    curie=WASTH.curie("statement"),
    model_uri=WASTH.right__statement,
    domain=None,
    range=Union[dict, TypedReference],
)

slots.right__earliest_date = Slot(
    uri=WASTH.earliest_date,
    name="right__earliest_date",
    curie=WASTH.curie("earliest_date"),
    model_uri=WASTH.right__earliest_date,
    domain=None,
    range=Optional[Union[dict, EventDate]],
)

slots.right__latest_date = Slot(
    uri=WASTH.latest_date,
    name="right__latest_date",
    curie=WASTH.curie("latest_date"),
    model_uri=WASTH.right__latest_date,
    domain=None,
    range=Optional[Union[dict, EventDate]],
)

slots.right__holder = Slot(
    uri=WASTH.holder,
    name="right__holder",
    curie=WASTH.curie("holder"),
    model_uri=WASTH.right__holder,
    domain=None,
    range=Optional[Union[dict, LegalBody]],
)

slots.legalBody__legal_body_type = Slot(
    uri=WASTH.legal_body_type,
    name="legalBody__legal_body_type",
    curie=WASTH.curie("legal_body_type"),
    model_uri=WASTH.legalBody__legal_body_type,
    domain=None,
    range=Optional[Union[str, "RepositoryType"]],
)

slots.legalBody__weblink = Slot(
    uri=WASTH.weblink,
    name="legalBody__weblink",
    curie=WASTH.curie("weblink"),
    model_uri=WASTH.legalBody__weblink,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.event__event_type = Slot(
    uri=WASTH.event_type,
    name="event__event_type",
    curie=WASTH.curie("event_type"),
    model_uri=WASTH.event__event_type,
    domain=None,
    range=Union[str, "EventType"],
)

slots.event__actor_role = Slot(
    uri=WASTH.actor_role,
    name="event__actor_role",
    curie=WASTH.curie("actor_role"),
    model_uri=WASTH.event__actor_role,
    domain=None,
    range=Optional[Union[Union[dict, Actor], list[Union[dict, Actor]]]],
)

slots.event__start_date = Slot(
    uri=WASTH.start_date,
    name="event__start_date",
    curie=WASTH.curie("start_date"),
    model_uri=WASTH.event__start_date,
    domain=None,
    range=Optional[Union[Union[dict, EventDate], list[Union[dict, EventDate]]]],
)

slots.event__end_date = Slot(
    uri=WASTH.end_date,
    name="event__end_date",
    curie=WASTH.curie("end_date"),
    model_uri=WASTH.event__end_date,
    domain=None,
    range=Optional[Union[Union[dict, EventDate], list[Union[dict, EventDate]]]],
)

slots.event__event_place = Slot(
    uri=WASTH.event_place,
    name="event__event_place",
    curie=WASTH.curie("event_place"),
    model_uri=WASTH.event__event_place,
    domain=None,
    range=Optional[Union[Union[dict, Site], list[Union[dict, Site]]]],
)

slots.event__method = Slot(
    uri=WASTH.method,
    name="event__method",
    curie=WASTH.curie("method"),
    model_uri=WASTH.event__method,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.event__things_present = Slot(
    uri=WASTH.things_present,
    name="event__things_present",
    curie=WASTH.curie("things_present"),
    model_uri=WASTH.event__things_present,
    domain=None,
    range=Optional[Union[Union[dict, RelatedWork], list[Union[dict, RelatedWork]]]],
)

slots.actor__actor_type = Slot(
    uri=WASTH.actor_type,
    name="actor__actor_type",
    curie=WASTH.curie("actor_type"),
    model_uri=WASTH.actor__actor_type,
    domain=None,
    range=Optional[Union[str, "AgentType"]],
)

slots.actor__actor_name = Slot(
    uri=WASTH.actor_name,
    name="actor__actor_name",
    curie=WASTH.curie("actor_name"),
    model_uri=WASTH.actor__actor_name,
    domain=None,
    range=Optional[Union[dict, TypedReference]],
)

slots.actor__role_in_event = Slot(
    uri=WASTH.role_in_event,
    name="actor__role_in_event",
    curie=WASTH.curie("role_in_event"),
    model_uri=WASTH.actor__role_in_event,
    domain=None,
    range=Optional[Union[str, "RoleType"]],
)

slots.actor__actor_qualifier = Slot(
    uri=WASTH.actor_qualifier,
    name="actor__actor_qualifier",
    curie=WASTH.curie("actor_qualifier"),
    model_uri=WASTH.actor__actor_qualifier,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ],
)

slots.actor__actor_extent = Slot(
    uri=WASTH.actor_extent,
    name="actor__actor_extent",
    curie=WASTH.curie("actor_extent"),
    model_uri=WASTH.actor__actor_extent,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ],
)

slots.eventDate__date_type = Slot(
    uri=WASTH.date_type,
    name="eventDate__date_type",
    curie=WASTH.curie("date_type"),
    model_uri=WASTH.eventDate__date_type,
    domain=None,
    range=Union[str, "DateType"],
)

slots.eventDate__date_value = Slot(
    uri=WASTH.date_value,
    name="eventDate__date_value",
    curie=WASTH.curie("date_value"),
    model_uri=WASTH.eventDate__date_value,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.stylePeriod__period_name_type = Slot(
    uri=WASTH.period_name_type,
    name="stylePeriod__period_name_type",
    curie=WASTH.curie("period_name_type"),
    model_uri=WASTH.stylePeriod__period_name_type,
    domain=None,
    range=Union[str, "PeriodNameType"],
)

slots.relatedEvent__event_name = Slot(
    uri=WASTH.event_name,
    name="relatedEvent__event_name",
    curie=WASTH.curie("event_name"),
    model_uri=WASTH.relatedEvent__event_name,
    domain=None,
    range=Union[Union[dict, Event], list[Union[dict, Event]]],
)

slots.thing__title_source = Slot(
    uri=WASTH.title_source,
    name="thing__title_source",
    curie=WASTH.curie("title_source"),
    model_uri=WASTH.thing__title_source,
    domain=None,
    range=Optional[
        Union[
            dict[
                Union[str, BibliographicCitationRefid],
                Union[dict, BibliographicCitation],
            ],
            list[Union[dict, BibliographicCitation]],
        ]
    ],
)

slots.thing__alt_name = Slot(
    uri=WASTH.alt_name,
    name="thing__alt_name",
    curie=WASTH.curie("alt_name"),
    model_uri=WASTH.thing__alt_name,
    domain=None,
    range=Optional[Union[Union[dict, Appellation], list[Union[dict, Appellation]]]],
)

slots.thing__tags = Slot(
    uri=WASTH.tags,
    name="thing__tags",
    curie=WASTH.curie("tags"),
    model_uri=WASTH.thing__tags,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.thing__temporal = Slot(
    uri=WASTH.temporal,
    name="thing__temporal",
    curie=WASTH.curie("temporal"),
    model_uri=WASTH.thing__temporal,
    domain=None,
    range=Optional[Union[Union[dict, Event], list[Union[dict, Event]]]],
)

slots.thing__repositories = Slot(
    uri=WASTH.repositories,
    name="thing__repositories",
    curie=WASTH.curie("repositories"),
    model_uri=WASTH.thing__repositories,
    domain=None,
    range=Optional[Union[Union[dict, Repository], list[Union[dict, Repository]]]],
)

slots.appellation__label = Slot(
    uri=WASTH.label,
    name="appellation__label",
    curie=WASTH.curie("label"),
    model_uri=WASTH.appellation__label,
    domain=None,
    range=Optional[str],
)

slots.appellation__appellation_preference = Slot(
    uri=WASTH.appellation_preference,
    name="appellation__appellation_preference",
    curie=WASTH.curie("appellation_preference"),
    model_uri=WASTH.appellation__appellation_preference,
    domain=None,
    range=Optional[Union[str, "LabelType"]],
)

slots.appellation__title_type = Slot(
    uri=WASTH.title_type,
    name="appellation__title_type",
    curie=WASTH.curie("title_type"),
    model_uri=WASTH.appellation__title_type,
    domain=None,
    range=Optional[Union[str, "TitleType"]],
)

slots.repository__repository_type = Slot(
    uri=WASTH.repository_type,
    name="repository__repository_type",
    curie=WASTH.curie("repository_type"),
    model_uri=WASTH.repository__repository_type,
    domain=None,
    range=Optional[Union[str, "RepositoryType"]],
)

slots.work__title_type = Slot(
    uri=WASTH.title_type,
    name="work__title_type",
    curie=WASTH.curie("title_type"),
    model_uri=WASTH.work__title_type,
    domain=None,
    range=Union[str, "TitleType"],
)

slots.work__work_type_condition = Slot(
    uri=TERM.lido00937,
    name="work__work_type_condition",
    curie=TERM.curie("lido00937"),
    model_uri=WASTH.work__work_type_condition,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__work_type_form = Slot(
    uri=TERM.lido00766,
    name="work__work_type_form",
    curie=TERM.curie("lido00766"),
    model_uri=WASTH.work__work_type_form,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__work_type_function = Slot(
    uri=TERM.lido00767,
    name="work__work_type_function",
    curie=TERM.curie("lido00767"),
    model_uri=WASTH.work__work_type_function,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__work_type_context = Slot(
    uri=TERM.lido00934,
    name="work__work_type_context",
    curie=TERM.curie("lido00934"),
    model_uri=WASTH.work__work_type_context,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__work_type_material_tech = Slot(
    uri=TERM.lido00789,
    name="work__work_type_material_tech",
    curie=TERM.curie("lido00789"),
    model_uri=WASTH.work__work_type_material_tech,
    domain=None,
    range=Optional[Union[Union[dict, MaterialTech], list[Union[dict, MaterialTech]]]],
)

slots.work__work_type_subject = Slot(
    uri=TERM.lido00768,
    name="work__work_type_subject",
    curie=TERM.curie("lido00768"),
    model_uri=WASTH.work__work_type_subject,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__work_type_use = Slot(
    uri=TERM.lido00938,
    name="work__work_type_use",
    curie=TERM.curie("lido00938"),
    model_uri=WASTH.work__work_type_use,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__classification_genre = Slot(
    uri=TERM.lido00853,
    name="work__classification_genre",
    curie=TERM.curie("lido00853"),
    model_uri=WASTH.work__classification_genre,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__classification_subject = Slot(
    uri=TERM.lido00932,
    name="work__classification_subject",
    curie=TERM.curie("lido00932"),
    model_uri=WASTH.work__classification_subject,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__classification_local = Slot(
    uri=TERM.lido01135,
    name="work__classification_local",
    curie=TERM.curie("lido01135"),
    model_uri=WASTH.work__classification_local,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__classification_special = Slot(
    uri=TERM.lido01144,
    name="work__classification_special",
    curie=TERM.curie("lido01144"),
    model_uri=WASTH.work__classification_special,
    domain=None,
    range=Optional[
        Union[Union[dict, ConceptReference], list[Union[dict, ConceptReference]]]
    ],
)

slots.work__part_of = Slot(
    uri=DCTERMS.isPartOf,
    name="work__part_of",
    curie=DCTERMS.curie("isPartOf"),
    model_uri=WASTH.work__part_of,
    domain=None,
    range=Optional[
        Union[
            Union[dict, LargerContextReference],
            list[Union[dict, LargerContextReference]],
        ]
    ],
)

slots.work__former_site = Slot(
    uri=WASTH.former_site,
    name="work__former_site",
    curie=WASTH.curie("former_site"),
    model_uri=WASTH.work__former_site,
    domain=None,
    range=Optional[Union[Union[dict, Site], list[Union[dict, Site]]]],
)

slots.work__intended_site = Slot(
    uri=WASTH.intended_site,
    name="work__intended_site",
    curie=WASTH.curie("intended_site"),
    model_uri=WASTH.work__intended_site,
    domain=None,
    range=Optional[Union[Union[dict, Site], list[Union[dict, Site]]]],
)

slots.work__other_site = Slot(
    uri=WASTH.other_site,
    name="work__other_site",
    curie=WASTH.curie("other_site"),
    model_uri=WASTH.work__other_site,
    domain=None,
    range=Optional[Union[Union[dict, Site], list[Union[dict, Site]]]],
)

slots.work__location_historic = Slot(
    uri=WASTH.location_historic,
    name="work__location_historic",
    curie=WASTH.curie("location_historic"),
    model_uri=WASTH.work__location_historic,
    domain=None,
    range=Optional[Union[Union[dict, LegalBody], list[Union[dict, LegalBody]]]],
)

slots.work__inscriptions = Slot(
    uri=WASTH.inscriptions,
    name="work__inscriptions",
    curie=WASTH.curie("inscriptions"),
    model_uri=WASTH.work__inscriptions,
    domain=None,
    range=Optional[Union[Union[dict, Inscription], list[Union[dict, Inscription]]]],
)

slots.work__collection = Slot(
    uri=LIDO.collection,
    name="work__collection",
    curie=LIDO.curie("collection"),
    model_uri=WASTH.work__collection,
    domain=None,
    range=Optional[Union[Union[dict, Collection], list[Union[dict, Collection]]]],
)

slots.work__related_works = Slot(
    uri=DCTERMS.related,
    name="work__related_works",
    curie=DCTERMS.curie("related"),
    model_uri=WASTH.work__related_works,
    domain=None,
    range=Optional[Union[Union[dict, RelatedWork], list[Union[dict, RelatedWork]]]],
)

slots.work__subject = Slot(
    uri=LIDO.subjectSet,
    name="work__subject",
    curie=LIDO.curie("subjectSet"),
    model_uri=WASTH.work__subject,
    domain=None,
    range=Optional[Union[Union[dict, Topic], list[Union[dict, Topic]]]],
)

slots.site__name = Slot(
    uri=LIDO.partOfPlace,
    name="site__name",
    curie=LIDO.curie("partOfPlace"),
    model_uri=WASTH.site__name,
    domain=None,
    range=Optional[Union[dict, GeonamesFeature]],
)

slots.site__site_type = Slot(
    uri=WASTH.site_type,
    name="site__site_type",
    curie=WASTH.curie("site_type"),
    model_uri=WASTH.site__site_type,
    domain=None,
    range=Optional[Union[str, "RepositoryType"]],
)

slots.site__location = Slot(
    uri=GEO.hasDefaultGeometry,
    name="site__location",
    curie=GEO.curie("hasDefaultGeometry"),
    model_uri=WASTH.site__location,
    domain=None,
    range=Union[dict, GeographicPoint],
)

slots.site__extent = Slot(
    uri=GEO.hasGeometry,
    name="site__extent",
    curie=GEO.curie("hasGeometry"),
    model_uri=WASTH.site__extent,
    domain=None,
    range=Optional[Union[dict, GeographicExtent]],
)

slots.site__event_place_type = Slot(
    uri=WASTH.event_place_type,
    name="site__event_place_type",
    curie=WASTH.curie("event_place_type"),
    model_uri=WASTH.site__event_place_type,
    domain=None,
    range=Optional[Union[str, "EventPlaceType"]],
)

slots.geographicPoint__lat = Slot(
    uri=WASTH.lat,
    name="geographicPoint__lat",
    curie=WASTH.curie("lat"),
    model_uri=WASTH.geographicPoint__lat,
    domain=None,
    range=Union[float, Latitude],
)

slots.geographicPoint__lon = Slot(
    uri=WASTH.lon,
    name="geographicPoint__lon",
    curie=WASTH.curie("lon"),
    model_uri=WASTH.geographicPoint__lon,
    domain=None,
    range=Union[float, Longitude],
)

slots.geographicPoint__alt = Slot(
    uri=WASTH.alt,
    name="geographicPoint__alt",
    curie=WASTH.curie("alt"),
    model_uri=WASTH.geographicPoint__alt,
    domain=None,
    range=Optional[float],
)

slots.geographicPoint__zoom = Slot(
    uri=WASTH.zoom,
    name="geographicPoint__zoom",
    curie=WASTH.curie("zoom"),
    model_uri=WASTH.geographicPoint__zoom,
    domain=None,
    range=Optional[int],
)

slots.geographicExtent__geometry_type = Slot(
    uri=WASTH.geometry_type,
    name="geographicExtent__geometry_type",
    curie=WASTH.curie("geometry_type"),
    model_uri=WASTH.geographicExtent__geometry_type,
    domain=None,
    range=Union[str, "GeometryType"],
)

slots.geographicExtent__coordinates = Slot(
    uri=WASTH.coordinates,
    name="geographicExtent__coordinates",
    curie=WASTH.curie("coordinates"),
    model_uri=WASTH.geographicExtent__coordinates,
    domain=None,
    range=Union[str, GeoJSONCoordinateArray],
)

slots.inscription__inscription_type = Slot(
    uri=WASTH.inscription_type,
    name="inscription__inscription_type",
    curie=WASTH.curie("inscription_type"),
    model_uri=WASTH.inscription__inscription_type,
    domain=None,
    range=Union[str, "InscriptionType"],
)

slots.topic__topic_type = Slot(
    uri=WASTH.topic_type,
    name="topic__topic_type",
    curie=WASTH.curie("topic_type"),
    model_uri=WASTH.topic__topic_type,
    domain=None,
    range=Union[str, "SubjectType"],
)

slots.collection__collection_type = Slot(
    uri=WASTH.collection_type,
    name="collection__collection_type",
    curie=WASTH.curie("collection_type"),
    model_uri=WASTH.collection__collection_type,
    domain=None,
    range=Union[str, "CollectionType"],
)

slots.Concept_content = Slot(
    uri=SKOS.scopeNote,
    name="Concept_content",
    curie=SKOS.curie("scopeNote"),
    model_uri=WASTH.Concept_content,
    domain=Concept,
    range=Optional[str],
)

slots.Resource_id = Slot(
    uri=DCTERMS.identifier,
    name="Resource_id",
    curie=DCTERMS.curie("identifier"),
    model_uri=WASTH.Resource_id,
    domain=Resource,
    range=Union[str, ResourceId],
)

slots.Resource_category = Slot(
    uri=TERM.lidoCategory,
    name="Resource_category",
    curie=TERM.curie("lidoCategory"),
    model_uri=WASTH.Resource_category,
    domain=Resource,
    range=Optional[Union[str, URIorCURIE]],
)

slots.MediaObject_title = Slot(
    uri=DCTERMS.title,
    name="MediaObject_title",
    curie=DCTERMS.curie("title"),
    model_uri=WASTH.MediaObject_title,
    domain=MediaObject,
    range=str,
)

slots.MediaObject_description = Slot(
    uri=DCTERMS.description,
    name="MediaObject_description",
    curie=DCTERMS.curie("description"),
    model_uri=WASTH.MediaObject_description,
    domain=MediaObject,
    range=str,
)

slots.MediaObject_content = Slot(
    uri=LIDO.descriptiveNoteValue,
    name="MediaObject_content",
    curie=LIDO.curie("descriptiveNoteValue"),
    model_uri=WASTH.MediaObject_content,
    domain=MediaObject,
    range=Optional[str],
)

slots.MediaObject_work_rights = Slot(
    uri=LIDO.rightsWorkSet,
    name="MediaObject_work_rights",
    curie=LIDO.curie("rightsWorkSet"),
    model_uri=WASTH.MediaObject_work_rights,
    domain=MediaObject,
    range=Union[Union[dict, Right], list[Union[dict, Right]]],
)

slots.TypedReference_refid = Slot(
    uri=DCTERMS.identifier,
    name="TypedReference_refid",
    curie=DCTERMS.curie("identifier"),
    model_uri=WASTH.TypedReference_refid,
    domain=TypedReference,
    range=Union[str, TypedReferenceRefid],
)

slots.Measurement_unit = Slot(
    uri=WASTH.unit,
    name="Measurement_unit",
    curie=WASTH.curie("unit"),
    model_uri=WASTH.Measurement_unit,
    domain=Measurement,
    range=Union[dict, TypedReference],
)

slots.LegalBody_identifiers = Slot(
    uri=WASTH.identifiers,
    name="LegalBody_identifiers",
    curie=WASTH.curie("identifiers"),
    model_uri=WASTH.LegalBody_identifiers,
    domain=LegalBody,
    range=Optional[
        Union[
            dict[Union[str, TypedReferenceRefid], Union[dict, TypedReference]],
            list[Union[dict, TypedReference]],
        ]
    ],
)

slots.LegalBody_category = Slot(
    uri=TERM.lidoCategory,
    name="LegalBody_category",
    curie=TERM.curie("lidoCategory"),
    model_uri=WASTH.LegalBody_category,
    domain=LegalBody,
    range=Optional[Union[str, URIorCURIE]],
)

slots.Event_title = Slot(
    uri=DCTERMS.title,
    name="Event_title",
    curie=DCTERMS.curie("title"),
    model_uri=WASTH.Event_title,
    domain=Event,
    range=Optional[str],
)

slots.Event_description = Slot(
    uri=DCTERMS.description,
    name="Event_description",
    curie=DCTERMS.curie("description"),
    model_uri=WASTH.Event_description,
    domain=Event,
    range=Optional[str],
)

slots.Event_content = Slot(
    uri=LIDO.descriptiveNoteValue,
    name="Event_content",
    curie=LIDO.curie("descriptiveNoteValue"),
    model_uri=WASTH.Event_content,
    domain=Event,
    range=Optional[str],
)

slots.Work_id = Slot(
    uri=DCTERMS.identifier,
    name="Work_id",
    curie=DCTERMS.curie("identifier"),
    model_uri=WASTH.Work_id,
    domain=Work,
    range=Union[str, WorkId],
)

slots.Work_title = Slot(
    uri=DCTERMS.title,
    name="Work_title",
    curie=DCTERMS.curie("title"),
    model_uri=WASTH.Work_title,
    domain=Work,
    range=str,
)

slots.Work_record_date = Slot(
    uri=DCTERMS.created,
    name="Work_record_date",
    curie=DCTERMS.curie("created"),
    model_uri=WASTH.Work_record_date,
    domain=Work,
    range=Union[str, XSDDate],
)

slots.Work_description = Slot(
    uri=DCTERMS.description,
    name="Work_description",
    curie=DCTERMS.curie("description"),
    model_uri=WASTH.Work_description,
    domain=Work,
    range=str,
)

slots.Work_category = Slot(
    uri=TERM.lidoCategory,
    name="Work_category",
    curie=TERM.curie("lidoCategory"),
    model_uri=WASTH.Work_category,
    domain=Work,
    range=Optional[Union[str, URIorCURIE]],
)

slots.Work_resources = Slot(
    uri=WASTH.resources,
    name="Work_resources",
    curie=WASTH.curie("resources"),
    model_uri=WASTH.Work_resources,
    domain=Work,
    range=Optional[
        Union[
            dict[Union[str, ResourceId], Union[dict, Resource]],
            list[Union[dict, Resource]],
        ]
    ],
)

slots.Work_media = Slot(
    uri=WASTH.media,
    name="Work_media",
    curie=WASTH.curie("media"),
    model_uri=WASTH.Work_media,
    domain=Work,
    range=Optional[Union[Union[dict, MediaObject], list[Union[dict, MediaObject]]]],
)

slots.Work_record_rights = Slot(
    uri=WASTH.record_rights,
    name="Work_record_rights",
    curie=WASTH.curie("record_rights"),
    model_uri=WASTH.Work_record_rights,
    domain=Work,
    range=Union[Union[dict, Right], list[Union[dict, Right]]],
)

slots.Work_work_rights = Slot(
    uri=LIDO.rightsWorkSet,
    name="Work_work_rights",
    curie=LIDO.curie("rightsWorkSet"),
    model_uri=WASTH.Work_work_rights,
    domain=Work,
    range=Union[Union[dict, Right], list[Union[dict, Right]]],
)

slots.Work_content = Slot(
    uri=LIDO.descriptiveNoteValue,
    name="Work_content",
    curie=LIDO.curie("descriptiveNoteValue"),
    model_uri=WASTH.Work_content,
    domain=Work,
    range=Optional[str],
)

slots.Topic_concept_name = Slot(
    uri=WASTH.concept_name,
    name="Topic_concept_name",
    curie=WASTH.curie("concept_name"),
    model_uri=WASTH.Topic_concept_name,
    domain=Topic,
    range=Union[dict, Concept],
)
