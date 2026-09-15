"""
TIPOS DE DADOS - ÍNDICE
1. int
2. float
3. type()
4. bool


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