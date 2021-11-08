v1 = int(input("Digite o primeiro numero: "))
v2 = int(input("Digite o segundo numero: "))
v3 = int(input("Digite o terceiro numero: "))
#Verificando quem e o maior
if v1 > v2 and v1 > v3:
    print(f"O maior valor e: {v1}")
if v2 > v1 and v2 > v3:
        print(f"O maior valor e: {v2}")
if v3 > v1 and v3 > v2:
    print(f"O maior valor e: {v3}")
#Verificando quem e o menor
if v1 < v2 and v1 < v3:
    print(f"O menor valor e: {v1}")
if v2 < v1 and v2 < v3:
    print(f"O menor valor e: {v2}")
if v3 < v1 and v3 < v2:
    print(f"O menor valor e: {v3}")

