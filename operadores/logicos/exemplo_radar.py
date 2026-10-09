"""
EXEMPLO DE RADAR

Operadores lógicos podem ser usados para combinar
várias condições.

O carro é multado quando:

1. Está acima da velocidade permitida.
2. Passou pelo local do radar.

and → exige que as duas condições sejam verdadeiras.

Experimento: mude velocidade para 50 ou local_carro
para 200 e veja a multa deixar de acontecer.
"""

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 70
local_carro = 99

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