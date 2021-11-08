from time import sleep
print("********** BEM VINDOS AO MATEUS INFORMATICA **********")
sleep(1)
preco = float(input("Digite o valor do produto R$: "))
print("Escolha as Opcoes de Pagamento Abaixo\n")
print("[ 1 ]PARA PAGAMENTOS A VISTA DESCONTO 10%\n[ 2 ]PARA PAGAMENTOS A VISTA NO CARTAO DESCONTO 5%\n[ 3 ]PAGAMENTOS PARCELADOS NO CARTAO ATE 2X SEM DESCONTO\n[ 4 ]PAGAMENTOS 3x OU MAIS NO CREDITO JUROS 20%.")
sleep(1)
opcao = int(input())
print("PROCESSANDO....\n")
sleep(1)
if opcao == 1:
    preco10 = preco -(preco * 10) / 100
    print(f"Sua compra e de R$:{preco:.2f} e vai custar R$:{preco10:.2f} no final.")
elif opcao == 2:
    preco2 = preco - (preco * 5) / 100
    print(f"Sua compra e de R$:{preco:.2f} e vai custar R$:{preco2:.2f} no final.")
elif opcao == 3:
    total = preco
    parc = total / 2
    print(f"Sua compra e de R$:{preco:.2f} e suas duas parcelas serao de R$:{parc:.2f}")
elif opcao == 4:
    total = (preco * 20) / 100 + preco
    totalParc = int(input("Quantas parcelas? "))
    parcTotal = total / totalParc
    print(f"Sua compra e de R$:{preco}, vai custar R$:{total:.2f} e suas parcelas serao de R${parcTotal}")
else:
    print("Opcao Invalida")
    exit()
sleep(1)
print("Obrigado por comprar Conosco!")
