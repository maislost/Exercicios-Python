km = float(input("Digite a Distancia que voce ira viajar:  "))
if km <= 200:
    valor = km * 0.50
    print(f"Voce ira viajar por {km:.2f}KM e o valor da viajem sera de: R${valor:.2f}")
else:
    valor = km * 0.45
    print(f"Voce ira viajar por {km:.2f} e o valor da viajem sera de: R${valor:.2f}")