"""
POP

pop() → remove do final ou do índice escolhido
e devolve o valor removido.
"""

lista = [10, 20, 30, 40]

lista.pop()

print(lista)   # [10, 20, 30]


# Podemos guardar o valor removido

lista = [10, 20, 30, 40]

ultimo_valor = lista.pop()

print(lista)                  # [10, 20, 30]
print('Removido:', ultimo_valor)   # 40


# Removendo pelo índice

lista = [10, 20, 30, 40]

ultimo_valor = lista.pop(3)

print(lista)                  # [10, 20, 30]
print('Removido:', ultimo_valor)   # 40