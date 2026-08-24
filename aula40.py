'''Calculadora com while'''

while True: 

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador(+-*/): ')
    
    num1_float = 0
    num2_float = 0
    numeros_validos = None


    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    print('Veja o resultado da soma Abaixo')

    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)



    sair = input('Quer [S]air: ').lower().startswith('s')

    if sair is True: 
        break
