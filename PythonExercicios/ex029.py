print("**********" * 5, "RADAR ELETRONICO", "**********" * 5)
velo = float(input("Qual e a sua velocidade? : "))
if velo > 70:
    print(f"Voce esta a {velo} KM/H !!!!")
    multa = (velo - 70) * 10
    print (f"Voce acabou de receber uma muta no valor de R$: {multa}")

else:
    print(f"Voce esta a {velo}KM/H. Boa Viajem!")
