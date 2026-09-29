nome_func = input('Nome do funcionário: ')
salario_func = float(input('Salário do funcionário: '))
depentes_func = int(input('Quantidade de dependentes: '))
novo_salario = 0

match depentes_func:
    case 0:
        novo_salario = salario_func + (salario_func* 5 /100)
    case 1| 2| 3:
        novo_salario = salario_func + (salario_func * 10 / 100)
    case 4| 5| 6: 
        novo_salario = salario_func + (salario_func * 15 / 100)
    case _:
        novo_salario = salario_func + (salario_func * 18 / 100)
print(f'O novo salário de {nome_func} será R${novo_salario}')