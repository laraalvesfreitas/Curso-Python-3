"""
CONTINUE E BREAK COMBINADOS

continue → pula a iteração atual e volta para a condição do while.
break → interrompe o loop imediatamente.
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')