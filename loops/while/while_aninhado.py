"""
WHILE ANINHADO

While aninhado → um while dentro de outro while.

O while interno é executado por completo
para cada repetição do while externo.
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')