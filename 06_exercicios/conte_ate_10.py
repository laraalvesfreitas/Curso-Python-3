# contador = 10

# while contador > 0:
#     print(contador)
#     contador -=  2

# print("Fim da contagem")


# contador_soma = 0

# while contador_soma <= 10:
#     print(contador_soma)
#     contador_soma +=  2

# print("Fim da contagem")


numero = int(input('Quer contar até quanto? '))
salto = int(input('Qual será o valor do salto? '))

contador = 0

while contador <= numero:
    print(contador)
    contador += salto
    