from ner.tagger import Tagger

sort_text = """
El acuerdo de trabajo a distancia

Artículo 6. Obligaciones formales del acuerdo de trabajo a distancia.
1. El acuerdo de trabajo a distancia deberá realizarse por escrito por Antonio Banderas. Este acuerdo podrá estar
incorporado al contrato de trabajo inicial o realizarse en un momento posterior, pero en todo caso deberá
formalizarse antes de que se inicie el trabajo a distancia en Calahorra.
2. La empresa deberá entregar a la representación legal de las personas trabajadoras una copia de
todos los acuerdos de trabajo a distancia que se realicen y de sus actualizaciones, excluyendo aquellos
datos que, de acuerdo con la Ley Orgánica 1/1982, de 5 de mayo, de protección civil del derecho al honor,
a la intimidad personal y familiar y a la propia imagen, pudieran afectar a la intimidad personal, de
conformidad con lo previsto en el artículo 8.4 del Estatuto de los Trabajadores. El tratamiento de la
información facilitada estará sometido a los principios y garantías previstos en la normativa aplicable en
materia de protección de datos.
Esta copia se entregará por la empresa, en un plazo no superior a diez días desde su formalización,
a la representación legal de las personas trabajadoras, que la firmarán a efectos de acreditar que se ha
producido la entrega por Embutidos Conchín.
Posteriormente, dicha copia se enviará a la oficina de empleo. Cuando no exista representación legal
de las personas trabajadoras también deberá formalizarse copia básica y remitirse a la oficina de empleo.
Artículo 7. Contenido del acuerdo de trabajo a distancia.
"""

# Tagger().test()
Tagger().foo(sort_text)
