"""
EXERCÍCIO: NÚMERO PAR OU ÍMPAR

Peça ao usuário para digitar um número inteiro.
Informe se o número é par ou ímpar.
Caso não seja um número inteiro, informe isso.

% (módulo) → retorna o resto da divisão.
Resto 0 → número par. Resto diferente de 0 → ímpar.
"""

numero_digitado = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_digitado)

    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é ímpar')

except:
    print('Você não digitou um número inteiro')