

contador = 1
conversao_realizadas = int(input('Quantas conversões serão realizadas? '))

while contador <= conversao_realizadas :
    valor_real = float(input('Digite o valor em R$ : '))
    conversao = (valor_real / 5.16 )
    print(f'O valor convertido é: R$ {conversao:.2f}')
    contador += 1
