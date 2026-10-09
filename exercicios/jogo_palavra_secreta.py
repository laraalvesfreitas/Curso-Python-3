"""
PROJETO: JOGO DA PALAVRA SECRETA

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