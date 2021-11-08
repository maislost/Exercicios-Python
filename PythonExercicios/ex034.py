#sal = float(input("Digite o valor do seu salario R$: "))
#if sal > 1250:
   # aumento = sal * 10 / 100
   # print(f"Seu aumento e de R$:{aumento:.2f}.\nO seu novo salario e de: R$:{sal + aumento:.2f} ")
#else:
   # aumento = sal * 15 / 100
   # print(f"Seu aumento e de R$:{aumento:.2f}.\nO seu novo salario e de: R$:{sal + aumento:.2f} ")
sal = float(input("Digite o valor do seu salario R$: "))
if sal > 1250:
    nsal = sal + (sal * 10 / 100)
else:
    nsal = sal + (sal * 15 / 100)
print(f"Quem ganhava R${sal:.2f}, passara a ganhar R${nsal:.2f}")
