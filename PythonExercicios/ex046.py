from time import sleep
print("-=" * 12)
print("Contagem Regressiva de Ano Novo!")
sleep(1)
for cont in range(10, -1, -1): #cont = contagem de N + N ou utilizar -1 na range para contar de N-N
    print(f"{cont}")
    sleep(1)
print("-=" * 12)
print("Feliz Ano novo!")
print("-=" * 12)