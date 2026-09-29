numero = int(input('Digite um número: '))
repetir = input('Quer continuar? ')

contador = numero
fatorial = 1



while True:
        fatorial = fatorial * contador
        contador -= 1
        if contador < 1:
            break

print(f'O valor do fatorial de {numero} é  {fatorial}')

