"""
F-STRING BÁSICA

f-string permite inserir variáveis dentro de textos.

:.2f → mostra o número com 2 casas decimais.
"""

nome = 'Luiz Otávio'
altura = 1.80
peso = 95

imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)   # Luiz Otávio tem 1.80 de altura,
print(linha_2)   # pesa 95 quilos e seu imc é
print(linha_3)   # 29.32