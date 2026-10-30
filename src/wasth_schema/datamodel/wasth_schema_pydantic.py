from __future__ import annotations

import re
from datetime import date
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


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
        "no GitHub, estudando\n"
        "[estes tutoriais em "
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
        '<img alt="Captura de tela" '
        'src="https://github.com/user-attachments/assets/6c22dcec-b8e1-4688-a504-d9ea640bdc43" '
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
        '<img alt="Captura de tela" '
        'src="https://github.com/user-attachments/assets/25905e40-99ef-4b23-b33e-cfe586c41001" '
        "/>\n"
        "\n"
        '<img alt="Captura de tela" '
        'src="https://github.com/user-attachments/assets/b5f6ef50-c122-4f01-8ec9-b16207a9b63d" '
        "/>\n"
        "\n"
        "Poderá então abrir uma solicitação de integração das suas "
        "alterações\n"
        "ao repositório principal (**pull request**):\n"
        "\n"
        '<img alt="Captura de tela" '
        'src="https://github.com/user-attachments/assets/56de1236-6fa0-47f3-9e94-06218dace0a8" '
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
        "Leia a especificação da ficha [Work](Work/) para saber como "
        "preencher as\n"
        "fichas de edificações dos Documentários da Arquitetura "
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
        ],
        "license": "MIT",
        "name": "wasth_schema",
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
            "geo": {
                "prefix_prefix": "geo",
                "prefix_reference": "http://www.opengis.net/ont/geosparql#",
            },
            "geonames": {
                "prefix_prefix": "geonames",
                "prefix_reference": "http://www.geonames.org/ontology#",
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
        "source_file": "src/wasth_schema/schema/wasth_schema.yaml",
        "title": "Esquema de dados do WASTH (Web App para Sítios Tradicionais e "
        "Históricos)",
        "types": {
            "CslCitekey": {
                "base": "str",
                "description": "Chave de citação compatível com o "
                "Citation Style Language, começando "
                "com '@'. Obter as chaves de citação "
                "das referências bibliográficas "
                "consultando a nossa biblioteca "
                "compartilhada no Zotero.\n",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "CslCitekey",
                "pattern": "^@[a-zA-Z0-9_][\\w:.#$%&\\-+?<>~/]*$",
                "uri": "xsd:string",
            },
            "GeoJSONCoordinateArray": {
                "base": "str",
                "description": "JSON array of GeoJSON "
                "positions. The valid "
                "nesting depends on the "
                "associated geometry "
                "type.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "GeoJSONCoordinateArray",
                "uri": "xsd:string",
            },
            "GeonamesId": {
                "base": "str",
                "description": "Identificador de lugar no GeoNames, "
                "na forma de um CURIE "
                "`geonames:1234`.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "GeonamesId",
                "pattern": "^geonames:[0-9]+$",
                "repr": "str",
                "uri": "xsd:anyURI",
            },
            "Latitude": {
                "base": "float",
                "description": "Latitude em graus decimais (separador: ponto).",
                "from_schema": "https://tradicional.arq.br/schema",
                "maximum_value": 90,
                "minimum_value": -90,
                "name": "Latitude",
                "uri": "xsd:double",
            },
            "Longitude": {
                "base": "float",
                "description": "Longitude em graus decimais (separador: ponto).",
                "from_schema": "https://tradicional.arq.br/schema",
                "maximum_value": 180,
                "minimum_value": -180,
                "name": "Longitude",
                "uri": "xsd:double",
            },
            "OlcPlusCode11": {
                "base": "str",
                "description": "Open Location Code (Plus Code) "
                "com resolução de 11 dígitos.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "OlcPlusCode11",
                "pattern": "^([2-9CFGHJMPQRVWX]{8})\\+([2-9CFGHJMPQRVWX]{3})$",
                "uri": "xsd:string",
            },
            "OrcidId": {
                "base": "str",
                "description": "ORCID iD, sem o prefixo https://orcid.org/.",
                "from_schema": "https://tradicional.arq.br/schema",
                "name": "OrcidId",
                "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$",
                "uri": "xsd:string",
            },
        },
    }
)


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
    modificação = "modification_activity"
    """
    Ação intencional que cria, altera ou modifica um objeto ou obra em um ou mais dos seus aspectos mas não em outros. Usar para ações que não possam ser definidas como tipos mais específicos de alteração.

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
    acréscimo = "part_addition"
    """
    Acréscimo a uma edificação existente, sem lhe alterar fundamentalmente a identidade, por meio da ampliação ou do acréscimo de elementos. O conjunto resultante continuará a ser identificado como a mesma obra anterior ao acréscimo.

    """
    eliminação_parcial = "part_removal"
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
    alteração = "modification_process"
    """
    Processo não deliberado de alteração nas características, aparência ou desempenho dos materiais que constituem um objeto. Por exemplo, corrosão, formação de cristais salinos, etc.

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
    condition_assessment = "condition_assessment"
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


class ObjectType(str):
    """
    The LIDO Object Type Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Object Type element, specifying the particular kind of object being in some way associated with the object/work that is the focus of the record.
    """

    pass


class ReferenceType(str, Enum):
    """
    Tipos de referências a objetos externos previstos no LIDO.
    """

    uri = "uri"
    iri = "iri"
    local = "local"


class RelationType(str):
    """
    Os tipos de relação entre objetos são definidos pelo VRA Core.
    """

    pass


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
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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


class BroaderConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    match: SkosBroaderRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["BroaderConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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


class NarrowerConceptReference(ConceptReference):
    """
    Relações hierárquicas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    match: SkosNarrowerRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["NarrowerConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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


class MappingConceptReference(ConceptReference):
    """
    Relações semânticas.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/concept"}
    )

    match: SkosMappingRelation = Field(
        default=...,
        description="""Tipo da relação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["MappingConceptReference"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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

    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
        json_schema_extra={
            "linkml_meta": {"domain_of": ["BibliographicCitation", "TypedReference"]}
        },
    )
    note: Optional[str] = Field(
        default=None,
        description="""Se necessário, incluir no campo `note` uma especificação adicional, como o número da página da referência bibliográfica de onde a informação foi extraída.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["BibliographicCitation"]}},
    )


class RelatedObject(ConfiguredBaseModel):
    """
    A wrapper for identifying information about an object or work, including collections, related to the object/work in focus. May include a weblink.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/resource"}
    )

    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    rel_type: RelationType = Field(
        default=...,
        description="""Usamos os tipos de relação previstos pelo [VRA Core]. Provavelmente necessitamos apenas de :
- `planFor` : desenho técnico bidimensional de levantamento
  (padrão, pode ser omitido) ;

- `modelFor` : modelo tridimensional, com ou sem informações construtivas
  associadas (BIM) ;

- `imageOf` : outras representações em duas dimensões da edificação ;
- `preparatoryFor` : representação técnica de projeto para intervenções a
  serem realizadas (ou já realizadas) na edificação.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Resource"]}},
    )
    related_object: str = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject"]}}
    )
    object_type: Optional[ObjectType] = Field(
        default=None,
        description="""Usar um vocabulário controlado para identificar o tipo de representação, por exemplo as hierarquias do Getty AAT [obras visuais](http://vocab.getty.edu/hier/aat/300191086). ou [formatos de informação](http://vocab.getty.edu/hier/aat/300220751)
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject"]}},
    )
    resources: Optional[dict[str, Resource]] = Field(
        default=None,
        description="""Os desenhos ou modelos da edificação são apresentados online por meio de imagens vetoriais ou bitmap.
Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização, imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :
As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type> e são inseridas na ficha como um mapa.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Work"]}},
    )
    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
(A FAZER) Ver [Instruções para carregar imagens e desenhos].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["RelatedObject", "Event", "Work"]}
        },
    )
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
        {
            "from_schema": "https://tradicional.arq.br/schema/resource",
            "slot_usage": {
                "related_object": {"name": "related_object", "range": "Work"}
            },
        }
    )

    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    rel_type: RelationType = Field(
        default=...,
        description="""Usamos os tipos de relação previstos pelo [VRA Core]. Provavelmente necessitamos apenas de :
- `planFor` : desenho técnico bidimensional de levantamento
  (padrão, pode ser omitido) ;

- `modelFor` : modelo tridimensional, com ou sem informações construtivas
  associadas (BIM) ;

- `imageOf` : outras representações em duas dimensões da edificação ;
- `preparatoryFor` : representação técnica de projeto para intervenções a
  serem realizadas (ou já realizadas) na edificação.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Resource"]}},
    )
    related_object: str = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject"]}}
    )
    object_type: Optional[ObjectType] = Field(
        default=None,
        description="""Usar um vocabulário controlado para identificar o tipo de representação, por exemplo as hierarquias do Getty AAT [obras visuais](http://vocab.getty.edu/hier/aat/300191086). ou [formatos de informação](http://vocab.getty.edu/hier/aat/300220751)
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject"]}},
    )
    resources: Optional[dict[str, Resource]] = Field(
        default=None,
        description="""Os desenhos ou modelos da edificação são apresentados online por meio de imagens vetoriais ou bitmap.
Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização, imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :
As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type> e são inseridas na ficha como um mapa.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Work"]}},
    )
    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
(A FAZER) Ver [Instruções para carregar imagens e desenhos].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["RelatedObject", "Event", "Work"]}
        },
    )
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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


class MediaObject(ConfiguredBaseModel):
    """
    Descrição e referência a um único arquivo de mídia.
    Obrigatoriamente deve conter uma URI.
    No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
    (A FAZER) Ver [Instruções para carregar imagens e desenhos].

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:MediaObject",
            "close_mappings": ["dctypes:Image"],
            "from_schema": "https://tradicional.arq.br/schema/resource",
        }
    )

    format: TypedReference = Field(
        default=...,
        description="""Campo disciplinado pela especificação [DublinCore] no campo [format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/format/). Esta especificação sugere a [lista de tipos de mídia IANA].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["MediaObject"], "slot_uri": "dcterms:format"}
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
    service: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal como a especificação [IIIF].""",
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
    alt: Optional[str] = Field(
        default=None,
        description="""Texto alternativo para leitores de tela ou outras formas de acessibilidade. Apenas texto sem formatação.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["MediaObject"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
    credit: Optional[str] = Field(
        default=None,
        description="""Informação sobre autoria ou responsabilidade.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    rights: Optional[list[Right]] = Field(
        default=None, json_schema_extra={"linkml_meta": {"domain_of": ["MediaObject"]}}
    )


class TypedReference(ConfiguredBaseModel):
    """
    Permite referenciar um registro local ou externo por meio da sua URI (localizador universal, como um link da internet, por padrão), IRI ou código na base local (não recomendado).
    -------------------------------------------------------------------------
    Reference to a local record, IRI, URI, or LIDO terminology term.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://tradicional.arq.br/schema/shared",
            "slot_usage": {"refid": {"key": True, "name": "refid"}},
        }
    )

    type: Optional[ReferenceType] = Field(
        default=ReferenceType("uri"),
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["TypedReference"],
                "ifabsent": "ReferenceType(uri)",
            }
        },
    )
    term: Optional[str] = Field(
        default=None,
        description="""LIDO terminology term.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["TypedReference"]}},
    )
    refid: str = Field(
        default=...,
        description="""Local or external identifier.""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["BibliographicCitation", "TypedReference"],
                "exact_mappings": ["schema:identifier"],
                "slot_uri": "dcterms:identifier",
            }
        },
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
                    "TypedReference",
                    "GeographicPoint",
                    "GeographicExtent",
                ]
            }
        },
    )

    @field_validator("term")
    def pattern_term(cls, v):
        pattern = re.compile(r"^http://terminology\.lido-schema\.org/lido[0-9]{5}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid term format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid term format: {v}"
            raise ValueError(err_msg)
        return v


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
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "Measurement"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    extent: Optional[TypedReference] = Field(
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
                    "RelatedObject",
                    "MediaObject",
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
    type: Optional[MeasurementType] = Field(
        default=MeasurementType("proper"),
        description="""designa a natureza da medida : largura, altura, área, etc. — usar um dos [tipos de dimensões ](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300226820) do Art and Architecture Thesaurus do Instituto Getty (AAT), enquanto não tivermos um vocabulário controlado próprio.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Measurement"],
                "ifabsent": "MeasurementType(proper)",
            }
        },
    )
    value: float = Field(
        default=...,
        description="""Valor numérico, usar ponto como separador decimal.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )
    qualifier: Optional[MeasurementQualifier] = Field(
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
    shape: Optional[str] = Field(
        default=None,
        description="""caso relevante, indicar a forma do elemento medido usando a [lista de formas do AAT](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300056273), enquanto não tivermos um vocabulário controlado próprio.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Measurement"]}},
    )
    event: Optional[str] = Field(
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

    type: MaterialTechType = Field(
        default=...,
        description="""Tipo da referência a um material ou técnica usado na obra: material de construção (support), revestimento (medium), técnica, instrumento, cor, etc.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["MaterialTech"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
---------------------------------------------------------------------
Qualifies the kind of rights type, whether it refers to a generic kind of right, like copyright or performance rights, or is a specific rights or license statement, for instance, Rights Statements or Creative Commons Licenses.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )
    rights_statement: TypedReference = Field(
        default=...,
        description="""Referencia, preferencialmente por meio de uma URI, as informações específicas dos direitos autorais incidentes sobre o item descrito.
Por padrão, as casas tradicionais pertencem ao domínio público até prova em contrário. Essa informação e a declaração de direitos NKC (Sem direito autoral conhecido) NÃO PODE ser omitida da ficha. Para o domínio público, portanto, indicar a referência : <https://rightsstatements.org/vocab/NKC/1.0/>.
---------------------------------------------------------------------
An index element for rights information being recorded. This can refer to a generic kind of right, such as copyright or a related right, but also be a specific rights or license statement like a standardized statement on copyright, usage, or access rights.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )
    start_date: Optional[EventDate] = Field(
        default=None,
        description="""Date on which a right is or was current.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Right"]}},
    )
    end_date: Optional[EventDate] = Field(
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


class LegalBody(ConfiguredBaseModel):
    """
    Referência a uma pessoa jurídica (pode ser um indivíduo detentor de direitos jurídicos específicos que se queira referenciar) ou entidade coletiva histórica.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/shared"}
    )

    type: Optional[RepositoryType] = Field(
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
    name: Optional[TypedReference] = Field(
        default=None,
        description="""Referencia a identidade do ente legal num vocabulário controlado ou repositório de identidades, tal como o ISNI.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["LegalBody"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
    type: Optional[AgentType] = Field(
        default=AgentType("personal"),
        description="""Define se o agente é uma pessoa, uma organização ou corporação, uma oficina, uma família, etc.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Actor"], "ifabsent": "AgentType(personal)"}
        },
    )
    name: Optional[TypedReference] = Field(
        default=None,
        description="""Nome do agente extraído de um vocabulário controlado.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    role_in_event: Optional[RoleType] = Field(
        default=None,
        description="""Ação desempenhada pelo agente no evento.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    qualifier: Optional[list[TypedReference]] = Field(
        default=None,
        description="""For the Attribution Qualifier Actor element choose a concept URI from the [attribution qualifiers hierarchy](http://vocab.getty.edu/hier/aat/300404264) of the Art & Architecture Thesaurus, or another linked open vocabulary.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Actor"]}},
    )
    extent: Optional[list[TypedReference]] = Field(
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

    type: DateType = Field(
        default=...,
        description="""Qualifica a confiabilidade da data como sendo conhecida ou estimada. A confiabilidade independe do grau de precisão da data.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["EventDate"]}},
    )
    date_value: Optional[date] = Field(
        default=None,
        description="""Usar o formato ISO-8601 (AAAA-MM-DD). Para datas imprecisas, usar o PRIMEIRO ou o ÚLTIMO dia, mês ou ano do período delimitado, conforme se tratar de uma data de corte inicial ou final para o evento, e descrever verbalmente o período no campo `display_date`.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["EventDate"]}},
    )


class StylePeriod(ConceptReference):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/temporal"}
    )

    type: PeriodNameType = Field(
        default=...,
        description="""Designa a natureza ou origem do nome do período ou estilo indicado.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["StylePeriod"]}},
    )
    concept_name: Optional[Concept] = Field(
        default=None,
        json_schema_extra={"linkml_meta": {"domain_of": ["ConceptReference", "Topic"]}},
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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


class RelatedEvent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/temporal"}
    )

    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    event_name: list[str] = Field(
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
            "slot_usage": {"description": {"name": "description", "required": True}},
        }
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
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
    concept_type: Optional[ConceptType] = Field(
        default=ConceptType("concept"),
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
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
    This class comprises identifiable immaterial items that make propositions about reality.
    These propositions may be expressed in text, graphics, images, audiograms, videograms, or by other similar means. Documentation databases are regarded as instances of E31 Document. This class should not be confused with the concept “document” in Information Technology, which is compatible with E73 Information Object.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "crm:E31_Document",
            "close_mappings": ["schema:ArchiveComponent"],
            "from_schema": "https://tradicional.arq.br/schema/resource",
        }
    )

    rel_type: RelationType = Field(
        default=...,
        description="""Usamos os tipos de relação previstos pelo [VRA Core]. Provavelmente necessitamos apenas de :
- `planFor` : desenho técnico bidimensional de levantamento
  (padrão, pode ser omitido) ;

- `modelFor` : modelo tridimensional, com ou sem informações construtivas
  associadas (BIM) ;

- `imageOf` : outras representações em duas dimensões da edificação ;
- `preparatoryFor` : representação técnica de projeto para intervenções a
  serem realizadas (ou já realizadas) na edificação.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Resource"]}},
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
    service: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Apenas no caso de a imagem ser fornecida como um serviço dinâmico online, tal como a especificação [IIIF].""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    unit: Optional[TypedReference] = Field(
        default=None,
        description="""Unidade de medida usada no dimensionamento do objeto ou da representação, por exemplo metros, milímetros ou palmos. Usar a [hierarquia de unidades de medida](https://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300379096) do AAT, ou do nosso próprio [vocabulário controlado].
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "Measurement"]}},
    )
    credit: Optional[str] = Field(
        default=None,
        description="""Informação sobre autoria ou responsabilidade.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource", "MediaObject"]}},
    )
    scale: Optional[float] = Field(
        default=None,
        description="""Número inverso da escala da imagem, se ela tiver uma resolução ou tamanho de página definidos. Por exemplo, para um desenho na escala 1 : 100, `scale: 100`.""",
        ge=0,
        json_schema_extra={"linkml_meta": {"domain_of": ["Resource"]}},
    )
    perspective: Optional[int] = Field(
        default=1,
        description="""Tipo de vista do desenho. Usar a numeração da ISO 19650–2 :

  - 0 = geral
  - 1 = planta baixa (padrão, pode ser omitido)
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
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Resource"], "ifabsent": "integer(1)"}
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
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
(A FAZER) Ver [Instruções para carregar imagens e desenhos].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["RelatedObject", "Event", "Work"]}
        },
    )
    type: EventType = Field(
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
    display_date: Optional[str] = Field(
        default=None,
        description="""Permite a expressão descritiva das datas de início e fim do evento, para contemplar variados graus de incerteza, ou de modo a representar a data em calendários diferentes do gregoriano. Omitir apenas se os valores numéricos das datas forem exatos.
""",
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
    place: Optional[list[Site]] = Field(
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
    related_events: Optional[list[RelatedEvent]] = Field(
        default=None,
        description="""A set of structured information about an event related to the event in focus, indicating the type of relationship where applicable.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
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
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
                    "RelatedObject",
                    "MediaObject",
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
    label_type: Optional[LabelType] = Field(
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
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Appellation"],
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
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Repository"],
                "ifabsent": "RepositoryType(corporate)",
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
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
    -------------------------------------------------------------------------
    An historical landmark or building.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "class_uri": "schema:LandmarksOrHistoricalBuildings",
            "close_mappings": ["crm:E22_Human-Made_Object"],
            "from_schema": "https://tradicional.arq.br/schema/work",
            "slot_usage": {
                "category": {
                    "ifabsent": "string(http://terminology.lido-schema.org/lido00096)",
                    "name": "category",
                },
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
                "id": {
                    "description": "Cada edificação terá um identificador "
                    "gerado a partir do seu "
                    "georreferenciamento usando Open "
                    'Location Code ("PlusCode"). Este '
                    "identificador usa o campo `id`, que "
                    "será gerado automaticamente pelo "
                    "programa WASTH.",
                    "name": "id",
                    "range": "OlcPlusCode11",
                },
                "record_author": {"name": "record_author", "required": True},
                "record_rights": {"name": "record_rights", "required": True},
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
    related_works: Optional[list[RelatedWork]] = Field(
        default=None,
        description="""A wrapper for identifying information about an object or work, including collections, related to the object/work in focus. May include a weblink.
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
O grupo relation é destinado unicamente a cadastrar relações desta edificação com objetos autônomos, tais como outras edificações, conjuntos urbanos, obras de artes visuais, referências bibliográficas ou acervos arquivísticos.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "dcterms:related"}
        },
    )
    resources: Optional[dict[str, Resource]] = Field(
        default=None,
        description="""Os desenhos ou modelos da edificação são apresentados online por meio de imagens vetoriais ou bitmap.
Cada desenho ou modelo pode ser apresentado sob várias representações, como pré-visualização, imagem original, ou serviço [IIIF]. Essas imagens devem ser identificadas como segue :
As categorias de representação previstas no [LIDO] podem ser consultadas em <http://terminology.lido-schema.org/resourceRepresentation_type> e são inseridas na ficha como um mapa.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["RelatedObject", "Work"]}},
    )
    media: Optional[list[MediaObject]] = Field(
        default=None,
        description="""Representações iconográficas deste objeto.
No caso de `preview_image` ou `provided_image`, o link deve referenciar diretamente o arquivo (ficheiro) da imagem. Em se tratando de `provided_3d` ou `service`, o link deve remeter a uma página web que forneça a respetiva API ou as informações acerca do modelo.
(A FAZER) Ver [Instruções para carregar imagens e desenhos].
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["RelatedObject", "Event", "Work"]}
        },
    )
    title_type: TitleType = Field(
        default=..., json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}}
    )
    work_type_condition: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""Descreve o estado físico da edificação quanto à sua aparência de completude, deterioração ou capacidade de desempenhar sua função.
Atende aos campos do [SICG](https://sicg.iphan.gov.br/sicg/manual/manual.html) \"estado de preservação\" e \"estado de conservação\".
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by their overall state such as appearance, level of damage, completeness, or quality. If an object is identified by its prevailing physical state, then it is qualified by condition.
Based on [AAT \"conditions\"](http://vocab.getty.edu/page/aat/300389724) and [CIDOC CRM \"E3 Condition State\"](http://cidoc-crm.org/html/cidoc_crm_v7.1.1_with_translations.html#E3)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
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
        description="""Nos Documentários de edificações, designa sobretudo o contexto imediato de implantação de uma edificação : urbana, rural, isolada, em correnteza, etc.
No Documentário de Lugares Tradicionais, designa o tipo de núcleo populacional : sítio isolado, povoação rural, vila ou cidade, por exemplo.
---------------------------------------------------------------------
Descriptors for objects that are distinguishable by their use or application within a particular physical location. If an object is identifiable by association with specific surroundings, it is qualified by location or context.
Based on [AAT Guidelines \"Types of Guide Terms\"](https://www.getty.edu/research/tools/vocabularies/guidelines/aat_3_1_hierarchical_rels.html)""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Work"],
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
    work_type_subject_type: Optional[list[ConceptReference]] = Field(
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
---------------------------------------------------------------------
A broad category for grouping objects on the basis of shared intrinsic characteristics. The relationship between an object/work and the object genre is a generic is-a-relation rather than a membership based on ascription to a subject group.
Note that the [AAT Object Genres](http://vocab.getty.edu/page/aat/300185711) hierarchy differs in its scope from Object genre here in that the AAT includes more specific terms grouped by various aspects. In general, AAT descriptors are not intended to be used as indexing terms for classification.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "term:lido00853"}
        },
    )
    classification_subject: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.
---------------------------------------------------------------------
A broad category for grouping objects or works on the basis of a topical association, including thematic or systematic classification, or an assignment by discipline. The relationship between an object/work and a subject category is a kind of membership based on ascription rather than a generic is-a relation.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "term:lido00932"}
        },
    )
    classification_local: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.
---------------------------------------------------------------------
A classification scheme for grouping objects on the basis of locally defined criteria, including categories corresponding to the curatorial departments of the repository, such as \"prints and drawings\", \"decorative arts\", \"North America\", \"invertebrates\", \"Bronze Age\" or \"textiles\". [Based on CCO \"Class\"](https://vraweb.org/wp-content/uploads/2020/04/CatalogingCulturalObjectsFullv2.pdf)""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "term:lido01135"}
        },
    )
    classification_special: Optional[list[ConceptReference]] = Field(
        default=None,
        description="""❓ Ainda não implementamos o bloco `objectClassification` do LIDO. Talvez ele não seja relevante para o documentário de arquitetura doméstica, e não é obrigatório no padrão LIDO nem no perfil de aplicação para arquitetura.
---------------------------------------------------------------------
A classification scheme for grouping objects on the basis of criteria defined within specific academic disciplines or cultural domains, such as the \"Hornbostel-Sachs Classification of Musical Instruments\", the \"Nickel-Strunz classification\", biological taxonomies etc. Refers to classification schemes that group objects on the basis of object characteristics, not on the basis of themes or topics which the objects or works are related to.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "term:lido01144"}
        },
    )
    part_of: Optional[list[TypedReference]] = Field(
        default=None,
        description="""Permite identificar o contexto geográfico ou administrativo ao qual a edificação se subordina, ou ainda um conjunto arquitetônico, urbanístico ou conceitual (por exemplo, uma série de casas) do qual ela faz parte.
---------------------------------------------------------------------
A set of structured information about a place that is the broader context for the place in focus, such as the district, state, or nation to which a city belongs.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "dcterms:isPartOf"}
        },
    )
    former_site: Optional[list[Site]] = Field(
        default=None,
        description="""Indica que a edificação não se encontra mais no local indicado, seja porque foi deslocada ou demolida.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    intended: Optional[list[Site]] = Field(
        default=None,
        description="""Sinaliza que a edificação devia ocupar um certo local, mas não chegou a ser construída.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    other: Optional[list[Site]] = Field(
        default=None,
        description="""Para casos de implantação não contemplados em nenhuma das categorias acima.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    location_historic: Optional[list[LocationHistoric]] = Field(
        default=None,
        description="""Antigas jurisdições ou designações para o lugar onde o objeto se encontra. Para um sítio de onde o objeto foi fisicamente removido, usar a lista `former_site`.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    inscriptions: Optional[list[Inscription]] = Field(
        default=None,
        description="""Marcas, símbolos ou textos gravados na edificação, especialmente aqueles referentes à estrutura como um todo e não específicos a alguma de suas partes. Não usar para iconografia.""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Work"]}},
    )
    collection: Optional[list[Union[Concept, Resource, Event, Repository, Work]]] = (
        Field(
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
    )
    work_rights: list[Right] = Field(
        default=...,
        description="""⚠️  Este bloco se refere a eventuais direitos autorais ou de propriedade sobre A EDIFICAÇÃO E O SEU PROJETO, não sobre o conteúdo da ficha, nem sobre a iconografia relacionada.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Work"], "slot_uri": "lido:rightsWorkSet"}
        },
    )
    id: str = Field(
        default=...,
        description="""Cada edificação terá um identificador gerado a partir do seu georreferenciamento usando Open Location Code (\"PlusCode\"). Este identificador usa o campo `id`, que será gerado automaticamente pelo programa WASTH.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: str = Field(
        default=...,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "ifabsent": "string(http://terminology.lido-schema.org/lido00096)",
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: list[Right] = Field(
        default=...,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
    Este bloco corresponde à terminologia do [DublinCore] `coverage > spatial`. Na especificação [LIDO], a localização física de um bem se confunde com a sua inserção institucional (repositório). Na formatação da nossa ficha, tentamos desfazer essa confusão separando o georreferenciamento e o repositório em blocos diferentes.
    As instruções de preenchimento específicas se encontram na documentação das classes que fornecem os dados para o sítio. Consulte também o [Tutorial de georreferenciamento](https://github.com/arqtrad/.github/wiki/Tutorial-de-georreferenciamento) para saber como localizar edificações não cadastradas nas bases de dados do patrimônio cultural (SICG ou SIPA).
    -------------------------------------------------------------------------
    This class comprises 4-dimensional point sets (volumes) in physical spacetime (in contrast to mathematical models of it) regardless of their true geometric forms. They may derive their identity from being the extent of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime. Intersections of instances of E92 Spacetime Volume, E53 Place, and E52 Time-Span are also regarded as instances of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives from or due to the limited precision up to which defining expression can be identified with a real extent in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time.

    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "class_uri": "crm:E92_Spacetime_Volume",
            "exact_mappings": ["schema:DefinedRegion"],
            "from_schema": "https://tradicional.arq.br/schema/work",
            "slot_usage": {
                "id": {
                    "description": "Incluir aqui um identificador da base "
                    "geonames na forma `geonames:1234`.\n",
                    "name": "id",
                    "range": "GeonamesId",
                }
            },
        }
    )

    type: Optional[RepositoryType] = Field(
        default=RepositoryType("geographic"),
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
        description="""Área da implantação da edificação ou sítio cadastrado. Usar o sistema de coordenadas geográficas EPSG:4326 (WGS84) sempre que possível.
---------------------------------------------------------------------
Polygonal, multipolygonal, or linear geographic extent associated with the place.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Site"], "slot_uri": "geo:hasGeometry"}
        },
    )
    event_place_type: Optional[EventPlaceType] = Field(
        default=None,
        description="""Se relevante para a ação, indicar se se trata do local de descobrimento do objeto, do local de origem ou destino do seu translado. Omitir caso o evento não se enquadre nesses casos.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site"]}},
    )
    id: str = Field(
        default=...,
        description="""Incluir aqui um identificador da base geonames na forma `geonames:1234`.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:identifier"}
        },
    )
    author: Optional[str] = Field(
        default=None,
        description="""ORCID iD da pessoa que escreveu a versão original da ficha. Alterar apenas no caso de a ficha ter sido substancialmente reescrita.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:contributor"}
        },
    )
    display: str = Field(
        default=...,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
No vocabulário controlado, preencher este campo OBRIGATORIAMENTE com `term:lido01193` (\"Objeto conceitual\").
---------------------------------------------------------------------
The LIDO Category Vocabulary is a structured controlled list of terms recommended to use as values in the LIDO Category element.
Examples are human-made object or natural object.""",
        json_schema_extra={
            "linkml_meta": {
                "designates_type": True,
                "domain_of": ["Thing"],
                "slot_uri": "term:lidoCategory",
            }
        },
    )
    record_rights: Optional[list[Right]] = Field(
        default=None,
        description="""Informações estruturadas sobre os direitos que incidem sobre o conteúdo textual desta ficha.
⚠️  Este grupo se refere aos direitos sobre o CONTEÚDO da ficha, não sobre os direitos incidentes sobre o objeto descrito.
---------------------------------------------------------------------
A set of structured information about rights regarding the content provided in this LIDO record.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Thing"]}},
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
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
            }
        },
    )
    date: Optional[date] = Field(
        default=None,
        description="""Data de inclusão da ficha.""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Thing"], "slot_uri": "dcterms:created"}
        },
    )
    title: str = Field(
        default=...,
        description="""Nome pelo qual este item é mais comumente conhecido. Outros nomes podem ser cadastrados em `alt_name`.
""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": ["Thing"],
                "exact_mappings": ["schema:name"],
                "slot_uri": "dcterms:title",
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

---------------------------------------------------------------------
Published or external identifiers for the object.
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
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
    source: Optional[list[LegalBody]] = Field(
        default=None,
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "RelatedObject",
                    "MediaObject",
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
                    "RelatedObject",
                    "MediaObject",
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
    type: GeometryType = Field(
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

    extent: Optional[TypedReference] = Field(
        default=None,
        description="""Indica a parte do objeto que está sendo medida — por exemplo, se a altura é até a linha de coroamento ou até a cumeeira, etc. — usar a `uri` de um vocabulário controlado.
""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Measurement", "Inscription", "Topic"]}
        },
    )
    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
                "slot_uri": "skos:scopeNote",
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
                    "RelatedObject",
                    "MediaObject",
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
    type: InscriptionType = Field(
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

    display: Optional[str] = Field(
        default=None,
        description="""A human-readable description for a thing""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "ConceptReference",
                    "BibliographicCitation",
                    "RelatedObject",
                    "MediaObject",
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
    extent: Optional[TypedReference] = Field(
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
    type: SubjectType = Field(
        default=...,
        description="""Categoriza o nível descritivo ou interpretativo do tema.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Topic"]}},
    )


class LocationHistoric(ConfiguredBaseModel):
    """
    Designações alternativas ou jurisdições antigas para o mesmo local, NÃO a localização original de uma construção fisicamente deslocada (para tanto, cadastrar outra localização do tipo `former_site`). Preencher apenas caso a nomenclatura seja relevante, por exemplo para nomear as antigas províncias de Portugal ou o Oeste da Bahia, que originalmente pertencia a Pernambuco, ou ainda se for relevante informar uma região física.
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {"from_schema": "https://tradicional.arq.br/schema/work"}
    )

    type: RepositoryType = Field(
        default=...,
        description="""Define se o local histórico designa uma jurisdição, um topônimo antigo, ou outro.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["LocationHistoric"]}},
    )
    name: TypedReference = Field(
        default=...,
        description="""Identificação do local com referência a um vocabulário controlado ou repositório de topônimos tal como o geonames.
""",
        json_schema_extra={"linkml_meta": {"domain_of": ["LocationHistoric"]}},
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


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ConceptReference.model_rebuild()
BroaderConceptReference.model_rebuild()
NarrowerConceptReference.model_rebuild()
MappingConceptReference.model_rebuild()
BibliographicCitation.model_rebuild()
RelatedObject.model_rebuild()
RelatedWork.model_rebuild()
MediaObject.model_rebuild()
TypedReference.model_rebuild()
Measurement.model_rebuild()
MaterialTech.model_rebuild()
Right.model_rebuild()
LegalBody.model_rebuild()
Actor.model_rebuild()
EventDate.model_rebuild()
StylePeriod.model_rebuild()
RelatedEvent.model_rebuild()
Thing.model_rebuild()
Concept.model_rebuild()
Resource.model_rebuild()
Event.model_rebuild()
Appellation.model_rebuild()
Repository.model_rebuild()
Work.model_rebuild()
Site.model_rebuild()
GeographicPoint.model_rebuild()
GeographicExtent.model_rebuild()
Inscription.model_rebuild()
Topic.model_rebuild()
LocationHistoric.model_rebuild()
Container.model_rebuild()
