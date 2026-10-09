"""
EXEMPLO COM MÚLTIPLAS VARIÁVEIS

Variáveis podem guardar tipos diferentes (str, int, bool, float)
e podem ser usadas para calcular o valor de outras.
"""

nome = 'Mariana'
sobrenome = 'Rodriguez'
idade = 25
ano_nascimento = 2026 - idade
maior_de_idade = idade >= 18
altura_metros = 1.62

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)       # 2001
print('É maior de idade?', maior_de_idade)        # True
print('Altura em metros:', altura_metros)