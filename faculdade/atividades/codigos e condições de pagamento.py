valordoproduto = float(input('insira o valor a ser pago do produto:'))

print('1 a vista em dinheiro ou em cheque')
print('2 a vista no cartão de crédito')
print('3 duas vezes no cartão de crédito')
print('4 três vezes no cartão de crédito')

meiodepagamento = str(input('insira o meio de pagamento: '))

emdinheiroouchequeavista = (valordoproduto * 0.90)
emcartaodecreditoavista = (valordoproduto * 0.85)
duasvezesnocartaodecredito = (valordoproduto * 1)
tresezesnocartaodecredito = (valordoproduto * 1.10)

if meiodepagamento == 'a vista em dinheiro' or meiodepagamento == 'cheque' or '1 a vista em dinheiro ou em cheque' :

    print(emdinheiroouchequeavista)

elif meiodepagamento == '2 a vista no cartão de crédito':
    print(emcartaodecreditoavista)

elif meiodepagamento == '3 duas vezes no cartão de credito':

    print(duasvezesnocartaodecredito)

elif meiodepagamento == '4 três vezes no cartão de crédito':
    print(tresezesnocartaodecredito)
else:
    print('código inserido invalido')