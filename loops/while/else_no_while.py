"""
WHILE / ELSE

else → executado quando o while termina normalmente.

Se o while for interrompido com break,
o else não será executado.

Experimento: troque o espaço em 'Valor qualquer' por outro
caractere e veja o else executar.
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