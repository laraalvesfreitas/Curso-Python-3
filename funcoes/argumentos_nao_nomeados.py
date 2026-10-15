'''
*args argumentos não nomeados

*args empacotamento e desempacotamento
'''

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 5, 9, 7, 6, 12, 30


soma_1 = soma(5, 2, 6, 4)
soma_2 = soma(*numeros)



print(*numeros)
print(soma_2)