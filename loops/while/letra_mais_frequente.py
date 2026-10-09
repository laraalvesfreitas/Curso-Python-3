"""
PROJETO: LETRA MAIS FREQUENTE EM UM TEXTO

count() → conta quantas vezes um caractere aparece na string.

A cada letra percorrida, compara a frequência atual
com a maior frequência já encontrada.
"""

texto = 'No Python temos tipagem dinâmica, orientação a objetos entre outros.'

i = 0
maior_frequencia = 0
letra_mais_frequente = ''

while i < len(texto):
    letra = texto[i]

    if letra == ' ':
        i += 1
        continue

    frequencia_atual = texto.count(letra)

    if maior_frequencia < frequencia_atual:
        maior_frequencia = frequencia_atual
        letra_mais_frequente = letra

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_frequente}" que apareceu '
    f'{maior_frequencia}x'
)