from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, ClassVar, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel


metamodel_version = "1.12.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True,
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "wasth",
        "default_range": "string",
        "description": "## Orientações gerais\n"
        "\n"
        "Todas as fichas dos projetos dos Documentários da arquitetura "
        "tradicional são\n"
        "arquivos de texto sem formatação, que podem ser criados e "
        "editados em\n"
        "programas como o Notepad++, Sublime Text, ou Zettlr, entre "
        "muitos outros.\n"
        "Elas podem, também, ser criadas e editadas diretamente online "
        "no repositório\n"
        "do GitHub.\n"
        "\n"
        "> ⚠️ As fichas **não** devem ser criadas nem editadas em "
        "processadores\n"
        "> de texto formatado, tais como Microsoft Word, Google Docs, "
        "ou LibreOffice.\n"
        "\n"
        "A ficha se divide em dois blocos\u2009:\n"
        "um bloco de metadados delimitado por linhas contendo apenas "
        "três hífens `---` e\n"
        "um bloco de conteúdo com texto livre.\n"
        "\n"
        "Os metadados são formatados segundo a especificação [YAML].\n"
        "O conteúdo é formatado segundo a especificação [Markdown],\n"
        "e pode incluir formatação específica do [Pandoc].\n"
        "\n"
        "Quanto às informações que devem ser inseridas na ficha,\n"
        "(quase) todos os campos são definidos pela especificação "
        "[LIDO] e,\n"
        "na medida do possível, têm uma equivalência com o "
        "[DublinCore].\n"
        "\n"
        "Na medida do possível, buscamos também adequar o conteúdo das "
        "fichas às\n"
        "normas de preenchimento das fichas de Cadastro (M301, M302) "
        "do\n"
        "Sistema Integrado de Conhecimento e Gestão ([SICG]) do\n"
        "Instituto do Patrimônio Histórico e Artístico Nacional "
        "(IPHAN).\n"
        "\n"
        "[YAML]: https://www.yaml.info/learn/index.html\n"
        "\n"
        "[Markdown]: "
        "https://programminghistorian.org/pt/licoes/introducao-ao-markdown\n"
        "\n"
        "[Pandoc]: "
        "https://programminghistorian.org/pt/licoes/autoria-sustentavel-texto-simples-pandoc-markdown\n"
        "\n"
        "[LIDO]: "
        "https://icom-documentation.mini.icom.museum/working-groups/lido/lido-overview/\n"
        "\n"
        "[DublinCore]: "
        "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/\n"
        "\n"
        "[SICG]: https://sicg.iphan.gov.br/sicg/manual/manual.html\n"
        "\n"
        "\n"
        "## Antes de começar\n"
        "\n"
        "Para contribuir com os Documentários da Arquitetura "
        "Tradicional, você ou\n"
        "o seu grupo de pesquisa precisa ter sua própria versão dos "
        "repositórios.\n"
        "\n"
        "Comece aprendendo um pouco sobre como trabalhar com controle "
        "de versão no Git e\n"
        "no GitHub, estudando [estes tutoriais em\n"
        "português](https://programminghistorian.org/pt/licoes/git-ferramenta-metodologica-projetos-historia-1)\n"
        "no site [Programming Historian].\n"
        "Em Windows ou MacOS, o jeito mais fácil de trabalhar com "
        "repositórios de dados\n"
        "no GitHub é instalando o [GitHub Desktop].\n"
        "No Linux, há outras opções, como o [SmartGit]\n"
        "(também disponível para Windows e MacOS).\n"
        "\n"
        "Em seguida, precisa **bifurcar** (fork) o repositório no qual "
        "vai trabalhar,\n"
        "provavelmente à partida o repositório da\n"
        "[Casa tradicional](https://github.com/arqtrad/casa/),\n"
        "usando o botão `Fork 🔽` como ilustrado abaixo\u2009:\n"
        "\n"
        '<img alt="Captura de tela"\n'
        " "
        'src="https://github.com/user-attachments/assets/6c22dcec-b8e1-4688-a504-d9ea640bdc43"\n'
        "/>\n"
        "\n"
        "A partir daí, pode trabalhar livremente na sua própria cópia "
        "do repositório,\n"
        "usando as ferramentas `🔄 Sync fork` e  `⤴️ Contribute` para, "
        "respectivamente,\n"
        "obter periodicamente atualizações *vindas do* repositório "
        "principal e\n"
        "propor as suas contribuições *para o* repositório principal.\n"
        "\n"
        '<img alt="Captura de tela"\n'
        " "
        'src="https://github.com/user-attachments/assets/25905e40-99ef-4b23-b33e-cfe586c41001"\n'
        "/>\n"
        "\n"
        '<img alt="Captura de tela"\n'
        " "
        'src="https://github.com/user-attachments/assets/b5f6ef50-c122-4f01-8ec9-b16207a9b63d"\n'
        "/>\n"
        "\n"
        "Poderá então abrir uma solicitação de integração das suas "
        "alterações\n"
        "ao repositório principal (**pull request**):\n"
        "\n"
        '<img alt="Captura de tela"\n'
        " "
        'src="https://github.com/user-attachments/assets/56de1236-6fa0-47f3-9e94-06218dace0a8"\n'
        "/>\n"
        "\n"
        "Se não estiver à vontade para manipular diretamente os "
        "repositórios do GitHub,\n"
        "sempre pode contribuir informações, sugestões ou desejos no\n"
        "[Fórum de discussão] deste projeto de pesquisa.\n"
        "Se tiver contribuições pontuais sobre fichas específicas, "
        "formatos ou lacunas,\n"
        "pode também abrir uma [*issue* no repositório da Casa].\n"
        "\n"
        "\n"
        "## Por onde começo\u2009?\n"
        "\n"
        "> Leia a especificação da ficha **[Work](Work/)** para saber "
        "como preencher\n"
        "> as fichas de edificações dos Documentários da Arquitetura "
        "Tradicional.\n"
        "\n"
        "\n"
        "[Programming Historian]: "
        "https://programminghistorian.org/pt/\n"
        "\n"
        "[GitHub Desktop]: "
        "https://github.com/apps/desktop?locale=pt-br\n"
        "\n"
        "[SmartGit]: https://www.smartgit.dev/\n"
        "\n"
        "[Fórum de discussão]: "
        "https://github.com/orgs/arqtrad/discussions\n"
        "\n"
        "[*issue* no repositório da Casa]: "
        "https://github.com/arqtrad/casa/issues\n"
        "\n"
        "[Zotero]: "
        "https://www.zotero.org/groups/2495935/arquitetura_tradicional_luso-brasileira/\n"
        "\n"
        "[Global Building Atlas]: "
        "https://github.com/zhu-xlab/GlobalBuildingAtlas\n"
        "\n"
        "[QGIS]: https://qgis.org/\n"
        "\n"
        "[ORCiD]: https://orcid.org/\n"
        "\n"
        "[SIPA]: https://monumentos.gov.pt/\n"
        "\n"
        "[HPIP]: https://hpip.org/\n"
        "\n"
        "[iPatrimonio]: https://ipatrimonio.org/\n"
        "\n"
        "[VRA Core]: https://www.loc.gov/standards/vracore/\n"
        "\n"
        "[ULAN]: "
        "https://www.getty.edu/research/tools/vocabularies/ulan\n"
        "\n"
        "[IIIF]: https://iiif.io/\n"
        "\n"
        "[lista de tipos de mídia IANA]: "
        "https://www.iana.org/assignments/media-types\n",
        "id": "https://tradicional.arq.br/schema",
        "imports": [
            "linkml:types",
            "classes/concept",
            "classes/resource",
            "classes/shared",
            "classes/temporal",
            "classes/thing",
            "classes/work",
            "classes/geonames",
        ],
        "license": "MIT",
        "name": "arqtrad_schema",
        "prefixes": {
            "EPSG": {
                "prefix_prefix": "EPSG",
                "prefix_reference": "http://www.opengis.net/def/crs/EPSG/0/",
            },
            "aat": {
                "prefix_prefix": "aat",
                "prefix_reference": "http://vocab.getty.edu/aat/",
            },
            "crm": {
                "prefix_prefix": "crm",
                "prefix_reference": "http://www.cidoc-crm.org/cidoc-crm/",
            },
            "dcterms": {
                "prefix_prefix": "dcterms",
                "prefix_reference": "http://purl.org/dc/terms/",
            },
            "dctypes": {
                "prefix_prefix": "dctypes",
                "prefix_reference": "http://purl.org/dc/dcmitype/",
            },
            "doi": {"prefix_prefix": "doi", "prefix_reference": "https://doi.org/"},
            "geo": {
                "prefix_prefix": "geo",
                "prefix_reference": "http://www.opengis.net/ont/geosparql#",
            },
            "geonames": {
                "prefix_prefix": "geonames",
                "prefix_reference": "https://www.geonames.org/ontology#",
            },
            "isni": {
                "prefix_prefix": "isni",
                "prefix_reference": "https://isni.org/isni/",
            },
            "iso": {
                "prefix_prefix": "iso",
                "prefix_reference": "http://purl.org/iso25964/skos-thes#",
            },
            "la": {
                "prefix_prefix": "la",
                "prefix_reference": "https://linked.art/ns/terms/",
            },
            "lido": {
                "prefix_prefix": "lido",
                "prefix_reference": "http://www.lido-schema.org/",
            },
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            },
            "rdfs": {
                "prefix_prefix": "rdfs",
                "prefix_reference": "http://www.w3.org/2000/01/rdf-schema#",
            },
            "schema": {
                "prefix_prefix": "schema",
                "prefix_reference": "http://schema.org/",
            },
            "skos": {
                "prefix_prefix": "skos",
                "prefix_reference": "http://www.w3.org/2004/02/skos/core#",
            },
            "term": {
                "prefix_prefix": "term",
                "prefix_reference": "http://terminology.lido-schema.org/",
            },
            "tgn": {
                "prefix_prefix": "tgn",
                "prefix_reference": "http://vocab.getty.edu/tgn/",
            },
            "ucum": {
                "prefix_prefix": "ucum",
                "prefix_reference": "http://purl.oclc.org/NET/muo/ucum/",
            },
            "ulan": {
                "prefix_prefix": "ulan",
                "prefix_reference": "http://vocab.getty.edu/ulan/",
            },
            "unesco": {
                "prefix_prefix": "unesco",
                "prefix_reference": "http://vocabularies.unesco.org/thesaurus/",
            },
            "vra": {"prefix_prefix": "vra", "prefix_reference": "http://purl.org/vra/"},
            "wasth": {
                "prefix_prefix": "wasth",
                "prefix_reference": "https://tradicional.arq.br/schema/",
            },
            "wd": {
                "prefix_prefix": "wd",
                "prefix_reference": "http://www.wikidata.org/entity/",
            },
        },
        "see_also": ["https://tradicional.arq.br/schema"],
        "settings": {
            "geojson_multi": {
                "setting_key": "geojson_multi",
                "setting_value": "\\[\\s*{geojson_poly}(?:\\s*,\\s*{geojson_poly})*\\s*\\]",
            },
            "geojson_num": {
                "setting_key": "geojson_num",
                "setting_value": "-?\\d+(?:\\.\\d+)?(?:[eE][+-]?\\d+)?",
            },
            "geojson_poly": {
                "setting_key": "geojson_poly",
                "setting_value": "\\[\\s*{geojson_ring}(?:\\s*,\\s*{geojson_ring})*\\s*\\]",
            },
            "geojson_pos": {
                "setting_key": "geojson_pos",
                "setting_value": "\\[\\s*{geojson_num}\\s*,\\s*{geojson_num}(?:\\s*,\\s*{geojson_num})?\\s*\\]",
            },
            "geojson_ring": {
                "setting_key": "geojson_ring",
                "setting_value": "\\[\\s*{geojson_pos}(?:\\s*,\\s*{geojson_pos}){3,}\\s*\\]",
            },
        },
        "source_file": "src/arqtrad_schema/schema/arqtrad_schema.yaml",
        "title": "Esquema de dados dos Documentários da Arquitetura Tradicional",
        "types": {
            "CslCitekey": {
                "description": "Chave de citação compatível com o "
                "Citation Style Language, começando "
                "com '@'. Obter as chaves de citação "
                "das referências bibliográficas "
                "consultando a nossa biblioteca "
                "compartilhada no Zotero.\n",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "CslCitekey",
                "pattern": "^@[a-zA-Z0-9_][\\w:.#$%&\\-+?<>~/]*$",
                "typeof": "string",
            },
            "GeoJSONCoordinateArray": {
                "description": "JSON array of GeoJSON "
                "positions. The valid "
                "nesting depends on the "
                "associated geometry "
                "type.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "GeoJSONCoordinateArray",
                "structured_pattern": {
                    "interpolated": True,
                    "partial_match": False,
                    "syntax": "^(?:{geojson_poly}|{geojson_multi})$",
                },
                "typeof": "string",
            },
            "Latitude": {
                "description": "Latitude em graus decimais (separador: ponto).",
                "from_schema": "https://tradicional.arq.br/schema",
                "maximum_value": 90,
                "minimum_value": -90,
                "name": "Latitude",
                "typeof": "double",
            },
            "Longitude": {
                "description": "Longitude em graus decimais (separador: ponto).",
                "from_schema": "https://tradicional.arq.br/schema",
                "maximum_value": 180,
                "minimum_value": -180,
                "name": "Longitude",
                "typeof": "double",
            },
            "OlcPlusCode11": {
                "description": "Open Location Code (Plus Code) "
                "com resolução de 11 dígitos.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "OlcPlusCode11",
                "pattern": "^([2-9CFGHJMPQRVWX]{8})\\+([2-9CFGHJMPQRVWX]{3})$",
                "typeof": "string",
            },
            "OrcidId": {
                "description": "ORCID iD, no formato "
                "`orcid:1234-5678-9012-345X` ou\n"
                "`https://orcid.org/1234-5678-9012-345X`.\n",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "OrcidId",
                "pattern": "^(?:https?://orcid\\.org/|orcid:)?\\d{4}-\\d{4}-\\d{4}-\\d{3}[\\dX]$",
                "typeof": "string",
            },
        },
    }
)


class FeatureClassEnum(str, Enum):
    administrativo = "A"
    """
    country, state, region,...
    """
    hidrografia = "H"
    """
    stream, lake, ...
    """
    paisagem = "L"
    """
    parks, area, ...
    """
    povoações = "P"
    """
    city, village,...
    """
    estradas = "R"
    """
    road, railroad
    """
    construções = "S"
    """
    spot, building, farm
    """
    topografia = "T"
    """
    mountain,hill,rock,...
    """
    batimetria = "U"
    """
    undersea
    """
    vegetação = "V"
    """
    forest,heath,...
    """


class FeatureCodeEnum(str, Enum):
    first_order_administrative_division = "ADM1"
    """
    a primary administrative division of a country, such as a state in the United States
    """
    historical_first_order_administrative_division = "ADM1H"
    """
    a former first-order administrative division
    """
    second_order_administrative_division = "ADM2"
    """
    a subdivision of a first-order administrative division
    """
    historical_second_order_administrative_division = "ADM2H"
    """
    a former second-order administrative division
    """
    third_order_administrative_division = "ADM3"
    """
    a subdivision of a second-order administrative division
    """
    historical_third_order_administrative_division = "ADM3H"
    """
    a former third-order administrative division
    """
    fourth_order_administrative_division = "ADM4"
    """
    a subdivision of a third-order administrative division
    """
    historical_fourth_order_administrative_division = "ADM4H"
    """
    a former fourth-order administrative division
    """
    fifth_order_administrative_division = "ADM5"
    """
    a subdivision of a fourth-order administrative division
    """
    historical_fifth_order_administrative_division = "ADM5H"
    """
    a former fifth-order administrative division
    """
    administrative_division = "ADMD"
    """
    an administrative division of a country, undifferentiated as to administrative level
    """
    historical_administrative_division = "ADMDH"
    """
    a former administrative division of a political entity, undifferentiated as to administrative level
    """
    school_district = "ADMS"
    """
    school district
    """
    leased_area = "LTER"
    """
    a tract of land leased to another country, usually for military installations
    """
    political_entity = "PCL"
    dependent_political_entity = "PCLD"
    freely_associated_state = "PCLF"
    historical_political_entity = "PCLH"
    """
    a former political entity
    """
    independent_political_entity = "PCLI"
    section_of_independent_political_entity = "PCLIX"
    semi_independent_political_entity = "PCLS"
    parish = "PRSH"
    """
    an ecclesiastical district
    """
    territory = "TERR"
    zone = "ZN"
    buffer_zone = "ZNB"
    """
    a zone recognized as a buffer between two nations in which military presence is minimal or absent
    """
    seaplane_landing_area = "AIRS"
    """
    a place on a waterbody where floatplanes land and take off
    """
    anchorage = "ANCH"
    """
    an area where vessels may anchor
    """
    bay = "BAY"
    """
    a coastal indentation between two capes or headlands, larger than a cove but smaller than a gulf
    """
    bays = "BAYS"
    """
    coastal indentations between two capes or headlands, larger than a cove but smaller than a gulf
    """
    bightLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BGHT"
    """
    an open body of water forming a slight recession in a coastline
    """
    bankLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BNK"
    """
    an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for most surface navigation
    """
    stream_bank = "BNKR"
    """
    a sloping margin of a stream channel which normally confines the stream to its channel on land
    """
    section_of_bank = "BNKX"
    bogLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BOG"
    """
    a wetland characterized by peat forming sphagnum moss, sedge, and other acid-water plants
    """
    icecap = "CAPG"
    """
    a dome-shaped mass of glacial ice covering an area of mountain summits or other high lands; smaller than an ice sheet
    """
    channel = "CHN"
    """
    the deepest part of a stream, bay, lagoon, or strait, through which the main current flows
    """
    lake_channelLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CHNL"
    """
    that part of a lake having water deep enough for navigation between islands, shoals, etc.
    """
    marine_channel = "CHNM"
    """
    that part of a body of water deep enough for navigation through an area otherwise not suitable
    """
    navigation_channel = "CHNN"
    """
    a buoyed channel of sufficient depth for the safe navigation of vessels
    """
    confluence = "CNFL"
    """
    a place where two or more streams or intermittent streams flow together
    """
    canal = "CNL"
    """
    an artificial watercourse
    """
    aqueduct = "CNLA"
    """
    a conduit used to carry water
    """
    canal_bend = "CNLB"
    """
    a conspicuously curved or bent section of a canal
    """
    drainage_canal = "CNLD"
    """
    an artificial waterway carrying water away from a wetland or from drainage ditches
    """
    irrigation_canal = "CNLI"
    """
    a canal which serves as a main conduit for irrigation water
    """
    navigation_canalLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CNLN"
    """
    a watercourse constructed for navigation of vessels
    """
    abandoned_canal = "CNLQ"
    underground_irrigation_canalLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CNLSB"
    """
    a gently inclined underground tunnel bringing water for irrigation from aquifers
    """
    section_of_canal = "CNLX"
    coveLEFT_PARENTHESISsRIGHT_PARENTHESIS = "COVE"
    """
    a small coastal indentation, smaller than a bay
    """
    tidal_creekLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CRKT"
    """
    a meandering channel in a coastal wetland subject to bi-directional tidal currents
    """
    current = "CRNT"
    """
    a horizontal flow of water in a given direction with uniform velocity
    """
    cutoff = "CUTF"
    """
    a channel formed as a result of a stream cutting through a meander neck
    """
    dockLEFT_PARENTHESISsRIGHT_PARENTHESIS = "DCK"
    """
    a waterway between two piers, or cut into the land for the berthing of ships
    """
    docking_basin = "DCKB"
    """
    a part of a harbor where ships dock
    """
    icecap_dome = "DOMG"
    """
    a comparatively elevated area on an icecap
    """
    icecap_depression = "DPRG"
    """
    a comparatively depressed area on an icecap
    """
    ditch = "DTCH"
    """
    a small artificial watercourse dug for draining or irrigating the land
    """
    drainage_ditch = "DTCHD"
    """
    a ditch which serves to drain the land
    """
    irrigation_ditch = "DTCHI"
    """
    a ditch which serves to distribute irrigation water
    """
    ditch_mouthLEFT_PARENTHESISsRIGHT_PARENTHESIS = "DTCHM"
    """
    an area where a drainage ditch enters a lagoon, lake or bay
    """
    estuary = "ESTY"
    """
    a funnel-shaped stream mouth or embayment where fresh water mixes with sea water under tidal influences
    """
    fishing_area = "FISH"
    """
    a fishing ground, bank or area where fishermen go to catch fish
    """
    fjord = "FJD"
    """
    a long, narrow, steep-walled, deep-water arm of the sea at high latitudes, usually along mountainous coasts
    """
    fjords = "FJDS"
    """
    long, narrow, steep-walled, deep-water arms of the sea at high latitudes, usually along mountainous coasts
    """
    waterfallLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLLS"
    """
    a perpendicular or very steep descent of the water of a stream
    """
    section_of_waterfallLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLLSX"
    mud_flatLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLTM"
    """
    a relatively level area of mud either between high and low tide lines, or subject to flooding
    """
    tidal_flatLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLTT"
    """
    a large flat area of mud or sand attached to the shore and alternately covered and uncovered by the tide
    """
    glacierLEFT_PARENTHESISsRIGHT_PARENTHESIS = "GLCR"
    """
    a mass of ice, usually at high latitudes or high elevations, with sufficient thickness to flow away from the source area in lobes, tongues, or masses
    """
    gulf = "GULF"
    """
    a large recess in the coastline, larger than a bay
    """
    geyser = "GYSR"
    """
    a type of hot spring with intermittent eruptions of jets of hot water and steam
    """
    harborLEFT_PARENTHESISsRIGHT_PARENTHESIS = "HBR"
    """
    a haven or space of deep water so sheltered by the adjacent land as to afford a safe anchorage for ships
    """
    section_of_harbor = "HBRX"
    inlet = "INLT"
    """
    a narrow waterway extending into the land, or connecting a bay or lagoon with a larger body of water
    """
    former_inlet = "INLTQ"
    """
    an inlet which has been filled in, or blocked by deposits
    """
    lake_bedLEFT_PARENTHESISsRIGHT_PARENTHESIS = "LBED"
    """
    a dried up or drained area of a former lake
    """
    lagoon = "LGN"
    """
    a shallow coastal waterbody, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature
    """
    lagoons = "LGNS"
    """
    shallow coastal waterbodies, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature
    """
    section_of_lagoon = "LGNX"
    lake = "LK"
    """
    a large inland body of standing water
    """
    crater_lake = "LKC"
    """
    a lake in a crater or caldera
    """
    intermittent_lake = "LKI"
    salt_lake = "LKN"
    """
    an inland body of salt water with no outlet
    """
    intermittent_salt_lake = "LKNI"
    oxbow_lake = "LKO"
    """
    a crescent-shaped lake commonly found adjacent to meandering streams
    """
    intermittent_oxbow_lake = "LKOI"
    lakes = "LKS"
    """
    large inland bodies of standing water
    """
    underground_lake = "LKSB"
    """
    a standing body of water in a cave
    """
    crater_lakes = "LKSC"
    """
    lakes in a crater or caldera
    """
    intermittent_lakes = "LKSI"
    salt_lakes = "LKSN"
    """
    inland bodies of salt water with no outlet
    """
    intermittent_salt_lakes = "LKSNI"
    section_of_lake = "LKX"
    salt_evaporation_ponds = "MFGN"
    """
    diked salt ponds used in the production of solar evaporated salt
    """
    mangrove_swamp = "MGV"
    """
    a tropical tidal mud flat characterized by mangrove vegetation
    """
    moorLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MOOR"
    """
    an area of open ground overlaid with wet peaty soils
    """
    marshLEFT_PARENTHESISesRIGHT_PARENTHESIS = "MRSH"
    """
    a wetland dominated by grass-like vegetation
    """
    salt_marsh = "MRSHN"
    """
    a flat area, subject to periodic salt water inundation, dominated by grassy salt-tolerant plants
    """
    narrows = "NRWS"
    """
    a navigable narrow part of a bay, strait, river, etc.
    """
    ocean = "OCN"
    """
    one of the major divisions of the vast expanse of salt water covering part of the earth
    """
    overfalls = "OVF"
    """
    an area of breaking waves caused by the meeting of currents or by waves moving against the current
    """
    pond = "PND"
    """
    a small standing waterbody
    """
    intermittent_pond = "PNDI"
    salt_pond = "PNDN"
    """
    a small standing body of salt water often in a marsh or swamp, usually along a seacoast
    """
    intermittent_salt_pondLEFT_PARENTHESISsRIGHT_PARENTHESIS = "PNDNI"
    ponds = "PNDS"
    """
    small standing waterbodies
    """
    fishponds = "PNDSF"
    """
    ponds or enclosures in which fish are kept or raised
    """
    intermittent_ponds = "PNDSI"
    salt_ponds = "PNDSN"
    """
    small standing bodies of salt water often in a marsh or swamp, usually along a seacoast
    """
    poolLEFT_PARENTHESISsRIGHT_PARENTHESIS = "POOL"
    """
    a small and comparatively still, deep part of a larger body of water such as a stream or harbor; or a small body of standing water
    """
    intermittent_pool = "POOLI"
    reach = "RCH"
    """
    a straight section of a navigable stream or channel between two bends
    """
    icecap_ridge = "RDGG"
    """
    a linear elevation on an icecap
    """
    roadstead = "RDST"
    """
    an open anchorage affording less protection than a harbor
    """
    reefLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RF"
    """
    a surface-navigation hazard composed of consolidated material
    """
    coral_reefLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RFC"
    """
    a surface-navigation hazard composed of coral
    """
    section_of_reef = "RFX"
    rapids = "RPDS"
    """
    a turbulent section of a stream associated with a steep, irregular stream bed
    """
    reservoirLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RSV"
    """
    an artificial pond or lake
    """
    intermittent_reservoir = "RSVI"
    water_tank = "RSVT"
    """
    a contained pool or tank of water at, below, or above ground level
    """
    ravineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RVN"
    """
    a small, narrow, deep, steep-sided stream channel, smaller than a gorge
    """
    sabkhaLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SBKH"
    """
    a salt flat or salt encrusted plain subject to periodic inundation from flooding or high tides
    """
    sound = "SD"
    """
    a long arm of the sea forming a channel between the mainland and an island or islands; or connecting two larger bodies of water
    """
    sea = "SEA"
    """
    a large body of salt water more or less confined by continuous land or chains of islands forming a subdivision of an ocean
    """
    shoalLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SHOL"
    """
    a surface-navigation hazard composed of unconsolidated material
    """
    sill = "SILU"
    """
    the low part of a gap or saddle separating basins
    """
    springLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SPNG"
    """
    a place where ground water flows naturally out of the ground
    """
    sulphur_springLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SPNS"
    """
    a place where sulphur ground water flows naturally out of the ground
    """
    hot_springLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SPNT"
    """
    a place where hot ground water flows naturally out of the ground
    """
    stream = "STM"
    """
    a body of running water moving to a lower level in a channel on land
    """
    anabranch = "STMA"
    """
    a diverging branch flowing out of a main stream and rejoining it downstream
    """
    stream_bend = "STMB"
    """
    a conspicuously curved or bent segment of a stream
    """
    canalized_stream = "STMC"
    """
    a stream that has been substantially ditched, diked, or straightened
    """
    distributaryLEFT_PARENTHESIS_iesRIGHT_PARENTHESIS = "STMD"
    """
    a branch which flows away from the main stream, as in a delta or irrigation canal
    """
    headwaters = "STMH"
    """
    the source and upper part of a stream, including the upper drainage basin
    """
    intermittent_stream = "STMI"
    section_of_intermittent_stream = "STMIX"
    stream_mouthLEFT_PARENTHESISsRIGHT_PARENTHESIS = "STMM"
    """
    a place where a stream discharges into a lagoon, lake, or the sea
    """
    abandoned_watercourse = "STMQ"
    """
    a former stream or distributary no longer carrying flowing water, but still evident due to lakes, wetland, topographic or vegetation patterns
    """
    streams = "STMS"
    """
    bodies of running water moving to a lower level in a channel on land
    """
    lost_river = "STMSB"
    """
    a surface stream that disappears into an underground channel, or dries up in an arid area
    """
    section_of_stream = "STMX"
    strait = "STRT"
    """
    a relatively narrow waterway, usually narrower and less extensive than a sound, connecting two larger bodies of water
    """
    swamp = "SWMP"
    """
    a wetland dominated by tree vegetation
    """
    irrigation_system = "SYSI"
    """
    a network of ditches and one or more of the following elements: water supply, reservoir, canal, pump, well, drain, etc.
    """
    canal_tunnel = "TNLC"
    """
    a tunnel through which a canal passes
    """
    wadi = "WAD"
    """
    a valley or ravine, bounded by relatively steep banks, which in the rainy season becomes a watercourse; found primarily in North Africa and the Middle East
    """
    wadi_bend = "WADB"
    """
    a conspicuously curved or bent segment of a wadi
    """
    wadi_junction = "WADJ"
    """
    a place where two or more wadies join
    """
    wadi_mouth = "WADM"
    """
    the lower terminus of a wadi where it widens into an adjoining floodplain, depression, or waterbody
    """
    wadies = "WADS"
    """
    valleys or ravines, bounded by relatively steep banks, which in the rainy season become watercourses; found primarily in North Africa and the Middle East
    """
    section_of_wadi = "WADX"
    whirlpool = "WHRL"
    """
    a turbulent, rotating movement of water in a stream
    """
    well = "WLL"
    """
    a cylindrical hole, pit, or tunnel drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface
    """
    abandoned_well = "WLLQ"
    wells = "WLLS"
    """
    cylindrical holes, pits, or tunnels drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface
    """
    wetland = "WTLD"
    """
    an area subject to inundation, usually characterized by bog, marsh, or swamp vegetation
    """
    intermittent_wetland = "WTLDI"
    watercourse = "WTRC"
    """
    a natural, well-defined channel produced by flowing water, or an artificial channel designed to carry flowing water
    """
    waterholeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "WTRH"
    """
    a natural hole, hollow, or small depression that contains water, used by man and animals, especially in arid areas
    """
    agricultural_colony = "AGRC"
    """
    a tract of land set aside for agricultural settlement
    """
    amusement_park = "AMUS"
    """
    Amusement Park are theme parks, adventure parks offering entertainment, similar to funfairs but with a fix location
    """
    area = "AREA"
    """
    a tract of land without homogeneous character or boundaries
    """
    drainage_basin = "BSND"
    """
    an area drained by a stream
    """
    petroleum_basin = "BSNP"
    """
    an area underlain by an oil-rich structural basin
    """
    battlefield = "BTL"
    """
    a site of a land battle of historical importance
    """
    clearing = "CLG"
    """
    an area in a forest with trees removed
    """
    common = "CMN"
    """
    a park or pasture for community use
    """
    concession_area = "CNS"
    """
    a lease of land by a government for economic development, e.g., mining, forestry
    """
    coalfield = "COLF"
    """
    a region in which coal deposits of possible economic value occur
    """
    continent = "CONT"
    """
    continent: Europe, Africa, Asia, North America, South America, Oceania, Antarctica
    """
    coast = "CST"
    """
    a zone of variable width straddling the shoreline
    """
    business_center = "CTRB"
    """
    a place where a number of businesses are located
    """
    housing_development = "DEVH"
    """
    a tract of land on which many houses of similar design are built according to a development plan
    """
    fieldLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLD"
    """
    an open as opposed to wooded area
    """
    irrigated_fieldLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FLDI"
    """
    a tract of level or terraced land which is irrigated
    """
    gasfield = "GASF"
    """
    an area containing a subterranean store of natural gas of economic value
    """
    grazing_area = "GRAZ"
    """
    an area of grasses and shrubs used for grazing
    """
    gravel_area = "GVL"
    """
    an area covered with gravel
    """
    industrial_area = "INDS"
    """
    an area characterized by industrial activity
    """
    arctic_land = "LAND"
    """
    a tract of land in the Arctic
    """
    locality = "LCTY"
    """
    a minor area or place of unspecified or mixed character and indefinite boundaries
    """
    military_base = "MILB"
    """
    a place used by an army or other armed service for storing arms and supplies, and for accommodating and training troops, a base from which operations can be initiated
    """
    mining_area = "MNA"
    """
    an area of mine sites where minerals and ores are extracted
    """
    maneuver_area = "MVA"
    """
    a tract of land where military field exercises are carried out
    """
    naval_base = "NVB"
    """
    an area used to store supplies, provide barracks for troops and naval personnel, a port for naval vessels, and from which operations are initiated
    """
    oasisLEFT_PARENTHESIS_esRIGHT_PARENTHESIS = "OAS"
    """
    an area in a desert made productive by the availability of water
    """
    oilfield = "OILF"
    """
    an area containing a subterranean store of petroleum of economic value
    """
    peat_cutting_area = "PEAT"
    """
    an area where peat is harvested
    """
    park = "PRK"
    """
    an area, often of forested land, maintained as a place of beauty, or for recreation
    """
    port = "PRT"
    """
    a place provided with terminal and transfer facilities for loading and discharging waterborne cargo or passengers, usually located in a harbor
    """
    quicksand = "QCKS"
    """
    an area where loose sand with water moving through it may become unstable when heavy objects are placed at the surface, causing them to sink
    """
    reserve = "RES"
    """
    a tract of public land reserved for future use or restricted as to use
    """
    agricultural_reserve = "RESA"
    """
    a tract of land reserved for agricultural reclamation and/or development
    """
    forest_reserve = "RESF"
    """
    a forested area set aside for preservation or controlled use
    """
    hunting_reserve = "RESH"
    """
    a tract of land used primarily for hunting
    """
    nature_reserve = "RESN"
    """
    an area reserved for the maintenance of a natural habitat
    """
    palm_tree_reserve = "RESP"
    """
    an area of palm trees where use is controlled
    """
    reservation = "RESV"
    """
    a tract of land set aside for aboriginal, tribal, or native populations
    """
    wildlife_reserve = "RESW"
    """
    a tract of public land reserved for the preservation of wildlife
    """
    region = "RGN"
    """
    an area distinguished by one or more observable physical or cultural characteristics
    """
    economic_region = "RGNE"
    """
    a region of a country established for economic development or for statistical purposes
    """
    historical_region = "RGNH"
    """
    a former historic area distinguished by one or more observable physical or cultural characteristics
    """
    lake_region = "RGNL"
    """
    a tract of land distinguished by numerous lakes
    """
    artillery_range = "RNGA"
    """
    a tract of land used for artillery firing practice
    """
    salt_area = "SALT"
    """
    a shallow basin or flat where salt accumulates after periodic inundation
    """
    snowfield = "SNOW"
    """
    an area of permanent snow and ice forming the accumulation area of a glacier
    """
    tribal_area = "TRB"
    """
    a tract of land used by nomadic or other tribes
    """
    populated_place = "PPL"
    """
    a city, town, village, or other agglomeration of buildings where people live and work
    """
    seat_of_a_first_order_administrative_division = "PPLA"
    """
    seat of a first-order administrative division (PPLC takes precedence over PPLA)
    """
    seat_of_a_second_order_administrative_division = "PPLA2"
    seat_of_a_third_order_administrative_division = "PPLA3"
    seat_of_a_fourth_order_administrative_division = "PPLA4"
    seat_of_a_fifth_order_administrative_division = "PPLA5"
    capital_of_a_political_entity = "PPLC"
    """
    capital of a political entity designated as an independent state
    """
    capital_of_a_dependency_or_special_area = "PPLCD"
    """
    capital or administrative center of a dependent political territory or area of special sovereignty
    """
    historical_capital_of_a_political_entity = "PPLCH"
    """
    a former capital of a political entity
    """
    farm_village = "PPLF"
    """
    a populated place where the population is largely engaged in agricultural activities
    """
    seat_of_government_of_a_political_entity = "PPLG"
    historical_populated_place = "PPLH"
    """
    a populated place that no longer exists
    """
    populated_locality = "PPLL"
    """
    an area similar to a locality but with a small group of dwellings or other buildings
    """
    abandoned_populated_place = "PPLQ"
    religious_populated_place = "PPLR"
    """
    a populated place whose population is largely engaged in religious occupations
    """
    populated_places = "PPLS"
    """
    cities, towns, villages, or other agglomerations of buildings where people live and work
    """
    destroyed_populated_place = "PPLW"
    """
    a village, town or city destroyed by a natural disaster, or by war
    """
    section_of_populated_place = "PPLX"
    israeli_settlement = "STLMT"
    causeway = "CSWY"
    """
    a raised roadway across wet ground or shallow water
    """
    oil_pipeline = "OILP"
    """
    a pipeline used for transporting oil
    """
    promenade = "PRMN"
    """
    a place for public walking, usually along a beach front
    """
    portage = "PTGE"
    """
    a place where boats, goods, etc., are carried overland between navigable waters
    """
    road = "RD"
    """
    an open way with improved surface for transportation of animals, people and vehicles
    """
    ancient_road = "RDA"
    """
    the remains of a road used by ancient cultures
    """
    road_bend = "RDB"
    """
    a conspicuously curved or bent section of a road
    """
    road_cut = "RDCUT"
    """
    an excavation cut through a hill or ridge for a road
    """
    road_junction = "RDJCT"
    """
    a place where two or more roads join
    """
    railroad_junction = "RJCT"
    """
    a place where two or more railroad tracks join
    """
    railroad = "RR"
    """
    a permanent twin steel-rail track on which freight and passenger cars move long distances
    """
    abandoned_railroad = "RRQ"
    caravan_route = "RTE"
    """
    the route taken by caravans
    """
    railroad_yard = "RYD"
    """
    a system of tracks used for the making up of trains, and switching and storing freight cars
    """
    street = "ST"
    """
    a paved urban thoroughfare
    """
    stock_route = "STKR"
    """
    a route taken by livestock herds
    """
    tunnel = "TNL"
    """
    a subterranean passageway for transportation
    """
    natural_tunnel = "TNLN"
    """
    a cave that is open at both ends
    """
    road_tunnel = "TNLRD"
    """
    a tunnel through which a road passes
    """
    railroad_tunnel = "TNLRR"
    """
    a tunnel through which a railroad passes
    """
    tunnels = "TNLS"
    """
    subterranean passageways for transportation
    """
    trail = "TRL"
    """
    a path, track, or route used by pedestrians, animals, or off-road vehicles
    """
    administrative_facility = "ADMF"
    """
    a government building
    """
    agricultural_facility = "AGRF"
    """
    a building and/or tract of land used for improving agriculture
    """
    airbase = "AIRB"
    """
    an area used to store supplies, provide barracks for air force personnel, hangars and runways for aircraft, and from which operations are initiated
    """
    airfield = "AIRF"
    """
    a place on land where aircraft land and take off; no facilities provided for the commercial handling of passengers and cargo
    """
    heliport = "AIRH"
    """
    a place where helicopters land and take off
    """
    airport = "AIRP"
    """
    a place where aircraft regularly land and take off, with runways, navigational aids, and major facilities for the commercial handling of passengers and cargo
    """
    abandoned_airfield = "AIRQ"
    terminal = "AIRT"
    """
    airport facilities for the handling of freight and passengers
    """
    amphitheater = "AMTH"
    """
    an oval or circular structure with rising tiers of seats about a stage or open space
    """
    archaeologicalSOLIDUSprehistoric_site = "ANS"
    """
    a place where archeological remains, old structures, or cultural artifacts are located
    """
    aquaculture_facility = "AQC"
    """
    facility or area for the cultivation of aquatic animals and plants, especially fish, shellfish, and seaweed, in natural or controlled marine or freshwater environments; underwater agriculture
    """
    arch = "ARCU"
    """
    a low bulge around the southeastern end of the island of Hawaii
    """
    archive = "ARCHV"
    """
    a place or institution where documents are preserved
    """
    piece_of_art = "ART"
    """
    a piece of art, like a sculpture, painting. In contrast to monument (MNMT) it is not commemorative.
    """
    astronomical_station = "ASTR"
    """
    a point on the earth whose position has been determined by observations of celestial bodies
    """
    asylum = "ASYL"
    """
    a facility where the insane are cared for and protected
    """
    athletic_field = "ATHF"
    """
    a tract of land used for playing team sports, and athletic track and field events
    """
    automatic_teller_machine = "ATM"
    """
    An unattended electronic machine in a public place, connected to a data system and related equipment and activated by a bank customer to obtain cash withdrawals and other banking services.
    """
    bank = "BNKU"
    """
    an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation
    """
    beacon = "BCN"
    """
    a fixed artificial navigation mark
    """
    bridge = "BDG"
    """
    a structure erected across an obstacle such as a stream, road, etc., in order to carry roads, railroads, and pedestrians across
    """
    ruined_bridge = "BDGQ"
    """
    a destroyed or decayed bridge which is no longer functional
    """
    apartment_building = "BLDA"
    """
    a building containing several individual apartments
    """
    buildingLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BLDG"
    """
    a structure built for permanent use, as a house, factory, etc.
    """
    office_building = "BLDO"
    """
    commercial building where business and/or services are conducted
    """
    boundary_marker = "BP"
    """
    a fixture marking a point along a boundary
    """
    barracks = "BRKS"
    """
    a building for lodging military personnel
    """
    breakwater = "BRKW"
    """
    a structure erected to break the force of waves at the entrance to a harbor or port
    """
    baling_station = "BSTN"
    """
    a facility for baling agricultural products
    """
    boatyard = "BTYD"
    """
    a waterside facility for servicing, repairing, and building small vessels
    """
    burial_caveLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BUR"
    """
    a cave used for human burials
    """
    bus_station = "BUSTN"
    """
    a facility comprising ticket office, platforms, etc. for loading and unloading passengers
    """
    bus_stop = "BUSTP"
    """
    a place lacking station facilities
    """
    cairn = "CARN"
    """
    a heap of stones erected as a landmark or for other purposes
    """
    caveLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CAVE"
    """
    an underground passageway or chamber, or cavity on the side of a cliff
    """
    church = "CH"
    """
    a building for public Christian worship
    """
    campLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CMP"
    """
    a site occupied by tents, huts, or other shelters for temporary use
    """
    logging_camp = "CMPL"
    """
    a camp used by loggers
    """
    labor_camp = "CMPLA"
    """
    a camp used by migrant or temporary laborers
    """
    mining_camp = "CMPMN"
    """
    a camp used by miners
    """
    oil_camp = "CMPO"
    """
    a camp used by oilfield workers
    """
    abandoned_camp = "CMPQ"
    refugee_camp = "CMPRF"
    """
    a camp used by refugees
    """
    cemetery = "CMTY"
    """
    a burial place or ground
    """
    communication_center = "COMC"
    """
    a facility, including buildings, antennae, towers and electronic equipment for receiving and transmitting information
    """
    corralLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CRRL"
    """
    a pen or enclosure for confining or capturing animals
    """
    casino = "CSNO"
    """
    a building used for entertainment, especially gambling
    """
    castle = "CSTL"
    """
    a large fortified building or set of buildings
    """
    customs_house = "CSTM"
    """
    a building in a port where customs and duties are paid, and where vessels are entered and cleared
    """
    courthouse = "CTHSE"
    """
    a building in which courts of law are held
    """
    atomic_center = "CTRA"
    """
    a facility where atomic research is carried out
    """
    community_center = "CTRCM"
    """
    a facility for community recreation and other activities
    """
    facility_center = "CTRF"
    """
    a place where more than one facility is situated
    """
    medical_center = "CTRM"
    """
    a complex of health care buildings including two or more of the following: hospital, medical school, clinic, pharmacy, doctor's offices, etc.
    """
    religious_center = "CTRR"
    """
    a facility where more than one religious activity is carried out, e.g., retreat, school, monastery, worship
    """
    space_center = "CTRS"
    """
    a facility for launching, tracking, or controlling satellites and space vehicles
    """
    courtyard = "CTYD"
    """
    an area surrounded by a building or complex and open to the sky
    """
    convent = "CVNT"
    """
    a building where a community of nuns lives in seclusion
    """
    dam = "DAM"
    """
    a barrier constructed across a stream to impound water
    """
    ruined_dam = "DAMQ"
    """
    a destroyed or decayed dam which is no longer functional
    """
    sub_surface_dam = "DAMSB"
    """
    a dam put down to bedrock in a sand river
    """
    dairy = "DARY"
    """
    a facility for the processing, sale and distribution of milk or milk products
    """
    dry_dock = "DCKD"
    """
    a dock providing support for a vessel, and means for removing the water so that the bottom of the vessel can be exposed
    """
    dockyard = "DCKY"
    """
    a facility for servicing, building, or repairing ships
    """
    dike = "DIKE"
    """
    an earth or stone embankment usually constructed for flood or stream control
    """
    diplomatic_facility = "DIP"
    """
    office, residence, or facility of a foreign government, which may include an embassy, consulate, chancery, office of charge d'affaires, or other diplomatic, economic, military, or cultural mission
    """
    fuel_depot = "DPOF"
    """
    an area where fuel is stored
    """
    estateLEFT_PARENTHESISsRIGHT_PARENTHESIS = "EST"
    """
    a large commercialized agricultural landholding with associated buildings and other facilities
    """
    oil_palm_plantation = "ESTO"
    """
    an estate specializing in the cultivation of oil palm trees
    """
    rubber_plantation = "ESTR"
    """
    an estate which specializes in growing and tapping rubber trees
    """
    sugar_plantation = "ESTSG"
    """
    an estate that specializes in growing sugar cane
    """
    tea_plantation = "ESTT"
    """
    an estate which specializes in growing tea bushes
    """
    section_of_estate = "ESTX"
    facility = "FCL"
    """
    a building or buildings housing a center, institute, foundation, hospital, prison, mission, courthouse, etc.
    """
    fire_station = "FIRE"
    """
    building housing firefighters and/or fire fighting equipment
    """
    foundry = "FNDY"
    """
    a building or works where metal casting is carried out
    """
    farm = "FRM"
    """
    a tract of land with associated buildings devoted to agriculture
    """
    abandoned_farm = "FRMQ"
    farms = "FRMS"
    """
    tracts of land with associated buildings devoted to agriculture
    """
    farmstead = "FRMT"
    """
    the buildings and adjacent service areas of a farm
    """
    fort = "FT"
    """
    a defensive structure or earthworks
    """
    ferry = "FY"
    """
    a boat or other floating conveyance and terminal facilities regularly used to transport people and vehicles across a waterbody
    """
    ferry_terminal = "FYT"
    """
    a place where ferries pick-up and discharge passengers, vehicles and or cargo
    """
    gate = "GATE"
    """
    a controlled access entrance or exit
    """
    gardenLEFT_PARENTHESISsRIGHT_PARENTHESIS = "GDN"
    """
    an enclosure for displaying selected plant or animal life
    """
    ghat = "GHAT"
    """
    a set of steps leading to a river, which are of religious significance, and at their base is usually a platform for bathing
    """
    guest_house = "GHSE"
    """
    a house used to provide lodging for paying guests
    """
    gas_oil_separator_plant = "GOSP"
    """
    a facility for separating gas from oil
    """
    local_government_office = "GOVL"
    """
    a facility housing local governmental offices, usually a city, town, or village hall
    """
    grave = "GRVE"
    """
    a burial site
    """
    hermitage = "HERM"
    """
    a secluded residence, usually for religious sects
    """
    halting_place = "HLT"
    """
    a place where caravans stop for rest
    """
    homestead = "HMSD"
    """
    a residence, owner's or manager's, on a sheep or cattle station, woolshed, outcamp, or Aboriginal outstation, specific to Australia and New Zealand
    """
    houseLEFT_PARENTHESISsRIGHT_PARENTHESIS = "HSE"
    """
    a building used as a human habitation
    """
    country_house = "HSEC"
    """
    a large house, mansion, or chateau, on a large estate
    """
    hospital = "HSP"
    """
    a building in which sick or injured, especially those confined to bed, are medically treated
    """
    clinic = "HSPC"
    """
    a medical facility associated with a hospital for outpatients
    """
    dispensary = "HSPD"
    """
    a building where medical or dental aid is dispensed
    """
    leprosarium = "HSPL"
    """
    an asylum or hospital for lepers
    """
    historical_site = "HSTS"
    """
    a place of historical importance
    """
    hotel = "HTL"
    """
    a building providing lodging and/or meals for the public
    """
    hut = "HUT"
    """
    a small primitive house
    """
    huts = "HUTS"
    """
    small primitive houses
    """
    military_installation = "INSM"
    """
    a facility for use of and control by armed forces
    """
    research_institute = "ITTR"
    """
    a facility where research is carried out
    """
    jetty = "JTY"
    """
    a structure built out into the water at a river mouth or harbor entrance to regulate currents and silting
    """
    landing = "LDNG"
    """
    a place where boats receive or discharge passengers and freight, but lacking most port facilities
    """
    leper_colony = "LEPC"
    """
    a settled area inhabited by lepers in relative isolation
    """
    library = "LIBR"
    """
    A place in which information resources such as books are kept for reading, reference, or lending.
    """
    landfill = "LNDF"
    """
    a place for trash and garbage disposal in which the waste is buried between layers of earth to build up low-lying land
    """
    lockLEFT_PARENTHESISsRIGHT_PARENTHESIS = "LOCK"
    """
    a basin in a waterway with gates at each end by means of which vessels are passed from one water level to another
    """
    lighthouse = "LTHSE"
    """
    a distinctive structure exhibiting a major navigation light
    """
    mall = "MALL"
    """
    A large, often enclosed shopping complex containing various stores, businesses, and restaurants usually accessible by common passageways.
    """
    marina = "MAR"
    """
    a harbor facility for small boats, yachts, etc.
    """
    factory = "MFG"
    """
    one or more buildings where goods are manufactured, processed or fabricated
    """
    brewery = "MFGB"
    """
    one or more buildings where beer is brewed
    """
    cannery = "MFGC"
    """
    a building where food items are canned
    """
    copper_works = "MFGCU"
    """
    a facility for processing copper ore
    """
    limekiln = "MFGLM"
    """
    a furnace in which limestone is reduced to lime
    """
    munitions_plant = "MFGM"
    """
    a factory where ammunition is made
    """
    phosphate_works = "MFGPH"
    """
    a facility for producing fertilizer
    """
    abandoned_factory = "MFGQ"
    sugar_refinery = "MFGSG"
    """
    a facility for converting raw sugar into refined sugar
    """
    market = "MKT"
    """
    a place where goods are bought and sold at regular intervals
    """
    millLEFT_PARENTHESISsRIGHT_PARENTHESIS = "ML"
    """
    a building housing machines for transforming, shaping, finishing, grinding, or extracting products
    """
    ore_treatment_plant = "MLM"
    """
    a facility for improving the metal content of ore by concentration
    """
    olive_oil_mill = "MLO"
    """
    a mill where oil is extracted from olives
    """
    sugar_mill = "MLSG"
    """
    a facility where sugar cane is processed into raw sugar
    """
    former_sugar_mill = "MLSGQ"
    """
    a sugar mill no longer used as a sugar mill
    """
    sawmill = "MLSW"
    """
    a mill where logs or lumber are sawn to specified shapes and sizes
    """
    windmill = "MLWND"
    """
    a mill or water pump powered by wind
    """
    water_mill = "MLWTR"
    """
    a mill powered by running water
    """
    mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MN"
    """
    a site where mineral ores are extracted from the ground by excavating surface pits and subterranean passages
    """
    gold_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNAU"
    """
    a mine where gold ore, or alluvial gold is extracted
    """
    coal_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNC"
    """
    a mine where coal is extracted
    """
    chrome_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNCR"
    """
    a mine where chrome ore is extracted
    """
    copper_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNCU"
    """
    a mine where copper ore is extracted
    """
    iron_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNFE"
    """
    a mine where iron ore is extracted
    """
    monument = "MNMT"
    """
    a commemorative structure or statue
    """
    salt_mineLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MNN"
    """
    a mine from which salt is extracted
    """
    abandoned_mine = "MNQ"
    quarryLEFT_PARENTHESIS_iesRIGHT_PARENTHESIS = "MNQR"
    """
    a surface mine where building stone or gravel and sand, etc. are extracted
    """
    mole = "MOLE"
    """
    a massive structure of masonry or large stones serving as a pier or breakwater
    """
    mosque = "MSQE"
    """
    a building for public Islamic worship
    """
    mission = "MSSN"
    """
    a place characterized by dwellings, school, church, hospital and other facilities operated by a religious group for the purpose of providing charitable services and to propagate religion
    """
    abandoned_mission = "MSSNQ"
    monastery = "MSTY"
    """
    a building and grounds where a community of monks lives in seclusion
    """
    metro_station = "MTRO"
    """
    metro station (Underground, Tube, or Metro)
    """
    museum = "MUS"
    """
    a building where objects of permanent interest in one or more of the arts and sciences are preserved and exhibited
    """
    novitiate = "NOV"
    """
    a religious house or school where novices are trained
    """
    nurseryLEFT_PARENTHESIS_iesRIGHT_PARENTHESIS = "NSY"
    """
    a place where plants are propagated for transplanting or grafting
    """
    observation_point = "OBPT"
    """
    a wildlife or scenic observation point
    """
    observatory = "OBS"
    """
    a facility equipped for observation of atmospheric or space phenomena
    """
    radio_observatory = "OBSR"
    """
    a facility equipped with an array of antennae for receiving radio waves from space
    """
    oil_pipeline_junction = "OILJ"
    """
    a section of an oil pipeline where two or more pipes join together
    """
    abandoned_oil_well = "OILQ"
    oil_refinery = "OILR"
    """
    a facility for converting crude oil into refined petroleum products
    """
    tank_farm = "OILT"
    """
    a tract of land occupied by large, cylindrical, metal tanks in which oil or liquid petrochemicals are stored
    """
    oil_well = "OILW"
    """
    a well from which oil may be pumped
    """
    opera_house = "OPRA"
    """
    A theater designed chiefly for the performance of operas.
    """
    palace = "PAL"
    """
    a large stately house, often a royal or presidential residence
    """
    pagoda = "PGDA"
    """
    a tower-like storied structure, usually a Buddhist shrine
    """
    pier = "PIER"
    """
    a structure built out into navigable water on piles providing berthing for ships and recreation
    """
    parking_lot = "PKLT"
    """
    an area used for parking vehicles
    """
    oil_pumping_station = "PMPO"
    """
    a facility for pumping oil through a pipeline
    """
    water_pumping_station = "PMPW"
    """
    a facility for pumping water from a major well or through a pipeline
    """
    post_office = "PO"
    """
    a public building in which mail is received, sorted and distributed
    """
    police_post = "PP"
    """
    a building in which police are stationed
    """
    abandoned_police_post = "PPQ"
    park_gate = "PRKGT"
    """
    a controlled access to a park
    """
    park_headquarters = "PRKHQ"
    """
    a park administrative facility
    """
    prison = "PRN"
    """
    a facility for confining prisoners
    """
    reformatory = "PRNJ"
    """
    a facility for confining, training, and reforming young law offenders
    """
    abandoned_prison = "PRNQ"
    power_station = "PS"
    """
    a facility for generating electric power
    """
    hydroelectric_power_station = "PSH"
    """
    a building where electricity is generated from water power
    """
    nuclear_power_station = "PSN"
    """
    nuclear power station
    """
    border_post = "PSTB"
    """
    a post or station at an international boundary for the regulation of movement of people and goods
    """
    customs_post = "PSTC"
    """
    a building at an international boundary where customs and duties are paid on goods
    """
    patrol_post = "PSTP"
    """
    a post from which patrols are sent out
    """
    pyramid = "PYR"
    """
    an ancient massive structure of square ground plan with four triangular faces meeting at a point and used for enclosing tombs
    """
    pyramids = "PYRS"
    """
    ancient massive structures of square ground plan with four triangular faces meeting at a point and used for enclosing tombs
    """
    quay = "QUAY"
    """
    a structure of solid construction along a shore or bank which provides berthing for ships and which generally provides cargo handling facilities
    """
    traffic_circle = "RDCR"
    """
    a road junction formed around a central circle about which traffic moves in one direction only
    """
    intersection = "RDIN"
    """
    a junction of two or more highways by a system of separate levels that permit traffic to pass from one to another without the crossing of traffic streams
    """
    golf_course = "RECG"
    """
    a recreation field where golf is played
    """
    racetrack = "RECR"
    """
    a track where races are held
    """
    restaurant = "REST"
    """
    A place where meals are served to the public
    """
    store = "RET"
    """
    a building where goods and/or services are offered for sale
    """
    resthouse = "RHSE"
    """
    a structure maintained for the rest and shelter of travelers
    """
    rookery = "RKRY"
    """
    a breeding place of a colony of birds or seals
    """
    religious_site = "RLG"
    """
    an ancient site of significant religious importance
    """
    retreat = "RLGR"
    """
    a place of temporary seclusion, especially for religious groups
    """
    ranchLEFT_PARENTHESISesRIGHT_PARENTHESIS = "RNCH"
    """
    a large farm specializing in extensive grazing of livestock
    """
    railroad_siding = "RSD"
    """
    a short track parallel to and joining the main track
    """
    railroad_signal = "RSGNL"
    """
    a signal at the entrance of a particular section of track governing the movement of trains
    """
    resort = "RSRT"
    """
    a specialized facility for vacation, health, or participation sports activities
    """
    railroad_station = "RSTN"
    """
    a facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight
    """
    abandoned_railroad_station = "RSTNQ"
    railroad_stop = "RSTP"
    """
    a place lacking station facilities where trains stop to pick up and unload passengers and freight
    """
    abandoned_railroad_stop = "RSTPQ"
    ruinLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RUIN"
    """
    a destroyed or decayed structure which is no longer functional
    """
    school = "SCH"
    """
    building(s) where instruction in one or more branches of knowledge takes place
    """
    agricultural_school = "SCHA"
    """
    a school with a curriculum focused on agriculture
    """
    college = "SCHC"
    """
    the grounds and buildings of an institution of higher learning
    """
    language_school = "SCHL"
    """
    Language Schools & Institutions
    """
    military_school = "SCHM"
    """
    a school at which military science forms the core of the curriculum
    """
    maritime_school = "SCHN"
    """
    a school at which maritime sciences form the core of the curriculum
    """
    technical_school = "SCHT"
    """
    post-secondary school with a specifically technical or vocational curriculum
    """
    State_Exam_Prep_Centre = "SECP"
    """
    state exam preparation centres
    """
    sheepfold = "SHPF"
    """
    a fence or wall enclosure for sheep and other small herd animals
    """
    shrine = "SHRN"
    """
    a structure or place memorializing a person or religious concept
    """
    storehouse = "SHSE"
    """
    a building for storing goods, especially provisions
    """
    sluice = "SLCE"
    """
    a conduit or passage for carrying off surplus water from a waterbody, usually regulated by means of a sluice gate
    """
    sanatorium = "SNTR"
    """
    a facility where victims of physical or mental disorders are treated
    """
    spa = "SPA"
    """
    a resort area usually developed around a medicinal spring
    """
    spillway = "SPLY"
    """
    a passage or outlet through which surplus water flows over, around or through a dam
    """
    square = "SQR"
    """
    a broad, open, public area near the center of a town or city
    """
    stable = "STBL"
    """
    a building for the shelter and feeding of farm animals, especially horses
    """
    stadium = "STDM"
    """
    a structure with an enclosure for athletic games with tiers of seats for spectators
    """
    scientific_research_base = "STNB"
    """
    a scientific facility used as a base from which research is carried out or monitored
    """
    coast_guard_station = "STNC"
    """
    a facility from which the coast is guarded by armed vessels
    """
    experiment_station = "STNE"
    """
    a facility for carrying out experiments
    """
    forest_station = "STNF"
    """
    a collection of buildings and facilities for carrying out forest management
    """
    inspection_station = "STNI"
    """
    a station at which vehicles, goods, and people are inspected
    """
    meteorological_station = "STNM"
    """
    a station at which weather elements are recorded
    """
    radio_station = "STNR"
    """
    a facility for producing and transmitting information by radio waves
    """
    satellite_station = "STNS"
    """
    a facility for tracking and communicating with orbiting satellites
    """
    whaling_station = "STNW"
    """
    a facility for butchering whales and processing train oil
    """
    steps = "STPS"
    """
    stones or slabs placed for ease in ascending or descending a steep slope
    """
    sewage_treatment_plant = "SWT"
    """
    facility for the processing of sewage and/or wastewater
    """
    synagogue = "SYG"
    """
    a place for Jewish worship and religious instruction
    """
    theater = "THTR"
    """
    a building or outdoor area used for live theatrical presentations, concerts, opera or dance productions, cinema, and/or other stage productions
    """
    tombLEFT_PARENTHESISsRIGHT_PARENTHESIS = "TMB"
    """
    a structure for interring bodies
    """
    templeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "TMPL"
    """
    an edifice dedicated to religious worship
    """
    cattle_dipping_tank = "TNKD"
    """
    a small artificial pond used for immersing cattle in chemically treated water for disease control
    """
    toll_gateSOLIDUSbarrier = "TOLL"
    """
    highway toll collection station
    """
    tower = "TOWR"
    """
    a high conspicuous structure, typically much higher than its diameter
    """
    tram = "TRAM"
    """
    rail vehicle along urban streets (also known as streetcar or trolley)
    """
    transit_terminal = "TRANT"
    """
    facilities for the handling of vehicular freight and passengers
    """
    triangulation_station = "TRIG"
    """
    a point on the earth whose position has been determined by triangulation
    """
    oil_pipeline_terminal = "TRMO"
    """
    a tank farm or loading facility at the end of an oil pipeline
    """
    temp_work_office = "TWO"
    """
    Temporary Work Offices
    """
    university_prep_school = "UNIP"
    """
    University Preparation Schools & Institutions
    """
    university = "UNIV"
    """
    An institution for higher learning with teaching and research facilities constituting a graduate school and professional schools that award master's degrees and doctorates and an undergraduate division that awards bachelor's degrees.
    """
    united_states_government_establishment = "USGE"
    """
    a facility operated by the United States Government in Panama
    """
    veterinary_facility = "VETF"
    """
    a building or camp at which veterinary services are available
    """
    wall = "WALL"
    """
    a thick masonry structure, usually enclosing a field or building, or forming the side of a structure
    """
    ancient_wall = "WALLA"
    """
    the remains of a linear defensive stone structure
    """
    weirLEFT_PARENTHESISsRIGHT_PARENTHESIS = "WEIR"
    """
    a small dam in a stream, designed to raise the water level or to divert stream flow through a desired channel
    """
    wharfLEFT_PARENTHESIS_vesRIGHT_PARENTHESIS = "WHRF"
    """
    a structure of open rather than solid construction along a shore or a bank which provides berthing for ships and cargo-handling facilities
    """
    wreck = "WRCK"
    """
    the site of the remains of a wrecked vessel
    """
    waterworks = "WTRW"
    """
    a facility for supplying potable water through a water source and a system of pumps and filtration beds
    """
    free_trade_zone = "ZNF"
    """
    an area, usually a section of a port, where goods may be received and shipped free of customs duty and of most customs regulations
    """
    zoo = "ZOO"
    """
    a zoological garden or park where wild animals are kept for exhibition
    """
    asphalt_lake = "ASPH"
    """
    a small basin containing naturally occurring asphalt
    """
    atollLEFT_PARENTHESISsRIGHT_PARENTHESIS = "ATOL"
    """
    a ring-shaped coral reef which has closely spaced islands on it encircling a lagoon
    """
    bar = "BAR"
    """
    a shallow ridge or mound of coarse unconsolidated material in a stream channel, at the mouth of a stream, estuary, or lagoon and in the wave-break zone along coasts
    """
    beach = "BCH"
    """
    a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves
    """
    beaches = "BCHS"
    """
    a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves
    """
    badlands = "BDLD"
    """
    an area characterized by a maze of very closely spaced, deep, narrow, steep-sided ravines, and sharp crests and pinnacles
    """
    boulder_field = "BLDR"
    """
    a high altitude or high latitude bare, flat area covered with large angular rocks
    """
    blowholeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BLHL"
    """
    a hole in coastal rock through which sea water is forced by a rising tide or waves and spurted through an outlet into the air
    """
    blowoutLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BLOW"
    """
    a small depression in sandy terrain, caused by wind erosion
    """
    bench = "BNCH"
    """
    a long, narrow bedrock platform bounded by steeper slopes above and below, usually overlooking a waterbody
    """
    butteLEFT_PARENTHESISsRIGHT_PARENTHESIS = "BUTE"
    """
    a small, isolated, usually flat-topped hill with steep sides
    """
    cape = "CAPE"
    """
    a land area, more prominent than a point, projecting into the sea and marking a notable change in coastal direction
    """
    cleftLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CFT"
    """
    a deep narrow slot, notch, or groove in a coastal cliff
    """
    caldera = "CLDA"
    """
    a depression measuring kilometers across formed by the collapse of a volcanic mountain
    """
    cliffLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CLF"
    """
    a high, steep to perpendicular slope overlooking a waterbody or lower area
    """
    canyon = "CNYU"
    """
    a relatively narrow, deep depression with steep sides, the bottom of which generally has a continuous slope
    """
    coneLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CONE"
    """
    a conical landform composed of mud or volcanic material
    """
    corridor = "CRDR"
    """
    a strip or area of land having significance as an access way
    """
    cirque = "CRQ"
    """
    a bowl-like hollow partially surrounded by cliffs or steep slopes at the head of a glaciated valley
    """
    cirques = "CRQS"
    """
    bowl-like hollows partially surrounded by cliffs or steep slopes at the head of a glaciated valley
    """
    craterLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CRTR"
    """
    a generally circular saucer or bowl-shaped depression caused by volcanic or meteorite explosive action
    """
    cuestaLEFT_PARENTHESISsRIGHT_PARENTHESIS = "CUET"
    """
    an asymmetric ridge formed on tilted strata
    """
    delta = "DLTA"
    """
    a flat plain formed by alluvial deposits at the mouth of a stream
    """
    depressionLEFT_PARENTHESISsRIGHT_PARENTHESIS = "DPR"
    """
    a low area surrounded by higher land and usually characterized by interior drainage
    """
    desert = "DSRT"
    """
    a large area with little or no vegetation due to extreme environmental conditions
    """
    duneLEFT_PARENTHESISsRIGHT_PARENTHESIS = "DUNE"
    """
    a wave form, ridge or star shape feature composed of sand
    """
    divide = "DVD"
    """
    a line separating adjacent drainage basins
    """
    sandy_desert = "ERG"
    """
    an extensive tract of shifting sand and sand dunes
    """
    fanLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FAN"
    """
    a fan-shaped wedge of coarse alluvium with apex merging with a mountain stream bed and the fan spreading out at a low angle slope onto an adjacent plain
    """
    ford = "FORD"
    """
    a shallow part of a stream which can be crossed on foot or by land vehicle
    """
    fissure = "FSR"
    """
    a crack associated with volcanism
    """
    gap = "GAPU"
    """
    a narrow break in a ridge or rise
    """
    gorgeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "GRGE"
    """
    a short, narrow, steep-sided section of a stream valley
    """
    headland = "HDLD"
    """
    a high projection of land extending into a large body of water beyond the line of the coast
    """
    hill = "HLLU"
    """
    an elevation rising generally less than 500 meters
    """
    hills = "HLSU"
    """
    elevations rising generally less than 500 meters
    """
    hammockLEFT_PARENTHESISsRIGHT_PARENTHESIS = "HMCK"
    """
    a patch of ground, distinct from and slightly above the surrounding plain or wetland. Often occurs in groups
    """
    rock_desert = "HMDA"
    """
    a relatively sand-free, high bedrock plateau in a hot desert, with or without a gravel veneer
    """
    interfluve = "INTF"
    """
    a relatively undissected upland between adjacent stream valleys
    """
    island = "ISL"
    """
    a tract of land, smaller than a continent, surrounded by water at high water
    """
    islet = "ISLET"
    """
    small island, bigger than rock, smaller than island.
    """
    artificial_island = "ISLF"
    """
    an island created by landfill or diking and filling in a wetland, bay, or lagoon
    """
    mangrove_island = "ISLM"
    """
    a mangrove swamp surrounded by a waterbody
    """
    islands = "ISLS"
    """
    tracts of land, smaller than a continent, surrounded by water at high water
    """
    land_tied_island = "ISLT"
    """
    a coastal island connected to the mainland by barrier beaches, levees or dikes
    """
    section_of_island = "ISLX"
    isthmus = "ISTH"
    """
    a narrow strip of land connecting two larger land masses and bordered by water
    """
    karst_area = "KRST"
    """
    a distinctive landscape developed on soluble rock such as limestone characterized by sinkholes, caves, disappearing streams, and underground drainage
    """
    lava_area = "LAVA"
    """
    an area of solidified lava
    """
    levee = "LEVU"
    """
    an embankment bordering a canyon, valley, or seachannel
    """
    mesaLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MESA"
    """
    a flat-topped, isolated elevation with steep slopes on all sides, less extensive than a plateau
    """
    moundLEFT_PARENTHESISsRIGHT_PARENTHESIS = "MND"
    """
    a low, isolated, rounded hill
    """
    moraine = "MRN"
    """
    a mound, ridge, or other accumulation of glacial till
    """
    mountain = "MTU"
    """
    a well-delineated subdivision of a large and complex positive feature
    """
    mountains = "MTS"
    """
    a mountain range or a group of mountains or high ridges
    """
    meander_neck = "NKM"
    """
    a narrow strip of land between the two limbs of a meander loop at its narrowest point
    """
    nunatak = "NTK"
    """
    a rock or mountain peak protruding through glacial ice
    """
    nunataks = "NTKS"
    """
    rocks or mountain peaks protruding through glacial ice
    """
    pan = "PAN"
    """
    a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool
    """
    pans = "PANS"
    """
    a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool
    """
    pass_ = "PASS"
    """
    a break in a mountain range or other high obstruction, used for transportation from one side to the other [See also gap]
    """
    peninsula = "PEN"
    """
    an elongate area of land projecting into a body of water and nearly surrounded by water
    """
    section_of_peninsula = "PENX"
    peak = "PKU"
    """
    a prominent elevation, part of a larger feature, either pointed or of very limited extent across the summit
    """
    peaks = "PKSU"
    """
    prominent elevations, part of a larger feature, either pointed or of very limited extent across the summit
    """
    plateau = "PLTU"
    """
    a comparatively flat-topped feature of considerable extent, dropping off abruptly on one or more sides
    """
    section_of_plateau = "PLATX"
    polder = "PLDR"
    """
    an area reclaimed from the sea by diking and draining
    """
    plainLEFT_PARENTHESISsRIGHT_PARENTHESIS = "PLN"
    """
    an extensive area of comparatively level to gently undulating land, lacking surface irregularities, and usually adjacent to a higher area
    """
    section_of_plain = "PLNX"
    promontoryLEFT_PARENTHESIS_iesRIGHT_PARENTHESIS = "PROM"
    """
    a bluff or prominent hill overlooking or projecting into a lowland
    """
    point = "PT"
    """
    a tapering piece of land projecting into a body of water, less prominent than a cape
    """
    points = "PTS"
    """
    tapering pieces of land projecting into a body of water, less prominent than a cape
    """
    beach_ridge = "RDGB"
    """
    a ridge of sand just inland and parallel to the beach, usually in series
    """
    ridgeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "RDGE"
    """
    a long narrow elevation with steep sides, and a more or less continuous crest
    """
    stony_desert = "REG"
    """
    a desert plain characterized by a surface veneer of gravel and stones
    """
    rock = "RK"
    """
    a conspicuous, isolated rocky mass
    """
    rockfall = "RKFL"
    """
    an irregular mass of fallen rock at the base of a cliff or steep slope
    """
    rocks = "RKS"
    """
    conspicuous, isolated rocky masses
    """
    sand_area = "SAND"
    """
    a tract of land covered with sand
    """
    dry_stream_bed = "SBED"
    """
    a channel formerly containing the water of a stream
    """
    escarpment = "SCRP"
    """
    a long line of cliffs or steep slopes separating level surfaces above and below
    """
    saddle = "SDLU"
    """
    a low part, resembling in shape a saddle, in a ridge or between contiguous seamounts
    """
    shore = "SHOR"
    """
    a narrow zone bordering a waterbody which covers and uncovers at high and low water, respectively
    """
    sinkhole = "SINK"
    """
    a small crater-shape depression in a karst area
    """
    slide = "SLID"
    """
    a mound of earth material, at the base of a slope and the associated scoured area
    """
    slopeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SLP"
    """
    a surface with a relatively uniform slope angle
    """
    spit = "SPIT"
    """
    a narrow, straight or curved continuation of a beach into a waterbody
    """
    spurLEFT_PARENTHESISsRIGHT_PARENTHESIS = "SPUR"
    """
    a subordinate ridge projecting outward from a hill, mountain or other elevation
    """
    talus_slope = "TAL"
    """
    a steep concave slope formed by an accumulation of loose rock fragments at the base of a cliff or steep slope
    """
    interdune_troughLEFT_PARENTHESISsRIGHT_PARENTHESIS = "TRGD"
    """
    a long wind-swept trough between parallel longitudinal dunes
    """
    terrace = "TERU"
    """
    a relatively flat horizontal or gently inclined surface, sometimes long and narrow, which is bounded by a steeper ascending slope on one side and by a steep descending slope on the opposite side
    """
    upland = "UPLD"
    """
    an extensive interior region of high land with low to moderate surface relief
    """
    valley = "VALU"
    """
    a relatively shallow, wide depression, the bottom of which usually has a continuous gradient
    """
    hanging_valley = "VALG"
    """
    a valley the floor of which is notably higher than the valley or shore to which it leads; most common in areas that have been glaciated
    """
    valleys = "VLSU"
    """
    a relatively shallow, wide depression, the bottom of which usually has a continuous gradient
    """
    section_of_valley = "VALX"
    volcano = "VLC"
    """
    a conical elevation composed of volcanic materials with a crater at the top
    """
    apron = "APNU"
    """
    a gentle slope, with a generally smooth surface, particularly found around groups of islands and seamounts
    """
    arrugado = "ARRU"
    """
    an area of subdued corrugations off Baja California
    """
    borderland = "BDLU"
    """
    a region adjacent to a continent, normally occupied by or bordering a shelf, that is highly irregular with depths well in excess of those typical of a shelf
    """
    banks = "BKSU"
    """
    elevations, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation
    """
    basin = "BSNU"
    """
    a depression more or less equidimensional in plan and of variable extent
    """
    cordillera = "CDAU"
    """
    an entire mountain system including the subordinate ranges, interior plateaus, and basins
    """
    canyons = "CNSU"
    """
    relatively narrow, deep depressions with steep sides, the bottom of which generally has a continuous slope
    """
    continental_rise = "CRSU"
    """
    a gentle slope rising from oceanic depths towards the foot of a continental slope
    """
    deep = "DEPU"
    """
    a localized deep area within the confines of a larger feature, such as a trough, basin or trench
    """
    shelf_edge = "EDGU"
    """
    a line along which there is a marked increase of slope at the outer margin of a continental shelf or island shelf
    """
    escarpment_LEFT_PARENTHESISor_scarpRIGHT_PARENTHESIS = "ESCU"
    """
    an elongated and comparatively steep slope separating flat or gently sloping areas
    """
    fan = "FANU"
    """
    a relatively smooth feature normally sloping away from the lower termination of a canyon or canyon system
    """
    flat = "FLTU"
    """
    a small level or nearly level area
    """
    fracture_zone = "FRZU"
    """
    an extensive linear zone of irregular topography of the sea floor, characterized by steep-sided or asymmetrical ridges, troughs, or escarpments
    """
    furrow = "FURU"
    """
    a closed, linear, narrow, shallow depression
    """
    gully = "GLYU"
    """
    a small valley-like feature
    """
    hole = "HOLU"
    """
    a small depression of the sea floor
    """
    knoll = "KNLU"
    """
    an elevation rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summit
    """
    knolls = "KNSU"
    """
    elevations rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summits
    """
    ledge = "LDGU"
    """
    a rocky projection or outcrop, commonly linear and near shore
    """
    mesa = "MESU"
    """
    an isolated, extensive, flat-topped elevation on the shelf, with relatively steep sides
    """
    mound = "MNDU"
    """
    a low, isolated, rounded hill
    """
    moat = "MOTU"
    """
    an annular depression that may not be continuous, located at the base of many seamounts, islands, and other isolated elevations
    """
    plain = "PLNU"
    """
    a flat, gently sloping or nearly level region
    """
    pinnacle = "PNLU"
    """
    a high tower or spire-shaped pillar of rock or coral, alone or cresting a summit
    """
    province = "PRVU"
    """
    a region identifiable by a group of similar physiographic features whose characteristics are markedly in contrast with surrounding areas
    """
    ridge = "RDGU"
    """
    a long narrow elevation with steep sides
    """
    ridges = "RDSU"
    """
    long narrow elevations with steep sides
    """
    reefs = "RFSU"
    """
    surface-navigation hazards composed of consolidated material
    """
    reef = "RFU"
    """
    a surface-navigation hazard composed of consolidated material
    """
    rise = "RISU"
    """
    a broad elevation that rises gently, and generally smoothly, from the sea floor
    """
    seachannel = "SCNU"
    """
    a continuously sloping, elongated depression commonly found in fans or plains and customarily bordered by levees on one or two sides
    """
    seachannels = "SCSU"
    """
    continuously sloping, elongated depressions commonly found in fans or plains and customarily bordered by levees on one or two sides
    """
    shelf = "SHFU"
    """
    a zone adjacent to a continent (or around an island) that extends from the low water line to a depth at which there is usually a marked increase of slope towards oceanic depths
    """
    shoal = "SHLU"
    """
    a surface-navigation hazard composed of unconsolidated material
    """
    shoals = "SHSU"
    """
    hazards to surface navigation composed of unconsolidated material
    """
    shelf_valley = "SHVU"
    """
    a valley on the shelf, generally the shoreward extension of a canyon
    """
    slope = "SLPU"
    """
    the slope seaward from the shelf edge to the beginning of a continental rise or the point where there is a general reduction in slope
    """
    seamounts = "SMSU"
    """
    elevations rising generally more than 1,000 meters and of limited extent across the summit
    """
    seamount = "SMU"
    """
    an elevation rising generally more than 1,000 meters and of limited extent across the summit
    """
    spur = "SPRU"
    """
    a subordinate elevation, ridge, or rise projecting outward from a larger feature
    """
    tablemounts_LEFT_PARENTHESISor_guyotsRIGHT_PARENTHESIS = "TMSU"
    """
    seamounts having a comparatively smooth, flat top
    """
    tablemount_LEFT_PARENTHESISor_guyotRIGHT_PARENTHESIS = "TMTU"
    """
    a seamount having a comparatively smooth, flat top
    """
    tongue = "TNGU"
    """
    an elongate (tongue-like) extension of a flat sea floor into an adjacent higher feature
    """
    trough = "TRGU"
    """
    a long depression of the sea floor characteristically flat bottomed and steep sided, and normally shallower than a trench
    """
    trench = "TRNU"
    """
    a long, narrow, characteristically very deep and asymmetrical depression of the sea floor, with relatively steep sides
    """
    bushLEFT_PARENTHESISesRIGHT_PARENTHESIS = "BUSH"
    """
    a small clump of conspicuous bushes in an otherwise bare area
    """
    cultivated_area = "CULT"
    """
    an area under cultivation
    """
    forestLEFT_PARENTHESISsRIGHT_PARENTHESIS = "FRST"
    """
    an area dominated by tree vegetation
    """
    fossilized_forest = "FRSTF"
    """
    a forest fossilized by geologic processes and now exposed at the earth's surface
    """
    grove = "GROVE"
    """
    a small wooded area or collection of trees growing closely together, occurring naturally or deliberately planted
    """
    grassland = "GRSLD"
    """
    an area dominated by grass vegetation
    """
    coconut_grove = "GRVC"
    """
    a planting of coconut trees
    """
    olive_grove = "GRVO"
    """
    a planting of olive trees
    """
    palm_grove = "GRVP"
    """
    a planting of palm trees
    """
    pine_grove = "GRVPN"
    """
    a planting of pine trees
    """
    heath = "HTH"
    """
    an upland moor or sandy area dominated by low shrubby vegetation including heather
    """
    meadow = "MDW"
    """
    a small, poorly drained area dominated by grassy vegetation
    """
    orchardLEFT_PARENTHESISsRIGHT_PARENTHESIS = "OCH"
    """
    a planting of fruit or nut trees
    """
    scrubland = "SCRB"
    """
    an area of low trees, bushes, and shrubs stunted by some environmental limitation
    """
    treeLEFT_PARENTHESISsRIGHT_PARENTHESIS = "TREE"
    """
    a conspicuous tree used as a landmark
    """
    tundra = "TUND"
    """
    a marshy, treeless, high latitude plain, dominated by mosses, lichens, and low shrub vegetation under permafrost conditions
    """
    vineyard = "VIN"
    """
    a planting of grapevines
    """
    vineyards = "VINS"
    """
    plantings of grapevines
    """
    not_available = "null"


class CountryCodeEnum(str, Enum):
    Andorra = "AD"
    United_Arab_Emirates = "AE"
    Afghanistan = "AF"
    Antigua_and_Barbuda = "AG"
    Anguilla = "AI"
    Albania = "AL"
    Armenia = "AM"
    Angola = "AO"
    Antarctica = "AQ"
    Argentina = "AR"
    American_Samoa = "AS"
    Austria = "AT"
    Australia = "AU"
    Aruba = "AW"
    Aland_Islands = "AX"
    Azerbaijan = "AZ"
    Bosnia_and_Herzegovina = "BA"
    Barbados = "BB"
    Bangladesh = "BD"
    Belgium = "BE"
    Burkina_Faso = "BF"
    Bulgaria = "BG"
    Bahrain = "BH"
    Burundi = "BI"
    Benin = "BJ"
    Saint_Barthelemy = "BL"
    Bermuda = "BM"
    Brunei = "BN"
    Bolivia = "BO"
    Bonaire_Saint_Eustatius_and_Saba = "BQ"
    Brazil = "BR"
    Bahamas = "BS"
    Bhutan = "BT"
    Bouvet_Island = "BV"
    Botswana = "BW"
    Belarus = "BY"
    Belize = "BZ"
    Canada = "CA"
    Cocos_Islands = "CC"
    Democratic_Republic_of_the_Congo = "CD"
    Central_African_Republic = "CF"
    Republic_of_the_Congo = "CG"
    Switzerland = "CH"
    Ivory_Coast = "CI"
    Cook_Islands = "CK"
    Chile = "CL"
    Cameroon = "CM"
    China = "CN"
    Colombia = "CO"
    Costa_Rica = "CR"
    Cuba = "CU"
    Cabo_Verde = "CV"
    Curacao = "CW"
    Christmas_Island = "CX"
    Cyprus = "CY"
    Czechia = "CZ"
    Germany = "DE"
    Djibouti = "DJ"
    Denmark = "DK"
    Dominica = "DM"
    Dominican_Republic = "DO"
    Algeria = "DZ"
    Ecuador = "EC"
    Estonia = "EE"
    Egypt = "EG"
    Western_Sahara = "EH"
    Eritrea = "ER"
    Spain = "ES"
    Ethiopia = "ET"
    Finland = "FI"
    Fiji = "FJ"
    Falkland_Islands = "FK"
    Micronesia = "FM"
    Faroe_Islands = "FO"
    France = "FR"
    Gabon = "GA"
    United_Kingdom = "GB"
    Grenada = "GD"
    Georgia = "GE"
    French_Guiana = "GF"
    Guernsey = "GG"
    Ghana = "GH"
    Gibraltar = "GI"
    Greenland = "GL"
    Gambia = "GM"
    Guinea = "GN"
    Guadeloupe = "GP"
    Equatorial_Guinea = "GQ"
    Greece = "GR"
    South_Georgia_and_the_South_Sandwich_Islands = "GS"
    Guatemala = "GT"
    Guam = "GU"
    Guinea_Bissau = "GW"
    Guyana = "GY"
    Hong_Kong = "HK"
    Heard_Island_and_McDonald_Islands = "HM"
    Honduras = "HN"
    Croatia = "HR"
    Haiti = "HT"
    Hungary = "HU"
    Indonesia = "ID"
    Ireland = "IE"
    Israel = "IL"
    Isle_of_Man = "IM"
    India = "IN"
    British_Indian_Ocean_Territory = "IO"
    Iraq = "IQ"
    Iran = "IR"
    Iceland = "IS"
    Italy = "IT"
    Jersey = "JE"
    Jamaica = "JM"
    Jordan = "JO"
    Japan = "JP"
    Kenya = "KE"
    Kyrgyzstan = "KG"
    Cambodia = "KH"
    Kiribati = "KI"
    Comoros = "KM"
    Saint_Kitts_and_Nevis = "KN"
    North_Korea = "KP"
    South_Korea = "KR"
    Kosovo = "XK"
    Kuwait = "KW"
    Cayman_Islands = "KY"
    Kazakhstan = "KZ"
    Laos = "LA"
    Lebanon = "LB"
    Saint_Lucia = "LC"
    Liechtenstein = "LI"
    Sri_Lanka = "LK"
    Liberia = "LR"
    Lesotho = "LS"
    Lithuania = "LT"
    Luxembourg = "LU"
    Latvia = "LV"
    Libya = "LY"
    Morocco = "MA"
    Monaco = "MC"
    Moldova = "MD"
    Montenegro = "ME"
    Saint_Martin = "MF"
    Madagascar = "MG"
    Marshall_Islands = "MH"
    North_Macedonia = "MK"
    Mali = "ML"
    Myanmar = "MM"
    Mongolia = "MN"
    Macao = "MO"
    Northern_Mariana_Islands = "MP"
    Martinique = "MQ"
    Mauritania = "MR"
    Montserrat = "MS"
    Malta = "MT"
    Mauritius = "MU"
    Maldives = "MV"
    Malawi = "MW"
    Mexico = "MX"
    Malaysia = "MY"
    Mozambique = "MZ"
    Namibia = "NA"
    New_Caledonia = "NC"
    Niger = "NE"
    Norfolk_Island = "NF"
    Nigeria = "NG"
    Nicaragua = "NI"
    The_Netherlands = "NL"
    Norway = "NO"
    Nepal = "NP"
    Nauru = "NR"
    Niue = "NU"
    New_Zealand = "NZ"
    Oman = "OM"
    Panama = "PA"
    Peru = "PE"
    French_Polynesia = "PF"
    Papua_New_Guinea = "PG"
    Philippines = "PH"
    Pakistan = "PK"
    Poland = "PL"
    Saint_Pierre_and_Miquelon = "PM"
    Pitcairn = "PN"
    Puerto_Rico = "PR"
    Palestinian_Territory = "PS"
    Portugal = "PT"
    Palau = "PW"
    Paraguay = "PY"
    Qatar = "QA"
    Reunion = "RE"
    Romania = "RO"
    Serbia = "RS"
    Russia = "RU"
    Rwanda = "RW"
    Saudi_Arabia = "SA"
    Solomon_Islands = "SB"
    Seychelles = "SC"
    Sudan = "SD"
    South_Sudan = "SS"
    Sweden = "SE"
    Singapore = "SG"
    Saint_Helena = "SH"
    Slovenia = "SI"
    Svalbard_and_Jan_Mayen = "SJ"
    Slovakia = "SK"
    Sierra_Leone = "SL"
    San_Marino = "SM"
    Senegal = "SN"
    Somalia = "SO"
    Suriname = "SR"
    Sao_Tome_and_Principe = "ST"
    El_Salvador = "SV"
    Sint_Maarten = "SX"
    Syria = "SY"
    Eswatini = "SZ"
    Turks_and_Caicos_Islands = "TC"
    Chad = "TD"
    French_Southern_Territories = "TF"
    Togo = "TG"
    Thailand = "TH"
    Tajikistan = "TJ"
    Tokelau = "TK"
    Timor_Leste = "TL"
    Turkmenistan = "TM"
    Tunisia = "TN"
    Tonga = "TO"
    Turkey = "TR"
    Trinidad_and_Tobago = "TT"
    Tuvalu = "TV"
    Taiwan = "TW"
    Tanzania = "TZ"
    Ukraine = "UA"
    Uganda = "UG"
    United_States_Minor_Outlying_Islands = "UM"
    United_States = "US"
    Uruguay = "UY"
    Uzbekistan = "UZ"
    Vatican = "VA"
    Saint_Vincent_and_the_Grenadines = "VC"
    Venezuela = "VE"
    British_Virgin_Islands = "VG"
    UFULL_STOPSFULL_STOP_Virgin_Islands = "VI"
    Vietnam = "VN"
    Vanuatu = "VU"
    Wallis_and_Futuna = "WF"
    Samoa = "WS"
    Yemen = "YE"
    Mayotte = "YT"
    South_Africa = "ZA"
    Zambia = "ZM"
    Zimbabwe = "ZW"
    Serbia_and_Montenegro = "CS"
    Netherlands_Antilles = "AN"


class TimezoneEnum(str, Enum):
    AmericaSOLIDUSSao_Paulo = "America/Sao_Paulo"
    """
    America/Sao_Paulo
    """
    AmericaSOLIDUSCaracas = "America/Caracas"
    """
    America/Caracas
    """
    AmericaSOLIDUSMontevideo = "America/Montevideo"
    """
    America/Montevideo
    """
    AmericaSOLIDUSGuatemala = "America/Guatemala"
    """
    America/Guatemala
    """
    AmericaSOLIDUSLa_Paz = "America/La_Paz"
    """
    America/La_Paz
    """
    AmericaSOLIDUSBelem = "America/Belem"
    """
    America/Belem
    """
    AmericaSOLIDUSAraguaina = "America/Araguaina"
    """
    America/Araguaina
    """
    AmericaSOLIDUSBahia = "America/Bahia"
    """
    America/Bahia
    """
    AmericaSOLIDUSArgentinaSOLIDUSCordoba = "America/Argentina/Cordoba"
    """
    America/Argentina/Cordoba
    """
    AmericaSOLIDUSMaceio = "America/Maceio"
    """
    America/Maceio
    """
    AmericaSOLIDUSFortaleza = "America/Fortaleza"
    """
    America/Fortaleza
    """
    AmericaSOLIDUSLima = "America/Lima"
    """
    America/Lima
    """
    AmericaSOLIDUSSantarem = "America/Santarem"
    """
    America/Santarem
    """
    AmericaSOLIDUSCayenne = "America/Cayenne"
    """
    America/Cayenne
    """
    AmericaSOLIDUSRio_Branco = "America/Rio_Branco"
    """
    America/Rio_Branco
    """
    AmericaSOLIDUSCampo_Grande = "America/Campo_Grande"
    """
    America/Campo_Grande
    """
    AmericaSOLIDUSNoronha = "America/Noronha"
    """
    America/Noronha
    """
    AmericaSOLIDUSPorto_Velho = "America/Porto_Velho"
    """
    America/Porto_Velho
    """
    AmericaSOLIDUSGuyana = "America/Guyana"
    """
    America/Guyana
    """
    AmericaSOLIDUSCuiaba = "America/Cuiaba"
    """
    America/Cuiaba
    """
    AmericaSOLIDUSManaus = "America/Manaus"
    """
    America/Manaus
    """
    AmericaSOLIDUSParamaribo = "America/Paramaribo"
    """
    America/Paramaribo
    """
    AmericaSOLIDUSAsuncion = "America/Asuncion"
    """
    America/Asuncion
    """
    AmericaSOLIDUSBoa_Vista = "America/Boa_Vista"
    """
    America/Boa_Vista
    """
    AmericaSOLIDUSCosta_Rica = "America/Costa_Rica"
    """
    America/Costa_Rica
    """
    AmericaSOLIDUSBogota = "America/Bogota"
    """
    America/Bogota
    """
    AmericaSOLIDUSEirunepe = "America/Eirunepe"
    """
    America/Eirunepe
    """
    AmericaSOLIDUSRecife = "America/Recife"
    """
    America/Recife
    """


class AgentType(str, Enum):
    """
    Tipo de agente na terminologia LIDO.
    """

    individual = "personal"
    coletivo = "corporate"
    """
    Uma entidade coletiva tal como uma oficina, escola (no sentido de um grupo de artistas que partilham um estilo semelhante), empresa, corporação de ofício, grupo étnico-cultural, ou outra agremiação na qual é impossível ou irrelevante delimitar as contribuições individuais.

    """
    familiar = "family"
    """
    Coletivo de agentes caracterizado por laços familiares, incluindo parentesco consanguíneo, por matrimônio, adotivo ou outras relações familiares socialmente sancionadas no seu contexto de origem.

    """
    outro = "other"


class CollectionType(str):
    """
    The LIDO Object Type Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Object Type element, specifying the particular kind of object being in some way associated with the object/work that is the focus of the record.
    """

    pass


class ConceptType(str, Enum):
    """
    Tipos de termos de vocabulário baseados no Getty AAT.

    """

    conceitos = "concept"
    LEFT_PARENTHESISnome_de_hierarquiaRIGHT_PARENTHESIS = "hierarchy_name"
    LESS_THAN_SIGNtermo_guiaGREATER_THAN_SIGN = "guide_term"
    Faceta = "facet"


class DateType(str, Enum):
    """
    Exatidão da data conhecida.
    """

    conhecida = "exact"
    """
    Designates a date that is definitely known, based on credible, documented fact.
    Note that *exact* does not preclude the granularity of the date expression.

    """
    provável = "estimated"
    """
    Designates a date that is uncertain, estimated broadly using available information about the work or the artist. For example, you could estimate that the earliest possible date for any work by a given artist is eighteen or twenty years after the artist's birth.
    Included are also dates that are inferred from known dates associated with the object. For instance, if the date of production is unknown, but the date when the object was found is known, there is evidence that the production must have taken place before the finding of the object.

    """


class DepictionType(str, Enum):
    """
    Designa a relação que a edificação descrita na ficha tem com a mídia relacionada.

    """

    representado_em = "depictedIn"
    """
    A obra descrita na ficha está representada na mídia relacionada, que será geralmente uma obra de arte ou fotografia depositada num repositório externo (catálogo de museu, Wikimedia Commons, etc.).

    """


class EventType(str, Enum):
    """
    O tipo de incidência sobre a edificação que o evento descreve. Usa a terminologia do LIDO em <http://terminology.lido-schema.org/eventType>.

    """

    criação = "creation"
    """
    Designa um acontecimento que leva à conceção de itens ou produtos de natureza imaterial, como obras literárias ou imagens. Não usar para a produção de bens materiais. Quando a conceção desses bens, como uma edificação, passa por um processo de criação intelectual atestada, usar para tanto o termo `designing` ("projeto").

    """
    projeto = "designing"
    """
    O projeto, na classificação de tipos de eventos do LIDO, designa a criação de um arcabouço conceitual para a organização da aparência de objetos tridimensionais, obras visuais, obras de arquitetura, ou sistemas técnicos.

    """
    produção = "production"
    """
    Designa ações que levam à existência de novos objetos, compreendendo ações como projeto e execução.

    """
    produção_de_um_exemplar = "item_production"
    """
    No caso de construções seriadas (por exemplo, casas idênticas numa vila operária), designa a produção de um exemplar singular dentro do conjunto. Usar quando for relevante individualizar a produção desses exemplares no âmbito da descrição do seu conjunto, mas não quando cada exemplar for indexado separadamente.

    """
    conclusão = "completion"
    """
    Processo que completa um objeto ou uma campanha de obras.

    """
    execução_do_projeto = "execution"
    """
    Ação de produzir um objeto com base num projeto, por oposição ao processo de projeto.

    """
    transformação = "transformation"
    """
    Ação que destrói um objeto e, usando substancialmente a mesma matéria, produz outro que mantém características reconhecíveis do objeto anterior mas é essencialmente distinto deste por sua natureza e identidade. Esta categoria pode ser usada tanto para designar a destruição do objeto antigo quanto a produção do objeto novo.
    Exemplos de transformação incluem o uso de espólios ou ruínas para produzir uma nova construção. Não deve ser confundido com `reconstruction` ("reconstrução"), que implica seja uma mudança de lugar, seja a reprodução da identidade visual e espacial da edificação anterior.

    """
    reconstrução = "reconstruction"
    """
    Ato de construir uma nova estrutura que substitui e se parece com uma construção anterior que já não subsiste, baseada em evidências históricas, arqueológicas, gráficas, literárias ou outras. A semelhança visual e, eventualmente, funcional é a característica principal de uma reconstrução, e ela pode ou não usar materiais sobrestantes da edificação anterior.
    A edificação destruída e a edificação reconstruída devem ser cadastradas em fichas distintas e relacionadas entre si.

    """
    remoção = "translocation"
    """
    A remoção designa o ato de se desmantelar uma edificação no seu local de origem para reconstruí-la em outro sítio. Para construções deslocadas sem serem desmanteladas, usar o tipo de evento `move` ("deslocação").
    Exemplos de remoção são aquela do templo de Abu Simbel, no Egito, ou ainda aquela da casa Erbo Stenzel em Curitiba do seu lote original para o parque São Lourenço (onde foi posteriormente destruída num incêndio).

    """
    alteração = "modification_process"
    """
    Processo não deliberado de alteração nas características, aparência ou desempenho dos materiais que constituem um objeto. Por exemplo, corrosão, formação de cristais salinos, etc.

    """
    conservação = "conservation"
    """
    Ação ou processo realizado visando à estabilidade e salvaguarda do objeto no longo prazo, incluindo a sua proteção contra danos ou deterioração e a prevenção da deterioração natural da sua matéria. No nosso vocabulário, a conservação é diferente da preservação e da restauração.

    """
    reforma = "conversion"
    """
    Intervenção significativa na materialidade e espacialidade de uma edificação, usando materiais e técnicas construtivas. Frequentemente resulta na alteração de uso ou de aparência da edificação, mas sem comprometer a sua identidade anterior.
    Sempre que possível, preferir designações mais específicas, tais como `addition`, `removal`, `adaptive_reuse`, `renewal`.

    """
    desmantelamento = "dismantling"
    """
    Ato de desmontar ou remover partes significativas de um objeto, especialmente com a intenção de reduzir ou desbilitar o seu uso. Particularmente, refere-se à desmontagem cuidadosa de modo a evitar danos ao material removido, visando à sua reutilização, reciclagem ou gestão de resíduos.

    """
    acréscimo = "addition"
    """
    Acréscimo a uma edificação existente, sem lhe alterar fundamentalmente a identidade, por meio da ampliação ou do acréscimo de elementos. O conjunto resultante continuará a ser identificado como a mesma obra anterior ao acréscimo.

    """
    eliminação_parcial = "removal"
    """
    Envolve a redução de uma edificação devida à eliminação de parte(s). Pode incluir a eliminação de anexos, de elementos construtivos, ou a exclusão de uma obra de um conjunto designado.

    """
    destruição_parcial = "partial_destruction_activity"
    """
    Ação intencional de destruir ou danificar partes de uma obra, sem lhe comprometer a identatidade enquanto objeto de documentação.

    """
    reconstituição = "remediation"
    """
    Atividades construtivas ou de gestão que têm por objetivo restituir uma obra a um estado anterior conhecido ou presumido, sobretudo após perdas catastróficas de materialidade ou integridade.

    """
    renovação = "renewal"
    """
    Ação que altera uma edificação de modo a recuperar a sua estrutura, atualizar a sua aparência, permitir a adequação a novos usos, aprimorar a sua eficiência energética, ou outras finalidades não relacionadas à preservação do patrimônio cultural ou que não tenham considerações patrimoniais como prioridade.

    """
    restauração = "restoration"
    """
    Alterações a um objeto que têm por objetivo restabelecer um estado original ou anterior conhecido ou presumido (usar em vez de `part_removal` --- "eliminação parcial" se a intenção dominante da eliminação tiver sido a restauração a um estado anterior).

    """
    perda_parcial = "partial_destruction_process"
    """
    Processo não intencional de degradação material, destruindo ou danificando partes de um objeto sem descaracterizar a sua identidade (por exemplo, sem convertê-lo numa ruína). Pode ser causado por condições ambientais continuadas ou por desastres naturais.

    """
    deterioração = "deterioration"
    """
    Processo de perda parcial de matéria, desempenho, ou funcionalidade de um objeto sem intervenção ou atuação deliberada. Geralmente causado por condições ambientais continuadas, mas pode ser agravado por desastres naturais. A deterioração pode levar ao `destruction_process` ("arruinamento") da edificação.

    """
    reutilização_adaptada = "adaptive_reuse"
    """
    Ação de converter ou adaptar uma edificação, em geral com valor histórico-cultural reconhecido, para novos usos ou aplicação em contexto distinto do original. Distinguir eventos de reutilização adaptativa de eventos que envolvem as intervenções físicas necessárias ou preparatórias a essa reutilização, usando o termo `conversion` ("reforma").

    """
    inauguração = "opening"
    """
    Ato pelo qual um objeto é declarado operacional, geralmente por meio de uma cerimônia, mas não necessariamente.

    """
    desafetação = "decommissioning"
    """
    Ação que acompanha ou sinaliza o encerramento da utilização de um objeto, geralmente associado à interdição física da edificação.

    """
    attribute_assignment = "attribute_assignment"
    assignment_to_curated_holding = "assignment_to_curated_holding"
    levantamento_e_avaliação_do_estado_de_conservação = "condition_assessment"
    """
    Ação que analisa as características físicas do objeto, seu estado de conservação e integridade formal.

    """
    cultural_context_assignment = "cultural_context_assignment"
    designation = "designation"
    deciphering = "deciphering"
    meaning_assignment = "meaning_assignment"
    name_assignment = "name_assignment"
    type_assignment = "type_assignment"
    ceremony = "ceremony"
    cornerstone = "cornerstone"
    groundbreaking = "groundbreaking"
    consecration = "consecration"
    deconsecration = "deconsecration"
    change_control_or_title = "change_control_or_title"
    change_control_and_title = "change_control_and_title"
    change_legal_title = "change_legal_title"
    restitution = "restitution"
    change_physical_control = "change_physical_control"
    collecting = "collecting"
    loss = "loss"
    commissioning = "commissioning"
    excavation = "excavation"
    exhibition = "exhibition"
    finding = "finding"
    marketing = "marketing"
    move = "move"
    req_assess = "req_assess"
    display_assess = "display_assess"
    move_assess = "move_assess"
    performance = "performance"
    planning = "planning"
    protection = "protection"
    publishing = "publishing"
    use = "use"
    end_existence = "end_existence"
    destruction = "destruction"
    destruction_activity = "destruction_activity"
    destruction_process = "destruction_process"
    unknown = "unknown"


class EventPlaceType(str, Enum):
    """
    Para eventos que implicam a deslocação do bem, indica se o local se refere ao descobrimento, à origem ou ao destino da obra.
    """

    discovery = "discovery"
    origin = "origin"
    destination = "destination"


class PeriodNameType(str, Enum):
    """
        O vocabulário de tipos de período/estilo do LIDO é uma lista controlada estruturada de termos recomendada para uso como valores do atributo de tipo do elemento Período/Estilo.
    O atributo de tipo qualifica o tipo particular de informação de período/estilo, como estilo, período ou movimento. Exemplos podem ser “neolítico” para um período, “impressionista” para um estilo ou “cubismo” para um movimento.
    Baseado na categoria do [CDWA "Styles/Periods/Groups/Movements"](http://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)

    """

    period = "period"
    """
    A distinct named historical or cultural portion or division of time during which something runs its course, characterized by some prevalent or distinguishing condition, circumstance, or occurrence, or by the rule of a particular government.

    """
    style = "style"
    """
    A distinct configuration of artistic elements that together constitute a named manner of expression peculiar to a certain epoch, people, or to a visual appearance, technique, or visual language adopted by particular adherents of that language.

    """
    group = "group"
    """
    A cultural group, which includes societies or groups of people characterized by common ideas, customs, social behavior, products, or way of life within a particular nation, people, or period.

    """
    movement = "movement"
    """
    The state or process in which events or conditions transpire, a tendency, or a trend evident at a particular time or in a particular sphere, particularly a course or series of actions and endeavours on the part of a group of people working towards a shared goal or to advance a shared political, social, or artistic objective.

    """
    dynasty = "dynasty"
    """
    The succession of rulers from the same family, line, stock, or group, during a particular period of time; extended to include all the people and culture surrounding this succession of rulers.

    """


class GeometryType(str, Enum):
    """
    Tipos de geometria do objeto geoJSON
    """

    Polygon = "Polygon"
    MultiPolygon = "MultiPolygon"


class InscriptionType(str, Enum):
    """
    Tipos de inscrições previstos no VRA Core.
    """

    signature = "signature"
    mark = "mark"
    caption = "caption"
    date = "date"
    text = "text"
    translation = "translation"
    other = "other"


class LabelType(str, Enum):
    """
    No SKOS, caracteriza se cada termo deve ser considerado preferencial ou alternativo, usado para indexação, oculto da visualização (usado apenas para buscas), etc.

    """

    alternative = "alternative"
    """
    Abreviações, abreviaturas, variantes lexicais e formas irregulares de singular ou plural podem ser incluídas como termos ou títulos alternativos para um conceito ou objeto. No caso de edificações ou conjuntos que são conhecidos por mais de um nome (por exemplo, pela sua função atual ou antiga, ou pelo endereço), selecionar `alternative` e indicar o tipo de título.
    """
    display = "display"
    """
    Nome a ser apresentado na interfaz pública, incluindo artigos se for o caso.
    """
    hidden = "hidden"
    """
    Uma variante do nome com erros comuns de grafia ou imprecisões lexicais, mas que seja relevante para buscas dos usuários. Deve ficar oculto da interfaz pública.
    """
    indexing = "indexing"
    """
    Nome, termo ou identificador a ser usado em indexação, por exemplo removendo artigos ou partículas iniciais, invertendo a ordem do nome e do sobrenome, etc.
    """
    preferred = "preferred"
    """
    O nome, termo ou título preferencial. Normalmente não usaremos esta opção pois o campo `title` já contempla a opção preferencial.
    """


class LargerContextType(str, Enum):
    """
        Tipos de relações entre partes e todo previstas no vocabulário controlado
    do LIDO. Inclui as categorias de relações hierárquicas e de relações
    associativas de parte ao todo.

    Ver <http://terminology.lido-schema.org/relatedWorkRelType>

    """

    fisicamente_contido_em = "physical_part_of"
    """
    Usar quando um objeto físico fizer parte integrante de um objeto ou complexo físico maior. Se o conjunto mais amplo for um construto interpretativo, usar a relação `has_borader_conceptual_context`.

    """
    parte_conceitual_de = "conceptual_part_of"
    """
    Usar quando um objeto intelectual for parte de uma entidade conceitual maior ou mais ampla.

    """
    tem_contexto_conceitual_mais_amplo = "has_borader_conceptual_context"
    """
    Usar quando um objeto físico for incluído segundo critérios interpretativos num conjunto conceitual mais amplo. Se o conjunto mais amplo for uma extensão física que compreende inequivocamente o objeto, usar a relação `physical_part_of`.

    """
    exemplar_de = "example_of"
    """
    Usar quando o objeto construído é a manifestação física de um conteúdo intelectual, podendo abarcar desde instâncias específicas de um projeto seriado (por exemplo, um exemplar das casas da SHIS — Sociedade de Habitações de Interesse Social — produzidas em Brasília a partir de 1969) até a realização edificada de um programa teórico específico (por exemplo, a Cité Radieuse de Marselha como exemplo da unité d'habitation de Le Corbusier).
    Vinculações teóricas ou conceituais com maior distância interpretativa (por exemplo, o Jardim América como exemplar de cidade–jardim) devem ser cadastradas no grupo `subject`.

    """
    tem_como_contexto_arquitetônico = "has_arch_context"
    """
    O objeto em causa foi concebido para integrar ou está situado no referido conjunto edificado, ou integra o contexto funcional deste.

    """
    tinha_como_contexto_arquitetônico = "had_arch_context"
    """
    O objeto em causa foi concebido para integrar ou esteve situado no referido conjunto edificado, mas não tem mais esse contexto por ter sido trasladado ou removido, ou porque o contexto foi destruído ou descaracterizado.

    """
    pertence_ao_mesmo_contexto_conceitual_que = "in_conceptual_whole_with"
    """
    Relação simétrica entre dois objetos que pertencem ao mesmo contexto conceitual. Usar apenas nos casos em que o conjunto conceitual maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.

    """
    pertence_ao_mesmo_contexto_material_que = "in_physical_whole_with"
    """
    Relação simétrica entre dois objetos que pertencem ao mesmo contexto material ou espacial. Usar apenas nos casos em que o conjunto arquitetônico maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.

    """
    pertenceu_ao_mesmo_contexto_que = "was_part_of_whole_with"
    """
    Relação simétrica entre dois objetos que pertenceram ao mesmo contexto conceitual, material ou espacial, mas já não pertencem devido a remoção, traslado, destruição ou reclassificação. Usar apenas nos casos em que o conjunto maior não for cadastrado no documentário, por motivos técnicos ou decisão científica.

    """
    foi_precedido_no_mesmo_sítio_por = "was_antedated"
    faz_parte_de = "is_part_of"
    """
    Relação genérica entre parte e todo. Sempre que possível, usar os tipos de relação mais específicos.

    """
    anteriormente_parte_de = "formerly_part_of"
    """
    O objeto físico em questão era anteriormente compreendido num conjunto edificado maior que não mais existe, seja porque o conjunto foi parcialmente demolido ou descaracterizado, ou porque suas outras partes foram trasladadas ou removidas.

    """
    parte_de = "is_was_part_of"
    """
    O objeto faz ou fazia parte de um conjunto físico maior, mas não é possível determinar se esse conjunto ainda existe ou não.

    """


class MaterialTechType(str, Enum):
    """
    A materialidade e as técnicas de produção ou intervenção na edificação devem ser categorizadas segundo esta classificação.

    """

    material = "material"
    medium = "medium"
    support = "support"
    color_name = "color_name"
    implement = "implement"
    technique = "technique"
    watermark = "watermark"
    other = "other"


class MeasurementQualifier(str, Enum):
    """
    Qualifica a confiabilidade das medidas aferidas.

    """

    interpretativa = "interpreted"
    """
    Metrologia interpretativa ou citação textual.
    """
    estimativa_visual = "estimated"
    """
    Estimativa obtida por comparação com uma escala gráfica, com medidas adjacentes conhecidas, ou por caminhamento, partes do corpo, etc.

    """
    extrapolada = "derived"
    """
    Extrapolado de um desenho ou modelo.
    """
    medida_no_local = "measured"
    """
    Medida obtida no local por meio de instrumentos manuais ou eletrônicos (trena, teodolito, etc.).

    """
    escaneada_digitalmente = "scanned"
    """
    Medida extraída de um escaneamento a laser de alta precisão ou de uma estação topográfica digital.

    """


class MeasurementType(str, Enum):
    """
    The type attribute qualifies whether the measurements given are features of the object proper or object requirements for handling the object, for instance, the maximum temperature variation.
    """

    proper = "proper"
    requirement = "requirement"


class ReferenceType(str, Enum):
    """
    Tipos de referências a objetos externos previstos no LIDO.

    """

    URI = "uri"
    IRI = "iri"
    Identificador_local = "local"


class RelatedWorkRelType(str, Enum):
    """
        Relações associativas entre objetos físicos ou criações intelectuais,
    definidas segundo o vocabulário do LIDO.
    Compreende as relações associativas, exceto aquelas de partes com o todo.

    Ver <http://terminology.lido-schema.org/relatedWorkRelType>

    """

    documentado_em = "documentedIn"
    """
    A obra descrita na ficha está documentada, discutida ou descrita na mídia relacionada, que em geral será um texto.

    """
    complementa = "complements"
    """
    Relação entre obras criadas independentemente uma da outra, mas que mais tarde passaram a ser consideradas ou usadas conjuntamente.

    """
    complementava = "complemented"
    """
    Relação entre obras criadas independentemente uma da outra, mas que mais tarde passaram a ser consideradas ou usadas conjuntamente, sendo essa associação posteriormente desfeita.

    """
    derivado_de = "derivedFrom"
    """
    A obra descrita é derivada ou sensivelmente influenciada pelo objeto relacionado.
    Preferir outras expressões de relação mais específicas sempre que possível. A relação `derivedFrom` deve ser reservada para casos em que a relação seja de variações e influências. Essas relações devem ser fundamentadas em interpretação bibliográfica.

    """
    próximo_a = "positionedNear"
    """
    Relação simétrica entre dois objetos situados em proximidade espacial, quando esta proximidade for significativa por razões compositivas, históricas ou funcionais.

    """


class ResourceType(str, Enum):
    """
        Relações associativas entre objetos físicos ou criações intelectuais, definidas segundo o vocabulário do LIDO. Compreende as relações de documentação técnica das edificações.
    Ver <http://terminology.lido-schema.org/relatedWorkRelType>
    """

    architecturalSurvey = "architecturalSurvey"
    planFor = "planFor"


class RepositoryType(str, Enum):
    """
    Type of repository or legal body.
    """

    institucional = "corporate"
    geográfico = "geographic"
    individual = "personal"
    outro = "other"


class RightsType(str, Enum):
    """
    LIDO expressions for rights types.
    """

    generic = "generic"
    specific = "specific"


class RoleType(str, Enum):
    """
    Contribuições de um agente a um evento.
    """

    author = "author"
    builder = "builder"
    collector = "collector"
    commissioner = "commissioner"
    composer = "composer"
    contractor = "contractor"
    creator = "creator"
    dealer = "dealer"
    decorator = "decorator"
    designer = "designer"
    developer = "developer"
    director = "director"
    donator = "donator"
    drafter = "drafter"
    drawer = "drawer"
    editor = "editor"
    engineer = "engineer"
    financier = "financier"
    formerOwner = "formerOwner"
    manufacturer = "manufacturer"
    owner = "owner"
    painter = "painter"
    partnerInSetWith = "partnerInSetWith"
    performer = "performer"
    photographer = "photographer"
    printer = "printer"
    producer = "producer"
    programmer = "programmer"
    restorer = "restorer"
    writer = "writer"


class SkosMappingRelation(str, Enum):
    """
    SKOS mapping properties.
    """

    close = "close"
    exact = "exact"
    broad = "broad"
    narrow = "narrow"
    related = "related"


class SkosBroaderRelation(str, Enum):
    """
    SKOS-THES broader relation type.
    """

    broader = "broader"
    transitive = "transitive"
    generic = "generic"
    instantial = "instantial"
    partitive = "partitive"


class SkosNarrowerRelation(str, Enum):
    """
    SKOS-THES narrower relation type.
    """

    broader = "broader"
    transitive = "transitive"
    generic = "generic"
    instantial = "instantial"
    partitive = "partitive"


class TitleType(str, Enum):
    """
    VRA Core title types.
    """

    brandName = "brandName"
    cited = "cited"
    creator = "creator"
    descriptive = "descriptive"
    former = "former"
    inscribed = "inscribed"
    owner = "owner"
    popular = "popular"
    repository = "repository"
    translated = "translated"
    other = "other"


class SubjectType(str, Enum):
    """
        The type attribute indicates the kind of subject information, whether it is, for instance, a description of a generic subject, an identification of a named individual, or an interpretation of the theme.
    Note that "Iconclass notations" are distinguished from other index terms for subject type in order to consider the impact of the type of indexing vocabulary with respect to information retrieval facilities.

    """

    descriptive = "descriptive"
    iconographic = "iconographic"
    concept = "concept"
    other = "other"


class ConceptReference(ConfiguredBaseModel):
    """
    Atribuição de vocabulário controlado com citação de apoio.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class BroaderConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    broader_match: SkosBroaderRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["BroaderConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class NarrowerConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    narrower_match: SkosNarrowerRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["NarrowerConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class MappingConceptReference(ConceptReference):
    """
    Relações semânticas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    mapping_match: SkosMappingRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["MappingConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class BibliographicCitation(ConfiguredBaseModel):
    """
    Cadastro de uma referência bibliográfica.
    Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "dcterms:BibliographicCitation",
            "close_mappings": ["crm:E31_Document", "schema:CreativeWork"],
            "from_schema": "https://tradicional.arq.br/schema/resource",
        }
    )

    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    refid: str = Field(
        default=...,
        description="""Se a fonte for cadastrada, o campo `refid` deve conter a chave de citação (`citation key`) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no [Zotero]. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se a referência que necessita citar não constar da biblioteca do Zotero, deve cadastrá-la primeiro nessa biblioteca para então extrair a chave de citação.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["BibliographicCitation"]}},
    )
    note: Optional[str] = Field(
        default=None,
        description="""Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["BibliographicCitation"]}},
    )


class TypedReference(ConfiguredBaseModel):
    """
    Permite referenciar um registro local ou externo por meio da sua URI (localizador universal, como um link da internet, por padrão), IRI ou código na base local (não recomendado).
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://tradicional.arq.br/schema/shared",
            "notes": [
                "Reference to a local record, IRI, URI, or LIDO terminology term."
            ],
            "slot_usage": {"refid": {"key": True, "name": "refid"}},
        }
    )

    refid_type: Optional[ReferenceType] = Field(
        default=ReferenceType("uri"),
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference"],
                "ifabsent": "ReferenceType(uri)",
            }
        },
    )
    refid: str = Field(
        default=...,
        description="""Local or external identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference"],
                "exact_mappings": ["schema:identifier"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class Measurement(ConfiguredBaseModel):
    """
    Informações estruturadas sobre as dimensões do objeto ou requisitos de condicionamento ambiental no espaço que ele ocupa. Para edificações, é recomendável cadastrar ao menos a área útil, testada e a altura de coroamento.
    Se a modulação original for conhecida ou puder ser deduzida por um estudo metrológico, é interessante cadastrar também as medidas históricas utilizadas (por exemplo, dimensões em palmos).
    O campo `description` permite uma representação textual das medidas da edificação, caso não seja viável cadastrar medidas individuais com precisão, ou seja preciso maior flexibilidade para explicar as dimensões.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "crm:E16_Measurement",
            "from_schema": "https://tradicional.arq.br/schema/shared",
            "notes": [
                "This class comprises actions measuring physical properties and "
                "other values that can be determined by a systematic, objective "
                "procedure of direct observation of particular states of physical "
                "reality.",
                "An instance of E16 Measurement may use simple counting or tools, "
                "such as yardsticks or radiation detection devices. The interest is "
                "in the method and care applied, so that the reliability of the "
                "result may be judged at a later stage, or research continued on "
                "the associated documents. The date of the event is important for "
                "dimensions, which may change value over time, such as the length "
                "of an object subject to shrinkage. Methods and devices employed "
                "should be associated with instances of E16 Measurement by "
                "properties such as: *P33 used specific technique*: E29 Design or "
                "Procedure, *P125 used object of type*: E55 Type, *P16 used "
                "specific object (was used for)*: E70 Thing, whereas basic "
                'techniques such as "carbon-14 dating" should be encoded using *P2 '
                "has type (is type of)*: E55 Type. Details of methods and devices "
                "reused or reusable in other instances of E16 Measurement should be "
                "documented for these entities rather than the measurements "
                "themselves, whereas details of particular execution may be "
                "documented by free text or by instantiating adequate "
                "sub-activities, if the detail may be of interest for an "
                "overarching query.",
                "Regardless whether a measurement is made by an instrument or by "
                "human senses, it represents the initial transition from physical "
                "reality to information without any other documented information "
                "object in between within the reasoning chain that would represent "
                "the result of the interaction of the observer or device with "
                "reality. Therefore, determining properties of an instance of E90 "
                "Symbolic Object is regarded as an instance of E13 Attribute "
                "Assignment, which may be inferred from observing and measuring "
                "representative carriers. In the case that the carrier can be "
                "named, the property *P16 used specific object (was used for)* "
                "should be used to indicate the instance(s) of E18 Physical Thing "
                "that was used as the empirical basis for the attribute assignment. "
                "For instance, inferring properties of depicted items using image "
                "material, such as satellite images, is not regarded as an instance "
                "of E16 Measurement, but as a subsequent instance of E13 Attribute "
                "Assignment. Rather, only the production of the images, understood "
                "as arrays of radiation intensities, is regarded as an instance of "
                "E16 Measurement. The same reasoning holds for other sensor data.",
            ],
            "related_mappings": ["dcterms:format"],
            "slot_usage": {"unit": {"name": "unit", "required": True}},
        }
    )

    unit: TypedReference = Field(
        default=...,
        description="""Unidade de medida usada no dimensionamento do objeto ou da representação, por exemplo metros, milímetros ou palmos. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096) do AAT, ou do nosso próprio [vocabulário controlado].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Resource", "MediaObject", "Measurement"]}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    format_extent: Optional[TypedReference] = Field(
        default=None,
        description="""Indica a parte do objeto que está sendo medida — por exemplo, se a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário controlado.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Measurement", "Inscription", "Topic"]}
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    related_events: Optional[list[RelatedEvent]] = Field(
        default=None,
        description="""Indica a ocorrência de outro acontecimento, vinculado ou não à mesma edificação, que apresenta algum tipo de relação com este evento ou com uma informação (por exemplo, a ação que resultou na obtenção da referida informação).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement", "Event"]}},
    )
    measurement_type: Optional[MeasurementType] = Field(
        default=MeasurementType("proper"),
        description="""O tipo de medida pode se referir ao objeto propriamente dito `proper` ou a um requisito para a sua conservação ou uso, `requirement`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Measurement"],
                "ifabsent": "MeasurementType(proper)",
            }
        },
    )
    measurement_extent: Optional[TypedReference] = Field(
        default=None,
        description="""designa a natureza da medida : largura, altura, área, etc. — usar um dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820) do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos um vocabulário controlado próprio.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )
    measurement_value: float = Field(
        default=...,
        description="""Valor numérico, usar ponto como separador decimal.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )
    measurement_qualifier: Optional[MeasurementQualifier] = Field(
        default=MeasurementQualifier("derived"),
        description="""Indica o grau de confiabilidade das medidas.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Measurement"],
                "ifabsent": "MeasurementQualifier(derived)",
            }
        },
    )
    measurement_shape: Optional[str] = Field(
        default=None,
        description="""caso relevante, indicar a forma do elemento medido usando a [lista de formas do AAT](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300056273), enquanto não tivermos um vocabulário controlado próprio.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )
    measurement_event: Optional[Event] = Field(
        default=None,
        description="""Descreve a ocasião em que as medidas foram aferidas, caso essa informação seja relevante (por exemplo, no âmbito de um levantamento prévio a intervenções que alteraram as dimensões da edificação).
Referencia um evento cadastrado em `temporal` pelo seu `id`.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )


class MaterialTech(ConceptReference):
    """
    Usar discernimento para identificar sistemas, materiais e técnicas que interessam ao conhecimento da edificação no seu conjunto, não a partes menos extensas ou pouco importantes.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/shared"}
    )

    material_tech_type: MaterialTechType = Field(
        default=...,
        description="""Tipo da referência a um material ou técnica usado na obra: material de construção (support), revestimento (medium), técnica, instrumento, cor, etc.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["MaterialTech"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class Right(ConfiguredBaseModel):
    """
    * Preencher `earliest_date` com a data de início da vigência dos
      direitos ou a data do preenchimento da ficha.

    * `latest_date` pode ser omitido se não houver fim da vigência.
    * `holder` pode ser omitido se a obra estiver no domínio público.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "crm:E30_Right",
            "from_schema": "https://tradicional.arq.br/schema/shared",
        }
    )

    rights_type: RightsType = Field(
        default=...,
        description="""Determina se os direitos ora descritos são uma licença específica (padrão) ou expressão genérica de copyright.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Right"],
                "notes": [
                    "Qualifies the kind of rights type, whether it refers to a generic "
                    "kind of right, like copyright or performance rights, or is a "
                    "specific rights or license statement, for instance, Rights "
                    "Statements or Creative Commons Licenses."
                ],
            }
        },
    )
    statement: TypedReference = Field(
        default=...,
        description="""Referencia, preferencialmente por meio de uma URI, as informações
específicas dos direitos autorais incidentes sobre o item descrito.

Por padrão, as casas tradicionais pertencem ao domínio público até
prova em contrário.
Essa informação e a declaração de direitos NKC (Sem direito autoral
conhecido) NÃO PODE ser omitida da ficha.
Para o domínio público, portanto, indicar a referência :
<https://rightsstatements.org/vocab/NKC/1.0/>.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Right"],
                "notes": [
                    "An index element for rights information being recorded. This can "
                    "refer to a generic kind of right, such as copyright or a related "
                    "right, but also be a specific rights or license statement like a "
                    "standardized statement on copyright, usage, or access rights."
                ],
            }
        },
    )
    earliest_date: Optional[EventDate] = Field(
        default=None,
        description="""Date on which a right is or was current.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )
    latest_date: Optional[EventDate] = Field(
        default=None,
        description="""Date on which a right is or will be no longer current.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )
    holder: Optional[LegalBody] = Field(
        default=None,
        description="""A set of elements identifying the person or the group of persons holding the rights referenced in Rights Type. Often refers to copyright and related rights, such as the right to reproduce, distribute, exhibit or use the entity in focus, for example, the object/work, resource or metadata record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )


class Actor(ConfiguredBaseModel):
    """
    Agent and role in an event.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/temporal"}
    )

    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    actor_type: Optional[AgentType] = Field(
        default=AgentType("personal"),
        description="""Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, uma família, etc.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Actor"], "ifabsent": "AgentType(personal)"}
        },
    )
    actor_name: Optional[TypedReference] = Field(
        default=None,
        description="""Nome do agente extraído de um vocabulário controlado.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    role_in_event: Optional[RoleType] = Field(
        default=None,
        description="""Ação desempenhada pelo agente no evento.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    actor_qualifier: Optional[list[TypedReference]] = Field(
        default=None,
        description="""For the Attribution Qualifier Actor element choose a concept URI from the [attribution qualifiers hierarchy](http://vocab.getty.edu/hier/aat/300404264) of the Art & Architecture Thesaurus, or another linked open vocabulary.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    actor_extent: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Parte da obra sobre a qual o agente interveio.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )


class EventDate(ConfiguredBaseModel):
    """
    Expressão complexa de uma data que pode se referir ao começo ou ao término de um evento pontual ou de uma decorrência prolongada. Permite expressar as datas de corte inicial e final, cada uma com seus respetivos graus de confiabilidade e de precisão.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "comments": [
                "⚠️  Não temos padrão estabelecido para datas anteriores ao "
                "calendário gregoriano (1583), antes de Cristo, ou convertidas "
                "de outros calendários. Datas no calendário juliano podem ser "
                "expressadas nominalmente. Datas da era ibérica podem usar o "
                "valor nominal do dia e do mês, tendo o ano convertido para o "
                "gregoriano. Datas de calendários não cristãos podem ser "
                "convertidas para a data gregoriana correspondente, mesmo as "
                "anteriores a 1583.\n"
                "Ver <https://en.wikipedia.org/wiki/ISO_8601#Dates> para a "
                "discussão dessa dificuldade, cuja solução depende do "
                "estabelecimento de um padrão específico para cada caso."
            ],
            "from_schema": "https://tradicional.arq.br/schema/temporal",
            "notes": [
                "A wrapper for the expression of a date by providing a set of years "
                "as earliest and latest date delimiting the respective span of "
                "time, usually given in the proleptic Gregorian calendar.\n"
                "If it is an exact date, possibly with time, repeat the same date "
                "(and time) in Earliest Date and Latest Date elements."
            ],
        }
    )

    date_type: DateType = Field(
        default=...,
        description="""Qualifica a confiabilidade da data como sendo conhecida ou estimada. A confiabilidade independe do grau de precisão da data.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["EventDate"]}},
    )
    date_value: Optional[date] = Field(
        default=None,
        description="""Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Para datas imprecisas, usar o PRIMEIRO ou o ÚLTIMO dia, mês ou ano do período delimitado, conforme se tratar de uma data de corte inicial ou final para o evento, e descrever verbalmente o período no campo `display_date`.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["EventDate"]}},
    )


class StylePeriod(ConceptReference):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/temporal"}
    )

    period_name_type: PeriodNameType = Field(
        default=...,
        description="""Designa a natureza ou origem do nome do período ou estilo indicado.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["StylePeriod"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )


class RelatedEvent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/temporal"}
    )

    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    event_name: list[Event] = Field(
        default=...,
        description="""Identifica o evento ralacionado.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["RelatedEvent"], "symmetric": True}
        },
    )


class Thing(ConfiguredBaseModel):
    """
    Esta classe compreende todas as coisas no universo do CIDOC CRM. É um conceito abstrato que prevê três propriedades gerais:
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

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "crm:E1_CRM_Entity",
            "exact_mappings": ["schema:Thing"],
            "from_schema": "https://tradicional.arq.br/schema/thing",
        }
    )

    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Thing",
        "http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity",
        "wasth:Thing",
        "crm:E1_CRM_Entity",
    ] = Field(
        default="crm:E1_CRM_Entity",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Concept(Thing):
    """
    Um conceito é uma unidade de conhecimento ou entendimento delimitada e definida com clareza, distinta de outros conceitos. Cada conceito pretende descrever um aspecto ou recorte da realidade empírica ou teórica, de modo que a sua definição seja amplamente conhecida e partilhada dentro do campo disciplinar ao qual ele pertence.
    Para além da clareza na definição do próprio conceito, estabelecer a sua relação com outros conceitos mais gerais ou mais específicos é importante ao se constituir um vocabulário controlado.
    Por isso, a definição de cada conceito DEVE se referir a bibliografia consagrada e, sempre que possível, a outros vocabulários controlados nacionais e estrangeiros.
    -------------------------------------------------------------------------
    A SKOS concept can be viewed as an idea or notion; a unit of thought. However, what constitutes a unit of thought is subjective, and this definition is meant to be suggestive, rather than restrictive.
    The notion of a SKOS concept is useful when describing the conceptual or intellectual structure of a knowledge organization system, and when referring to specific ideas or meanings established within a KOS.
    Note that, because SKOS is designed to be a vehicle for representing semi-formal KOS, such as thesauri and classification schemes, a certain amount of flexibility has been built in to the formal definition of this class.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "skos:Concept",
            "exact_mappings": ["schema:DefinedTerm"],
            "from_schema": "https://tradicional.arq.br/schema/concept",
            "slot_usage": {
                "content": {
                    "description": "Notas de escopo sobre o conceito.",
                    "name": "content",
                    "slot_uri": "skos:scopeNote",
                }
            },
        }
    )

    broader: Optional[list[BroaderConceptReference]] = Field(
        default=None,
        description="""Um conceito de significação mais genérica. Conceitos genéricos são tipicamente representados como pais em uma hierarquia de conceitos (árvore).
Preenchimento manual.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Concept"], "slot_uri": "skos:broader"}
        },
    )
    narrower: Optional[list[NarrowerConceptReference]] = Field(
        default=None,
        description="""Um conceito de significação mais específica. Conceitos específicos são tipicamente representados como descendentes em uma hierarquia de conceitos (árvore).
Derivado automaticamente das relações `broader` em outras fichas. NÃO preencher manualmente.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Concept"], "slot_uri": "skos:narrower"}
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha e o detentor desses direitos.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Concept", "Work"],
                "notes": [
                    "A set of structured information about rights regarding the content "
                    "provided in this LIDO record."
                ],
            }
        },
    )
    concept_type: Optional[ConceptType] = Field(
        default=ConceptType("concept"),
        description="""Tipos de termos de vocabulário baseados no Getty AAT.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Concept"],
                "ifabsent": "ConceptType(concept)",
            }
        },
    )
    mapping: Optional[list[MappingConceptReference]] = Field(
        default=None,
        description="""Um conceito com o qual existe um relacionamento semântico associativo. Usar em referência a vocabulários externos, como o Getty Art and Architecture Thesaurus.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Concept"]}},
    )
    relation: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Um conceito com o qual existe um relacionamento semântico associativo. Usar em referência ao nosso próprio vocabulário controlado.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Concept"], "slot_uri": "skos:related"}
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Concept",
        "http://www.w3.org/2004/02/skos/core#Concept",
        "wasth:Concept",
        "skos:Concept",
    ] = Field(
        default="skos:Concept",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Notas de escopo sobre o conceito.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class RelatedObject(Thing):
    """
    A set of structured information about an object or work, or a group of objects or works related to the object/work in focus, including the kind of relationship between them. May include bibliographic objects in which the object/work is documented or mentioned.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"abstract": True, "from_schema": "https://tradicional.arq.br/schema/resource"}
    )

    work_rights: Optional[list[Right]] = Field(
        default=None,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/RelatedObject", "wasth:RelatedObject"
    ] = Field(
        default="wasth:RelatedObject",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


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
    O grupo relation é destinado unicamente a cadastrar relações desta edificação com objetos autônomos, tais como outras edificações, conjuntos urbanos, obras de artes visuais, referências bibliográficas ou acervos arquivísticos.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/resource"}
    )

    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedWork", "LargerContextReference", "Event", "Work"]
            }
        },
    )
    relation_type: RelatedWorkRelType = Field(
        default=...,
        description="""Indica o tipo de relação entre a edificação descrita na ficha e o objeto relacionado. O sujeito do tipo é sempre a obra titular da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedWork"],
                "slot_uri": "lido:relatedWorkRelType",
            }
        },
    )
    work_rights: Optional[list[Right]] = Field(
        default=None,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/RelatedWork", "wasth:RelatedWork"
    ] = Field(
        default="wasth:RelatedWork",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class LargerContextReference(RelatedObject):
    """
    Tipo de relação específica entre obras a ser usado quando o objeto descrito na ficha é ou era parte integrante de outro objeto, físico ou intelectual.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/resource"}
    )

    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedWork", "LargerContextReference", "Event", "Work"]
            }
        },
    )
    context_type: LargerContextType = Field(
        default=...,
        description="""O tipo de relação entre os objetos.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["LargerContextReference"],
                "slot_uri": "lido:relatedWorkRelType",
            }
        },
    )
    work_rights: Optional[list[Right]] = Field(
        default=None,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/LargerContextReference",
        "wasth:LargerContextReference",
    ] = Field(
        default="wasth:LargerContextReference",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Resource(Thing):
    """
    Este grupo identifica um recurso visual ou documental que fornece informações técnicas ou uma representação ilustrativa da obra à qual ele se relaciona.
    Recursos produzidos pela equipe dos Documentários da Arquitetura Tradicional são descritos na ficha de cada edificação, no grupo `resources`. Representações e documentos externos são referidos nos grupos `media` e `related_works`, respetivamente.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "crm:E31_Document",
            "close_mappings": ["schema:ArchiveComponent"],
            "from_schema": "https://tradicional.arq.br/schema/resource",
            "notes": [
                "This class comprises identifiable immaterial items that make "
                "propositions about reality.\n"
                "These propositions may be expressed in text, graphics, images, "
                "audiograms, videograms, or by other similar means. Documentation "
                "databases are regarded as instances of E31 Document. This class "
                "should not be confused with the concept “document” in Information "
                "Technology, which is compatible with E73 Information Object."
            ],
            "slot_usage": {
                "category": {
                    "ifabsent": "string(http://terminology.lido-schema.org/lido01193)",
                    "name": "category",
                },
                "id": {"identifier": True, "name": "id"},
            },
        }
    )

    format: str = Field(
        default=...,
        description="""Campo disciplinado pela especificação [DublinCore] no campo [format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/). Esta especificação sugere a lista de tipos de mídia IANA : <https://www.iana.org/assignments/media-types>.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Resource", "MediaObject"],
                "slot_uri": "dcterms:format",
            }
        },
    )
    scale: Optional[float] = Field(
        default=None,
        description="""Número inverso da escala da imagem ou desenho, se tiver uma resolução ou tamanho de página definidos. Por exemplo, para um desenho na escala 1 : 100, `scale: 100`.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    unit: Optional[TypedReference] = Field(
        default=None,
        description="""Unidade de medida usada no dimensionamento do objeto ou da representação, por exemplo metros, milímetros ou palmos. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096) do AAT, ou do nosso próprio [vocabulário controlado].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Resource", "MediaObject", "Measurement"]}
        },
    )
    preview_image: Optional[str] = Field(
        default=None,
        description="""Uma única miniatura da imagem original.
Obs.: não usamos a opção `placeholder`, ela será preenchida automaticamente em caso de ausência da miniatura, nem outros tipos de miniaturas que não imagens. A especificação LIDO admite listar mais de uma miniatura, mas tampouco prevemos essa hipótese.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    provided_image: Optional[list[str]] = Field(
        default=None,
        description="""Lista de versões ampliadas ou originais da imagem, vetorial ou bitmap.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    provided_3d: Optional[list[str]] = Field(
        default=None,
        description="""Modelo tridimensional ou IFC da edificação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    resource_service: Optional[list[str]] = Field(
        default=None,
        description="""Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal como a especificação [IIIF].
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    credit: Optional[str] = Field(
        default=None,
        description="""Informação sobre autoria ou responsabilidade.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    work_rights: Optional[list[Right]] = Field(
        default=None,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    resource_type: ResourceType = Field(
        default=...,
        description="""Usamos os tipos de relação previstos pelo LIDO em `relatedWorkRelType > Associative relationships > Derivative relationships`. Provavelmente necessitamos apenas de :
- `planFor` : desenho técnico bidimensional de levantamento
  (padrão, pode ser omitido) ;

- `modelFor` : modelo tridimensional, com ou sem informações construtivas
  associadas (BIM) ;

- `imageOf` : outras representações em duas dimensões da edificação ;
- `preparatoryFor` : representação técnica de projeto para intervenções a
  serem realizadas (ou já realizadas) na edificação.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Resource"],
                "slot_uri": "lido:relatedWorkRelType",
            }
        },
    )
    perspective: int = Field(
        default=...,
        description="""Tipo de vista do desenho. Usar a numeração da ISO 19650–2 :

  - 0 = sem projeção ou representação não visual
  - 1 = planta baixa
  - 2 = elevação
  - 3 = corte
  - 4 = mapa de elementos
  - 5 = detalhe
  - 6 = mapa de revestimentos
  - 7 = planta de forro
  - 8 = vista ou modelo 3D
  - 9 = definido pelo agente
""",
        ge=0,
        le=9,
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource"]}},
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Resource",
        "http://www.cidoc-crm.org/cidoc-crm/E31_Document",
        "wasth:Resource",
        "crm:E31_Document",
    ] = Field(
        default="crm:E31_Document",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "ifabsent": "string(http://terminology.lido-schema.org/lido01193)",
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class MediaObject(RelatedObject):
    """
    Descrição e referência a um único arquivo de mídia.
    O `id` deve ser uma URI apontando para a localização permanente da mídia, não diretamente para um arquivo de imagem.
    Obrigatoriamente deve conter um link para o recurso online, seja na forma de `provided_image`, `provided_3d` ou `resource_service`. É importante, também, fornecer o link para uma miniatura que será usada como pré-visualização, em `preview_image`.
    No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
    Por exemplo, no caso de uma imagem hospedada no Wikimedia Commons:
    ``` id: https://commons.wikimedia.org/wiki/File:BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg preview_image: https://thumb.wikimedia.org/wikipedia/commons/thumb/8/86/BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg/330px-BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg provided_image:
      - https://upload.wikimedia.org/wikipedia/commons/8/86/BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg
    resource_service:
      - https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&format=json&titles=File:BR-DF-Planaltina-Casarao_azul-PP-090421-3018.jpg
    ```
    Não armazenamos imagens ou outros arquivos de mídia nos sites dos Documentários da Arquitetura Tradicional.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:MediaObject",
            "close_mappings": ["dctypes:Image"],
            "from_schema": "https://tradicional.arq.br/schema/resource",
            "slot_usage": {
                "content": {
                    "description": "Opcional, para descrever com mais "
                    "detalhe a representação.\n",
                    "name": "content",
                },
                "description": {
                    "description": "Texto alternativo para "
                    "leitores de tela ou outras "
                    "formas de acessibilidade. "
                    "Apenas texto sem formatação.\n",
                    "name": "description",
                    "required": True,
                },
                "title": {
                    "description": "Título breve para identificar este "
                    "recurso visual na listagem.\n",
                    "name": "title",
                    "required": True,
                },
                "work_rights": {"name": "work_rights", "required": True},
            },
        }
    )

    format: str = Field(
        default=...,
        description="""Campo disciplinado pela especificação [DublinCore] no campo [format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/). Esta especificação sugere a lista de tipos de mídia IANA : <https://www.iana.org/assignments/media-types>.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Resource", "MediaObject"],
                "slot_uri": "dcterms:format",
            }
        },
    )
    scale: Optional[float] = Field(
        default=None,
        description="""Número inverso da escala da imagem ou desenho, se tiver uma resolução ou tamanho de página definidos. Por exemplo, para um desenho na escala 1 : 100, `scale: 100`.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    unit: Optional[TypedReference] = Field(
        default=None,
        description="""Unidade de medida usada no dimensionamento do objeto ou da representação, por exemplo metros, milímetros ou palmos. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096) do AAT, ou do nosso próprio [vocabulário controlado].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Resource", "MediaObject", "Measurement"]}
        },
    )
    preview_image: Optional[str] = Field(
        default=None,
        description="""Uma única miniatura da imagem original.
Obs.: não usamos a opção `placeholder`, ela será preenchida automaticamente em caso de ausência da miniatura, nem outros tipos de miniaturas que não imagens. A especificação LIDO admite listar mais de uma miniatura, mas tampouco prevemos essa hipótese.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    provided_image: Optional[list[str]] = Field(
        default=None,
        description="""Lista de versões ampliadas ou originais da imagem, vetorial ou bitmap.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    provided_3d: Optional[list[str]] = Field(
        default=None,
        description="""Modelo tridimensional ou IFC da edificação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    resource_service: Optional[list[str]] = Field(
        default=None,
        description="""Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal como a especificação [IIIF].
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    measurements: Optional[list[Measurement]] = Field(
        default=None,
        description="""A wrapper for information about the dimensions, or other measurements, of the object/work in focus. May also include extents of the parts of a complex object or work.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["MediaObject", "Event", "Work"]}
        },
    )
    credit: Optional[str] = Field(
        default=None,
        description="""Informação sobre autoria ou responsabilidade.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    depiction_type: DepictionType = Field(
        default=...,
        description="""O tipo de representação que a mídia contém. A edificação descrita na ficha é sempre o sujeito da relação.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["MediaObject"],
                "slot_uri": "lido:relatedWorkRelType",
            }
        },
    )
    work_rights: list[Right] = Field(
        default=...,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    title: str = Field(
        default=...,
        description="""Título breve para identificar este recurso visual na listagem.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: str = Field(
        default=...,
        description="""Texto alternativo para leitores de tela ou outras formas de acessibilidade. Apenas texto sem formatação.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/MediaObject",
        "http://schema.org/MediaObject",
        "wasth:MediaObject",
        "schema:MediaObject",
    ] = Field(
        default="schema:MediaObject",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Opcional, para descrever com mais detalhe a representação.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class LegalBody(Thing):
    """
    Referência a uma pessoa jurídica (pode ser um indivíduo detentor de direitos jurídicos específicos que se queira referenciar) ou entidade coletiva histórica.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:Organization",
            "close_mappings": ["crm:E39_Actor"],
            "from_schema": "https://tradicional.arq.br/schema/shared",
            "notes": [
                "This class comprises people, either individually or in groups, who "
                "have the potential to perform intentional actions of kinds for "
                "which they can be held responsible.",
                "O schema.org prevê um atributo `fundedItem` (do tipo `Grant`) para "
                "uma `Organization`.",
            ],
            "slot_usage": {
                "category": {"ifabsent": "string(term:lido00413)", "name": "category"},
                "identifiers": {
                    "description": "Referencia a identidade do "
                    "ente legal num vocabulário "
                    "controlado ou repositório de "
                    "identidades, tal como o "
                    "ISNI.\n",
                    "name": "identifiers",
                },
            },
        }
    )

    legal_body_type: Optional[RepositoryType] = Field(
        default=RepositoryType("corporate"),
        description="""Define a natureza do ente legal : pessoa jurídica, perímetro geográfico de tutela, etc.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["LegalBody"],
                "ifabsent": "RepositoryType(corporate)",
            }
        },
    )
    weblink: Optional[str] = Field(
        default=None,
        description="""Link para uma página descritiva da entidade.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["LegalBody"]}},
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/LegalBody",
        "http://schema.org/Organization",
        "wasth:LegalBody",
        "schema:Organization",
    ] = Field(
        default="schema:Organization",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "ifabsent": "string(term:lido00413)",
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Referencia a identidade do ente legal num vocabulário controlado ou repositório de identidades, tal como o ISNI.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Event(Thing):
    """
    Um evento é um processo específico e coerente, delimitável, de interações entre fatores materiais, humanos e físico-ambientais, que afetam objetos de modo característico ao tipo de processo em jogo. Pode tratar-se de uma ação ou um conjunto articulado de ações intencionais, de consequências imprevistas de ações intencionais, ou de processos naturais sem intervenção humana.
    -------------------------------------------------------------------------
    This class comprises distinct, delimited and coherent processes and interactions of a material nature, in cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way characteristic of the kind of process. Typical examples are meetings, births, deaths, actions of decision taking, making or inventing things, but also more complex and extended ones such as conferences, elections, building of a castle, or battles.
    While the continuous growth of a tree lacks the limits characteristic of an event, its germination from a seed does qualify as an event. Similarly, the blowing of the wind lacks the distinctness and limits of an event, but a hurricane, flood or earthquake would qualify as an event. Mental processes are considered as events, in cases where they are connected with the material externalization of their results; for example, the creation of a poem, a performance or a change of intention that becomes obvious from subsequent actions or declarations.
    The effects of an instance of E5 Event may not lead to relevant permanent changes of properties or relations of the items involved in it, for example an unrecorded performance. Of course, in order to be documented, some kind of evidence for an event must exist, be it witnesses, traces or products of the event.
    While instances of E4 Period always require some form of coherence between its constituent phenomena, in addition, the essential constituents of instances of E5 Event should contribute to an overall effect; for example, the statements made during a meeting and the listening of the audience.
    Viewed at a coarse level of detail, an instance of E5 Event may appear as if it had an ‘instantaneous’ overall effect, but any process or interaction of material nature in reality have an extent in time and space. At a fine level, instances of E5 Event may be analysed into component phenomena and phases within a space and timeframe, and as such can be seen as a period, regardless of the size of the phenomena. The reverse is not necessarily the case: not all instances of E4 Period give rise to a noteworthy overall effect and are thus not instances of E5 Event.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "crm:E5_Event",
            "exact_mappings": ["schema:Event"],
            "from_schema": "https://tradicional.arq.br/schema/temporal",
            "slot_usage": {
                "content": {
                    "description": "Descrição textual mais extensa do "
                    "acontecimento, quando necessário "
                    "ou relevante. Pode conter texto "
                    "formatado e referências "
                    "bibliográficas.\n",
                    "name": "content",
                },
                "description": {
                    "description": "Permite a expressão descritiva "
                    "das datas de início e fim do "
                    "evento, para contemplar "
                    "variados graus de incerteza, "
                    "ou de modo a representar a "
                    "data em calendários diferentes "
                    "do gregoriano. Omitir apenas "
                    "se os valores numéricos das "
                    "datas forem exatos.\n",
                    "name": "description",
                },
                "title": {
                    "description": "Um nome breve para o evento, sem formatação.\n",
                    "name": "title",
                },
            },
        }
    )

    style_period: Optional[list[StylePeriod]] = Field(
        default=None,
        description="""Denomina o(s) período(s) em que o evento decorreu, em qualquer escala relevante para o conhecimento : geológica, arqueológica, histórica ou artística. A identificação do período ou estilo deve ser relevante para as características que o objeto adquiriu devido a esse evento, não somente uma coincidência cronológica.
---------------------------------------------------------------------
An index element for the period in which the event happened, comprising information about geologic time scale, archaelogical, historical, or artistic period, style, or art movement, whose characteristics are represented by the object or work.
Note that \"Period/Style\" corresponds to \"Style\" in CDWA as shorthand for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html).
Examples may be Neolithic for a period, Impressionist for a style, or Cubism for a movement.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event", "Work"]}},
    )
    culture: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Designa o contexto cultural ou étnico no qual o objeto foi afetado pelo evento em questão, desde que as características de tal contexto estejam refletidas no objeto. O preenchimento do contexto cultural é especialmente relevante quando os agentes envolvidos na produção ou alteração do objeto são desconhecidos.
---------------------------------------------------------------------
An index element for the cultural context from which the object/work in focus originated. Used if the creator or producer is unknown, or if the cultural context is of particular interest. Examples may include the name of a culture, a nation, or an ethnic group.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event", "Work"]}},
    )
    measurements: Optional[list[Measurement]] = Field(
        default=None,
        description="""A wrapper for information about the dimensions, or other measurements, of the object/work in focus. May also include extents of the parts of a complex object or work.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["MediaObject", "Event", "Work"]}
        },
    )
    material: Optional[list[MaterialTech]] = Field(
        default=None,
        description="""Descreve a natureza do material empregado na edificação, no elemento ou no evento descritos. Conforme necessário e segundo o discernimento de quem preenche a ficha, pode se referir a matérias-primas ou a produtos prontos para uso.
Espólios ou partes de outras edificações reutilizadas podem ser descritos segundo os materiais de que são constituídos, mas a procedência não deve ser cadastrada neste item. Para tanto, devem ser utilizados os eventos no grupo `temporal`.
-------------------------------------------------------------------------
This class is a specialization of E55 Type and comprises the concepts of materials.
Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing).
This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E57 Material, e.g. “instances of gold”.
It is recommended that internationally or nationally agreed codes and terminology should be used.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Event", "Work"],
                "exact_mappings": ["vra:Material"],
                "slot_uri": "crm:E57_Material",
            }
        },
    )
    technique: Optional[list[MaterialTech]] = Field(
        default=None,
        description="""Processos, técnicas, métodos e saberes postos em prática no conjunto da edificação e nas suas partes mais significativas, considerando a sua produção e alterações substanciais, bem como a sua eventual destruição.
-------------------------------------------------------------------------
The production or manufacturing processes, techniques, and methods incorporated in the fabrication or alteration of the work or image.
""",
        json_schema_extra={
            "linkml_meta": {
                "close_mappings": ["crm:E55_Type"],
                "domain_of": ["Event", "Work"],
                "slot_uri": "vra:Technique",
            }
        },
    )
    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedWork", "LargerContextReference", "Event", "Work"]
            }
        },
    )
    related_events: Optional[list[RelatedEvent]] = Field(
        default=None,
        description="""Indica a ocorrência de outro acontecimento, vinculado ou não à mesma edificação, que apresenta algum tipo de relação com este evento ou com uma informação (por exemplo, a ação que resultou na obtenção da referida informação).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement", "Event"]}},
    )
    event_type: EventType = Field(
        default=...,
        description="""Categoriza o evento segundo os vários tipos de ações, de processos, ou de resultados (início ou fim da existência, transformação).
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    actor_role: Optional[list[Actor]] = Field(
        default=None,
        description="""Identificação de um agente e do seu papel no evento.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    start_date: Optional[list[EventDate]] = Field(
        default=None,
        description="""Data inicial do evento ou mais antiga data presumida para o seu decurso. Omitir se desconhecida.
Por ora, é responsabilidade de quem preenche a ficha assegurar que `start_date` e `end_date` ocorram em ordem cronológica. Não dispomos de validação automática para tanto.
""",
        min_length=0,
        max_length=2,
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    end_date: Optional[list[EventDate]] = Field(
        default=None,
        description="""Data final do evento ou mais tardia data presumida para o seu decurso. Omitir se desconhecida.
Por ora, é responsabilidade de quem preenche a ficha assegurar que `start_date` e `end_date` ocorram em ordem cronológica. Não dispomos de validação automática para tanto.
""",
        min_length=0,
        max_length=2,
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    event_place: Optional[list[Site]] = Field(
        default=None,
        description="""Lugares associados ao evento, sem incluir o próprio local no qual se situa a edificação.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    method: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""An index element for the method by which the event is or was carried out. Examples may include an acquisition method or a field collection method.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    things_present: Optional[list[RelatedWork]] = Field(
        default=None,
        description="""A set of structured information for a related object or work that is or was present at the event in focus. Repeated if there are multiple related objects or works.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    title: Optional[str] = Field(
        default=None,
        description="""Um nome breve para o evento, sem formatação.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""Permite a expressão descritiva das datas de início e fim do evento, para contemplar variados graus de incerteza, ou de modo a representar a data em calendários diferentes do gregoriano. Omitir apenas se os valores numéricos das datas forem exatos.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Event",
        "http://www.cidoc-crm.org/cidoc-crm/E5_Event",
        "wasth:Event",
        "crm:E5_Event",
    ] = Field(
        default="crm:E5_Event",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Descrição textual mais extensa do acontecimento, quando necessário ou relevante. Pode conter texto formatado e referências bibliográficas.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Appellation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/thing"}
    )

    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    label: Optional[str] = Field(
        default=None,
        description="""Nome ou título (texto sem formatação).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Appellation"]}},
    )
    appellation_preference: Optional[LabelType] = Field(
        default=LabelType("alternative"),
        description="""Indica se o nome em questão deve ser oculto ou não, se é uma versão alternativa ou uma variante de grafia, etc.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Appellation"],
                "ifabsent": "LabelType(alternative)",
            }
        },
    )
    title_type: Optional[TitleType] = Field(
        default=TitleType("descriptive"),
        description="""Categoriza a natureza do nome dado ao objeto ou conceito.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Appellation", "Work"],
                "ifabsent": "TitleType(descriptive)",
            }
        },
    )


class Repository(Thing):
    """
    Entidade com existência jurídica e espacial.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:Organization",
            "from_schema": "https://tradicional.arq.br/schema/thing",
        }
    )

    site: Site = Field(
        default=...,
        description="""A localização real, atual da edificação — é o que será usado em quase todos os casos.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Repository", "Work"]}},
    )
    legal_body: LegalBody = Field(
        default=...,
        description="""Informações estruturadas sobre a pessoa jurídica.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Repository"]}},
    )
    repository_type: Optional[RepositoryType] = Field(
        default=RepositoryType("corporate"),
        description="""Categoriza a natureza física ou jurídica do repositório.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Repository"],
                "ifabsent": "RepositoryType(corporate)",
            }
        },
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Repository",
        "http://schema.org/Organization",
        "wasth:Repository",
        "schema:Organization",
    ] = Field(
        default="schema:Organization",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Work(Thing):
    """
    Nos Documentários da Arquitetura Tradicional, esta ficha é usada para cadastrar uma edificação, um conjunto arquitetônico, ou ainda uma parte significativa de uma edificação.
    <h3>Especificação e modelo de preenchimento</h3>
    As instruções de preeenchimento para cada elemento da ficha se encontram na seção [Slots](#slots).
    Observe como exemplo de ficha (quase) completamente preenchida a [Casa dos Sete Candeeiros](https://github.com/arqtrad/casa/blob/main/br-ba-salvador-casa_7_candeeiros.md?plain=1).
    Em caso de dúvidas quanto à formatação da ficha, observe as informações acerca da especificação [YAML](https://www.yaml.info/learn/index.html).
    Todos os grupos que começam com um hífen `-` são listas que podem conter qualquer número de linhas ou blocos.
    A ordem dos blocos não é importante, mas a hierarquia dentro de cada bloco e a indentação de dois espaços por nível hierárquico, sim.
    O caractere `#` indica o início de um comentário, que prossegue até o final da linha. Os comentários e as linhas que contêm apenas comentários devem ser apagados das fichas preenchidas.
    Campos não preenchidos também devem ser apagadas das fichas.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:LandmarksOrHistoricalBuildings",
            "close_mappings": ["crm:E22_Human-Made_Object"],
            "exactly_one_of": [
                {"slot_conditions": {"author": {"name": "author", "required": True}}},
                {"slot_conditions": {"authors": {"name": "authors", "required": True}}},
            ],
            "from_schema": "https://tradicional.arq.br/schema/work",
            "notes": [
                "An historical landmark or building.",
                "This class comprises all persistent physical objects of any size "
                "that are purposely created by human activity and have physical "
                "boundaries that separate them completely in an objective way from "
                "other objects.\n"
                "The class also includes all aggregates of objects made for "
                "functional purposes of whatever kind, independent of physical "
                "coherence, such as a set of chessmen.",
            ],
            "slot_usage": {
                "category": {"ifabsent": "string(term:lido00096)", "name": "category"},
                "content": {
                    "description": "Deixe uma linha em branco após o "
                    "fechamento dos metadados e inclua "
                    "aqui uma descrição morfológica e "
                    "histórica da edificação com texto "
                    "livre, usando formatação "
                    "Markdown.\n"
                    "Poderá incluir um segundo bloco de "
                    "metadados para indicar as "
                    "referências bibliográficas da "
                    "descrição textual, no campo "
                    "`nocite`. O formato é uma lista de "
                    "chaves de citação do Zotero (cada "
                    "uma começando com `@`) separadas "
                    "por vírgulas:\n"
                    "```yaml Conteúdo textual em "
                    "formato *Markdown* com citações "
                    "[@citekey].\n"
                    '--- nocite: "@*" --- ```\n',
                    "name": "content",
                },
                "description": {"name": "description", "required": True},
                "id": {
                    "description": "Cada edificação terá um identificador "
                    "gerado a partir do seu "
                    "georreferenciamento usando Open "
                    'Location Code ("PlusCode"). Este '
                    "identificador usa o campo `id`, que "
                    "será gerado automaticamente pelo "
                    "programa WASTH.",
                    "identifier": True,
                    "name": "id",
                    "range": "OlcPlusCode11",
                },
                "media": {
                    "description": "Nos Documentários da Arquitetura "
                    "Tradicional, desdobramos o grupo "
                    "LIDO "
                    "[`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) "
                    "em quatro tipos de "
                    "relacionamentos\u2009:\n"
                    "1. `part_of`\u2009: a edificação "
                    "descrita na ficha é intrinsecamente "
                    "parte\n"
                    "   de um conjunto arquitetônico ou "
                    "urbanístico maior, quando se trata\n"
                    "   de uma parte fisicamente "
                    "vinculada a outra edificaçao ou um\n"
                    "   elemento concebido dentro de um "
                    "projeto de conjunto.\n"
                    "\n"
                    "2. `related_works`\u2009: a "
                    "edificação descrita na ficha pode "
                    "ser\n"
                    "   relacionada, por meio de "
                    "interpretação historiográfica, a "
                    "outras\n"
                    "   edificações ou objetos (fontes "
                    "primárias escritas ou visuais,\n"
                    "   obras de arte em geral, outras "
                    "edificações, etc.).\n"
                    "\n"
                    "3. `media`\u2009: fotografias ou "
                    "imagens históricas (desenhos "
                    "técnicos ou\n"
                    "   artísticos, pinturas, estampas, "
                    "etc.) que representem fielmente a\n"
                    "   aparência da edificação descrita "
                    "na ficha.\n"
                    "\n"
                    "4. `resources`\u2009: desenhos "
                    "técnicos em formato vetorial e,\n"
                    "   eventualmente, modelos "
                    "tridimensionais ou outras formas de\n"
                    "   informação técnica que não cabem "
                    "no formato da ficha, mas que\n"
                    "   foram produzidas pela equipe e "
                    "colaboradores do projeto de\n"
                    "   pesquisa.\n",
                    "name": "media",
                },
                "record_date": {"name": "record_date", "required": True},
                "record_rights": {"name": "record_rights", "required": True},
                "resources": {
                    "description": "Os desenhos ou modelos da "
                    "edificação são apresentados "
                    "online por meio de imagens "
                    "vetoriais ou bitmap.\n"
                    "Cada desenho ou modelo pode ser "
                    "apresentado sob várias "
                    "representações, como "
                    "pré-visualização, imagem "
                    "original, ou serviço [IIIF]. "
                    "Essas imagens devem ser "
                    "identificadas como segue\u2009:\n"
                    "As categorias de representação "
                    "previstas no [LIDO] podem ser "
                    "consultadas em "
                    "<http://terminology.lido-schema.org/resourceRepresentation_type> "
                    "e são inseridas na ficha como um "
                    "mapa.\n"
                    "Nos Documentários da Arquitetura "
                    "Tradicional, desdobramos o grupo "
                    "LIDO "
                    "[`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) "
                    "em quatro tipos de "
                    "relacionamentos\u2009:\n"
                    "1. `part_of`\u2009: a edificação "
                    "descrita na ficha é "
                    "intrinsecamente parte\n"
                    "   de um conjunto arquitetônico "
                    "ou urbanístico maior, quando se "
                    "trata\n"
                    "   de uma parte fisicamente "
                    "vinculada a outra edificaçao ou "
                    "um\n"
                    "   elemento concebido dentro de "
                    "um projeto de conjunto.\n"
                    "\n"
                    "2. `related_works`\u2009: a "
                    "edificação descrita na ficha "
                    "pode ser\n"
                    "   relacionada, por meio de "
                    "interpretação historiográfica, a "
                    "outras\n"
                    "   edificações ou objetos "
                    "(fontes primárias escritas ou "
                    "visuais,\n"
                    "   obras de arte em geral, "
                    "outras edificações, etc.).\n"
                    "\n"
                    "3. `media`\u2009: fotografias ou "
                    "imagens históricas (desenhos "
                    "técnicos ou\n"
                    "   artísticos, pinturas, "
                    "estampas, etc.) que representem "
                    "fielmente a\n"
                    "   aparência da edificação "
                    "descrita na ficha.\n"
                    "\n"
                    "4. `resources`\u2009: desenhos "
                    "técnicos em formato vetorial e,\n"
                    "   eventualmente, modelos "
                    "tridimensionais ou outras formas "
                    "de\n"
                    "   informação técnica que não "
                    "cabem no formato da ficha, mas "
                    "que\n"
                    "   foram produzidas pela equipe "
                    "e colaboradores do projeto de\n"
                    "   pesquisa.\n",
                    "name": "resources",
                },
                "title": {"name": "title", "required": True},
                "work_rights": {"name": "work_rights", "required": True},
            },
        }
    )

    site: Site = Field(
        default=...,
        description="""A localização real, atual da edificação — é o que será usado em quase todos os casos.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Repository", "Work"]}},
    )
    measurements: Optional[list[Measurement]] = Field(
        default=None,
        description="""A wrapper for information about the dimensions, or other measurements, of the object/work in focus. May also include extents of the parts of a complex object or work.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["MediaObject", "Event", "Work"]}
        },
    )
    material: Optional[list[MaterialTech]] = Field(
        default=None,
        description="""Descreve a natureza do material empregado na edificação, no elemento ou no evento descritos. Conforme necessário e segundo o discernimento de quem preenche a ficha, pode se referir a matérias-primas ou a produtos prontos para uso.
Espólios ou partes de outras edificações reutilizadas podem ser descritos segundo os materiais de que são constituídos, mas a procedência não deve ser cadastrada neste item. Para tanto, devem ser utilizados os eventos no grupo `temporal`.
-------------------------------------------------------------------------
This class is a specialization of E55 Type and comprises the concepts of materials.
Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple, should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing).
This type is used categorically in the model without reference to instances of it, i.e. the Model does not foresee the description of instances of instances of E57 Material, e.g. “instances of gold”.
It is recommended that internationally or nationally agreed codes and terminology should be used.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Event", "Work"],
                "exact_mappings": ["vra:Material"],
                "slot_uri": "crm:E57_Material",
            }
        },
    )
    technique: Optional[list[MaterialTech]] = Field(
        default=None,
        description="""Processos, técnicas, métodos e saberes postos em prática no conjunto da edificação e nas suas partes mais significativas, considerando a sua produção e alterações substanciais, bem como a sua eventual destruição.
-------------------------------------------------------------------------
The production or manufacturing processes, techniques, and methods incorporated in the fabrication or alteration of the work or image.
""",
        json_schema_extra={
            "linkml_meta": {
                "close_mappings": ["crm:E55_Type"],
                "domain_of": ["Event", "Work"],
                "slot_uri": "vra:Technique",
            }
        },
    )
    style_period: Optional[list[StylePeriod]] = Field(
        default=None,
        description="""Denomina o(s) período(s) em que o evento decorreu, em qualquer escala relevante para o conhecimento : geológica, arqueológica, histórica ou artística. A identificação do período ou estilo deve ser relevante para as características que o objeto adquiriu devido a esse evento, não somente uma coincidência cronológica.
---------------------------------------------------------------------
An index element for the period in which the event happened, comprising information about geologic time scale, archaelogical, historical, or artistic period, style, or art movement, whose characteristics are represented by the object or work.
Note that \"Period/Style\" corresponds to \"Style\" in CDWA as shorthand for [Style/Period/Group/Movement/Dynasty](https://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html).
Examples may be Neolithic for a period, Impressionist for a style, or Cubism for a movement.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event", "Work"]}},
    )
    culture: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Designa o contexto cultural ou étnico no qual o objeto foi afetado pelo evento em questão, desde que as características de tal contexto estejam refletidas no objeto. O preenchimento do contexto cultural é especialmente relevante quando os agentes envolvidos na produção ou alteração do objeto são desconhecidos.
---------------------------------------------------------------------
An index element for the cultural context from which the object/work in focus originated. Used if the creator or producer is unknown, or if the cultural context is of particular interest. Examples may include the name of a culture, a nation, or an ethnic group.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event", "Work"]}},
    )
    resources: Optional[list[Resource]] = Field(
        default=None,
        description="""Os desenhos ou modelos da edificação são apresentados online por meio de imagens vetoriais ou bitmap.
Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização, imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :
As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type> e são inseridas na ficha como um mapa.
Nos Documentários da Arquitetura Tradicional, desdobramos o grupo LIDO [`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) em quatro tipos de relacionamentos :
1. `part_of` : a edificação descrita na ficha é intrinsecamente parte
   de um conjunto arquitetônico ou urbanístico maior, quando se trata
   de uma parte fisicamente vinculada a outra edificaçao ou um
   elemento concebido dentro de um projeto de conjunto.

2. `related_works` : a edificação descrita na ficha pode ser
   relacionada, por meio de interpretação historiográfica, a outras
   edificações ou objetos (fontes primárias escritas ou visuais,
   obras de arte em geral, outras edificações, etc.).

3. `media` : fotografias ou imagens históricas (desenhos técnicos ou
   artísticos, pinturas, estampas, etc.) que representem fielmente a
   aparência da edificação descrita na ficha.

4. `resources` : desenhos técnicos em formato vetorial e,
   eventualmente, modelos tridimensionais ou outras formas de
   informação técnica que não cabem no formato da ficha, mas que
   foram produzidas pela equipe e colaboradores do projeto de
   pesquisa.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, desdobramos o grupo LIDO [`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) em quatro tipos de relacionamentos :
1. `part_of` : a edificação descrita na ficha é intrinsecamente parte
   de um conjunto arquitetônico ou urbanístico maior, quando se trata
   de uma parte fisicamente vinculada a outra edificaçao ou um
   elemento concebido dentro de um projeto de conjunto.

2. `related_works` : a edificação descrita na ficha pode ser
   relacionada, por meio de interpretação historiográfica, a outras
   edificações ou objetos (fontes primárias escritas ou visuais,
   obras de arte em geral, outras edificações, etc.).

3. `media` : fotografias ou imagens históricas (desenhos técnicos ou
   artísticos, pinturas, estampas, etc.) que representem fielmente a
   aparência da edificação descrita na ficha.

4. `resources` : desenhos técnicos em formato vetorial e,
   eventualmente, modelos tridimensionais ou outras formas de
   informação técnica que não cabem no formato da ficha, mas que
   foram produzidas pela equipe e colaboradores do projeto de
   pesquisa.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedWork", "LargerContextReference", "Event", "Work"]
            }
        },
    )
    work_rights: list[Right] = Field(
        default=...,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre O OBJETO OU RECURSO QUE ESTÁ SENDO DESCRITO, não sobre o preenchimento da ficha.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["RelatedObject", "Resource", "Work"],
                "slot_uri": "lido:rightsWorkSet",
            }
        },
    )
    record_rights: list[Right] = Field(
        default=...,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha e o detentor desses direitos.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Concept", "Work"],
                "notes": [
                    "A set of structured information about rights regarding the content "
                    "provided in this LIDO record."
                ],
            }
        },
    )
    title_type: TitleType = Field(
        default=...,
        description="""Categoriza a natureza do nome dado ao objeto.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Appellation", "Work"]}},
    )
    work_type_condition: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Descreve o estado físico da edificação quanto à sua aparência de completude, deterioração ou capacidade de desempenhar sua função.
Atende aos campos do [SICG](https://sicg.iphan.gov.br/sicg/manual/manual.html) \"estado de preservação\" e \"estado de conservação\".""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "Descriptors for objects that are distinguishable by their overall "
                    "state such as appearance, level of damage, completeness, or "
                    "quality. If an object is identified by its prevailing physical "
                    "state, then it is qualified by condition.\n"
                    "Based on [AAT "
                    '"conditions"](http://vocab.getty.edu/page/aat/300389724) and '
                    '[CIDOC CRM "E3 Condition '
                    'State"](http://cidoc-crm.org/html/cidoc_crm_v7.1.1_with_translations.html#E3)'
                ],
                "recommended": True,
                "slot_uri": "term:lido00937",
            }
        },
    )
    work_type_form: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, designa uma tipologia formal.
O vocabulário controlado para este item está em processo de estruturação.
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by their physical form or by the manner in which they are presented. If an object is identified by sight, then it is qualified by form.
Based on [AAT Guidelines \"Types of Guide Terms\"](https://www.getty.edu/research/tools/vocabularies/guidelines/aat_3_1_hierarchical_rels.html)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "recommended": True,
                "slot_uri": "term:lido00766",
            }
        },
    )
    work_type_function: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Nos Documentários de edificações, designa um dos sete tipos de propósitos concebidos por C. William Westfall e Samir Younés em *Architectural Type and Character*.
No Documentário de Lugares, designa o papel administrativo da localidade, por exemplo freguesia, sede municipal, capital estadual ou nacional.
---------------------------------------------------------------------
Objects that are distinguishable by the particular purpose for which they are designed or used. If an object is identifiable by its intended use, then it is qualified by function.
Based on [AAT Guidelines \"Types of Guide Terms\"](https://www.getty.edu/research/tools/vocabularies/guidelines/aat_3_1_hierarchical_rels.html)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "recommended": True,
                "slot_uri": "term:lido00767",
            }
        },
    )
    work_type_context: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Nos Documentários de edificações, designa sobretudo o contexto
imediato de implantação de uma edificação : urbana, rural, isolada,
em correnteza, etc.

No Documentário de Lugares Tradicionais, designa o tipo de núcleo
populacional : sítio isolado, povoação rural, vila ou cidade,
por exemplo.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "Descriptors for objects that are distinguishable by their use or "
                    "application within a particular physical location. If an object is "
                    "identifiable by association with specific surroundings, it is "
                    "qualified by location or context.\n"
                    'Based on [AAT Guidelines "Types of Guide '
                    'Terms"](https://www.getty.edu/research/tools/vocabularies/guidelines/aat_3_1_hierarchical_rels.html)'
                ],
                "recommended": True,
                "slot_uri": "term:lido00934",
            }
        },
    )
    work_type_material_tech: Optional[list[MaterialTech]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, refere-se à caracterização construtiva geral da edificação.
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by their materials encorporated, or the techniques used to create the object or work. If an object is identified by the substances detected and/or the processes employed, then it is qualified by material or technique.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "recommended": True,
                "slot_uri": "term:lido00789",
            }
        },
    )
    work_type_subject: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, indica, se houver, uma classificação iconográfica mais específica do que `form` ou `function`.
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by their topics, themes, or other content of the work. If an object is identified by what it is of or about, then it is qualified by subject.
Based on [AAT \"subjects\"](http://vocab.getty.edu/page/aat/300404126)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "recommended": True,
                "slot_uri": "term:lido00768",
            }
        },
    )
    work_type_use: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, designa propriamente a(s) classificação(ões) de usos do solo ou atividades predominante(s) na edificação atualmente.
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by the way they are employed, occupied, applied, or function. If an object is identifiable by its particular mode of use, it is qualified by use.
Based on [AAT \"use\"](http://vocab.getty.edu/page/aat/300068844)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "recommended": True,
                "slot_uri": "term:lido00938",
            }
        },
    )
    classification_genre: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A broad category for grouping objects on the basis of shared "
                    "intrinsic characteristics. The relationship between an object/work "
                    "and the object genre is a generic is-a-relation rather than a "
                    "membership based on ascription to a subject group.\n"
                    "Note that the [AAT Object "
                    "Genres](http://vocab.getty.edu/page/aat/300185711) hierarchy "
                    "differs in its scope from Object genre here in that the AAT "
                    "includes more specific terms grouped by various aspects. In "
                    "general, AAT descriptors are not intended to be used as indexing "
                    "terms for classification."
                ],
                "slot_uri": "term:lido00853",
            }
        },
    )
    classification_subject: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A broad category for grouping objects or works on the basis of a "
                    "topical association, including thematic or systematic "
                    "classification, or an assignment by discipline. The relationship "
                    "between an object/work and a subject category is a kind of "
                    "membership based on ascription rather than a generic is-a "
                    "relation."
                ],
                "slot_uri": "term:lido00932",
            }
        },
    )
    classification_local: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A classification scheme for grouping objects on the basis of "
                    "locally defined criteria, including categories corresponding to "
                    'the curatorial departments of the repository, such as "prints and '
                    'drawings", "decorative arts", "North America", "invertebrates", '
                    '"Bronze Age" or "textiles". [Based on CCO '
                    '"Class"](https://vraweb.org/wp-content/uploads/2020/04/CatalogingCulturalObjectsFullv2.pdf)'
                ],
                "slot_uri": "term:lido01135",
            }
        },
    )
    classification_special: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A classification scheme for grouping objects on the basis of "
                    "criteria defined within specific academic disciplines or cultural "
                    'domains, such as the "Hornbostel-Sachs Classification of Musical '
                    'Instruments", the "Nickel-Strunz classification", biological '
                    "taxonomies etc. Refers to classification schemes that group "
                    "objects on the basis of object characteristics, not on the basis "
                    "of themes or topics which the objects or works are related to."
                ],
                "slot_uri": "term:lido01144",
            }
        },
    )
    part_of: Optional[list[LargerContextReference]] = Field(
        default=None,
        description="""Permite identificar um conjunto arquitetônico, urbanístico ou conceitual (por exemplo, uma série de casas) do qual a edificação faz parte.
Nos Documentários da Arquitetura Tradicional, desdobramos o grupo LIDO [`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) em quatro tipos de relacionamentos :
1. `part_of` : a edificação descrita na ficha é intrinsecamente parte
   de um conjunto arquitetônico ou urbanístico maior, quando se trata
   de uma parte fisicamente vinculada a outra edificaçao ou um
   elemento concebido dentro de um projeto de conjunto.

2. `related_works` : a edificação descrita na ficha pode ser
   relacionada, por meio de interpretação historiográfica, a outras
   edificações ou objetos (fontes primárias escritas ou visuais,
   obras de arte em geral, outras edificações, etc.).

3. `media` : fotografias ou imagens históricas (desenhos técnicos ou
   artísticos, pinturas, estampas, etc.) que representem fielmente a
   aparência da edificação descrita na ficha.

4. `resources` : desenhos técnicos em formato vetorial e,
   eventualmente, modelos tridimensionais ou outras formas de
   informação técnica que não cabem no formato da ficha, mas que
   foram produzidas pela equipe e colaboradores do projeto de
   pesquisa.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "dcterms:isPartOf"}
        },
    )
    former_site: Optional[list[Site]] = Field(
        default=None,
        description="""Indica que a edificação não se encontra mais no local indicado, seja porque foi deslocada ou demolida.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    intended_site: Optional[list[Site]] = Field(
        default=None,
        description="""Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser construída.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    other_site: Optional[list[Site]] = Field(
        default=None,
        description="""Para casos de implantação não contemplados em nenhuma das categorias acima.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    location_historic: Optional[list[LegalBody]] = Field(
        default=None,
        description="""Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a localização original de uma construção fisicamente deslocada (para tanto, cadastrar outra localização do tipo `former_site`). Preencher apenas caso a nomenclatura seja relevante, por exemplo para nomear as antigas províncias de Portugal ou o Oeste da Bahia, que originalmente pertencia a Pernambuco, ou ainda se for relevante informar uma região física.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    inscriptions: Optional[list[Inscription]] = Field(
        default=None,
        description="""Marcas, símbolos ou textos gravados na edificação, especialmente aqueles referentes à estrutura como um todo e não específicos a alguma de suas partes. Não usar para iconografia.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    collection: Optional[list[Collection]] = Field(
        default=None,
        description="""Descreve conjuntos conceituais nos quais a edificação foi incluída, por exemplo catálogos raisonnés, obras de referência, exposições, ou agrupamentos *ad-hoc* para formar coleções temáticas de acordo com as necessidades do projeto de investigação.
Para o pertencimento a perímetros de sítios históricos tombados/classificados, preencher o grupo `identifiers`. Para a identificação de proprietários ou responsáveis, preencher o grupo `work_rights`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A set of identifying and indexing information about the collection "
                    "the object/work in focus is gathered into or is a member of.\n"
                    "Collection applies to any accumulated group of physical or digital "
                    "items, conceptually or physically brought together on the basis of "
                    "a focal characteristic. Use cases for grouping items into a "
                    "collection are various and may span curated holdings in museums, "
                    "departmental collections, sets of items to be displayed in an "
                    "exhibition, or aggregations bound informally for cataloging and "
                    "retrieval purposes."
                ],
                "slot_uri": "lido:collection",
            }
        },
    )
    related_works: Optional[list[RelatedWork]] = Field(
        default=None,
        description="""O grupo `related_works` é destinado unicamente a cadastrar relações desta edificação com objetos autônomos, tais como outras edificações, conjuntos urbanos, obras de artes visuais, referências bibliográficas ou acervos arquivísticos.
⚠️  OS DESENHOS PRODUZIDOS POR ESTE PROJETO DE PESQUISA DEVEM SER CADASTRADOS NO GRUPO `resources`.
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

Nos Documentários da Arquitetura Tradicional, desdobramos o grupo LIDO [`relatedWorksWrap`](https://lido-schema.org/schema/v1.1/lido-v1.1.html#relatedWorksWrap) em quatro tipos de relacionamentos :
1. `part_of` : a edificação descrita na ficha é intrinsecamente parte
   de um conjunto arquitetônico ou urbanístico maior, quando se trata
   de uma parte fisicamente vinculada a outra edificaçao ou um
   elemento concebido dentro de um projeto de conjunto.

2. `related_works` : a edificação descrita na ficha pode ser
   relacionada, por meio de interpretação historiográfica, a outras
   edificações ou objetos (fontes primárias escritas ou visuais,
   obras de arte em geral, outras edificações, etc.).

3. `media` : fotografias ou imagens históricas (desenhos técnicos ou
   artísticos, pinturas, estampas, etc.) que representem fielmente a
   aparência da edificação descrita na ficha.

4. `resources` : desenhos técnicos em formato vetorial e,
   eventualmente, modelos tridimensionais ou outras formas de
   informação técnica que não cabem no formato da ficha, mas que
   foram produzidas pela equipe e colaboradores do projeto de
   pesquisa.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
                "notes": [
                    "A wrapper for identifying information about an object or work, "
                    "including collections, related to the object/work in focus. May "
                    "include a weblink."
                ],
                "slot_uri": "dcterms:related",
            }
        },
    )
    subject: Optional[list[Topic]] = Field(
        default=None,
        description="""Recomenda-se articular o tema em três níveis : descrição, identificação e interpretação.
DESCRIÇÃO se refere a elementos imediatamente reconhecíveis sem necessidade de conhecimento especializado : coluna(ta)s, arcadas, brasões, cunhais, ornamentos em geral.
IDENTIFICAÇÃO se refere ao reconhecimento das particularidades arquitetônicas ou iconográficas dos elementos : p. ex. as colunas são da ordem toscana, a abóbada é de aresta, o brasão pertence a tal família...
INTERPRETAÇÃO diz respeito ao significado iconológico, alegórico ou político dos elementos, incluindo questões de status e estilo.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "lido:subjectSet"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: str = Field(
        default=...,
        description="""Cada edificação terá um identificador gerado a partir do seu georreferenciamento usando Open Location Code (\"PlusCode\"). Este identificador usa o campo `id`, que será gerado automaticamente pelo programa WASTH.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: date = Field(
        default=...,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Work",
        "http://schema.org/LandmarksOrHistoricalBuildings",
        "wasth:Work",
        "schema:LandmarksOrHistoricalBuildings",
    ] = Field(
        default="schema:LandmarksOrHistoricalBuildings",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "ifabsent": "string(term:lido00096)",
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Deixe uma linha em branco após o fechamento dos metadados e inclua aqui uma descrição morfológica e histórica da edificação com texto livre, usando formatação Markdown.
Poderá incluir um segundo bloco de metadados para indicar as referências bibliográficas da descrição textual, no campo `nocite`. O formato é uma lista de chaves de citação do Zotero (cada uma começando com `@`) separadas por vírgulas:
```yaml Conteúdo textual em formato *Markdown* com citações [@citekey].
--- nocite: \"@*\" --- ```
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class Site(Thing):
    """
    O georreferenciamento é o cerne do projeto dos Documentários da Arquitetura Tradicional. Ele permite investigar a distribuição geográfica das características construtivas e morfológicas das edificações cadastradas.
    As instruções de preenchimento específicas se encontram na documentação das classes que fornecem os dados para o sítio. Consulte também o [Tutorial de georreferenciamento](https://github.com/arqtrad/.github/wiki/Tutorial-de-georreferenciamento) para saber como localizar edificações não cadastradas nas bases de dados do patrimônio cultural (SICG ou SIPA).

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "crm:E92_Spacetime_Volume",
            "comments": [
                "Este bloco corresponde à terminologia do [DublinCore] `coverage "
                "> spatial`. Na especificação [LIDO], a localização física de um "
                "bem se confunde com a sua inserção institucional (repositório). "
                "Na formatação da nossa ficha, tentamos desfazer essa confusão "
                "separando o georreferenciamento e o repositório em blocos "
                "diferentes."
            ],
            "exact_mappings": ["schema:DefinedRegion"],
            "from_schema": "https://tradicional.arq.br/schema/work",
            "notes": [
                "This class comprises 4-dimensional point sets (volumes) in "
                "physical spacetime (in contrast to mathematical models of it) "
                "regardless of their true geometric forms. They may derive their "
                "identity from being the extent of a material phenomenon or from "
                "being the interpretation of an expression defining an extent in "
                "spacetime. Intersections of instances of E92 Spacetime Volume, E53 "
                "Place, and E52 Time-Span are also regarded as instances of E92 "
                "Spacetime Volume. An instance of E92 Spacetime Volume is either "
                "contiguous or composed of a finite number of contiguous subsets. "
                "Its boundaries may be fuzzy due to the properties of the phenomena "
                "it derives from or due to the limited precision up to which "
                "defining expression can be identified with a real extent in "
                "spacetime. The duration of existence of an instance of E92 "
                "Spacetime Volume is its projection on time."
            ],
        }
    )

    name: Optional[GeonamesFeature] = Field(
        default=None,
        description="""Permite identificar o contexto geográfico ou administrativo ao qual
a edificação se subordina, usando a base <https://geonames.org>.
Referenciar a localidade por meio do código identificador na forma:
`geonameid: 1234`
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Site", "GeonamesFeature"],
                "notes": [
                    "A set of structured information about a place that is the broader "
                    "context for the place in focus, such as the district, state, or "
                    "nation to which a city belongs."
                ],
                "slot_uri": "lido:partOfPlace",
            }
        },
    )
    site_type: Optional[RepositoryType] = Field(
        default=RepositoryType("geographic"),
        description="""Categoriza a natureza do recorte que define o sítio.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Site"],
                "ifabsent": "RepositoryType(geographic)",
            }
        },
    )
    location: GeographicPoint = Field(
        default=...,
        description="""Coordenadas geográficas do ponto que permite situar a edificação no mapa para fins ilustrativos. Usar o sistema de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível.
---------------------------------------------------------------------
Representative point location for the place, normally in EPSG:4326 (WGS 84).""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Site"], "slot_uri": "geo:hasDefaultGeometry"}
        },
    )
    extent: Optional[GeographicExtent] = Field(
        default=None,
        description="""Área da implantação da edificação ou sítio cadastrado. Usar o sistema de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Site"],
                "notes": [
                    "Polygonal, multipolygonal, or linear geographic extent associated "
                    "with the place."
                ],
                "slot_uri": "geo:hasGeometry",
            }
        },
    )
    event_place_type: Optional[EventPlaceType] = Field(
        default=None,
        description="""Se relevante para a ação, indicar se se trata do local de descobrimento do objeto, do local de origem ou destino do seu translado. Omitir caso o evento não se enquadre nesses casos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site"]}},
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Site",
        "http://www.cidoc-crm.org/cidoc-crm/E92_Spacetime_Volume",
        "wasth:Site",
        "crm:E92_Spacetime_Volume",
    ] = Field(
        default="crm:E92_Spacetime_Volume",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class GeographicPoint(ConfiguredBaseModel):
    """
    Coordenadas do ponto que situa o sítio na visualização do mapa.
    A fonte preferencial de autoridade para o georreferenciamento é um órgão público, por exemplo o IPHAN no Brasil (usando as coordenadas informadas no [SICG]) ou a DGMN em Portugal (usando as coordenadas informadas no [SIPA]).
    Caso não haja georreferenciamento oficial, usar uma planta cadastral municipal georreferenciada ou, na falta desta, o [Global Building Atlas]. Nesses casos, para se obter as coordenadas de georreferenciamento, é preciso usar um Sistema de Informações Geográficas da sua preferência.
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

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/work"}
    )

    srs_name: Optional[str] = Field(
        default=None,
        description="""Names the coordinate reference system (CRS) that defines the semantics of the lat/long pair according to the ISO6709 standard. Sempre que possível, usar EPSG:4326, senão os sistemas de referência nacionais.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["GeographicPoint", "GeographicExtent"],
                "recommended": True,
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    lat: float = Field(
        default=...,
        description="""Latitude em graus decimais (separador decimal: ponto).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["GeographicPoint"]}},
    )
    lon: float = Field(
        default=...,
        description="""Longitude em graus decimais (separador decimal: ponto).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["GeographicPoint"]}},
    )
    alt: Optional[float] = Field(
        default=None,
        description="""Altitude em metros (separador decimal: ponto)""",
        ge=-1000,
        le=10000,
        json_schema_extra={"linkml_meta": {"domain_of": ["GeographicPoint"]}},
    )
    zoom: Optional[int] = Field(
        default=13,
        description="""Usado para visualizar o mapa mais de longe se a precisão das coordenadas for baixa.
""",
        ge=0,
        le=18,
        json_schema_extra={
            "linkml_meta": {"domain_of": ["GeographicPoint"], "ifabsent": "integer(13)"}
        },
    )


class GeographicExtent(ConfiguredBaseModel):
    """
    Coordenadas do polígono que define o sítio.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/work"}
    )

    srs_name: Optional[str] = Field(
        default=None,
        description="""Names the coordinate reference system (CRS) that defines the semantics of the lat/long pair according to the ISO6709 standard. Sempre que possível, usar EPSG:4326, senão os sistemas de referência nacionais.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["GeographicPoint", "GeographicExtent"],
                "recommended": True,
            }
        },
    )
    source: Optional[LegalBody] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    geometry_type: GeometryType = Field(
        default=...,
        description="""Tipo da geometria descrita pelas coordenadas.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["GeographicExtent"]}},
    )
    coordinates: str = Field(
        default=...,
        description="""No QGIS, usar a ferramenta `Get WKT` para obter as coordenadas do polígono (`extent`) com a opção `Get JSON` — copiar apenas os colchetes `[[[ ]]]` e os valores numéricos dentro deles.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["GeographicExtent"]}},
    )


class Inscription(ConfiguredBaseModel):
    """
    A descrição da inscrição informa local, dimensões e características. Os tipos de descrição podem ser extraídos da hierarquia Getty: <http://vocab.getty.edu/page/aat/300220469>.
    Os itens das listas de `material` e `technique` DEVEM usar o nosso [vocabulário controlado](https://vocabulario.tradicional.arq.br).
    Essa distinção é especialmente relevante no caso de revestimentos, como estuques, azulejos ou pinturas decorativas, por oposição à base sobre a qual eles são aplicados.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/work"}
    )

    format_extent: Optional[TypedReference] = Field(
        default=None,
        description="""Indica a parte do objeto que está sendo medida — por exemplo, se a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário controlado.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Measurement", "Inscription", "Topic"]}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    inscription_type: InscriptionType = Field(
        default=InscriptionType("text"),
        description="""Determina a natureza da inscrição.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Inscription"], "ifabsent": "string(text)"}
        },
    )


class Topic(ConfiguredBaseModel):
    """
    Subject or iconographic topic.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://tradicional.arq.br/schema/work",
            "slot_usage": {"concept_name": {"name": "concept_name", "required": True}},
        }
    )

    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    format_extent: Optional[TypedReference] = Field(
        default=None,
        description="""Indica a parte do objeto que está sendo medida — por exemplo, se a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário controlado.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Measurement", "Inscription", "Topic"]}
        },
    )
    concept_name: Concept = Field(
        default=...,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    topic_type: SubjectType = Field(
        default=...,
        description="""Categoriza o nível descritivo ou interpretativo do tema.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Topic"]}},
    )


class Collection(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/work"}
    )

    collection_type: CollectionType = Field(
        default=...,
        description="""Descreve a natureza da coleção.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Collection"]}},
    )
    title: Optional[str] = Field(
        default=None,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference", "Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
            }
        },
    )
    id: Optional[str] = Field(
        default=None,
        description="""Identificador globalmente único para este objeto ou recurso.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha, no caso de uma única pessoa ser responsável. Este campo foi mantido apenas por compatibilidade, preferir `authors` daqui para a frente mesmo quando houver uma só pessoa responsável pela ficha.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    authors: Optional[list[str]] = Field(
        default=None,
        description="""ORCID iD das pessoas que escreveram a versão original da ficha, no caso de várias pessoas terem contribuído igualmente.
Usar o formato `orcid:1234-5678-9012-345X` ou `https://orcid.org/1234-5678-9012-345X` (temporariamente também é aceito o formato `1234-5678-9012-345X`).
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    record_date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha. Usar o formato ISO-8601 entre aspas `\"AAAA-MM-DD\"`.
Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    description: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "TypedReference",
                    "Measurement",
                    "RelatedEvent",
                    "Thing",
                    "Inscription",
                    "Topic",
                ],
                "exact_mappings": ["schema:description"],
                "slot_uri": "dcterms:description",
            }
        },
    )
    category: Literal[
        "https://tradicional.arq.br/schema/Collection", "wasth:Collection"
    ] = Field(
        default="wasth:Collection",
        description="""Uma classificação ampla para o objeto descrito na ficha, usando o vocabulário controlado do LIDO.
Nos documentários de edificações, preencher este campo OBRIGATORIAMENTE com `term:lido00096` (\"Objeto manufaturado\").
Nos recursos gráficos de uma obra, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "notes": [
                    "The LIDO Category Vocabulary is a structured controlled list of "
                    "terms recommended to use as values in the LIDO Category element.\n"
                    "Examples are human-made object or natural object."
                ],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    identifiers: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Números de inventário e demais códigos que identificam este objeto em outras bases de dados.
Caso esta edificação esteja cadastrada em outras bases de dados (por exemplo, [SICG], [SIPA], [HPIP], [iPatrimonio], etc.), pode preencher a lista `identifiers` como segue.
:clipboard: O conteúdo de cada bloco é uma lista recuada em dois espaços com respeito à categoria superior. Seus itens são :
* `type` é o tipo de referência : pode ser `uri` (padrão), `iri` ou
  `local` — se estiver em dúvida, omita esta linha ;

* `refid` é obrigatório : representa o identificador do conceito no
  vocabulário controlado ou no repositório de origem — normalmente
  será uma URI (um link para a página web do cadastro) ;

* `description` deve ser usado para representar textualmente
  o número de inventário, código identificador ou outra informação
  que individualize o objeto na base externa (por exemplo, livro do
  tombo e número do processo de tombamento, no Brasil) ;

* `bibliographic_citation` é opcional e permite citar uma lista de
  referências bibliográficas que validem a inclusão deste termo.

* `source` também é opcional e permite cadastrar os dados da pessoa
  jurídica responsável pelo registro.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "notes": ["Published or external identifiers for the object."],
            }
        },
    )
    bibliographic_citation: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""📚  Cadastro de uma referência bibliográfica.
O campo `refid` deve conter a chave de citação (citation key) que consta do registro bibliográfico na biblioteca do nosso projeto de pesquisa no Zotero, começando com arroba @. Em geral, a chave de citação é o DOI ou ISBN da publicação, mas pode ser diferente.
Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
Usar o campo `description` para formatar a referência, caso a formatação automática do Zotero não for satisfatória.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "TypedReference",
                    "Measurement",
                    "Actor",
                    "Thing",
                    "Appellation",
                    "GeographicPoint",
                    "GeographicExtent",
                    "Inscription",
                ],
                "recommended": True,
                "slot_uri": "dcterms:bibliographicCitation",
            }
        },
    )
    content: Optional[str] = Field(
        default=None,
        description="""Conteúdo textual descritivo ou explicativo.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing", "Inscription"],
                "recommended": True,
                "slot_uri": "lido:descriptiveNoteValue",
            }
        },
    )
    title_source: Optional[list[BibliographicCitation]] = Field(
        default=None,
        description="""A fonte do título title_source é opcional ; um título pode ser atestado em mais de uma fonte, por isso este campo é uma lista de itens (cada item começa com um hífen).""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    alt_name: Optional[list[Appellation]] = Field(
        default=None,
        description="""O bloco `alt_name` permite cadastrar outros nomes pelos quais o objeto ou conceito será eventualmente conhecido. É uma lista opcional de itens, e se existir, os campos de cada item da lista devem ser preenchidos como os do título principal.
O campo `label` ou `description` de cada item contém o texto do título (nome).
Este bloco pode ser omitido por completo se não houver títulos alternativos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    tags: Optional[list[str]] = Field(
        default=None,
        description="""Lista de palavras-chave que caracterizam o objeto, de modo não estruturado. Recomenda-se usar uma palavra-chave de cada um dos recortes abaixo:
- Geográfico ; - Cronológico ; - Histórico-cultural ; - Técnico-construtivo ; - Temático ou tipológico ; - Funcional.
---------------------------------------------------------------------
Provisional uncontrolled keywords. Prefer `classifications` or `subject` for curated vocabulary terms.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    temporal: Optional[list[Event]] = Field(
        default=None,
        description="""Descrição dos eventos associados ao ciclo de vida da edificação ou à existência e/ou uso do objeto ou conceito.
Ler a respetiva documentação para estruturar este campo.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )
    repositories: Optional[list[Repository]] = Field(
        default=None,
        description="""Nos Documentários da Arquitetura Tradicional, usamos repositórios para indicar a inclusão da edificação em perímetros de sítios tombados/classificados do patrimônio, áreas de interesse histórico-cultural, etc.
O repositório é cadastrado como uma pessoa jurídica dotada de extensão geográfica.
---------------------------------------------------------------------
A set of elements for the identification, name and location of the repository that is responsible for the object/work in focus.
Repeated if there are several designations known, or if former repositories or geographic places should be listed.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
    )


class GeonamesFeature(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "geonames:Feature",
            "from_schema": "https://tradicional.arq.br/schema/geonames",
        }
    )

    geonameid: int = Field(
        default=...,
        description="""Integer id of record in geonames database""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "235530",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "13713056"}],
            }
        },
    )
    name: Optional[str] = Field(
        default=None,
        description="""Name of geographical point (utf8) varchar(200)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "126931",
                    }
                },
                "domain_of": ["Place", "Site", "GeonamesFeature"],
                "examples": [{"value": "Sítio Julião"}],
                "slot_uri": "geonames:name",
            }
        },
    )
    asciiname: Optional[str] = Field(
        default=None,
        description="""Name of geographical point in plain ascii characters, varchar(200)
""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "126467",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "Sitio Juliao"}],
            }
        },
    )
    alternatenames: Optional[str] = Field(
        default=None,
        description="""Alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000) """,
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "118603",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [
                    {
                        "value": "Armenian Apostolic Church of Saint John the "
                        "Baptist,Hayastaneaycʻ Arakʻelakan Surb Yovhannes "
                        "Mkrticʻ ekegecʻi,Igreja Apostolica Armenia Sao Joao "
                        "Batista,Igreja Apostólica Armênia São João "
                        "Batista,Surb Hovhannes Mkrticʻ ekegecʻi,Հայաստանեայց "
                        "Առաքելական Սուրբ Յովհաննէս Մկրտիչ եկեղեցի,Սուրբ "
                        "Հովհաննես Մկրտիչ եկեղեցի\n"
                    }
                ],
                "slot_uri": "geonames:alternatenames",
            }
        },
    )
    latitude: Optional[float] = Field(
        default=None,
        description="""Latitude in decimal degrees (wgs84)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "191229",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "-6.1516"}],
                "slot_uri": "wgs84:lat",
            }
        },
    )
    longitude: Optional[float] = Field(
        default=None,
        description="""Longitude in decimal degrees (wgs84)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "190039",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "-39.59999"}],
                "slot_uri": "wgs84:long",
            }
        },
    )
    feature_class: Optional[FeatureClassEnum] = Field(
        default=None,
        description="""See http://www.geonames.org/export/codes.html, char(1)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "9"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "S"}],
                "slot_uri": "geonames:featureClass",
            }
        },
    )
    feature_code: Optional[FeatureCodeEnum] = Field(
        default=None,
        description="""See http://www.geonames.org/export/codes.html, varchar(10)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "319",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "HSE"}],
                "slot_uri": "geonames:featureCode",
            }
        },
    )
    country_code: Optional[CountryCodeEnum] = Field(
        default=None,
        description="""ISO-3166 2-letter country code, 2 characters""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "1"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "BR"}],
                "slot_uri": "geonames:countryCode",
            }
        },
    )
    cc2: Optional[str] = Field(
        default=None,
        description="""Alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "22"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "CO"}],
            }
        },
    )
    admin1_code: Optional[int] = Field(
        default=None,
        description="""Fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
Most adm1 are FIPS codes. ISO codes are used for US, CH, BE and ME. UK and Greece are using an additional level between country and fips code. The code '00' stands for general features where no specific adm1 code is defined.
The corresponding admin feature is found with the same countrycode and adminX codes and the respective feature code ADMx.
""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "28"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "06"}],
            }
        },
    )
    admin2_code: Optional[int] = Field(
        default=None,
        description="""Code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "5577",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "2300309"}],
            }
        },
    )
    admin3_code: Optional[int] = Field(
        default=None,
        description="""code for third level administrative division, varchar(20)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "45"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "09"}],
            }
        },
    )
    admin4_code: Optional[str] = Field(
        default=None,
        description="""code for fourth level administrative division, varchar(20)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "0"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
            }
        },
    )
    population: Optional[int] = Field(
        default=None,
        description="""bigint (8 byte int)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "9242",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "15"}],
                "slot_uri": "geonames:population",
            }
        },
    )
    elevation: Optional[int] = Field(
        default=None,
        description="""in meters, integer""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "701",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "303"}],
            }
        },
    )
    dem: Optional[int] = Field(
        default=None,
        description="""Digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "1706",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "406"}],
            }
        },
    )
    timezone: Optional[TimezoneEnum] = Field(
        default=None,
        description="""the iana timezone id (see file timeZone.txt) varchar(40)""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {"tag": "num_distinct_values", "value": "28"}
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "America/Fortaleza"}],
            }
        },
    )
    modification_date: Optional[date] = Field(
        default=None,
        description="""date of last modification in yyyy-MM-dd format""",
        json_schema_extra={
            "linkml_meta": {
                "annotations": {
                    "num_distinct_values": {
                        "tag": "num_distinct_values",
                        "value": "1414",
                    }
                },
                "domain_of": ["Place", "GeonamesFeature"],
                "examples": [{"value": "2026-10-09"}],
            }
        },
    )


class Container(ConfiguredBaseModel):
    """
    Todos os elementos do documentário.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema", "tree_root": True}
    )

    works: Optional[list[Work]] = Field(
        default=None,
        description="""Todas as edificações documentadas.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Container"]}},
    )
    concepts: Optional[list[Concept]] = Field(
        default=None,
        description="""Todos os termos de vocabulário controlado.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Container"]}},
    )
    places: Optional[list[GeonamesFeature]] = Field(
        default=None,
        description="""Lugares indexados pelo Geonames""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Container"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ConceptReference.model_rebuild()
BroaderConceptReference.model_rebuild()
NarrowerConceptReference.model_rebuild()
MappingConceptReference.model_rebuild()
BibliographicCitation.model_rebuild()
TypedReference.model_rebuild()
Measurement.model_rebuild()
MaterialTech.model_rebuild()
Right.model_rebuild()
Actor.model_rebuild()
EventDate.model_rebuild()
StylePeriod.model_rebuild()
RelatedEvent.model_rebuild()
Thing.model_rebuild()
Concept.model_rebuild()
RelatedObject.model_rebuild()
RelatedWork.model_rebuild()
LargerContextReference.model_rebuild()
Resource.model_rebuild()
MediaObject.model_rebuild()
LegalBody.model_rebuild()
Event.model_rebuild()
Appellation.model_rebuild()
Repository.model_rebuild()
Work.model_rebuild()
Site.model_rebuild()
GeographicPoint.model_rebuild()
GeographicExtent.model_rebuild()
Inscription.model_rebuild()
Topic.model_rebuild()
Collection.model_rebuild()
GeonamesFeature.model_rebuild()
Container.model_rebuild()
