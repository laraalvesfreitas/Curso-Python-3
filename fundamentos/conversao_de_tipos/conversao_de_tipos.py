"""
CONVERSÃO DE TIPOS (TYPE CONVERSION / TYPECASTING / COERCION)

É o ato de converter um tipo em outro.

Tipos imutáveis e primitivos:
str, int, float, bool

int()   → converte para número inteiro
float() → converte para número com ponto flutuante
bool()  → converte para True ou False
str()   → converte para texto
"""

print(int('1'), type(int('1')))      # 1 <class 'int'>

print(type(float('1') + 1))          # <class 'float'>

print(bool(' '))                     # True (espaço não é vazio)

print(str(11) + 'b')                 # 11b

# Experimento: tente int('abc') e veja o erro (ValueError).
# Esse é o erro que o try/except trata.