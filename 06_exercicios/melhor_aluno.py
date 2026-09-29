print('ESCOLA SANTA PACIENCIA: ')
print(20 * '-')


quantidade_alunos = int(input('Quantos alunos a turma tem? '))


aluno = 1
melhor_nota = 0
nome_melhor_aluno = None

while(aluno <= quantidade_alunos):
    print(f'ALUNO: {aluno}')
    nome_aluno = input('Nome do aluno: ')
    nota_aluno = float(input(f'Digite a nota do {nome_aluno}: '))
    if(nota_aluno >= melhor_nota):
        melhor_nota = nota_aluno
        nome_melhor_aluno = nome_aluno
    aluno += 1
    print(20 * '-')

if nome_melhor_aluno is not None:
    print(f'O melhor aproveitamento foi de {nome_melhor_aluno} com a nota {melhor_nota}')
else:
    print(f'Nenhum aluno cadastrado')


