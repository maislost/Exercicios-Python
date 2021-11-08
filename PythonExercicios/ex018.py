# Faca um programa que leia um angulo qualquer e mostre na tela
# O valor do Seno, cosseno e tangente desse angulo
import math
angulo = float(input("Digite o angulo que voce deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O Angulo {angulo} tem o seno de :{seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O Angulo {angulo} tem o cosseno de: {seno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"O Angulo {angulo} tem a tangente de: {tangente:.2f}")

