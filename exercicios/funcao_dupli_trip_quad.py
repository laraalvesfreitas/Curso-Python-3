# '''
#  Crie funçôes que duplicam, triplicam e quadriplicam o número recebido como parâmetro
#  '''

def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quaduplica = criar_multiplicador(4)

num_informado = int(input('Digite um número: '))

print(f'Número informado {num_informado} duplicado: {duplica(num_informado)}')
print(f'Número informado {num_informado} triplicado: {triplica(num_informado)}')
print(f'Número informado {num_informado}  quaduplicado: {quaduplica(num_informado)}')