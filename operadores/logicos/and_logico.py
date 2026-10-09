"""
AND

and → todas as condições precisam ser verdadeiras
para o resultado ser verdadeiro.

Digite E e a senha 123456 para entrar.
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')