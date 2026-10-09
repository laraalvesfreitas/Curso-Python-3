"""
CONTINUE

continue → interrompe a iteração atual
e passa para a próxima.
"""

for i in range(10):

    if i == 2:
        print('i é 2, pulando...')
        continue

    print(i)