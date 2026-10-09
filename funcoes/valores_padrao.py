"""
VALORES PADRÃO PARA PARÂMETROS

Ao definir uma função, os parâmetros podem ter valores padrão.
Se o valor não for enviado, o valor padrão será usado.

Parâmetros com valor padrão devem vir depois
dos parâmetros sem valor padrão.
"""

def subtrair(x, y, z=None):

    if z is not None:
        print(f'{x = } {y = } {z = }', '|', ' x - y - z = ', x - y - z)
    else:
        print(f'{x = } {y = }', '|', ' x - y = ', x - y)


print('SUBTRAÇÃO')

subtrair(15, 6)              # z usa o valor padrão (None)
subtrair(y=12, x=22, z=9)    # z informado