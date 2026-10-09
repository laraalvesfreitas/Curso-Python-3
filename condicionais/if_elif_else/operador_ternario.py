"""
OPERADOR TERNÁRIO (CONDICIONAL DE UMA LINHA)

Operador ternário → permite escrever um if/else
simples em uma única linha.

Sintaxe:
<valor> if <condição> else <outro valor>

Também pode ser encadeado, formando vários
"elif" na mesma linha.
"""

condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

digito = 9
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('valor' if False else 'outro valor ' if False else 'fim')