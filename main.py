from sys import exit
		
def CalculaMedia():
  n1 = float(input("Entre com um número inteiro qualquer: "))
  n2 = float(input("Entre com outro número inteiro qualquer: "))
  media = (n1 + n2)/2
  print("A média dos números inteiros %i e %i é: %2f" % (n1,n2,media))

def OrdenarDezNumeros():
    lista = []
    while len(lista) < 11:
        n = int(input("Digite um número inteiro qualquer: "))
        lista.append(n)
    lista_ordenada = sorted(lista)
    for i in lista_ordenada:
	      print(i)

def EscreveNomeNVezes():
    nome = "Vascaíno"
    n = int(input("Digite um número inteiro qualquer: "))
    lista = []
    while len(lista) < n:
	      lista.append(nome)
    for i in lista:
	      print(i)
		
def Inicio():
    resposta = int(input("Digite\n1 para CalculaMedia\n2 para OrdenarDezNumeros\n3 para EscreveNomeNVezes ou 4 para sair."))
    if resposta == 1:
      CalculaMedia()
    elif resposta == 2:
	    OrdenarDezNumeros()
    elif resposta == 3:
      EscreveNomeNVezes()
    else:
        exit()
    
while True:
  Inicio()
