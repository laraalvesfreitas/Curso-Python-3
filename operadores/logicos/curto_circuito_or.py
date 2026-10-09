"""
CURTO-CIRCUITO COM OR

No or, quando o Python encontra um valor Truthy,
ele pode parar a avaliação, pois o resultado já será
verdadeiro.

Também pode ser usado para definir um valor padrão.

Experimento: aperte Enter sem digitar nada.
"""

senha = input('Senha: ') or 'Sem senha'

print(senha)