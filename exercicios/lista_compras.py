

lista_compras = []


while True: 
    print('[1] INSERIR\t [2] APAGAR\t [3] LISTAR VALORES DA LISTA\t [4] SAIR\t')

    try: 
        menu = int(input('SELECIONE UMA OPÇÃO '))
    


        if menu == 1:
            valor = input('Valor: ')
            lista_compras.append(valor)
            
        elif menu == 2: 
            indice_apagar = int(input('Digite o indice para apagar: '))
            
            if indice_apagar <0 or indice_apagar >= len(lista_compras):
                print('Não foi possivel apagar. Índice inexistente ')
                continue
            else:
                valor_removido =  lista_compras.pop(indice_apagar)
                print ('Valor removido', valor_removido)

        elif menu == 3:
            if not lista_compras: 
                print('LISTA VAZIA... \n')
            else: 
                for indice,valor in enumerate(lista_compras):
                    print(indice,valor)

        elif menu == 4:
            print('SAINDO...')
            break
        else:
            print('Opção inválida')
    except ValueError:
         print('Digite apenas números.')
         continue