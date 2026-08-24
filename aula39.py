nome = 'Lara Alves'
indice = 0

tamanho_nome = len(nome)

nome_formatado = ''

while indice < len(nome):
    letra = nome[indice]
    nome_formatado += f'{letra}*'
    indice += 1

print(nome_formatado)


