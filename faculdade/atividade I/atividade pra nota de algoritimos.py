altura = float(input('escreva sua altura em metros: '))
sexo = str(input('escreva seu sexo: '))

if sexo == 'feminino' and altura < 1.60:
    print('altura abaixo da média feminina')
else:
    if sexo == 'feminino' and altura > 1.60:
        print('dentro da media femina')

    if sexo == 'masculino' and altura > 1.80:
        print('acima da média masculina')
    else:
        print('dentro da média masculina')
