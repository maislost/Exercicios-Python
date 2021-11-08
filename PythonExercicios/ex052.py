n = int(input("Digite um numero qualquer: "))
t = 0                              # Calcula o numero de divisiveis.
for c in range(1, n + 1):
    if n % c == 0:                # Este if vai mostar todos os numeros de resto 0 na divisao
        print("\033[33m", end=" ")
        t += 1
    else:
        print("\033[31m", end=" ")
    print(f"{c}", end=" ")
print(f"\n\033[mO numero {n} foi divisivel {t} vezes")
if t == 2:                         # So vai ser primo se for dividido por no maximo 2x
    print("Por isto ele e primo")
else:
    print("Por isto ele nao e primo")