# numero = int(input('Quer contar até quanto? '))
# soma = 0

# contador = 0

# while contador <= numero:
#     print(contador)
#     contador += 1
#     soma = contador + soma

# print(F'A soma dos números é: {soma}')


soma = 0
contador = 1
maior_valor = None
menor_valor = None

while contador <= 5:
    valor = int(input(f'Digite o {contador}° valor: '))
    contador += 1
    soma = soma + valor

    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
    
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

print(f'A soma dos valores é: {soma}')
print(f'O maior valor digitado foi {maior_valor}')
print(f'O menor valor digitado foi {menor_valor}')
    