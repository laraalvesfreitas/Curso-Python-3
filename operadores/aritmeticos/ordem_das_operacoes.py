"""
ORDEM DAS OPERAÇÕES

Python segue uma ordem para realizar cálculos:

1. () → parênteses
2. ** → exponenciação
3. *, /, //, % → multiplicação, divisão,
   divisão inteira e módulo
4. +, - → adição e subtração
"""

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)

print(conta_1)  # 1024

# Passo a passo:
# (0.5 + 0.5) = 1.0 → int(1.0) = 1
# (1 + 1) ** (5 + 5) = 2 ** 10 = 1024