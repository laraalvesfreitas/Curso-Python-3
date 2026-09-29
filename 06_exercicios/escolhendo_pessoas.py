homem_cast = 0
mulher_loir = 0

while True: 

    continuar = ('QUER CONTINUAR? [S]/[N]')

    sexo = input('Digite o seu sexo: ')
    idade = int(input('Digite a sua idade: '))

    print(10 * '-')
    
    print('[1] PRETO')
    print('[2] CATANHO')
    print('[3] LOIRO')
    print('[4] RUIVO')
    cabelo =  input('Cor do cabelo: ')
    

    if sexo == 'Masculino' and (idade >= 18) and cabelo == '2':
        homem_cast += 1
    if sexo == 'Feminino' and (idade >= 25)   and (idade <= 30) and cabelo == '3':
        mulher_loir += 1

    
    continuar = input ('QUER CONTINUAR? [S]/[N]')
    if continuar == 'N':
        break

print(f'Total de homens com mais de 18 anos e cabelos castanhos {homem_cast}')
print(f'Total de mulheres entre 25 e 30 anos e cabelos loiros {mulher_loir}')