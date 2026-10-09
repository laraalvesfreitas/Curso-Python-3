"""
ITERÁVEL E ITERADOR

Iterável → pode ser percorrido, como str, list e range.

Iterador → fornece um valor por vez.

iter() → transforma um iterável em um iterador.

next() → pega o próximo valor do iterador.
"""

texto = 'Luiz'

for letra in texto:
    print(letra)


# O que o for faz por baixo dos panos:

iterador = iter(texto)

print(next(iterador))  # L
print(next(iterador))  # u
print(next(iterador))  # i
print(next(iterador))  # z