n = int(input("Digite um numero: "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end="")
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    contador += 1
print(" -> FIM")
