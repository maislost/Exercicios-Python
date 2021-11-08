# Calcule o preco de um produto com o desconto de 5%

preco = float(input("Digite o valor do produto: R$"))
desconto = preco - (preco * 5/100)
print(f" O valor do produto com desconto e de: R${desconto:.2f}")