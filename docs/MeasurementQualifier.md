---
search:
  boost: 2.0
---


# Enum: MeasurementQualifier 




_Qualifica a confiabilidade das medidas aferidas._

__



<div data-search-exclude markdown="1">

URI: [wasth:MeasurementQualifier](https://tradicional.arq.br/schema/MeasurementQualifier)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| interpreted | None | Metrologia interpretativa ou citação textual | Title: interpretativa<br>|
| estimated | None | Estimativa obtida por comparação com uma escala gráfica, com medidas adjacent... | Title: estimativa visual<br>|
| derived | None | Extrapolado de um desenho ou modelo | Title: extrapolada<br>|
| measured | None | Medida obtida no local por meio de instrumentos manuais ou eletrônicos (trena... | Title: medida no local<br>|
| scanned | None | Medida extraída de um escaneamento a laser de alta precisão ou de uma estação... | Title: escaneada digitalmente<br>|




## Slots

| Name | Description |
| ---  | --- |
| [measurement_qualifier](measurement_qualifier.md) | Indica que as medidas são aproximadas |










## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: MeasurementQualifier
description: 'Qualifica a confiabilidade das medidas aferidas.

  '
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  interpreted:
    text: interpreted
    description: Metrologia interpretativa ou citação textual.
    title: interpretativa
  estimated:
    text: estimated
    description: 'Estimativa obtida por comparação com uma escala gráfica, com medidas
      adjacentes conhecidas, ou por caminhamento, partes do corpo, etc.

      '
    title: estimativa visual
  derived:
    text: derived
    description: Extrapolado de um desenho ou modelo.
    title: extrapolada
  measured:
    text: measured
    description: 'Medida obtida no local por meio de instrumentos manuais ou eletrônicos
      (trena, teodolito, etc.).

      '
    title: medida no local
  scanned:
    text: scanned
    description: 'Medida extraída de um escaneamento a laser de alta precisão ou de
      uma estação topográfica digital.

      '
    title: escaneada digitalmente

```
</details>

</div>