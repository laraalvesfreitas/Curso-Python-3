nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'MEDIA: {media}')

if(media >= 9):
    print('APROVEITAMENTO A')
elif(media >= 7 ):
    print('APROVEITAMENTO B')
elif(media >= 5 ):
    print('APROVEITAMENTO C')
elif(media >= 3 ):
    print('APROVEITAMENTO D')
elif(media >= 1 ):
    print('APROVEITAMENTO E')
else:
    print('REPROVADO')