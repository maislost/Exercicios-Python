contador = soma = media = maior = menor = 0
continuar = "S"
while continuar in "Ss":
    num = int(input("Digite um numero inteiro: "))
    soma += num
    continuar = str(input("Voce deseja continuar? [S/N] ")).upper().strip()[0] #considera apenas a primeira letra
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / contador
print(f"A sua media e de: {media:.2f}")
print(f" O seu maior numero foi {maior} e o menor {menor}")
print("FIM")
