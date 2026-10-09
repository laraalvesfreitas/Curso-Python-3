"""
WHILE → SINTAXE BÁSICA

while → enquanto

Executa uma ação enquanto uma condição for verdadeira.

Loop infinito → quando o código não tem fim.

Digite 'sair' para encerrar o loop.
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break