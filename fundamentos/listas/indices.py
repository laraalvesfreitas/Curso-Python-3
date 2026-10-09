"""
ÍNDICES (POSITIVOS E NEGATIVOS)

Os índices começam em 0.
Índices negativos contam a partir do final.
"""

#        0      1              2    3    4
#        +----------------------------->
#       -5     -4             -3   -2   -1

lista = [123, True, 'Luiz Otávio', 1.2, []]

print(lista[2])         # Luiz Otávio
print(type(lista[2]))   # <class 'str'>

# Índice negativo
lista[-3] = 'Maria'

print(lista)   # [123, True, 'Maria', 1.2, []]