"""
FOR ANINHADO

For aninhado → um for dentro de outro for.

O segundo for é executado por completo
para cada repetição do primeiro for.
"""

for i in range(10):

    for j in range(1, 3):
        print(i, j)

# Saída: (0 1) (0 2) (1 1) (1 2) (2 1) (2 2) ... (9 1) (9 2)