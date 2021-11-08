from time import sleep
num = int(input("Digite um numero inteiro qualquer: "))
print('''Escolha uma das bases para conversao:
[1] conversao binaria
[2] conversao octal
[3] conversao hexadecimal\n''')
opcao = int(input("Escolha sua opcao: \n"))
print("Convertendo...\n")

sleep(3)

if opcao == 1:
    print(f"{num} convertido para binario e igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para octal e igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal e igual a{hex(num)[2:]} ")
else:
    print("Opcao invalida")
print("Fim da conversao")
