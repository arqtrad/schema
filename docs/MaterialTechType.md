---
search:
  boost: 2.0
---


# Enum: MaterialTechType 




_A materialidade e as técnicas de produção ou intervenção na edificação devem ser categorizadas segundo esta classificação._

__



<div data-search-exclude markdown="1">

URI: [wasth:MaterialTechType](https://tradicional.arq.br/schema/MaterialTechType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| material | term:lido00132 |  |
| medium | term:lido00513 |  |
| support | term:lido00514 |  |
| color_name | term:lido00479 |  |
| implement | term:lido00248 |  |
| technique | term:lido00131 |  |
| watermark | term:lido00427 |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [material_tech_type](material_tech_type.md) | Tipo da referência a um material ou técnica usado na obra: material de constr... |








## Notes

* The physical matter or substance from which an object is made, including any tangible substances, either naturally or synthetically derived, ranging from specific materials to types of material designated by their function. The term comprises both the media that are incorporated in an object and any support to which the media are applied.
Based on [AAT "materials (matter)"](http://vocab.getty.edu/page/aat/300010358); [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2)
Use the most specific term for the material that is appropriate. It is strongly recommended to take the indexing term from a published controlled vocabulary, preferably a Linked Open Vocabulary, for example the Art & Architecture Thesaurus, specifically its [Materials hierarchy](http://www.getty.edu/vow/AATFullDisplay?find=materials&amp;logic=AND&amp;note=&amp;page=1&amp;subjectid=300010357).
* Medium, as a value for the type attribute of the LIDO Term Materials/Techniques element, designates the material that is applied to a support in the making of an object or a work of art, such as ink on paper or oil paint on canvas; often a particular technique or techniques are closely associated with the media. Based on [AAT "media (artists' materials)"](http://vocab.getty.edu/page/aat/300163343); [CDWA Materials/Techniques](https://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#implement).
In many forms of art, a distinction is made between materials used as the media, and materials used as the support. Medium is the material applied to the support. For example, for a drawing described as pen and brown ink and black chalk on paper, pen is the instrument, ink and black chalk are the media, and paper is the support. [Cited from Categories for the Description of Works of Art (CDWA) "Materials/Techniques"]
* Support, as a value for the type attribute of the LIDO Term Materials/Techniques element, designates the surface material to which media are applied or a work is mounted, for example canvas, oak panel, laid paper, wood, copper, glass, or marble. For example, with paintings, drawings, prints, or photographs, the media would be applied to the surface of a support such as paper, wood panel, canvas, or glass in order to create the image. Used typically for two-dimensional works, although the concept may apply to any work.
Based on [AAT "supports"](http://vocab.getty.edu/page/aat/300014844); [CDWA "Materials/Techniques"](https://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#implement)
* Record a term specifying the color, tint, or hue of the material, particularly if color is an unusual or important characteristic of the object. [All colored impressions of materials of an object are meant, not just parts treated with dyestuff. The information refers to the overall effect of color, not only as cause of, e.g., dyeing or painting.]
It is recommended to use internationally approved standard color charts, codes and terminology such as the Universal Color Language (UCL). Use preferably [color names as specified by the Art & Architecture Thesaurus](http://vocab.getty.edu/aat/300080438) (AAT). Centroid color numbers, which refer to the appropriate color-blocks on the [Inter-Society Color Council and National Bureau of Standards (ISCC-NBS) color name charts](https://en.wikipedia.org/wiki/ISCC%E2%80%93NBS_system), are also provided by the AAT.
* Implement, as a value for the type attribute of the LIDO Term Materials/Techniques element, designates any object used to carry out the technique in order to create or modify an object, including equipment, tools, apparatus, utensils, instruments, and other things employed in any trade or used in executing a task or work.
Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2); [AAT "implements"](http://vocab.getty.edu/page/aat/300404585)
* Technique, as a value for the type attribute of the LIDO Term Materials/Techniques element, designates the manner, method, or process applied in the creation, design, or modification of an object.
Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2).
Use the most specific term for indexing that is appropriate. It is strongly recommended to take the indexing term from a published controlled vocabulary, preferably a [Linked Open Vocabulary](http://lov.okfn.org/dataset/lov/), for example the Art & Architecture Thesaurus, specifically its [Processes and Techniques hierarchy](http://www.getty.edu/vow/AATHierarchy?find=techniques&amp;logic=AND&amp;note=&amp;page=1&amp;subjectid=300053001).
For information about scientific methods by which an object was found or collected, such as field collection methods in archaeology, use the LIDO Event Method element.
* Watermark, as a value for the type attribute of the LIDO Term Materials/Techniques element, designates an identification of the watermark type or name. A watermark is a design incorporated into paper as it is made, typically a sign of the manufacturer, or a proof of authenticity for documents and banknotes. The mark is visible through transmitted light, appearing as translucent or shaded area.
Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#WatermarkIdentification); [AAT "watermarks"](http://vocab.getty.edu/aat/300028749)
It is recommended to use as indexing terms descriptors of internationally or nationally approved classifications, such as the [Watermark Information System](http://www.wasserzeichen-online.de/wzis/index.php), the [Index of watermark classes and subclasses](http://www.paperhistory.org/Standards/IPHN2.1.1_en.pdf), provided as a [Registration Standard](http://www.paperhistory.org/Standards/) of the [International Association of Paper Historians (IPH)](http://www.paperhistory.org/index.php), or the [Watermark Descriptor Tables](http://www.gravell.org/descriptors.php?&amp;&amp;offset=&amp;rectotal=&amp;query=), provided by the [Thomas L. Gravell Watermark Archive](http://www.gravell.org/).



## Identifier and Mapping Information





### Schema Source


* from schema: https://tradicional.arq.br/schema






## LinkML Source

<details>
```yaml
name: MaterialTechType
description: 'A materialidade e as técnicas de produção ou intervenção na edificação
  devem ser categorizadas segundo esta classificação.

  '
notes:
- 'The physical matter or substance from which an object is made, including any tangible
  substances, either naturally or synthetically derived, ranging from specific materials
  to types of material designated by their function. The term comprises both the media
  that are incorporated in an object and any support to which the media are applied.

  Based on [AAT "materials (matter)"](http://vocab.getty.edu/page/aat/300010358);
  [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2)

  Use the most specific term for the material that is appropriate. It is strongly
  recommended to take the indexing term from a published controlled vocabulary, preferably
  a Linked Open Vocabulary, for example the Art & Architecture Thesaurus, specifically
  its [Materials hierarchy](http://www.getty.edu/vow/AATFullDisplay?find=materials&amp;logic=AND&amp;note=&amp;page=1&amp;subjectid=300010357).'
- 'Medium, as a value for the type attribute of the LIDO Term Materials/Techniques
  element, designates the material that is applied to a support in the making of an
  object or a work of art, such as ink on paper or oil paint on canvas; often a particular
  technique or techniques are closely associated with the media. Based on [AAT "media
  (artists'' materials)"](http://vocab.getty.edu/page/aat/300163343); [CDWA Materials/Techniques](https://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#implement).

  In many forms of art, a distinction is made between materials used as the media,
  and materials used as the support. Medium is the material applied to the support.
  For example, for a drawing described as pen and brown ink and black chalk on paper,
  pen is the instrument, ink and black chalk are the media, and paper is the support.
  [Cited from Categories for the Description of Works of Art (CDWA) "Materials/Techniques"]'
- 'Support, as a value for the type attribute of the LIDO Term Materials/Techniques
  element, designates the surface material to which media are applied or a work is
  mounted, for example canvas, oak panel, laid paper, wood, copper, glass, or marble.
  For example, with paintings, drawings, prints, or photographs, the media would be
  applied to the surface of a support such as paper, wood panel, canvas, or glass
  in order to create the image. Used typically for two-dimensional works, although
  the concept may apply to any work.

  Based on [AAT "supports"](http://vocab.getty.edu/page/aat/300014844); [CDWA "Materials/Techniques"](https://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#implement)'
- 'Record a term specifying the color, tint, or hue of the material, particularly
  if color is an unusual or important characteristic of the object. [All colored impressions
  of materials of an object are meant, not just parts treated with dyestuff. The information
  refers to the overall effect of color, not only as cause of, e.g., dyeing or painting.]

  It is recommended to use internationally approved standard color charts, codes and
  terminology such as the Universal Color Language (UCL). Use preferably [color names
  as specified by the Art & Architecture Thesaurus](http://vocab.getty.edu/aat/300080438)
  (AAT). Centroid color numbers, which refer to the appropriate color-blocks on the
  [Inter-Society Color Council and National Bureau of Standards (ISCC-NBS) color name
  charts](https://en.wikipedia.org/wiki/ISCC%E2%80%93NBS_system), are also provided
  by the AAT.'
- 'Implement, as a value for the type attribute of the LIDO Term Materials/Techniques
  element, designates any object used to carry out the technique in order to create
  or modify an object, including equipment, tools, apparatus, utensils, instruments,
  and other things employed in any trade or used in executing a task or work.

  Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2);
  [AAT "implements"](http://vocab.getty.edu/page/aat/300404585)'
- 'Technique, as a value for the type attribute of the LIDO Term Materials/Techniques
  element, designates the manner, method, or process applied in the creation, design,
  or modification of an object.

  Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#RTFToC2).

  Use the most specific term for indexing that is appropriate. It is strongly recommended
  to take the indexing term from a published controlled vocabulary, preferably a [Linked
  Open Vocabulary](http://lov.okfn.org/dataset/lov/), for example the Art & Architecture
  Thesaurus, specifically its [Processes and Techniques hierarchy](http://www.getty.edu/vow/AATHierarchy?find=techniques&amp;logic=AND&amp;note=&amp;page=1&amp;subjectid=300053001).

  For information about scientific methods by which an object was found or collected,
  such as field collection methods in archaeology, use the LIDO Event Method element.'
- 'Watermark, as a value for the type attribute of the LIDO Term Materials/Techniques
  element, designates an identification of the watermark type or name. A watermark
  is a design incorporated into paper as it is made, typically a sign of the manufacturer,
  or a proof of authenticity for documents and banknotes. The mark is visible through
  transmitted light, appearing as translucent or shaded area.

  Based on [CDWA "Materials/Techniques"](http://www.getty.edu/research/publications/electronic_publications/cdwa/8materials.html#WatermarkIdentification);
  [AAT "watermarks"](http://vocab.getty.edu/aat/300028749)

  It is recommended to use as indexing terms descriptors of internationally or nationally
  approved classifications, such as the [Watermark Information System](http://www.wasserzeichen-online.de/wzis/index.php),
  the [Index of watermark classes and subclasses](http://www.paperhistory.org/Standards/IPHN2.1.1_en.pdf),
  provided as a [Registration Standard](http://www.paperhistory.org/Standards/) of
  the [International Association of Paper Historians (IPH)](http://www.paperhistory.org/index.php),
  or the [Watermark Descriptor Tables](http://www.gravell.org/descriptors.php?&amp;&amp;offset=&amp;rectotal=&amp;query=),
  provided by the [Thomas L. Gravell Watermark Archive](http://www.gravell.org/).'
from_schema: https://tradicional.arq.br/schema
rank: 1000
permissible_values:
  material:
    text: material
    meaning: term:lido00132
  medium:
    text: medium
    meaning: term:lido00513
  support:
    text: support
    meaning: term:lido00514
  color_name:
    text: color_name
    meaning: term:lido00479
  implement:
    text: implement
    meaning: term:lido00248
  technique:
    text: technique
    meaning: term:lido00131
  watermark:
    text: watermark
    meaning: term:lido00427
  other:
    text: other

```
</details>

</div>