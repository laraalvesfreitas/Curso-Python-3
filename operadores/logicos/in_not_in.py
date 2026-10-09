"""
IN E NOT IN

in → verifica se um valor está dentro de outro.

not in → verifica se um valor não está dentro de outro.

O resultado é True ou False.
"""

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

print(encontrar not in nome)   # o inverso do in