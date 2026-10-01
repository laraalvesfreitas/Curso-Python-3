"""
TIPOS DE DADOS - ÍNDICE
1. int
2. float
3. type()
4. bool
5. Imprecisão de ponto flutuante


TIPOS DE DADOS

Python = Linguagem de programação

Tipo de tipagem:
- Dinâmica
- Forte
"""


# ==================================================
# INT
# ==================================================

"""
int -> Número inteiro

O tipo int representa qualquer número
positivo ou negativo.
"""

print(11)
print(-11)
print(0)


# ==================================================
# FLOAT
# ==================================================

"""
float -> Número com ponto flutuante
"""

print(1.1)
print(10.11)
print(0.0)
print(-1.5)


# ==================================================
# TYPE
# ==================================================

"""
A função type() mostra o tipo
que o Python inferiu ao valor.
"""

print(type(0))
print(type(1.1))
print(type(-1.1))
print(type(0.0))


# ==================================================
# BOOL
# ==================================================

"""
bool -> Booleano

Existem duas respostas possíveis:
True  -> Verdadeiro
False -> Falso
"""

print(10 == 10)  # True
print(10 == 11)  # False

print(type(True))
print(type(False))

print(type(10 == 10))
print(type(10 == 11))




# ==================================================
# IMPRECISÃO DE PONTO FLUTUANTE
# ==================================================

"""
Imprecisão de ponto flutuante

Operações com float podem gerar resultados com
pequenos erros de arredondamento (ex: 0.1 + 0.2
não dá exatamente 0.3 internamente).

O módulo decimal resolve isso, representando
os números com precisão exata, ideal para cálculos
financeiros ou onde a exatidão é importante.
"""

import decimal

numero_1 = decimal.Decimal('0.5')
numero_2 = decimal.Decimal('0.2')
soma = numero_1 + numero_2

print(f'A soma dos números é {soma}')
print(round(soma, 2))