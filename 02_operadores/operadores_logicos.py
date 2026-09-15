# ==================================================
# OPERADORES LÓGICOS
# ==================================================

"""
Operadores lógicos → usados para combinar ou inverter
condições.

and → e
or  → ou
not → não

and → todas as condições precisam ser verdadeiras.

or → pelo menos uma condição precisa ser verdadeira.

not → inverte o resultado lógico.

Os operadores lógicos trabalham com True e False.
"""


# ==================================================
# VALORES FALSY
# ==================================================

"""
Falsy → valores que são considerados falsos pelo Python.

Principais valores Falsy:

0
0.0
''
False
None

Qualquer outro valor geralmente é considerado Truthy.
"""


# ==================================================
# AND
# ==================================================

"""
and → todas as condições precisam ser verdadeiras
para o resultado ser verdadeiro.
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# ==================================================
# CURTO-CIRCUITO COM AND
# ==================================================

"""
Curto-circuito → o Python para de avaliar as condições
assim que já consegue determinar o resultado.

No and, ao encontrar um valor Falsy, o restante
não precisa ser avaliado.
"""

print(True and False and True)
print(True and 0 and True)


# ==================================================
# OR
# ==================================================

"""
or → pelo menos uma condição precisa ser verdadeira
para o resultado ser verdadeiro.
"""

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# ==================================================
# CURTO-CIRCUITO COM OR
# ==================================================

"""
No or, quando o Python encontra um valor Truthy,
ele pode parar a avaliação, pois o resultado já será
verdadeiro.

Também pode ser usado para definir um valor padrão.
"""

senha = input('Senha: ') or 'Sem senha'

print(senha)


# ==================================================
# NOT
# ==================================================

"""
not → inverte o valor lógico.

True  → False
False → True
"""

print(not True)
print(not False)


# ==================================================
# IN E NOT IN
# ==================================================

"""
in → verifica se um valor está dentro de outro.

not in → verifica se um valor não está dentro de outro.

O resultado é True ou False.
"""

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


# ==================================================
# EXEMPLO DE RADAR
# ==================================================

"""
Operadores lógicos podem ser usados para combinar
várias condições.

O carro é multado quando:

1. Está acima da velocidade permitida.
2. Passou pelo local do radar.

and → exige que as duas condições sejam verdadeiras.
"""

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = (
    local_carro >= LOCAL_1 - RADAR_RANGE
    and local_carro <= LOCAL_1 + RADAR_RANGE
)

carro_multado_radar_1 = (
    carro_passou_radar_1 and vel_carro_pass_radar_1
)

if vel_carro_pass_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou pelo radar 1')

if carro_multado_radar_1:
    print('Carro multado no radar 1')