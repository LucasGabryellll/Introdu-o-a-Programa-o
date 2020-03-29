from datetime import datetime
now = datetime.now()
x = str(now.day) + ' '+str(now.month)+ ' '+str(now.year)


def exibirpost():
    nomek = input("Para exibir suas postagens digite seu nome: ")
    arq2 = open('{}.txt'.format(nomek), 'r+')
    vito = arq2.readlines()
    print(vito[1::])




def exibirdd():
    nomej = input("Para exibir seus dados digite seu nome: ")
    verificador = True
    arq4 = open('usuarios.txt','r')
    monteiro = arq4.readlines()
    casaca = arq4.readline()
    while verificador :
        for i in monteiro:
            if nomej in i:
                arq2 = open('{}.txt'.format(nomej),'r+')
                tata = arq2.readlines()
                print(tata[0])
                verificador = False
            elif nomej not in i:
                nomej = input("Para exibir seus dados digite seu nome: ")

def usuario():
    arq = open('usuarios.txt','r')
    y = arq.readlines()
    print("\033[4;35mUsuarios cadastrados\033[m")

def cadastro ():
    arq = open('usuarios.txt','a')
    dicionario = dict()
    nome = input('Qual o nome: ')
    apelido = input('Qual o apelido: ')
    idade = str(input('Qual a idade: '))
    dicionario = nome+' '+apelido+' '+idade+' '+'\n'

    arq.write(dicionario)
    aqr1 = open("{}.txt".format(nome),"w")
    aqr1.write(dicionario+"\n")

    arq.close()

def writepostagem():
    verificador = True
    identificação = input("Qual usuario quer postar: ").strip()
    aqr1 = open("{}.txt".format(identificação), "a")
    quantidadepost = int(input("Quastas postagens: "))
    for i in range (quantidadepost):
        opost = input("Qual a mensagem: ").strip()
        while verificador:
            if len(opost) >120:
                opost = input("Digite uma mensagem com o máximo de 120 caracteres: ").strip()
            else:
                aqr1.write(opost + "\n")
                verificador = False







def menu():
    verificador = True
    acesso = None
    print(" \033[36m-=-\033[m" * 10, "\n")
    print('''              \033[1;32;mBEM VINDO\033[m                         
                 \033[1;32;mAO\033[m               
              \033[1;30;m\033[4mArquenet\033[m\n''')
    print(" \033[36m-=-\033[m" * 10, "\n")
    usuario()
    while verificador:
        print("\n\n\n")
        acesso = str(input("""Selecione as opções de entrada
         [1] Ler as postagens de alguem
         [2] Exibir os dados de alguem
         [3] Cadastro
         [4] Postar
         [5] Para Encerrar o Programa
         >>>"""))

        if acesso == "1":
            exibirpost()
            acesso = None

        if acesso == "2":
            exibirdd()
            acesso = None
        if acesso == "3":
            cadastro()
            acesso = None
        if acesso == "4":
            writepostagem()
            acesso = None
        elif acesso == "5":
            verificador = False
       # else :
            #print("\033[1;31mINVÁLIDO\033[m")
           # acesso = str(input("Selecione Uma Entrada Válida: "))
menu()