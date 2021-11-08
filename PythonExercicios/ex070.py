maior_valor = menor_valor = total = contador = 0
while True:
    produto = str(input("Digite o nome do produto: "))
    valor = float(input("Valor: "))
    contador += 1
    total += valor
    if maior_valor > 1000:
        maior_valor += 1
    if contador == 1:
        menor_valor = valor
    else:
        if valor < menor_valor:
            menor_valor = valor
    resp = str(input("Deseja Continuar Comprando? [S/N] ")).stripstrip().upper()[0]
    if resp == "N":
        break
print("FIM DO PROGRAMA")
print(f"O total de compras foi de R$ {total:.2f}")
print(f"Temos {maior_valor} custando mais de R$1000,00")
print(f"O Produto mais barato foi {menor_valor}")
