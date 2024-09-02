inicio= int(input('escreva a o inicio do intervalo: :'))
fim = int(input('escreva o fim do intervalo:'))
soma_dos_pares=0
soma_dos_impares=0
if inicio >= fim:
    print('a ordem está errada')
print('lista da soma dos pares:')
for x in range(inicio, fim+1 ):
   if x %2 == 0 :
       soma_dos_pares = soma_dos_pares + x
       print(soma_dos_pares)
print('lista de soma dos impares: ')
for y in range(inicio,fim+1):
     if y == 0 :
        soma_dos_impares = soma_dos_impares + y
        print(soma_dos_impares)
         
print('fim')