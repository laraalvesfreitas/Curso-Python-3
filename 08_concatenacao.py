concatenacao = 'Luiz' + ' ' + 'Otávio'

print(concatenacao)


a_dez_vezes = 'A' * 10

tres_vezes_luiz = 3 * 'Luiz'

print(a_dez_vezes)

print(tres_vezes_luiz)



# f-string permite inserir variáveis dentro de textos

nome = 'Luiz Otávio'
altura = 1.80
peso = 95

imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# .format() permite inserir valores dentro de uma string

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c
)

print(formato)