"""
FLAG (BANDEIRA) PARA CONTROLE DE FLUXO

Flag → variável usada para marcar se algo aconteceu.

Aqui, 'passou_no_if' começa como None (nenhum evento
aconteceu ainda) e só recebe True se a condição
dentro do if for verdadeira.

Isso permite checar depois, em outro ponto do código,
se aquele bloco chegou a ser executado.

Experimento: troque condicao para True e compare a saída.
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