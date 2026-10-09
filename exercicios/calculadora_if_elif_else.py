while True: 
    print('\n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Sair')


    opcao= input('Digite uma opção: ')

    if opcao == '5': 
            print('Calculadora encerrada')
            break

    num1_float = float(input('Digite o primeiro número: '))
    num2_float = float(input('Digite o segundo número: '))

    
    if opcao == '1': 
        print(f'A soma dos números é {num1_float + num2_float}' )
    elif opcao == '2':
        print(f'A subtração dos números é {num1_float - num2_float}' )
    elif opcao == '3':
        print(f'A multiplicação dos números é {num1_float * num2_float}' )
    elif opcao == '4':
        print(f'A divisão dos números é {num1_float / num2_float}' )
    else: 
        print("Você escolheu uma opção incorreta")

