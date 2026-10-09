"""
DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES

O * também pode ser usado para desempacotar um
iterável (string, lista, tupla etc.) diretamente
na chamada de uma função, passando cada item
como um argumento separado.

print(*lista) é equivalente a:
print(lista[0], lista[1], lista[2], lista[3])
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 'Luiz', 'João']
tupla = ('Python ', 'é', 'legal')
salas = [
    ['Maria', 'Helen'],
    ['Elaine'],
    ['luiz', 'João', 'Eduarda'],
]

print(*lista)             # Maria Helena Luiz João
print(*string)            # A B C D
print(*tupla)             # Python  é legal
print(*salas, sep='\n')   # cada lista interna em uma linha