# ==================================================
# ADIÇÃO
# ==================================================

"""
+ → soma dois valores.
"""

adicao = 10 + 10

print('Adição', adicao)


# ==================================================
# SUBTRAÇÃO
# ==================================================

"""
- → subtrai um valor de outro.
"""

subtracao = 10 - 5

print('Subtração', subtracao)


# ==================================================
# MULTIPLICAÇÃO
# ==================================================

"""
* → multiplica dois valores.
"""

multiplicacao = 10 * 10

print('Multiplicação', multiplicacao)


# ==================================================
# DIVISÃO
# ==================================================

"""
/ → realiza uma divisão e retorna um número float.
"""

divisao = 10 / 3

print('Divisão', divisao)


# ==================================================
# DIVISÃO INTEIRA
# ==================================================

"""
// → realiza a divisão e retorna apenas a parte inteira
do resultado.
"""

divisao_inteira = 10 // 3

print('Divisão inteira', divisao_inteira)


# ==================================================
# EXPONENCIAÇÃO
# ==================================================

"""
** → eleva um número a uma potência.

Exemplo:
2 ** 3 = 2 × 2 × 2 = 8
"""

exponenciacao = 2 ** 10

print('Exponenciação', exponenciacao)


# ==================================================
# MÓDULO
# ==================================================

"""
% → retorna o resto da divisão.

Muito usado para verificar se um número é par ou ímpar.
"""

modulo = 55 % 2

print('Módulo', modulo)


# ==================================================
# VERIFICAR NÚMERO PAR
# ==================================================

"""
n % 2 == 0 → verifica se o número é par.

Se o resto da divisão por 2 for 0,
o número é par.
"""

print(10 % 8 == 0)

print(16 % 8 == 0)

print(10 % 2 == 0)

print(15 % 2 == 0)

print(16 % 2 == 0)


# ==================================================
# ORDEM DAS OPERAÇÕES
# ==================================================

"""
Python segue uma ordem para realizar cálculos:

1. () → parênteses
2. ** → exponenciação
3. *, /, //, % → multiplicação, divisão,
   divisão inteira e módulo
4. +, - → adição e subtração
"""

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)

print(conta_1)


# ==================================================
# CÁLCULO DO IMC
# ==================================================

"""
IMC → Índice de Massa Corporal.

Fórmula:

IMC = peso / (altura × altura)

peso → em quilogramas
altura → em metros
"""

nome = 'Maria Luiza'
altura = 1.65
peso = 63

imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é', imc)