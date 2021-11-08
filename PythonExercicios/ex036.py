vCasa = float(input("Qual e o valor da casa para financiar ?\nR$: "))
vSal = float(input("Qual e a sua renda mensal ?\nR$: "))
vAnos = int(input("Em quantos anos ira pagar ?\n"))
vMensal = vCasa / (vAnos * 12)
if vMensal <= (vSal * 30)/100:
    print(f"Seu financiamento ficou no valor de R${vMensal:.2f} e foi aprovado\n")
else:
    print(f"Seu financiamento ficou no valor de R${vMensal:.2f} e foi negado")

print("Tenha um otimo dia.")