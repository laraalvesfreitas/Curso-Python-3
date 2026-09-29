print('CONTAGEM INTELIGENTE ')
print(20 * '-')


inicio = int(input('Inicio: '))
final = int(input('Final: '))
contador = inicio

print(20 * '-')
print('CONTANDO ')
print(20 * '-')

if final > inicio:
    contador = inicio
    while contador <= final:
        print(f'{contador}.. ')
        contador += 1

else:
    contador = inicio
    while contador >= final:
        print(f'{contador}.. ')
        contador = contador - 1