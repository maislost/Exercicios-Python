soma = 0
num = 0
cont= 0
num = int(input("Digite um numero [999 para sair] : "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite um numero [999 para sair] : "))

print(f"Ao total foram somados {cont} numeros")
print(f"O resultado da soma e: {soma}")
print("ACABOU!")