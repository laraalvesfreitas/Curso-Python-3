"""
INPUT() E CONVERSÃO DE TIPOS

input() recebe dados digitados pelo usuário.

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

Os valores recebidos pelo input() são sempre textos (str).
int() converte o texto para número inteiro.
"""

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# Experimento: tire o int() e some direto numero_1 + numero_2.
# Digitando 2 e 3, o resultado será '23' (texto concatenado).