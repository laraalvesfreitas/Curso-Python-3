"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_digitado = input('Digite um número inteiro: ')

# try: 
#     numero_inteiro = int(numero_digitado)

#     if (numero_inteiro % 2 == 0):
#         print(f'{numero_inteiro} é par')
#     else:
#         print(f'{numero_inteiro} é impar')

# except:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_digitada = input('Que horas é agora? ')
hora_int = int(hora_digitada)

if hora_int <11 :
    print('Bom dia!')
elif hora_int < 17:
    print('Boa tarde!')
else: 
    print('Boa noite!')




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite o seu primeiro nome: ')
# tamanho_nome = len(nome)

# print(len(nome))

# if tamanho_nome <4:
#     print("Seu nome é curto")
# elif tamanho_nome <6:
#     print("Seu nome é normal")
# else: 
#     print("Seu nome é muito grande")


    