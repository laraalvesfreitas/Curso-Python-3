"""
INTRODUÇÃO AO TRY/EXCEPT

try → tenta executar o código
except → executa quando ocorre um erro

Útil para evitar que o programa quebre quando
o usuário digita algo inesperado (ex: texto
no lugar de número).
"""

numero_str = input(
    'Vou dobrar o número que você digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')