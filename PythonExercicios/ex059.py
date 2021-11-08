v1 = int(input("Digite o primeiro Valor: "))
v2 = int(input("Digite o segundo Valor: "))
opcao = 0
print('-='* 12)
while opcao != 5:
    print('''[1] para soma
[2] para multiplicar
[3] para maior
[4] digite novos numeros
[5] para sair do programa
''')
    opcao = int(input("Qual opcao voce deseja realizar? "))
    if opcao == 1:
        soma = v1 + v2
        print(f"Sua Soma de {v1} + {v2} e de: {soma}")
    elif opcao == 2:
        mult = v1 * v2
        print(f"Sua multiplicacao entre {v1} * {v2} de: {mult}")
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f"Entre {v1} e {v2}, o maior valor e de {maior}")
    elif opcao == 4:
        print("Escolha novamente seus valores.")
        v1 = int(input("Primeiro Valor: "))
        v2 = int(input("Segundo Valor: "))
    elif opcao == 5:
        print("Finalizando ....")
    else:
        print("Opcao Invalida, tente novamente!")
    print("-=" * 12)
print("Fim do Programa! Volte Sempre")
