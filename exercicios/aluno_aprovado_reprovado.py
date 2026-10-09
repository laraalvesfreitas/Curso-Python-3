print( 20 * "-")
print('ESCOLA VILA LIMOEIRO')
print( 20 * "-")

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print( 20 * "-")
print('MÉDIA')
print(media)

if(media >= 7):
    print('Aluno aprovado')
elif(media >= 5 and media <7):
    print('Aluno em recuperação.')
else: 
    print('Aluno reprovado')