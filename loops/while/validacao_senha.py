"""
PROJETO: VALIDAÇÃO DE SENHA

Loop continua enquanto a senha digitada
for diferente da senha salva.

Atenção: sem um limite de tentativas,
esse loop pode rodar infinitamente.

A senha salva é '123456'.
"""

senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')