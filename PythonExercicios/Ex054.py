from datetime import date
atual = date.today().year                  # Aqui estou pegando a data atual do meu sistema.
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f"Em que ano a {pess} pessoa nasceu? "))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print(f"Esta pessoa e maior")
    else:
        totmenor += 1
        print("Esta pessoa e menor")
print(f"Ao todos tivemos {totmaior} pessoas maiores de idade")
print(f"E tambem tivemos {totmenor} pessoas de menor idade")
