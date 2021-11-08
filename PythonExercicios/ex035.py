ladoA = int(input("Digite a primeira medida: "))
ladoB = int(input("Digite a segunda medida: "))
ladoC = int(input("Digite a terceira medida: "))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print("Com estas medidas voce pode formar um triangulo, Parabens!!!!!")
else:
    print("Voce nao pode formar um triangulo com estas medidas")

