"""
FORMATAÇÃO COM OPERADOR %

%s → string
%d → inteiro
%i → inteiro
%f → float
%x / %X → hexadecimal
"""

nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)   # Luiz, o preço é R$1000.96

print('O hexadecimal de %d é %08X' % (1500, 1500))   # O hexadecimal de 1500 é 000005DC