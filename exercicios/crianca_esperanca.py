print( 20 * "-")
print('CRIANÇA ESPERANÇA')
print( 20 * "-")

print('MUITO OBRIGADA POR AJUDAR')
print('[1] PARA DOAR R$10 ')
print('[2] PARA DOAR R$25 ')
print('[3] PARA DOAR R$50 ')
print('[4] PARA DOAR OUTROS VALORES ')
print('[5] PARA CANCELAR ')

doacao = int(input('Digite uma opção: '))

if doacao == 1:
    print('Sua doação foi de 10 reais')
elif doacao == 2:
    print('Sua doação foi de 25 reais')
elif doacao == 3:
    print('Sua doação foi de 50 reais')
elif doacao == 4:
    valor = int(input('Digite o valor que deseja doar: '))
    print(f'Sua doação foi de {valor} reais.')
elif doacao == 5:
    print('Operação cancelada')
else:
    print('Opção invalida')




