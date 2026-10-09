"""
COMPARANDO VALORES DIGITADOS (IF / ELIF / ELSE)

if → executa um código se a condição for verdadeira.

elif → verifica outra condição caso o if seja falso.

else → executa o código caso nenhuma das condições
anteriores seja verdadeira.

if / elif / else → usados para tomar decisões
dentro do programa.

Atenção: o input() sempre retorna str. Comparar strings
é feito caractere por caractere, não pelo valor numérico.
Por isso '10' > '9' dá False (o '1' vem antes do '9').
Para comparar como números, converta com int() ou float().
"""

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')

elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')

else:
    print(f'{segundo_valor=} é igual o {primeiro_valor=}')

# Experimento: digite 10 e 9 e veja o resultado.
# Depois converta os dois valores com int() e rode de novo.