bangu = int(input('Quantos gols bangu fez?'))
madureira = int(input('Quantos gols madureira fez?'))

diferenca =  abs(bangu - madureira)
print(F'A DIFERENÇA DE GOLS FOI {diferenca}')

if (diferenca == 0):
    print('STATUS: EMPATE')
elif (diferenca >= 1 and diferenca<5):
    print('STATUS: PARTIDA NORMAL')
else:
    print('GOLEADA')
