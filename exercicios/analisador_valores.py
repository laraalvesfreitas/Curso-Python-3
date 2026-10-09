divididos_por_5 = 0
soma = 0
valor_nulo = 0
soma_par = 0

valor = 1

for valores in range(5):
    valor_digitado = int(input('Digite um valor: '))
    soma = soma + valor_digitado
    media = soma / 5

    if valor_digitado % 5 == 0:
        divididos_por_5  += 1
    if valor_digitado == 0:
        valor_nulo += 1
    if valor_digitado % 2 == 0:
        soma_par = soma_par + valor_digitado

print(f'A soma dos números é: {soma}')
print(f'A média dos números digitados é {media}')
print(f'Números que são divididos por 5 são {divididos_por_5}')
print(f'Números com valor nulo são: {valor_nulo}')
print(f'A soma dos números pares é: {soma_par}')