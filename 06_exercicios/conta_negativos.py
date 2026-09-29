contador = 1
total_numeros_negativos = 0

while True:
    numero = int(input('Digite um número: '))
    contador += 1

    if numero <= 0:
        total_numeros_negativos += 1

      
    if contador >5:
        break

print(f'Foram digitados {total_numeros_negativos} números negativos') 