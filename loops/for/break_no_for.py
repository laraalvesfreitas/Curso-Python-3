"""
BREAK

break → interrompe o loop imediatamente.
"""

for i in range(10):

    if i == 8:
        print('i é 8, interrompendo...')
        break

    print(i)