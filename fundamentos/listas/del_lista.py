"""
DEL

del → apaga um índice da lista.
Diferente do pop, não devolve o valor removido.
"""

lista = [10, 20, 30, 40]

del lista[2]

print(lista)   # [10, 20, 40]


# Também podemos usar índice negativo

lista = [10, 20, 30, 40]

del lista[-1]

print(lista)   # [10, 20, 30]