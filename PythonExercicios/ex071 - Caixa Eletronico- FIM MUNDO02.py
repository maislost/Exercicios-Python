n = int(input("Digite o valor do saque: "))
total = n
total_notas = 0
ced_maior = 50
while True:
    if total >= ced_maior:
        total -= ced_maior
        total_notas += 1
    else:
        print(f"Total de {total_notas} cedulas de R${ced_maior}")
        if ced_maior == 50:
            ced_maior = 20
        elif ced_maior == 20:
            ced_maior = 10
        elif ced_maior == 10:
            ced_maior = 1
        total_notas = 0
        if total == 0:
            break
