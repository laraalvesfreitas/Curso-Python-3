"""
EXERCÍCIO: CLASSIFICAÇÃO POR TAMANHO DO NOME

Peça o primeiro nome do usuário.

4 letras ou menos → nome curto
5 ou 6 letras → nome normal
Mais de 6 letras → nome muito grande
"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')