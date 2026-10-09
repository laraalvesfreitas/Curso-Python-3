"""
EXEMPLO COM CONDIÇÃO INTERMEDIÁRIA VERDADEIRA

Aqui condicao1 e condicao2 são False, então o
elif só para na condicao3 — mesmo condicao4
sendo True, ela nunca chega a ser verificada.
"""

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')

elif condicao2:
    print('Código para condição 2')

elif condicao3:
    print('Código para condição 3')

elif condicao4:
    print('Código para condição 4')

else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')