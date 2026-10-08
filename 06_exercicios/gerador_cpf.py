import random

for eem_cpfs in range(100):


    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0,9))



    contador_regressivo = 10
    resultado = 0

    for digito in nove_digitos:
        resultado += int(digito) * contador_regressivo
            
        contador_regressivo -= 1

    resultado_multiplicado = resultado * 10
    resto_divisao = resultado_multiplicado % 11
    digito_1 = resto_divisao

    if resto_divisao > 9:
            digito_1 = 0
    else:
        digito_1 = resto_divisao


    '''
    Validação do segundo digito do cpf
    cpf = 746.824.890-70

    '''
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_d2 = 11
    resultado_d2 = 0

    for digito_2 in dez_digitos:
        resultado_d2 += int(digito_2) * contador_regressivo_d2
        contador_regressivo_d2 -= 1

    resultado_multiplicado_d2 = resultado_d2 * 10
    resto_divisao_d2 = resultado_multiplicado_d2 % 11
    digito_d2 = resto_divisao_d2

    if resto_divisao_d2 > 9:
            digito_d2 = 0
    else:
        digito_d2 = resto_divisao_d2



    cpf_validado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_d2}'
    print(cpf_validado_pelo_calculo)