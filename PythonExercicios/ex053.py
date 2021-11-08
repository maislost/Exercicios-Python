# AQUI ESTAMOS FAZENDO UM EXERCICIO SOBRE PALINDROMOS
frase = (input("Digite uma frase: ")).strip().upper() #.stripp remove espacos da esquerda e da direita.
palavras = frase.split()                              # Aqui estamos convertendo a frase em palavras criando uma divisao.
junto = "".join(palavras)                             # Aqui estamos juntando as palavras e removendo os espacos entre as palavras.
inverso = ""
for letra in range(len(junto) - 1,- 1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} e {inverso}  ")
if inverso == junto:
    print("Temos um Palindromo!")
else:
    print("A frase digitada nao e um palindromo")
