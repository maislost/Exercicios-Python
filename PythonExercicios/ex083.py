expressao  = str(input('Digite uma expressão: '))
lista = []
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) >  0:
            lista.pop()
        else:
            lista.append(')') 
            break
if len(lista) == 0:
    print('Sua Expressao está validada!')
else:
    print('Sua Expressao nao está correta!')
     
