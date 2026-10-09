"""
RETORNO DAS FUNÇÕES (return)

return → devolve um valor para quem chamou a função,
permitindo guardá-lo em uma variável ou usá-lo
em outras operações.

Sem return, a função retorna None.
"""

def soma(x, y):
    return x + y


soma1 = soma(2, 6)
soma2 = soma(3, 7)

print(soma1 + soma2)    # 18