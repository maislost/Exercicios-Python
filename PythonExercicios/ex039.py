#idade = int(input("Digite a sua idade: \n"))
#if idade == 18:
    #print(f"Voce tem {idade} anos e esta na hora de se alistar.")
    #print("Procure uma Junta militar mais proxima\n")
#elif idade > 18:
    #print(f"Voce tem {idade} anos e perdeu o alistamento.")
    #print("Procure uma junta militar mais proxima para mais informacoes.\n")
#else:
    #print(f'''Ainda nao e a hora de voce se alistar
#procure a junta militar quando voce completar
#{id18} anos\n''')
#print("inscricao Encerrada.")

from datetime import date
from time import sleep
sexo = int(input("Digite [1] se voce for do sexo masculino ou [2] para feminino: "))

if sexo == 1:
    print("Homens obrigatoriamente precisam se alistar")
    sleep(1)
    print("Comecando a Inscricao ....")
    sleep(1)
elif sexo == 2:
    print("Mulheres nao precisam se alistar")
    exit()
else:
    print("Opcao Invalida")
    exit()

atual = date.today().year
nasc = int(input("Digite o ano do seu Nascimento: \n"))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}\n")
if idade == 18:
    print("Voce precisa se alistar, procure uma junta militar mais proxima\n")
elif idade > 18:
    saldo = idade - 18
    print(f"Voce deveria ter se alistado a {saldo} atras.\n")
    ano = atual - saldo
    print(f"Seu alistamento foi em {ano}")
else:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} ano's para voce se alistar\n")
    ano = atual + saldo
    print(f"Seu alistamento sera em: {ano}")
sleep(1)
print("Fim da Inscricao.")