"""
CÁLCULO DO IMC

IMC → Índice de Massa Corporal.

Fórmula:

IMC = peso / (altura × altura)

peso → em quilogramas
altura → em metros
"""

nome = 'Maria Luiza'
altura = 1.65
peso = 63

imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é', imc)