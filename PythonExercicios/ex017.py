# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#Calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f"O valor da hipotenusa e: {hi:.2f}")
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")


