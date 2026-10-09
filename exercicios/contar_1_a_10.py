contador = 1
numero = int(input('Quer ver a tabuada de qual número? '))

while True: 
    resultado = numero * contador
    print(f' {numero} x {contador} = {resultado}')
    contador += 1

    if contador >= 11:
        break