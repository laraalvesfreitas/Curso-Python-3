# ==================================================
# OPERADORES DE COMPARAÇÃO
# ==================================================

"""
Operadores de comparação (relacionais)

>  → maior
>= → maior ou igual
<  → menor
<= → menor ou igual
== → igual
!= → diferente

Os operadores de comparação sempre retornam:
True → verdadeiro
False → falso
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(maior)
print(maior_ou_igual)
print(menor)
print(menor_ou_igual)
print(igual)
print(diferente)


# ==================================================
# IF / ELIF / ELSE
# ==================================================

"""
if → executa um código se a condição for verdadeira.

elif → verifica outra condição caso o if seja falso.

else → executa o código caso nenhuma das condições
anteriores seja verdadeira.

if / elif / else → usados para tomar decisões
dentro do programa.
"""

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')

elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')

else:
    print(f'{segundo_valor=} é igual o {primeiro_valor=}')