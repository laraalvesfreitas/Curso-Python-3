"""
WHILE - ÍNDICE
1. Sintaxe básica e loop com input
2. Contador simples
3. continue e break combinados
4. while aninhado
5. Percorrendo string com while (índice manual)
6. Projeto: calculadora com while
7. while / else
8. Projeto: letra mais frequente em um texto
9. Projeto: validação de senha


WHILE → enquanto

Executa uma ação enquanto uma condição for verdadeira.

Loop infinito → quando o código não tem fim.
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break


# ==================================================
# CONTADOR SIMPLES
# ==================================================

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')


# ==================================================
# CONTINUE E BREAK COMBINADOS
# ==================================================

"""
continue → pula a iteração atual e volta para a condição do while.
break → interrompe o loop imediatamente.
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')


# ==================================================
# WHILE ANINHADO
# ==================================================

"""
While aninhado → um while dentro de outro while.

O while interno é executado por completo
para cada repetição do while externo.
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')


# ==================================================
# PERCORRENDO STRING COM ÍNDICE MANUAL
# ==================================================

"""
Diferente do for, o while não percorre a string
automaticamente — é preciso controlar o índice
manualmente com uma variável (indice += 1).
"""

nome = 'Lara Alves'

indice = 0
nome_formatado = ''

while indice < len(nome):
    letra = nome[indice]
    nome_formatado += f'{letra}*'
    indice += 1

print(nome_formatado)


# ==================================================
# PROJETO: CALCULADORA COM WHILE
# ==================================================

"""
while True → mantém a calculadora rodando até o usuário sair.

try/except → trata erro quando o valor digitado não é numérico.

continue → volta para o início do loop em caso de erro de validação.

startswith() → verifica se a resposta do usuário começa com 's'.
"""

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador(+-*/): ')

    num1_float = 0
    num2_float = 0
    numeros_validos = None

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Veja o resultado da soma Abaixo')

    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)

    sair = input('Quer [S]air: ').lower().startswith('s')

    if sair is True:
        break


# ==================================================
# WHILE / ELSE
# ==================================================

"""
else → executado quando o while termina normalmente.

Se o while for interrompido com break,
o else não será executado.
"""

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')

print('Fora do while.')


# ==================================================
# PROJETO: LETRA MAIS FREQUENTE EM UM TEXTO
# ==================================================

"""
count() → conta quantas vezes um caractere aparece na string.

A cada letra percorrida, compara a frequência atual
com a maior frequência já encontrada.
"""

texto = 'No Python temos tipagem dinâmica, orientação a objetos entre outros.'

i = 0
maior_frequencia = 0
letra_mais_frequente = ''

while i < len(texto):
    letra = texto[i]

    if letra == ' ':
        i += 1
        continue

    frequencia_atual = texto.count(letra)

    if maior_frequencia < frequencia_atual:
        maior_frequencia = frequencia_atual
        letra_mais_frequente = letra

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_frequente}" que apareceu '
    f'{maior_frequencia}x'
)


# ==================================================
# PROJETO: VALIDAÇÃO DE SENHA
# ==================================================

"""
Loop continua enquanto a senha digitada
for diferente da senha salva.

Atenção: sem um limite de tentativas,
esse loop pode rodar infinitamente.
"""

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')