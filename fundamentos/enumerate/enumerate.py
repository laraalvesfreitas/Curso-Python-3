"""
ENUMERATE - ÍNDICE
1. enumerate() com índices e valores


ENUMERATE

enumerate() enumera iteráveis, retornando o índice
e o valor de cada item ao mesmo tempo.

Muito útil quando você precisa saber a posição
do item durante a iteração, sem precisar controlar
um contador manualmente.
"""

frutas = ['Banana', 'uva', 'kiwi']

frutas.append('Maça')

for indice, fruta in enumerate(frutas):
    print(indice, fruta)