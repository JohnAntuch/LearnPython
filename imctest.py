peso = float(input('How much do you weight?'))

altura = float(input('How tall are you?'))

imc = peso / altura ** 2

print('Seu IMC é {}'.format(imc))

if imc < 16:
    print('Be careful')
elif imc < 25:
    print('Nice')
elif imc > 30:
    print('LOL')
