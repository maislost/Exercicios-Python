n1 = float(input("Digite aqui sua primeira nota: "))
n2 = float(input("Digite aqui sua segunda nota: "))
n3 = float(input("Digite aqui sua terceira nota: "))
media = (n1+n2+n3)/3
if media >=7:
    print(f"Voce teve uma media de {media:.2f} e foi APROVADO, parabens!")
elif media >=5 and media <7:
    print(f"Voce teve uma media de {media:.2f} e esta de RECUPERACAO, estude muito!")
else:
    print(f"Voce teve uma media de {media:.2f} e foi REPROVADO, estude mais!")
