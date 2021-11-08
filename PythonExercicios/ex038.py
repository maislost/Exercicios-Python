from time import sleep
num1 = float(input("Escolha um numero qualquer: \n"))
num2 = float(input("Escolha um segundo numero qualquer: \n"))
print("Comparado....\n")
sleep(2)
if num1 > num2:
    print(f"{num1} e maior que {num2}")
elif num1 < num2:
    print(f"{num1} e menor que {num2}")
else:
    print(f"{num1} e igual ao {num2}")
print("Fim das Comparacoes")