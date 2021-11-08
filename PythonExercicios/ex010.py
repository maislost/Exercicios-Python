# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere 1 USD = 5.5
real = float(input("Digite qual e o valor que voce tem na sua carteira: R$"))
dolar = real / 5.5
print(f"O valor que voce tem na carteira e de: R${real:.2f} e pode comprar U$ {dolar:.2f} dolares ")
