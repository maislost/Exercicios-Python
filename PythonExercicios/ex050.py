soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1 # aqui ele esta contando quantos numeros foram inseridos.
print(f"Voce informou {cont} numeros PARES e a soma deles sao {soma}")
