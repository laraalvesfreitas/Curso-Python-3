print(20 * '-')
print(20 * '-')

print('|                  MENU          |')
print(20 * '-')
print(20 * '-')
print('|  [1]          DE 1 A 10        |')
print('|  [2]          DE 10 A 1        |')
print('|  [3]             SAIR          |')

print(20 * '-')
print(20 * '-')

contador = 1

while True: 
    resposta = int(input(''))

    if resposta == 1:

        contador = 1
        while contador <=  10:
            print(contador)
            contador = contador + 1
            
    elif resposta == 2:
        contador = 10
        while contador >= 1:
            print(contador)
            contador -= 1

    elif resposta == 3:
        print('SAINDO')
        break
    else:
        print('Digite uma opção válida')
        resposta = int(input(''))
