"""
.FORMAT()

.format() permite inserir valores dentro de uma string,
referenciando os nomes definidos entre chaves.
"""

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c
)

print(formato)   # b=BBBBBB a=AAAAA a=AAAAA c=1.10