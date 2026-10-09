"""
INSERT

insert(indice, valor) → adiciona um item
no índice escolhido, empurrando os demais.
"""

lista = [10, 20, 30, 40]

lista.insert(1, 15)

print(lista)   # [10, 15, 20, 30, 40]