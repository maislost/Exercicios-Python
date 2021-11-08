#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idadeH = 0
nome_velho = 0
tot_mulher_20 = 0
for p in range(1,5):
    print(f"----- {p} pessoa -----")
    nome = str(input(f"Digite um nome: ")).strip()
    idade = int(input("Informe a idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if p == 1 and sexo in "Mm":
        maior_idadeH = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maior_idadeH:
        maior_idadeH = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        tot_mulher_20 += 1
media_idade = soma_idade / 4
print(f"A media de idade do grupo e de {media_idade} anos.")
print(f"A idade do homem mais velho e: {maior_idadeH}", end="")
print(f" e o nome dele e: {nome_velho}")
print(f"O total de mulheres com menos de 20 anos e de: {tot_mulher_20}")
