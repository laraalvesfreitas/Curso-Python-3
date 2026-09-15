"""
LISTAS - ÍNDICE
1. Criando uma lista
2. Índices (positivos e negativos)
3. Alterando valores
4. append
5. insert
6. pop
7. del
8. clear
9. extend
10. + (concatenação)
11. for in com listas
12. enumerate


LISTAS EM PYTHON

Tipo: list
- Mutável
- Suporta vários valores de qualquer tipo
- Trabalha com índices e fatiamento
- Permite adicionar, alterar e remover valores

CRUD:
    Create - Criar
    Read   - Ler
    Update - Alterar
    Delete - Apagar
"""


# ==================================================
# 1. CRIANDO UMA LISTA
# ==================================================

lista = [123, True, 'Luiz Otávio', 1.2, []]

print(lista)
print(type(lista))


# ==================================================
# 2. ÍNDICES
# ==================================================

#        0      1              2    3    4
#        +----------------------------->
#       -5     -4             -3   -2   -1

lista = [123, True, 'Luiz Otávio', 1.2, []]

print(lista[2])
print(type(lista[2]))

# Índice negativo
lista[-3] = 'Maria'

print(lista)


# ==================================================
# 3. ALTERANDO VALORES
# ==================================================

lista = [10, 20, 30, 40]

lista[2] = 300

print(lista)


# ==================================================
# 4. APPEND
# Adiciona um item ao final da lista
# ==================================================

lista = [10, 20, 30, 40]

lista.append(50)

print(lista)


# ==================================================
# 5. INSERT
# Adiciona um item no índice escolhido
# ==================================================

lista = [10, 20, 30, 40]

lista.insert(1, 15)

print(lista)


# ==================================================
# 6. POP
# Remove do final ou do índice escolhido
# ==================================================

lista = [10, 20, 30, 40]

lista.pop()

print(lista)

# Podemos guardar o valor removido

lista = [10, 20, 30, 40]

ultimo_valor = lista.pop()

print(lista)
print('Removido:', ultimo_valor)

# Removendo pelo índice

lista = [10, 20, 30, 40]

ultimo_valor = lista.pop(3)

print(lista)
print('Removido:', ultimo_valor)


# ==================================================
# 7. DEL
# Apaga um índice
# ==================================================

lista = [10, 20, 30, 40]

del lista[2]

print(lista)

# Também podemos usar índice negativo

lista = [10, 20, 30, 40]

del lista[-1]

print(lista)


# ==================================================
# 8. CLEAR
# Limpa a lista
# ==================================================

lista = [10, 20, 30, 40]

lista.clear()

print(lista)


# ==================================================
# 9. EXTEND
# Estende a lista com os valores de outra lista
# ==================================================

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_a.extend(lista_b)

print(lista_a)


# ==================================================
# 10. + (CONCATENAÇÃO)
# Junta duas listas
# ==================================================

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

print(lista_c)


# ==================================================
# 11. FOR IN COM LISTAS
# ==================================================

lista = ['Maria', 'João', 'Caio']

for nome in lista:
    print(nome)


# ==================================================
# 12. ENUMERATE
# Exibe os índices e os valores da lista
# ==================================================

lista = ['Maria', 'Luiz', 'João']

for indice, nome in enumerate(lista):
    print(f'{indice} {nome}')