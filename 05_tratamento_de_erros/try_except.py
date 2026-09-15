"""
TRY/EXCEPT - ÍNDICE
1. Introdução ao try/except
2. Exercício: número par ou ímpar
3. Exercício: saudação de acordo com a hora


TRY/EXCEPT

try → tenta executar o código
except → executa quando ocorre um erro

Útil para evitar que o programa quebre quando
o usuário digita algo inesperado (ex: texto
no lugar de número).
"""

numero_str = input(
    'Vou dobrar o número que você digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')


# ==================================================
# EXERCÍCIO: NÚMERO PAR OU ÍMPAR
# ==================================================

"""
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


# ==================================================
# EXERCÍCIO: SAUDAÇÃO DE ACORDO COM A HORA
# ==================================================

"""
Pergunte a hora ao usuário e exiba:

0-11  → Bom dia
12-17 → Boa tarde
18-23 → Boa noite
"""

hora_digitada = input('Que horas são agora? ')

try:
    hora_int = int(hora_digitada)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')

except:
    print('Você não digitou um número inteiro')