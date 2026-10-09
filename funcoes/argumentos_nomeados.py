"""
ARGUMENTOS NOMEADOS E NÃO NOMEADOS

Argumento nomeado → tem nome e sinal de igual (y=2).
Argumento não nomeado → recebe apenas o valor, na ordem
em que os parâmetros foram definidos.

Com argumentos nomeados, a ordem não importa.
"""

def soma(x, y, z):
    print(f'{x = } {y = } {z = }', '|', ' x + y + z = ', x + y + z)


print('SOMA')

soma(1, 2, 5)            # não nomeados
soma(y=2, x=1, z=9)      # nomeados (ordem livre)