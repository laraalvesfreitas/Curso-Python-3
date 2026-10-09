print( 20 * "-")
print('DEPARTAMENTO DE TRANSITO')
print( 20 * "-")

ano_atual = int(input('Em qual ano estamos? '))
ano_nasc = int(input('Qual ano você nasceu? '))

print( 20 * "-")
print('STATUS')
idade = ano_atual - ano_nasc
print(f'Você tem {idade} anos')

if(idade >= 18):
    print('Você está apto para dirigir')
else:
    print('Você não está apto a dirigir')

print( 20 * "-")
