#escreva um programa que leia o preço de um produto e a forma
#de pagamento (1 para dinheiro, 2 para cartão). Se for pago em dinheiro, aplique
#um desconto de 10% no preço final.

preço = float(input('insira o preço do produto: '))
desconto = preço * 0.1
comdesconto = preço - desconto

print('1 para dinheiro')
print('2 para cartão')

formadepagamento = int(input('insira o a forma de pagamento: '))

if formadepagamento == 1:
   print(comdesconto)
else:
   print(preço)
