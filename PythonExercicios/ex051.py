p = int(input("Primeiro Termo: "))
r = int(input("A Razao: "))
dec = p + (10-1) * r # formula pra encontrar o decimo termo.
for c in range(p,dec + r, r): # dec + r pois o python ignora o ultimo valor.
    print(f"{c}", end=' ')
print("ACABOU!")