from time import sleep
from datetime import date
nome = (input("Digite o seu nome completo: \n"))
atual = date.today().year
nascimento = int(input("Digite aqui o seu ano de nascimento: \n"))
idade = atual - nascimento
print(f"O Atleta {nome} tem {idade} anos.")
print("Pesquisando.....")
sleep(1.5)
if idade <= 9:
    print(f"Categoria: MiRIM")
elif idade <= 14:
    print(f"Categoria: INFANTIL")
elif idade <= 19:
    print(f"Categoria: JUNIOR")
elif idade <= 25:
    print(f"Categoria: SENIOR")
else:
    print(f"Categoria: MASTER")
sleep(0.5)
print("FIM DA PESQUISA")
