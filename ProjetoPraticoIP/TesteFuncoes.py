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

    verificar = True
    arq4 = open('usuarios.txt','r')
    monteiro = arq4.readlines()
    while verificar:
        for i in monteiro:
            if nomej in i:
                arq2 = open('{}.txt'.format(nomej),'r+')
                tata = arq2.readlines()
                print(tata[0])
                return nomej
                verificar = False
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
    now = datetime.now()
    x = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
    identificação = input("Qual usuario quer postar: ").strip()
    verificar = True
    arq4 = open('usuarios.txt', 'r')
    monteiro = arq4.readlines()
    while verificar:
        for i in monteiro:
            if identificação in i:
                aqr1 = open("{}.txt".format(identificação), "a")
                quantidadepost = int(input("Quantas postagens: "))
                for i in range(quantidadepost):
                    opost = input("Qual a mensagem: ").strip()
                    while verificador:
                        if len(opost) >120:
                            opost = input("Digite uma mensagem com o máximo de 120 caracteres: ").strip()
                        else:
                            aqr1.write(opost)
                            aqr1.write(" " + x + "\n")
                            verificador = False

                verificar = False
                return identificação
            elif identificação not in i:
                identificação = input("Digite um usuario valido: ")
                identificação = identificação
            verificar = True


def menu():
    verificador = True
    acesso = None
    print(" \033[36m-=-\033[m" * 10, "\n")
    print('''              \033[1;33;mBEM VINDO\033[m                         
                 \033[1;33;mAO\033[m               
              \033[1;31;m\033[4mArquenet\033[m\n''')
    print(" \033[36m-=-\033[m" * 10, "\n")
    usuario()
    while verificador:
        print("\n\n")
        acesso = str(input("""Selecione as opções de entrada
         \033[34m[1]\033[m Ler as postagens de alguem
         \033[34m[2]\033[m Exibir os dados de alguem
         \033[34m[3]\033[m Cadastro
         \033[34m[4]\033[m Postar
         \033[34m[5]\033[m Para Encerrar o Programa
         >>>"""))
        print("\033[36m-=-\033[m" * 13, "\n")


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
        if acesso == "5":
            verificador = False
            print("""
    \033[33mObrigado pela preferencia
        volte sempre ao.... \033[m 
            \033[1;31mARQUENET\033[m""")
        if acesso == None:
            acesso = None
        else:
            print("\033[1;31mINVÁLIDO\033[m")

menu()