from tkinter import * ##biblioteca para abrir a interace
#import os ##biblioteca de automação, para salvar os dados num bloco de notas
import modulotelaprincipal


listaemail = []
listasenha = []
listanome = []


janela = Tk()
janela.title('Login / cadastro')
janela.geometry('700x500')
janela.configure(bg='black')
janela.minsize(width=700, height=500)
janela.state('zoomed')



def janelacadastro():
    telacadastro = Toplevel()
    telacadastro.title('EFETUAR CADASTRO')
    telacadastro.configure(bg='black')
    telacadastro.state('zoomed')

    botaoprosseguir = Button(telacadastro,text='Prosseguir para Login',command=telacadastro.destroy)
    botaoprosseguir.place(x= 100, y= 350)

     ######## LABELS CADASTRO ##########
    titulo = Label(telacadastro, text='CADASTRO PHOENIX SUSHI',font=('Arial',15,'bold'),bg='red')
    titulo.pack()

    nomecadastro = Label(telacadastro, text='NOME:',font=('Arial',12,'bold'),bg='orange')
    nomecadastro.place(x=100,y=50)

    emailcadastro = Label(telacadastro, text='EMAIL:',font=('Arial',12,'bold'),bg='orange')
    emailcadastro.place(x=100, y=150)

    senhacadastro = Label(telacadastro, text='SENHA:',font=('Arial',12,'bold'),bg='orange')
    senhacadastro.place(x=100, y=250)



    ############## CAIXAS DE TEXTO CADASTRO ################

    textonome = Entry(telacadastro, bd=3, width = 32, font=('Arial',13,),justify=LEFT)
    textonome.place(x=180,y=48)

    textoemail = Entry(telacadastro, bd=3, width= 32, font=('Arial',13),justify=LEFT)
    textoemail.place(x=180, y=148)

    textosenha = Entry(telacadastro, bd=3, width=32, font=('Arial',13),justify=LEFT)
    textosenha.place(x=180,y=248)


    ##FUNÇÃO PARA SALVAR NOME, EMAIL E SENHA NUM "BANCO DE DADOS"

    def salvar():
        """""
        caminho = os.path.dirname(__file__)
        arquivo = caminho + "\\contascadastradas.py"
        abrir = open(arquivo, "a")
        abrir.write('\nnome: %s' % textonome.get())
        abrir.write('\nEmail: %s' % textoemail.get())
        abrir.write('\nSenha: %s' % textosenha.get())
        abrir.write('\n\n')
        abrir.close()
        """

        inseriremail = textoemail.get()
        inserirsenha = textosenha.get()
        inserirnome = textonome.get()

        if inseriremail == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=300)
            print('erro')

        elif inserirsenha == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=300)
            print('erro')

        elif inserirnome == "":
            erro = Label(telacadastro, text='Nenhum campo deve ficar em branco',font=('Arial',12,'bold'),bg='red')
            erro.place(x=100, y=300)
            print('erro')

        else:
            sucesso = Label(telacadastro,
                            text='Conta registrada com sucesso! Prossiga para o login clicando no botão abaixo.',
                            font=('Arial', 12, 'bold'), bg='lightgreen')
            sucesso.place(x=100, y=300)
            registrar['state'] = DISABLED


            listaemail.append(inseriremail)
            listasenha.append(inserirsenha)
            listanome.append(inserirnome)
            print(listasenha)
            print(listaemail)
            print(listanome)



    ####################################################

    registrar = Button(telacadastro,text='REGISTRAR',command=salvar)
    registrar.place(x = 300, y=350)



########### DESIGNS #################

fundo = PhotoImage(file='fundo2.png')
labeltela = Label(janela, image=fundo)
labeltela.pack()

botaoentrar = PhotoImage(file='botaoentrar.png')
botaocadastrar = PhotoImage(file='botaocadastrar.png')


############ caixas de entrada de texto para login ###########

email = Entry(janela, bd=3, width=32, font=('Arial',13),justify=LEFT)
email.place(x=970, y=198)


password = StringVar() #### comando para esconder a senha com *
senha = Entry(janela, textvariable = password, show='*', bd=3, width=32, font=('Arial',13),justify=LEFT)
senha.place(x=970, y=366)



def entrar():
    emailget = email.get()
    senhaget = senha.get()


    if emailget in listaemail and senhaget in listasenha:
        logado = Label(text='BEM-VINDO!! Redirecionando para o cardápio.',font=('Arial',14,'bold'),bg='lightgreen')
        logado.place(x=900,y=440)
        janela.destroy()
        modulotelaprincipal.abrirrestaurante()

    else:
        negado = Label(text='Dados inválidos',font=('Arial',14),bg='red')
        negado.place(x=1000,y=440)


##################### DEFININDO AS IMAGENS DOS BOTÕES ####################


buttomentrar = Button(janela, image=botaoentrar,command=entrar)
buttomentrar.place(x=992,y=497)

buttomcadastrar = Button(janela, image=botaocadastrar,command=janelacadastro)
buttomcadastrar.place(x=992, y= 630)


janela.mainloop()