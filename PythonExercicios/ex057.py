sexo = str(input("Informe seu sexo: [ M / F ]")).strip().upper()[0]
print(f"Informe o seu sexo: {sexo}")
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos. Por favor, informe o seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")