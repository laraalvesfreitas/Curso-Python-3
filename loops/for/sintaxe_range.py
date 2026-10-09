"""
FOR → SINTAXE BÁSICA E RANGE()

for → usado para percorrer valores e repetir uma ação.

range(start, stop, step)

start → valor inicial
stop → valor final (não incluído)
step → intervalo entre os valores
"""

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)