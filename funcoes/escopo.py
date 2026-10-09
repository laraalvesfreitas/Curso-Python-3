"""
ESCOPO DE FUNÇÕES EM PYTHON

Escopo → local onde aquele código pode ser alcançado.

Escopo global → alcançável por todo o código.
Escopo local → só nomes do mesmo local podem ser alcançados.

Não temos acesso a nomes de escopos internos
nos escopos externos.

global → faz uma variável do escopo externo ser
a mesma do escopo interno.

Experimento: descomente os `global` e veja o que muda.
"""

x = 1
y = ''

def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global y
        x = 11
        y = 2
        print(x, y)

    print(x)
    outra_funcao()


print(x)
escopo()
print(x)

# Saída (com os global comentados):
# 1
# 10
# 11 2
# 1