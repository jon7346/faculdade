#Faça um algoritmo que leia a idade de uma pessoa e seu
#estado civil (S para solteiro, C para casado, V para viúvo e D para
#divorciado). Se a pessoa for solteira e tiver menos de 30 anos, exiba
#"Ainda está curtindo a vida!". Se for casada, exiba "Desejamos
#felicidades ao casal!".
idade = int(input('insira a sua idade: '))

print("para responder o estado civil use :"
      "S para solteiro, C para casado, V para viúvo e D para divorciado.")

estadocivil = str(input('insira o seu estado civil: '))

if estadocivil == 'S' and idade < 30:
    print('Ainda está curtindo a vida!')

elif estadocivil == 'c':
    print("Desejamos felicidades ao casal!")


