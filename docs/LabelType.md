---
search:
  boost: 2.0
---


# Enum: LabelType 




_No SKOS, caracteriza se cada termo deve ser considerado preferencial ou alternativo, usado para indexação, oculto da visualização (usado apenas para buscas), etc._

__



<div data-search-exclude markdown="1">

URI: [wasth:LabelType](https://tradicional.arq.br/schema/LabelType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| alternative | skos:altLabel | Abreviações, abreviaturas, variantes lexicais e formas irregulares de singula... |
| display | term:lido00526 | Nome a ser apresentado na interfaz pública, incluindo artigos se for o caso |
| hidden | skos:hiddenLabel | Uma variante do nome com erros comuns de grafia ou imprecisões lexicais, mas ... |
| indexing | term:lido00961 | Nome, termo ou identificador a ser usado em indexação, por exemplo removendo ... |
| preferred | skos:prefLabel | O nome, termo ou título preferencial |




## Slots

| Name | Description |
| ---  | --- |
| [title_preference](title_preference.md) | Indica se o nome em questão deve ser oculto ou não, se é uma versão alternati... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: LabelType
description: 'No SKOS, caracteriza se cada termo deve ser considerado preferencial
  ou alternativo, usado para indexação, oculto da visualização (usado apenas para
  buscas), etc.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  alternative:
    text: alternative
    description: Abreviações, abreviaturas, variantes lexicais e formas irregulares
      de singular ou plural podem ser incluídas como termos ou títulos alternativos
      para um conceito ou objeto. No caso de edificações ou conjuntos que são conhecidos
      por mais de um nome (por exemplo, pela sua função atual ou antiga, ou pelo endereço),
      selecionar `alternative` e indicar o tipo de título.
    meaning: skos:altLabel
  display:
    text: display
    description: Nome a ser apresentado na interfaz pública, incluindo artigos se
      for o caso.
    meaning: term:lido00526
  hidden:
    text: hidden
    description: Uma variante do nome com erros comuns de grafia ou imprecisões lexicais,
      mas que seja relevante para buscas dos usuários. Deve ficar oculto da interfaz
      pública.
    meaning: skos:hiddenLabel
  indexing:
    text: indexing
    description: Nome, termo ou identificador a ser usado em indexação, por exemplo
      removendo artigos ou partículas iniciais, invertendo a ordem do nome e do sobrenome,
      etc.
    meaning: term:lido00961
  preferred:
    text: preferred
    description: O nome, termo ou título preferencial. Normalmente não usaremos esta
      opção pois o campo `title` já contempla a opção preferencial.
    meaning: skos:prefLabel

```
</details>

</div>