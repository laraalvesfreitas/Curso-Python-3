"""
DESEMPACOTAMENTO - ÍNDICE
1. Introdução ao desempacotamento com *
2. Desempacotamento em chamadas de métodos e funções.


DESEMPACOTAMENTO (UNPACKING)

Permite atribuir os valores de uma lista (ou outro
iterável) diretamente a variáveis, em uma única linha.

_ → convenção usada para indicar que aquele valor
não importa e não será utilizado no código.

* → "engole" todos os valores restantes que não
foram atribuídos a uma variável específica, guardando
-os em uma lista.
"""

_, nome, *_ = ['João', 'Lara', 'Maria', 'Luisa']

print(nome)

"""
Nesse exemplo:
- o 1º valor ('João') vai para o primeiro _  → descartado
- o 2º valor ('Lara') vai para 'nome'        → usado
- os valores restantes ('Maria', 'Luisa')    → vão para
  o segundo _ como uma lista, e também são descartados

Saída: Lara
"""

# ==================================================
# 2. DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES
# ==================================================

"""
O * também pode ser usado para desempacotar um
iterável (string, lista, tupla etc.) diretamente
na chamada de uma função, passando cada item
como um argumento separado.

print(*lista) é equivalente a:
print(lista[0], lista[1], lista[2], lista[3])
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 'Luiz', 'João']
tupla = ('Python ', 'é', 'legal')
salas = [
    ['Maria', 'Helen'],
    ['Elaine'],
    ['luiz', 'João', 'Eduarda'],
]

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')