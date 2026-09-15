"""
STRINGS - ÍNDICE
1. Aspas simples e duplas
2. Escape de caracteres
3. Raw string (r"")
4. Fatiamento de strings
5. Exercício: trabalhando com strings (input do usuário)
6. Exercício: classificação por tamanho do nome
7. Método zfill()
8. Concatenação e repetição de strings
9. f-string básica
10. .format()
11. Formatação com operador %
12. f-string avançada (alinhamento, precisão, !r)


STRINGS

str -> string -> texto

Strings são textos que estão dentro de aspas.
"""


# ==================================================
# ASPAS SIMPLES
# ==================================================

print('Luiz Otávio')

print(1, 'Luiz "Otávio"')


# ==================================================
# ASPAS DUPLAS
# ==================================================

print("Luiz Otávio")

print(2, "Luiz 'Otávio'")


# ==================================================
# ESCAPE
# ==================================================

"""
\ → usado para "escapar" um caractere especial,
permitindo usar aspas duplas dentro de uma string
que também usa aspas duplas.
"""

print("Luiz \"Otávio\"")


# ==================================================
# RAW STRING (r"")
# ==================================================

"""
r"" → ignora os caracteres de escape,
imprimindo a string exatamente como foi digitada.
"""

print(r"Luiz \"Otávio\"")


# ==================================================
# FATIAMENTO DE STRINGS
# ==================================================

"""
Fatiamento de strings

[i:f:p]

i = início
f = fim
p = passo

Os índices começam em 0.

Também podemos usar índices negativos.
"""

variavel = 'Olá mundo'

print(variavel[3:7])

# len() retorna a quantidade de caracteres
print(len(variavel))


# ==================================================
# EXERCÍCIO: TRABALHANDO COM STRINGS
# ==================================================

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')


# ==================================================
# EXERCÍCIO: CLASSIFICAÇÃO POR TAMANHO DO NOME
# ==================================================

"""
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


# ==================================================
# MÉTODO ZFILL()
# ==================================================

"""
zfill() preenche uma string com zeros à esquerda
até atingir a quantidade de caracteres informada.
"""

string = '1000'

print(string.zfill(10))


# ==================================================
# CONCATENAÇÃO E REPETIÇÃO DE STRINGS
# ==================================================

concatenacao = 'Luiz' + ' ' + 'Otávio'

print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'

print(a_dez_vezes)
print(tres_vezes_luiz)


# ==================================================
# F-STRING BÁSICA
# ==================================================

"""
f-string permite inserir variáveis dentro de textos.
"""

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


# ==================================================
# .FORMAT()
# ==================================================

"""
.format() permite inserir valores dentro de uma string,
referenciando os nomes definidos entre chaves.
"""

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


# ==================================================
# FORMATAÇÃO COM OPERADOR %
# ==================================================

"""
%s → string
%d → inteiro
%i → inteiro
%f → float
%x / %X → hexadecimal
"""

nome = 'Luiz'
preco = 1000.95897643

variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))


# ==================================================
# F-STRING AVANÇADA
# ==================================================

"""
Alinhamento, largura, sinal, preenchimento com zero
e separador de milhar podem ser combinados dentro
da f-string.

!r → mostra a representação do valor (repr),
útil para diferenciar string de outros tipos.
"""

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')

print(f'{1000.4873648123746:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')