"""
DESEMPACOTAMENTO - ÍNDICE
1. Introdução ao desempacotamento com *


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