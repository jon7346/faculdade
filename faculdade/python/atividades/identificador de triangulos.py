lado1 = float(input("digite o comprimento de um dos lados:"))
lado2 = float(input("digite o comprimento de outro lado do triângulo:"))
lado3 = float(input("digite o comprimento do ultimo lado do triangulo:"))

if lado1 == lado2 == lado3:
 print('O triangulo escalo')
elif lado2 == lado3:
  print('o triagulo é isóselis')
elif lado1 == lado2:
  print('o triagulo é isóselis')
elif lado1 == lado3:
  print("o trinagulo è isóselis")
else:
  print('O triangulo é escaleno')

