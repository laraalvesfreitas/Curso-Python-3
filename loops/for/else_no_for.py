"""
ELSE NO FOR

else → executa quando o for termina normalmente.

Se o for for interrompido com break,
o else não será executado.

Experimento: troque o 8 por 20 e veja o else executar.
"""

for i in range(10):

    if i == 8:
        print('i é 8, seu else não executará')
        break

else:
    print('For completo com sucesso!')