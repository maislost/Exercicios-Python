# Defina a dimencao, a area e quantos litros de tinta serao necessarios para pintar uma parede. Mostre na tela os valores requisitados.
# Sabe-se que 1 litro de tinta pinta 2m²
plargura = float(input("Digite o valor da largura da parede: "))
paltura = float(input("Digite o valor da altura da parede: "))
area = paltura * plargura
print(f"A sua parede tem dimensao de {plargura}x{paltura} com uma area de {area}m²")
tinta = area / 2
print(f"A quantidade de tinta que sera utilizada e de: {tinta:.2f} litros")
