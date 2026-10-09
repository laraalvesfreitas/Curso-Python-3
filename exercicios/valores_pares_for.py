valor = int(input('Digite um valor: '))

if valor % 2 == 1:
   valor = valor - 1

for c in range(valor,0, -2):
    print(c)