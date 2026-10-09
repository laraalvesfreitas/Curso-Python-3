"""
ENUMERATE

enumerate() → exibe os índices e os valores da lista
ao mesmo tempo.
"""

lista = ['Maria', 'Luiz', 'João']

for indice, nome in enumerate(lista):
    print(f'{indice} {nome}')

# Saída:
# 0 Maria
# 1 Luiz
# 2 João