t = int(input("Digite o Primeiro Termo: "))
razao = int(input("Digite a Razao: "))
termo = t
contador = 1
total = 0
mais = 10
while mais != 0:   
    total = total + mais
    while contador <= total:
        termo = termo + razao
        print(f"{termo} -> ", end=" ")
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("FIM")
