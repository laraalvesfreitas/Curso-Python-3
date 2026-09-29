

lista_compras = []


while True: 

    print('[1] INSERIR')
    print('[2] APAGAR')
    print('[3] LISTAR VALORES DA LISTA')
    print('[4] SAIR')
    menu = int(input('\nSELECIONE UMA OPÇÃO '))
   

    if menu == 3:
        if not lista_compras: 
            print('LISTA VAZIA... \n')
        else: 
            print(lista_compras)

    elif menu == 4:
        print('SAINDO...')
        break

'''
Exercício em andamento
'''