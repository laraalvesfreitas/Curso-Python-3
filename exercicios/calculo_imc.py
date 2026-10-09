peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

print(f'O seu IMC é: {imc :.2f}')

if(imc <17):
    print(' muito abaixo do peso')
elif (imc >=17 and imc <18.5):
    print(' abaixo do peso')
elif (imc >= 18.5 and imc <25):
    print(' peso ideal')
elif (imc >=25 and imc <30):
    print('sobrepeso')
elif(imc >=30 and imc <35):
    print('obesidade')
elif(imc >=35 and imc <40):
    print('Obesidade severa')
else:
    print('Obesidade morbida')

