from xmlrpc.client import boolean


stop = False
while stop == False:
    try:
        nome = input(("Insira seu nome: "))
        nascimento = int (input("Digite o ano do seu nascimento: "))
        if(nascimento >= 1922 and nascimento <=2021):
            nascimento = 2022 - nascimento 
            print("\n o nome do usuario é " + nome + " e a idade é " +str(nascimento))
            break
    except:
        print("Dados invalidos")
        print("Por favor insira os dados corretamente")
