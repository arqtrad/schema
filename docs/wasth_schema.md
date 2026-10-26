# wasth_schema

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
