'''
Introdução as funções (def) em python

Funções são trechos de código usados para replicar determinada ação ao longo do código
Elas podem receber valores parâmetros (argumentos) e retornar um valor específico
Por padrão funçoes python retornam none (nada)

'''

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Maria')

'''
Argumentos nomedados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    print(f'{x = } {y = } {z = }', '|',' x + y + z= ' ,x + y + z)

print('\nSOMA')

soma(1,2,5)
soma(y=2, x=1, z= 9)


'''
Valores padrão para  parêmetros
Ao definir uma função, os parêmtros podem ter valores padrão. 
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado 
'''

def subtrair(x, y, z= None):

    if z is not None:
        print(f'{x = } {y = } {z = }', '|',' x - y - z= ' ,x - y - z)
    else:
        print(f'{x = } {y = }', '|',' x - y = ' ,x - y )


print('\nSUBTRAÇÃO')

subtrair(15,6)
subtrair(y=12, x=22, z= 9)
