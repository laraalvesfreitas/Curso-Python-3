"""
PRINT COM SEP E END

sep → define o separador entre os valores impressos.
end → define o que é impresso ao final (padrão: '\n').
"""

print(12, 34, 1011, sep='', end='#')

print(56, 78, sep='-', end='\n')

# Saída:
# 123410 11#56-78
# (o primeiro print não pula linha, por isso o segundo
#  começa logo depois do #)