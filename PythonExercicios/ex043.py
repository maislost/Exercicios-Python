peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite aqui sua altura: "))
imc = peso/(altura ** 2)
if imc < 16:
    print("Magreza grave")
elif 16 <= imc < 17:
    print("Magreza Moderada")
elif 17 <= imc < 18.5:
    print("Magreza Leve")
elif 18.5 <= imc < 25:
    print("Saudavel")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade I")
elif 35 <= imc < 40:
    print("Obesidade II")
else:
    print("Obesidade III")
