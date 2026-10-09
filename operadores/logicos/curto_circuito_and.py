"""
CURTO-CIRCUITO COM AND

Curto-circuito → o Python para de avaliar as condições
assim que já consegue determinar o resultado.

No and, ao encontrar um valor Falsy, o restante
não precisa ser avaliado.

O and retorna o primeiro valor Falsy que encontrar
(ou o último valor, se todos forem Truthy).
"""

print(True and False and True)   # False
print(True and 0 and True)       # 0