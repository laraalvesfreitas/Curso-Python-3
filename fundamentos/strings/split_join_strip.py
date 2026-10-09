"""
SPLIT, JOIN E STRIP

split() → divide uma string em uma lista,
          usando o separador informado.

join()  → une os itens de uma lista em uma
          única string, usando o separador
          informado antes do método.

strip() → remove espaços em branco (ou outros
          caracteres) do início e do fim da string.
"""

frase = 'Olha só que   , função legal.         '

lista_frases_sem_edicao = frase.split(',')

lista_frases_com_edicao = []

for trecho in lista_frases_sem_edicao:
    lista_frases_com_edicao.append(trecho.strip())

print(lista_frases_com_edicao)   # ['Olha só que', 'função legal.']

frases_unidas = '-'.join(lista_frases_com_edicao)
print(frases_unidas)             # Olha só que-função legal.