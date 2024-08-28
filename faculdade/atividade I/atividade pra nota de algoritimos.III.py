#Crie um algoritmo que leia a idade de uma pessoa e a
#quantidade de livros que ela leu no último mês. Se tiver menos de 18 anos e não
#tiver lido pelo menos 2 livros, exiba a mensagem "Precisa ler mais para
#desenvolver o hábito da leitura".
idade = int(input('insira sua idade: '))
numerodelivros = int(input('insira a quantidade de livros que leu no ultimo mês: '))

if idade < 18 and numerodelivros <= 2:
    print("Precisa ler mais para desenvolver o hábito da leitura")
else:
    print('você não prescisa desenvolver o hábito da leitura')
