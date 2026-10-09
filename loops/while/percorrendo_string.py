"""
PERCORRENDO STRING COM ÍNDICE MANUAL

Diferente do for, o while não percorre a string
automaticamente — é preciso controlar o índice
manualmente com uma variável (indice += 1).
"""

nome = 'Lara Alves'

indice = 0
nome_formatado = ''

while indice < len(nome):
    letra = nome[indice]
    nome_formatado += f'{letra}*'
    indice += 1

print(nome_formatado)