tot010 = 0
soma_imp = 0

for c in range(1,6):
    valor = int(input('Digite um valor: '))

    if(valor >= 0 and valor <=10):
        tot010 = tot010 + 1
    if(valor % 2 == 1):
            soma_imp = soma_imp + valor

print('Ao todo foram ', tot010, 'Valores entre 0 e 10')
print(f'A soma dos impares é {soma_imp}')
