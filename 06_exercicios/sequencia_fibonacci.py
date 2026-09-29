anterior_1 = 0
anterior_2 = 1

print(anterior_1)
print(anterior_2)

for numeros in range(15):
    atual = anterior_1 + anterior_2
    print(atual)
    anterior_1 = anterior_2
    anterior_2 = atual
    