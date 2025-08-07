peso =float(input("peso do usuário: "))
altura = float(input("altura do usuário: "))

imc = peso/altura**2
print(imc)
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 30:
    print("obeso")
else:
    print("individuo no peso normal")
