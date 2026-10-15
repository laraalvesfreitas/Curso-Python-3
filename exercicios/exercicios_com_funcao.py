'''
Crie uma função que  multiplica todos os argumentos não nomeados recebidos, retorne o valor para uma variável e mostre o valor da variável
'''


def multiplicar(*args):
    total = 1
    
    for numero in args:
        total *= numero 
    return total

total_multiplicacao = multiplicar(1, 9, 28, 30, 10)

print(total_multiplicacao)

'''
Crie uma função que retorna se o número é par ou ímpar. 
'''

def par_impar(numero):
    if numero % 2 == 0:
        return 'Este número é par'
    
    return 'Este número é ímpar'

resultado = par_impar(3)

print(resultado)