maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input(f"Digite aqui o peso da {c} pessoa: "))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso < menor:
            maior = peso
        if peso > maior:
            menor = peso
print(f"O maior peso medido foi de {maior}")
print(f"O Menor peso medido foi de {menor}")
