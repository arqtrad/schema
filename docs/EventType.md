---
search:
  boost: 2.0
---


# Enum: EventType 




_O tipo de incidência sobre a edificação que o evento descreve. Usa a terminologia do LIDO em <http://terminology.lido-schema.org/eventType>._

__



<div data-search-exclude markdown="1">

URI: [wasth:EventType](https://tradicional.arq.br/schema/EventType)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| creation | term:lido0001 | Designa um acontecimento que leva à conceção de itens ou produtos de natureza... | Title: criação<br>|
| designing | term:lido00224 | O projeto, na classificação de tipos de eventos do LIDO, designa a criação de... | Title: projeto<br>|
| production | term:lido00007 | Designa ações que levam à existência de novos objetos, compreendendo ações co... | Title: produção<br>|
| item_production | term:lido01096 | No caso de construções seriadas (por exemplo, casas idênticas numa vila operá... | Title: produção de um exemplar<br>|
| completion | term:lido00025 | Processo que completa um objeto ou uma campanha de obras | Title: conclusão<br>|
| execution | term:lido00031 | Ação de produzir um objeto com base num projeto, por oposição ao processo de ... | Title: execução do projeto<br>|
| transformation | term:lido00029 | Ação que destrói um objeto e, usando substancialmente a mesma matéria, produz... | Title: transformação<br>|
| reconstruction | lido:lido00723 | Ato de construir uma nova estrutura que substitui e se parece com uma constru... | Title: reconstrução<br>|
| translocation | lido:lido01159 | A remoção designa o ato de se desmantelar uma edificação no seu local de orig... | Title: remoção<br>|
| modification_activity | term:lido00006 | Ação intencional que cria, altera ou modifica um objeto ou obra em um ou mais... | Title: modificação<br>|
| conservation | term:lido00402 | Ação ou processo realizado visando à estabilidade e salvaguarda do objeto no ... | Title: conservação<br>|
| conversion | term:lido01178 | Intervenção significativa na materialidade e espacialidade de uma edificação,... | Title: reforma<br>|
| dismantling | term:lido01179 | Ato de desmontar ou remover partes significativas de um objeto, especialmente... | Title: desmantelamento<br>|
| part_addition | term:lido00008 | Acréscimo a uma edificação existente, sem lhe alterar fundamentalmente a iden... | Title: acréscimo<br>|
| part_removal | term:lido00021 | Envolve a redução de uma edificação devida à eliminação de parte(s) | Title: eliminação parcial<br>|
| partial_destruction_activity | term:lido01187 | Ação intencional de destruir ou danificar partes de uma obra, sem lhe comprom... | Title: destruição parcial<br>|
| remediation | term:lido01180 | Atividades construtivas ou de gestão que têm por objetivo restituir uma obra ... | Title: reconstituição<br>|
| renewal | term:lido01183 | Ação que altera uma edificação de modo a recuperar a sua estrutura, atualizar... | Title: renovação<br>|
| restoration | term:lido00034 | Alterações a um objeto que têm por objetivo restabelecer um estado original o... | Title: restauração<br>|
| modification_process | term:lido01155 | Processo não deliberado de alteração nas características, aparência ou desemp... | Title: alteração<br>|
| partial_destruction_process | term:lido01157 | Processo não intencional de degradação material, destruindo ou danificando pa... | Title: perda parcial<br>|
| deterioration | term:lido01160 | Processo de perda parcial de matéria, desempenho, ou funcionalidade de um obj... | Title: deterioração<br>|
| adaptive_reuse | term:lido01161 | Ação de converter ou adaptar uma edificação, em geral com valor histórico-cul... | Title: reutilização adaptada<br>|
| opening | term:lido01169 | Ato pelo qual um objeto é declarado operacional, geralmente por meio de uma c... | Title: inauguração<br>|
| decommissioning | term:lido01170 | Ação que acompanha ou sinaliza o encerramento da utilização de um objeto, ger... | Title: desafetação<br>|
| attribute_assignment | None |  ||
| assignment_to_curated_holding | None |  ||
| condition_assessment | None |  ||
| cultural_context_assignment | None |  ||
| designation | None |  ||
| deciphering | None |  ||
| meaning_assignment | None |  ||
| name_assignment | None |  ||
| type_assignment | None |  ||
| ceremony | None |  ||
| cornerstone | None |  ||
| groundbreaking | None |  ||
| consecration | None |  ||
| deconsecration | None |  ||
| change_control_or_title | None |  ||
| change_control_and_title | None |  ||
| change_legal_title | None |  ||
| restitution | None |  ||
| change_physical_control | None |  ||
| collecting | None |  ||
| loss | None |  ||
| commissioning | None |  ||
| excavation | None |  ||
| exhibition | None |  ||
| finding | None |  ||
| marketing | None |  ||
| move | None |  ||
| req_assess | None |  ||
| display_assess | None |  ||
| move_assess | None |  ||
| performance | None |  ||
| planning | None |  ||
| protection | None |  ||
| publishing | None |  ||
| use | None |  ||
| end_existence | None |  ||
| destruction | None |  ||
| destruction_activity | None |  ||
| destruction_process | None |  ||
| unknown | None |  ||




## Slots

| Name | Description |
| ---  | --- |
| [event_type](event_type.md) | Categoriza o evento segundo os vários tipos de ações, de processos, ou de res... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: EventType
description: 'O tipo de incidência sobre a edificação que o evento descreve. Usa a
  terminologia do LIDO em <http://terminology.lido-schema.org/eventType>.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  creation:
    text: creation
    description: 'Designa um acontecimento que leva à conceção de itens ou produtos
      de natureza imaterial, como obras literárias ou imagens. Não usar para a produção
      de bens materiais. Quando a conceção desses bens, como uma edificação, passa
      por um processo de criação intelectual atestada, usar para tanto o termo `designing`
      ("projeto").

      '
    meaning: term:lido0001
    title: criação
    source: crm:E65_Creation
    exact_mappings:
    - vra:wasCreated
  designing:
    text: designing
    description: 'O projeto, na classificação de tipos de eventos do LIDO, designa
      a criação de um arcabouço conceitual para a organização da aparência de objetos
      tridimensionais, obras visuais, obras de arquitetura, ou sistemas técnicos.

      '
    meaning: term:lido00224
    title: projeto
    comments:
    - 'Em contraste com "Criação", que descreve a criação de um objeto ou obra em
      nível conceitual, recomenda-se usar "Projeto" para todos os eventos em que é
      criado um objeto físico que prepara a produção de um objeto mais acabado ou
      serve como modelo direto para ele. Frequentemente, trata-se de desenhos usados
      como esboços na produção de pinturas, esculturas ou edificações. Pode também
      ser um modelo tridimensional do qual se produz um molde; objetos preparatórios
      podem igualmente ser gerados digitalmente.

      Recomenda-se usar este termo quando ele for parte de diversos acontecimentos
      na história da produção da edificação que precisam ser distinguidos entre si,
      cada qual tendo ocorrido em diferentes momentos e envolvento agentes distintos.

      Se o objeto que está sendo descrito na ficha é ele próprio um projeto ou outra
      forma de elemento preparatório para a construção, o termo mais indicado para
      o eventType é `production` ("produção").'
    source: aat:300102051
    exact_mappings:
    - vra:wasDesigned
  production:
    text: production
    description: 'Designa ações que levam à existência de novos objetos, compreendendo
      ações como projeto e execução.

      '
    meaning: term:lido00007
    title: produção
    notes:
    - Detalhar os processos e técnicas que levaram à produção do objeto na seção materiais
      e técnicas do evento, por exemplo indicando os sistemas construtivos empregados.
    source: crm:E12_Production
    exact_mappings:
    - vra:wasProduced
  item_production:
    text: item_production
    description: 'No caso de construções seriadas (por exemplo, casas idênticas numa
      vila operária), designa a produção de um exemplar singular dentro do conjunto.
      Usar quando for relevante individualizar a produção desses exemplares no âmbito
      da descrição do seu conjunto, mas não quando cada exemplar for indexado separadamente.

      '
    meaning: term:lido01096
    title: produção de um exemplar
    comments:
    - Este tipo de evento não deve ser usado para designar a produção de partes do
      processo produtivo, tais como projetos, maquetes, protótipos ou moldes. Quando
      for relevante informar a produção de um exemplar, deve-se precisar quais características
      permitem identificá-lo dentro do conjunto (endereço, variações, etc.).
    source: crm:E22_Human-Made_Object
    close_mappings:
    - aat:300404024
  completion:
    text: completion
    description: 'Processo que completa um objeto ou uma campanha de obras.

      '
    meaning: term:lido00025
    title: conclusão
    source: aat:300053844
    close_mappings:
    - aat:300390560
  execution:
    text: execution
    description: 'Ação de produzir um objeto com base num projeto, por oposição ao
      processo de projeto.

      '
    meaning: term:lido00031
    title: execução do projeto
    source: aat:300069715
    close_mappings:
    - aat:300069715
    - http://d-nb.info/gnd/4456788-1
  transformation:
    text: transformation
    description: 'Ação que destrói um objeto e, usando substancialmente a mesma matéria,
      produz outro que mantém características reconhecíveis do objeto anterior mas
      é essencialmente distinto deste por sua natureza e identidade. Esta categoria
      pode ser usada tanto para designar a destruição do objeto antigo quanto a produção
      do objeto novo.

      Exemplos de transformação incluem o uso de espólios ou ruínas para produzir
      uma nova construção. Não deve ser confundido com `reconstruction` ("reconstrução"),
      que implica seja uma mudança de lugar, seja a reprodução da identidade visual
      e espacial da edificação anterior.

      '
    meaning: term:lido00029
    title: transformação
    source: crm:E81_Transformation
  reconstruction:
    text: reconstruction
    description: 'Ato de construir uma nova estrutura que substitui e se parece com
      uma construção anterior que já não subsiste, baseada em evidências históricas,
      arqueológicas, gráficas, literárias ou outras. A semelhança visual e, eventualmente,
      funcional é a característica principal de uma reconstrução, e ela pode ou não
      usar materiais sobrestantes da edificação anterior.

      A edificação destruída e a edificação reconstruída devem ser cadastradas em
      fichas distintas e relacionadas entre si.

      '
    meaning: lido:lido00723
    title: reconstrução
    source: aat:300081531
    exact_mappings:
    - wd:Q2478058
    close_mappings:
    - https://d-nb.info/gnd/4065958-6
    broad_mappings:
    - aat:300053744
  translocation:
    text: translocation
    description: 'A remoção designa o ato de se desmantelar uma edificação no seu
      local de origem para reconstruí-la em outro sítio. Para construções deslocadas
      sem serem desmanteladas, usar o tipo de evento `move` ("deslocação").

      Exemplos de remoção são aquela do templo de Abu Simbel, no Egito, ou ainda aquela
      da casa Erbo Stenzel em Curitiba do seu lote original para o parque São Lourenço
      (onde foi posteriormente destruída num incêndio).

      '
    meaning: lido:lido01159
    title: remoção
    source: https://www.vdl-denkmalpflege.de/fileadmin/dateien/Brosch%C3%BCren/VdL_Leitbild_Final_160527__1_.pdf
    exact_mappings:
    - https://d-nb.info/gnd/4258556-9
    broad_mappings:
    - aat:300149370
  modification_activity:
    text: modification_activity
    description: 'Ação intencional que cria, altera ou modifica um objeto ou obra
      em um ou mais dos seus aspectos mas não em outros. Usar para ações que não possam
      ser definidas como tipos mais específicos de alteração.

      '
    meaning: term:lido00006
    title: modificação
    source: crm:E11_Modification
    exact_mappings:
    - vra:wasAlteration
    close_mappings:
    - aat:300105442
  conservation:
    text: conservation
    description: 'Ação ou processo realizado visando à estabilidade e salvaguarda
      do objeto no longo prazo, incluindo a sua proteção contra danos ou deterioração
      e a prevenção da deterioração natural da sua matéria. No nosso vocabulário,
      a conservação é diferente da preservação e da restauração.

      '
    meaning: term:lido00402
    title: conservação
    source: aat:300404519
    close_mappings:
    - vra:wasRestored
    - aat:300404519
    - http://d-nb.info/gnd/4114279-2
    broad_mappings:
    - term:lido00006
  conversion:
    text: conversion
    description: 'Intervenção significativa na materialidade e espacialidade de uma
      edificação, usando materiais e técnicas construtivas. Frequentemente resulta
      na alteração de uso ou de aparência da edificação, mas sem comprometer a sua
      identidade anterior.

      Sempre que possível, preferir designações mais específicas, tais como `addition`,
      `removal`, `adaptive_reuse`, `renewal`.

      '
    meaning: term:lido01178
    title: reforma
    source: https://www.duden.de/rechtschreibung/umbauen_umgebaut
    exact_mappings:
    - https://d-nb.info/gnd/4061577-7
    close_mappings:
    - https://www.designingbuildings.co.uk/wiki/Conversion
    broad_mappings:
    - term:lido00006
  dismantling:
    text: dismantling
    description: 'Ato de desmontar ou remover partes significativas de um objeto,
      especialmente com a intenção de reduzir ou desbilitar o seu uso. Particularmente,
      refere-se à desmontagem cuidadosa de modo a evitar danos ao material removido,
      visando à sua reutilização, reciclagem ou gestão de resíduos.

      '
    meaning: term:lido01179
    title: desmantelamento
    source: aat:300061163
    exact_mappings:
    - wd:Q52161698
    - https://d-nb.info/gnd/4149065-4
    close_mappings:
    - https://en.wikipedia.org/wiki/Deconstruction_(building)
    - https://www.designingbuildings.co.uk/wiki/Deconstruction
    broad_mappings:
    - wd:Q52161698
    - aat:300404064
  part_addition:
    text: part_addition
    description: 'Acréscimo a uma edificação existente, sem lhe alterar fundamentalmente
      a identidade, por meio da ampliação ou do acréscimo de elementos. O conjunto
      resultante continuará a ser identificado como a mesma obra anterior ao acréscimo.

      '
    meaning: term:lido00008
    title: acréscimo
    source: crm:E79_Part_Addition
    broad_mappings:
    - term:lido00006
  part_removal:
    text: part_removal
    description: 'Envolve a redução de uma edificação devida à eliminação de parte(s).
      Pode incluir a eliminação de anexos, de elementos construtivos, ou a exclusão
      de uma obra de um conjunto designado.

      '
    meaning: term:lido00021
    title: eliminação parcial
    source: crm:E80_Part_Removal
    narrow_mappings:
    - term:lido01187
    broad_mappings:
    - aat:300224146
    - term:lido00006
  partial_destruction_activity:
    text: partial_destruction_activity
    description: 'Ação intencional de destruir ou danificar partes de uma obra, sem
      lhe comprometer a identatidade enquanto objeto de documentação.

      '
    meaning: term:lido01187
    title: destruição parcial
    source: crm:E6_Destruction
    narrow_mappings:
    - term:lido01180
    broad_mappings:
    - term:lido00021
    - term:lido00022
  remediation:
    text: remediation
    description: 'Atividades construtivas ou de gestão que têm por objetivo restituir
      uma obra a um estado anterior conhecido ou presumido, sobretudo após perdas
      catastróficas de materialidade ou integridade.

      '
    meaning: term:lido01180
    title: reconstituição
    source: https://www.duden.de/rechtschreibung/rueckbauen
    exact_mappings:
    - https://d-nb.info/gnd/4410380-3
    related_mappings:
    - https://historicengland.org.uk/advice/hpg/uwandhc/unlawfulworks/
    broad_mappings:
    - term:lido00034
    - term:lido01187
  renewal:
    text: renewal
    description: 'Ação que altera uma edificação de modo a recuperar a sua estrutura,
      atualizar a sua aparência, permitir a adequação a novos usos, aprimorar a sua
      eficiência energética, ou outras finalidades não relacionadas à preservação
      do patrimônio cultural ou que não tenham considerações patrimoniais como prioridade.

      '
    meaning: term:lido01183
    title: renovação
    source: aat:300389648
    close_mappings:
    - aat:300260783
    - aat:300077781
    narrow_mappings:
    - wd:Q2144402
    broad_mappings:
    - https://d-nb.info/gnd/4152832-3
    - term:lido00006
  restoration:
    text: restoration
    description: 'Alterações a um objeto que têm por objetivo restabelecer um estado
      original ou anterior conhecido ou presumido (usar em vez de `part_removal` ---
      "eliminação parcial" se a intenção dominante da eliminação tiver sido a restauração
      a um estado anterior).

      '
    meaning: term:lido00034
    title: restauração
    source: aat:300053742
    exact_mappings:
    - vra:wasRestored
    close_mappings:
    - wd:Q217102
    - aat:300053742
    - http://d-nb.info/gnd/4049600-4
  modification_process:
    text: modification_process
    description: 'Processo não deliberado de alteração nas características, aparência
      ou desempenho dos materiais que constituem um objeto. Por exemplo, corrosão,
      formação de cristais salinos, etc.

      '
    meaning: term:lido01155
    title: alteração
    source: aat:300105442
    close_mappings:
    - crm:E11_Modification
    narrow_mappings:
    - term:lido01157
    broad_mappings:
    - term:lido01154
  partial_destruction_process:
    text: partial_destruction_process
    description: 'Processo não intencional de degradação material, destruindo ou danificando
      partes de um objeto sem descaracterizar a sua identidade (por exemplo, sem convertê-lo
      numa ruína). Pode ser causado por condições ambientais continuadas ou por desastres
      naturais.

      '
    meaning: term:lido01157
    title: perda parcial
    close_mappings:
    - crm:E6_Destruction
    narrow_mappings:
    - term:lido01160
    broad_mappings:
    - term:lido01155
    - term:lido00022
  deterioration:
    text: deterioration
    description: 'Processo de perda parcial de matéria, desempenho, ou funcionalidade
      de um objeto sem intervenção ou atuação deliberada. Geralmente causado por condições
      ambientais continuadas, mas pode ser agravado por desastres naturais. A deterioração
      pode levar ao `destruction_process` ("arruinamento") da edificação.

      '
    meaning: term:lido01160
    title: deterioração
    source: aat:300054106
    close_mappings:
    - https://d-nb.info/gnd/4745718-1
    - wd:Q94643648
    broad_mappings:
    - term:lido01157
  adaptive_reuse:
    text: adaptive_reuse
    description: 'Ação de converter ou adaptar uma edificação, em geral com valor
      histórico-cultural reconhecido, para novos usos ou aplicação em contexto distinto
      do original. Distinguir eventos de reutilização adaptativa de eventos que envolvem
      as intervenções físicas necessárias ou preparatórias a essa reutilização, usando
      o termo `conversion` ("reforma").

      '
    meaning: term:lido01161
    title: reutilização adaptada
    source: aat:300056392
    exact_mappings:
    - wd:Q111749149
    close_mappings:
    - https://d-nb.info/gnd/4042840-0
    - aat:300417716
    - wd:Q21021151
    narrow_mappings:
    - term:lido01170
    - term:lido01169
    broad_mappings:
    - term:lido00004
  opening:
    text: opening
    description: 'Ato pelo qual um objeto é declarado operacional, geralmente por
      meio de uma cerimônia, mas não necessariamente.

      '
    meaning: term:lido01169
    title: inauguração
    source: aat:300054769
    close_mappings:
    - wd:Q3010369
    - https://d-nb.info/gnd/4338947-8
    narrow_mappings:
    - aat:300404068
    broad_mappings:
    - wd:Q29933838
    - term:lido01161
  decommissioning:
    text: decommissioning
    description: 'Ação que acompanha ou sinaliza o encerramento da utilização de um
      objeto, geralmente associado à interdição física da edificação.

      '
    meaning: term:lido01170
    title: desafetação
    source: https://www.designingbuildings.co.uk/wiki/Decommissioning_buildings
    close_mappings:
    - https://en.wikipedia.org/wiki/Decommissioning
    - https://d-nb.info/gnd/4125246-9
    narrow_mappings:
    - https://d-nb.info/gnd/4513722-5
    broad_mappings:
    - wd:Q29933838
    - term:lido01161
  attribute_assignment:
    text: attribute_assignment
  assignment_to_curated_holding:
    text: assignment_to_curated_holding
  condition_assessment:
    text: condition_assessment
  cultural_context_assignment:
    text: cultural_context_assignment
  designation:
    text: designation
  deciphering:
    text: deciphering
  meaning_assignment:
    text: meaning_assignment
  name_assignment:
    text: name_assignment
  type_assignment:
    text: type_assignment
  ceremony:
    text: ceremony
  cornerstone:
    text: cornerstone
  groundbreaking:
    text: groundbreaking
  consecration:
    text: consecration
  deconsecration:
    text: deconsecration
  change_control_or_title:
    text: change_control_or_title
  change_control_and_title:
    text: change_control_and_title
  change_legal_title:
    text: change_legal_title
  restitution:
    text: restitution
  change_physical_control:
    text: change_physical_control
  collecting:
    text: collecting
  loss:
    text: loss
  commissioning:
    text: commissioning
    exact_mappings:
    - vra:wasCommission
  excavation:
    text: excavation
  exhibition:
    text: exhibition
    close_mappings:
    - vra:wasPresented
  finding:
    text: finding
    exact_mappings:
    - vra:wasDiscovered
  marketing:
    text: marketing
  move:
    text: move
  req_assess:
    text: req_assess
  display_assess:
    text: display_assess
  move_assess:
    text: move_assess
  performance:
    text: performance
    exact_mappings:
    - vra:wasPerformed
  planning:
    text: planning
  protection:
    text: protection
  publishing:
    text: publishing
    exact_mappings:
    - vra:wasPublished
  use:
    text: use
  end_existence:
    text: end_existence
  destruction:
    text: destruction
  destruction_activity:
    text: destruction_activity
  destruction_process:
    text: destruction_process
  unknown:
    text: unknown

```
</details>

</div>