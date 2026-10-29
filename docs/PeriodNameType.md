---
search:
  boost: 2.0
---


# Enum: PeriodNameType 




_O vocabulário de tipos de período/estilo do LIDO é uma lista controlada estruturada de termos recomendada para uso como valores do atributo de tipo do elemento Período/Estilo._

_O atributo de tipo qualifica o tipo particular de informação de período/estilo, como estilo, período ou movimento. Exemplos podem ser “neolítico” para um período, “impressionista” para um estilo ou “cubismo” para um movimento._

_Baseado na categoria do [CDWA "Styles/Periods/Groups/Movements"](http://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)_

__



<div data-search-exclude markdown="1">

URI: [wasth:PeriodNameType](https://tradicional.arq.br/schema/PeriodNameType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| period | term:lido00731 | A distinct named historical or cultural portion or division of time during wh... |
| style | term:lido00732 | A distinct configuration of artistic elements that together constitute a name... |
| group | term:lido00735 | A cultural group, which includes societies or groups of people characterized ... |
| movement | term:lido00733 | The state or process in which events or conditions transpire, a tendency, or ... |
| dynasty | term:lido00734 | The succession of rulers from the same family, line, stock, or group, during ... |




## Slots

| Name | Description |
| ---  | --- |
| [period_name_type](period_name_type.md) | Designa a natureza ou origem do nome do período ou estilo indicado |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: PeriodNameType
description: 'O vocabulário de tipos de período/estilo do LIDO é uma lista controlada
  estruturada de termos recomendada para uso como valores do atributo de tipo do elemento
  Período/Estilo.

  O atributo de tipo qualifica o tipo particular de informação de período/estilo,
  como estilo, período ou movimento. Exemplos podem ser “neolítico” para um período,
  “impressionista” para um estilo ou “cubismo” para um movimento.

  Baseado na categoria do [CDWA "Styles/Periods/Groups/Movements"](http://www.getty.edu/research/publications/electronic_publications/cdwa/17styles.html)

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  period:
    text: period
    description: 'A distinct named historical or cultural portion or division of time
      during which something runs its course, characterized by some prevalent or distinguishing
      condition, circumstance, or occurrence, or by the rule of a particular government.

      '
    meaning: term:lido00731
  style:
    text: style
    description: 'A distinct configuration of artistic elements that together constitute
      a named manner of expression peculiar to a certain epoch, people, or to a visual
      appearance, technique, or visual language adopted by particular adherents of
      that language.

      '
    meaning: term:lido00732
  group:
    text: group
    description: 'A cultural group, which includes societies or groups of people characterized
      by common ideas, customs, social behavior, products, or way of life within a
      particular nation, people, or period.

      '
    meaning: term:lido00735
  movement:
    text: movement
    description: 'The state or process in which events or conditions transpire, a
      tendency, or a trend evident at a particular time or in a particular sphere,
      particularly a course or series of actions and endeavours on the part of a group
      of people working towards a shared goal or to advance a shared political, social,
      or artistic objective.

      '
    meaning: term:lido00733
  dynasty:
    text: dynasty
    description: 'The succession of rulers from the same family, line, stock, or group,
      during a particular period of time; extended to include all the people and culture
      surrounding this succession of rulers.

      '
    meaning: term:lido00734

```
</details>

</div>