"""
NONE / IS - ÍNDICE
1. None e a verificação com is / is not
2. Flag (bandeira) para controle de fluxo


NONE → representa ausência de valor

is → verifica se é o mesmo objeto/valor None
is not → verifica se não é None

Diferente de ==, o is compara identidade do objeto,
não apenas o valor — por isso é a forma recomendada
para comparar com None.
"""

valor = None

if valor is None:
    print('O valor é None')

if valor is not None:
    print('O valor não é None')


# ==================================================
# FLAG (BANDEIRA) PARA CONTROLE DE FLUXO
# ==================================================

"""
Flag → variável usada para marcar se algo aconteceu.

Aqui, 'passou_no_if' começa como None (nenhum evento
aconteceu ainda) e só recebe True se a condição
dentro do if for verdadeira.

Isso permite checar depois, em outro ponto do código,
se aquele bloco chegou a ser executado.
"""

condicao = False

passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')