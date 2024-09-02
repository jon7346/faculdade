numero1 = float(input("digite o numero 1:"))
numero2 = float(input("digite o numero 2:"))
numero3 = float(input("digite o numero 3:"))
maior = numero1

if maior > numero2:
    maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero2

print(maior)