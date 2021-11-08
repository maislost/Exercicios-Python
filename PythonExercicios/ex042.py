m1 = float(input("PRIMEIRO SEGUIMENTO: "))
m2 = float(input("SEGUNDO SEGUIMENTO: "))
m3 = float(input("TERCEIRO SEGUIMENTO: "))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print(" Os seguimentos acima podem formar um triangulo ", end="")
    if m1 == m2 == m3:
        print("EQUILATERO!")
    elif m1 != m2 != m3 != m1:
        print("ESCALENO!")
    else:
        print("ISOSCELES!")

else:
    print("Estes seguimentos nao podem formar um triangulo.")

