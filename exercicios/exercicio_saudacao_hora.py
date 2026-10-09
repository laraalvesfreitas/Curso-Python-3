"""
EXERCÍCIO: SAUDAÇÃO DE ACORDO COM A HORA

Pergunte a hora ao usuário e exiba:

0-11  → Bom dia
12-17 → Boa tarde
18-23 → Boa noite
"""

hora_digitada = input('Que horas são agora? ')

try:
    hora_int = int(hora_digitada)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')

except:
    print('Você não digitou um número inteiro')