palavras = ('Carro', 'Moto', 'Onibus', 'Caminhao', 'Barco', 'Navio')
for vogais in palavras:
    print(f'\nNa palavra {vogais.upper()} temos ', end='')
    for letras in vogais:
        if letras.lower() in 'aeiou':
            print(letras.lower() , end='')
