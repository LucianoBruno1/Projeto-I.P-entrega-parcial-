from tkinter import *

listaemail = []
listasenha = []



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
    #fundocadastro = PhotoImage(file='teladecadastro.png')
    #labelfundocadastro = Label(telacadastro, image=fundocadastro)
    #labelfundocadastro.pack()

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



########### DESIGNS #################

fundo = PhotoImage(file='fundo2.png')
labeltela = Label(janela, image=fundo)
labeltela.pack()

botaoentrar = PhotoImage(file='botaoentrar.png')
botaocadastrar = PhotoImage(file='botaocadastrar.png')


############ caixas de entrada de texto ###########

email = Entry(janela, bd=3, width=32, font=('Arial',13),justify=LEFT)
email.place(x=970, y=198)


password = StringVar() #### comando para esconder a senha com *
senha = Entry(janela, textvariable = password, show='*', bd=3, width=32, font=('Arial',13),justify=LEFT)
senha.place(x=970, y=366)


##################### DEFININDO AS IMAGENS DOS BOTÕES ####################

buttomentrar = Button(janela, image=botaoentrar)
buttomentrar.place(x=992,y=497)

buttomcadastrar = Button(janela, image=botaocadastrar,command=janelacadastro)
buttomcadastrar.place(x=992, y= 630)



janela.mainloop()