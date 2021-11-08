while True:
    n= int(input("Escolha a sua tabuada : "))
    if n < 0:
        print("Programa Encerrado.")
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
