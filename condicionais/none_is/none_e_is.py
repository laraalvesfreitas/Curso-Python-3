"""
NONE / IS

None → representa ausência de valor

is → verifica se é o mesmo objeto/valor None
is not → verifica se não é None

Diferente de ==, o is compara identidade do objeto,
não apenas o valor. Por isso é a forma recomendada
para comparar com None.
"""

valor = None

if valor is None:
    print('O valor é None')

if valor is not None:
    print('O valor não é None')

# Experimento: troque None por 10 e veja qual if executa.