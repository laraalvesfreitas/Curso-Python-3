"""
IMPRECISÃO DE PONTO FLUTUANTE

Operações com float podem gerar resultados com
pequenos erros de arredondamento (ex: 0.1 + 0.2
não dá exatamente 0.3 internamente).

O módulo decimal resolve isso, representando
os números com precisão exata, ideal para cálculos
financeiros ou onde a exatidão é importante.
"""

import decimal

# Com float, o erro aparece:
print(0.1 + 0.2)   # 0.30000000000000004

# Com Decimal, o resultado é exato:
numero_1 = decimal.Decimal('0.5')
numero_2 = decimal.Decimal('0.2')
soma = numero_1 + numero_2

print(f'A soma dos números é {soma}')   # 0.7
print(round(soma, 2))                   # 0.70