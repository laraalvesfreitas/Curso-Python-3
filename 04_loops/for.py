"""
FOR - ÍNDICE
1. Sintaxe básica e range()
2. Iterável e iterador
3. continue
4. break
5. else no for
6. for aninhado
7. Projeto: jogo da palavra secreta


for → usado para percorrer valores e repetir uma ação.

range(start, stop, step)

start → valor inicial
stop → valor final (não incluído)
step → intervalo entre os valores
"""

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)


# ==================================================
# ITERÁVEL E ITERADOR
# ==================================================

"""
Iterável → pode ser percorrido, como str, list e range.

Iterador → fornece um valor por vez.

iter() → transforma um iterável em um iterador.

next() → pega o próximo valor do iterador.
"""

texto = 'Luiz'

for letra in texto:
    print(letra)


# ==================================================
# CONTINUE
# ==================================================

"""
continue → interrompe a iteração atual
e passa para a próxima.
"""

for i in range(10):

    if i == 2:
        print('i é 2, pulando...')
        continue

    print(i)


# ==================================================
# BREAK
# ==================================================

"""
break → interrompe o loop imediatamente.
"""

for i in range(10):

    if i == 8:
        print('i é 8, interrompendo...')
        break

    print(i)


# ==================================================
# ELSE NO FOR
# ==================================================

"""
else → executa quando o for termina normalmente.

Se o for for interrompido com break,
o else não será executado.
"""

for i in range(10):

    if i == 8:
        print('i é 8, seu else não executará')
        break

else:
    print('For completo com sucesso!')


# ==================================================
# FOR ANINHADO
# ==================================================

"""
For aninhado → um for dentro de outro for.

O segundo for é executado para cada repetição
do primeiro for.
"""

for i in range(10):

    for j in range(1, 3):
        print(i, j)


# ==================================================
# JOGO DA PALAVRA SECRETA
# ==================================================

"""
while True → mantém o jogo em execução.

input() → recebe uma informação do usuário.

len() → verifica a quantidade de caracteres.

in → verifica se um valor está dentro de outro.

+= → adiciona um valor à variável.

continue → volta para o início do loop.

for → percorre cada letra da palavra.

break → encerra o jogo.

if / else → verifica as condições do jogo.
"""

palavra_secreta = 'cachorro'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU, PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Você acertou na tentativa', numero_tentativas)
        break