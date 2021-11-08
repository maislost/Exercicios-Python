tot18 = tot_M = tot_H = 0
while True:
    idade = int(input("Digite a Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("[M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_H += 1
    if sexo == 'F' and idade < 20:
        tot_M += 1
    continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
    if continuar != 'S':
        break
print(f"Ao total temos {tot18} pessoas maiores de 18.")
print(f"Ao todo temos {tot_H} casados")
print(f"E temos {tot_M} mulheres com menos de 20 anos.")
