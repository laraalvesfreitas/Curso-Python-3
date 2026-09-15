"""
VARIÁVEIS - ÍNDICE
1. Regras e convenções (PEP8)
2. Exemplo simples de atribuição
3. Exemplo com múltiplas variáveis
4. input() e conversão de tipos


VARIÁVEIS

Variáveis são usadas para salvar algo na memória do computador.

PEP8: inicie variáveis com letras minúsculas.
Pode usar números e underline _.

O sinal de = é o operador de atribuição.
Ele é usado para atribuir um valor a um nome (variável).

Uso:
nome_variavel = expressão

Exemplos:
nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')

print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)
"""

nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18

print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)


# ==================================================
# EXEMPLO COM MÚLTIPLAS VARIÁVEIS
# ==================================================

nome = 'Mariana'
sobrenome = 'Rodriguez'
idade = 25
ano_nascimento = 2026 - idade
maior_de_idade = idade >= 18
altura_metros = 1.62

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)


# ==================================================
# INPUT() E CONVERSÃO DE TIPOS
# ==================================================

"""
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