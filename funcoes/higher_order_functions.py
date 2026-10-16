'''
Higher Order Functions

Funções de Primeira classe

Em Python, funções de primeira classe (ou first-class functions) significam que as funções são tratadas como objetos de primeira classe. Elas possuem os mesmos direitos e usos de qualquer outro tipo de dado, como números, strings ou listas

'''

def saudacao(nome):
  return f'Olá, {nome}!'


# Atribuindo a função a uma variável (sem os parênteses)
operacao = saudacao

print(operacao('Maria'))  # Saída: Olá, Maria!

