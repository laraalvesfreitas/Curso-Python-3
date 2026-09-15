"""
IF / ELIF / ELSE - ÍNDICE
1. Sintaxe básica (if / elif / else)
2. Ordem de verificação das condições
3. If independente de outros blocos
4. Exemplo com condição intermediária verdadeira


IF / ELIF / ELSE

if → se
elif → senão se
else → senão
"""

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(12341234)

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')


# ==================================================
# ORDEM DE VERIFICAÇÃO DAS CONDIÇÕES
# ==================================================

"""
O elif verifica as condições na ordem.
Quando uma condição é verdadeira, as próximas
não são verificadas (mesmo que também sejam True).
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


# ==================================================
# IF INDEPENDENTE DE OUTROS BLOCOS
# ==================================================

"""
Um novo if pode ser criado independentemente
de qualquer if/elif/else anterior — não há
ligação entre eles.
"""

if 10 == 10:
    print('Outro if')

print('Fora do if')


# ==================================================
# EXEMPLO COM CONDIÇÃO INTERMEDIÁRIA VERDADEIRA
# ==================================================

"""
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