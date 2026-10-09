"""
DESEMPACOTAMENTO (UNPACKING) NA ATRIBUIÇÃO

Permite atribuir os valores de uma lista (ou outro
iterável) diretamente a variáveis, em uma única linha.

_ → convenção usada para indicar que aquele valor
não importa e não será utilizado no código.

* → "engole" todos os valores restantes que não
foram atribuídos a uma variável específica,
guardando-os em uma lista.
"""

_, nome, *_ = ['João', 'Lara', 'Maria', 'Luisa']

print(nome)  # Lara

"""
Nesse exemplo:
- o 1º valor ('João') vai para o primeiro _  → descartado
- o 2º valor ('Lara') vai para 'nome'        → usado
- os valores restantes ('Maria', 'Luisa')    → vão para
  o segundo _ como uma lista, e também são descartados
"""

# Experimento: troque `_` por nomes de verdade e imprima todos:
# primeiro, nome, *resto = ['João', 'Lara', 'Maria', 'Luisa']
# print(primeiro, nome, resto)