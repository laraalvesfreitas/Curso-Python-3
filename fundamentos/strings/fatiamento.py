"""
FATIAMENTO DE STRINGS

[i:f:p]

i = início
f = fim (não incluído)
p = passo

Os índices começam em 0.

Também podemos usar índices negativos.
"""

variavel = 'Olá mundo'

print(variavel[3:7])    # ' mun' (começa com um espaço)
print(variavel[::-1])   # odnum álO (passo -1 inverte a string)

# len() retorna a quantidade de caracteres
print(len(variavel))    # 9