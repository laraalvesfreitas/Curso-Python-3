valor_emprestimo = int(input("Digite o valor do emprestimo: "))
quantidade_parcelas = int(input("Em quantas parcelas gostaria de pagar? "))
juros = (valor_emprestimo * 20) / 100
valor_total= juros + valor_emprestimo
valor_parcela = valor_total / quantidade_parcelas

print(f'Você pagara {quantidade_parcelas} parcelas de  {valor_parcela} e o valor total do emprestimo é de {valor_total}')
