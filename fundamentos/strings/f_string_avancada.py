"""
F-STRING AVANÇADA

Formatação básica de strings:

s - string
d - inteiro
f - float
x ou X - hexadecimal

> - alinha à direita
< - alinha à esquerda
^ - centraliza

.2f - quantidade de casas decimais
+ - mostra o sinal do número
0 - preenche com zeros

Alinhamento, largura, sinal, preenchimento com zero
e separador de milhar podem ser combinados dentro
da f-string.

!r → mostra a representação do valor (repr),
útil para diferenciar string de outros tipos.
"""

variavel = 'ABC'

print(f'{variavel}')         # ABC
print(f'{variavel: >10}')    # alinhado à direita
print(f'{variavel: <10}.')   # alinhado à esquerda
print(f'{variavel: ^10}.')   # centralizado

print(f'{1000.4873648123746:0=+10,.1f}')   # sinal, zeros e separador de milhar

print(f'O hexadecimal de 1500 é {1500:08X}')   # 000005DC

print(f'{variavel!r}')       # 'ABC' (com as aspas)