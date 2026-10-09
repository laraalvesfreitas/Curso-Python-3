"""
ORDEM DE VERIFICAÇÃO DAS CONDIÇÕES

O elif verifica as condições na ordem.
Quando uma condição é verdadeira, as próximas
não são verificadas (mesmo que também sejam True).

Aqui todas são True, mas só a primeira executa.
"""

condicao1 = True
condicao2 = True
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