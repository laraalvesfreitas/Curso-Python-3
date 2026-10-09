"""
VALORES FALSY

Falsy → valores que são considerados falsos pelo Python.

Principais valores Falsy:

0
0.0
''
False
None

Qualquer outro valor geralmente é considerado Truthy.
"""

print(bool(0))       # False
print(bool(0.0))     # False
print(bool(''))      # False
print(bool(False))   # False
print(bool(None))    # False

print(bool(1))       # True
print(bool('a'))     # True
print(bool(' '))     # True (espaço não é vazio)