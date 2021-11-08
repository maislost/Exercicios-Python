# Crie um programa que mostre o nome com:
# Todas as letras maiusculas e minusculas
# Quantas letras ao todo sem considerar os espacos
# Quantas letras tem o primeiro nome
frase = str(input("Digite um nome: ")).strip() #strip remove os espacos no comeco e no final da frase
espacos = frase.count(" ")
print(f"Seu nome em maiusculo e: {frase.upper()}")
print(f"Seu nome em minusculo e: {frase.lower()}")
print(f"Seu nome tem ao todo {len(frase) - espacos}") # esta funcao esta contando quantas palavras existem e removendo os espacos entre elas tambem.


