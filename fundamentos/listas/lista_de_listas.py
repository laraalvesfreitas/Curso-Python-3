"""
LISTA DE LISTAS E SEUS ÍNDICES

Uma lista pode conter outras listas (ou até
outros tipos, como tuplas) dentro dela.

Para acessar um valor, usa-se um índice para
cada "nível" da estrutura.

sala[0]    → acessa a 1ª lista interna
sala[0][1] → acessa o 2º item dentro dessa lista
"""

sala = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],
]

print(sala[0][1])      # 'Helena' → 1ª lista, índice 1
print(sala[2][2])      # 'Eduarda' → 3ª lista, índice 2
print(sala[2][3][2])   # 20 → 3ª lista, índice 3 (tupla), índice 2 da tupla