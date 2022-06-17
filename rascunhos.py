from tkinter import *
import os

lista=[]


restaurante = Tk()
restaurante.title('PHOENIX SUSHI DELIVERY')
restaurante.geometry('700x500')
restaurante.configure(background = 'lightskyblue4')
restaurante.minsize(width = 700, height = 500)
restaurante.state('zoomed')



#Label para o nome do restaurante e slogan

nome = Label(text='BEM VINDO AO PHOENIX SUSHI DELIVERY ', font=('Arial',20,'bold'), bg='red')
nome.place(x=500,y=0)

description = Label(text='O SUSHI DE SABOR MITOLÓGICO!', font =('Arial',15,'bold'), bg='red')
description.place(x=630, y= 40)


 #####################################   LABEL PARA AS COMIDAS   ############################################################3

subgruposushi = Label(text='SUSHIS', font=('Arial',15,'bold'),bg='yellow')
subgruposushi.place(x=30, y= 70)

#LABEL HOTROLL
hotroll = Label(text='Hot Roll(10un)', font=('Arial',12,'bold'), bg='lightskyblue4')
hotrollpreco = Label(text='R$15,00', font=('Arial',10,'bold'), bg='tomato')
hotrollpreco.place(x=40, y=160)
hotroll.place(x=20, y=130)
hotrollspinbox =Spinbox(from_= 0, to=10, width=8)
hotrollspinbox.place(x=280, y=132)

#LABEL CARIOCA

carioca = Label(text ='Carioca (10un)', font=('Arial',12,'bold'), bg='lightskyblue4')
cariocapreco = Label(text='R$15,00', font=('Arial',10,'bold'), bg='tomato')
carioca.place(x=20,y=240)
cariocapreco.place(x=40,y=270)
cariocaspinbox =Spinbox(from_= 0, to=10, width=8)
cariocaspinbox.place(x=280, y=240)

#LABEL HOSSOMAKI

hossomaki = Label(text='Hossomaki (10un)', font=('Arial',12,'bold'),bg='lightskyblue4')
hossomakipreco = Label(text='R$13,00', font=('Arial',10,'bold'),bg='tomato')
hossomaki.place(x=20,y=340)
hossomakipreco.place(x=40,y=370)
hossomakispinbox =Spinbox(from_= 0, to=10, width=8)
hossomakispinbox.place(x=280, y=342)

#LABEL URAMAKI

uramaki = Label(text='Uramaki (10un)', font=('Arial',12,'bold'),bg='lightskyblue4')
uramakipreco = Label(text='R$18,00', font=('Arial',10,'bold'),bg='tomato')
uramaki.place(x=20,y=440)
uramakipreco.place(x=40,y=470)
uramakispinbox =Spinbox(from_= 0, to=10, width=8)
uramakispinbox.place(x=280, y=442)

#LABEL SASHIMI SALMAO

sashimisalmao = Label(text='Sashimi salmão (5un)', font=('Arial',12,'bold'),bg='lightskyblue4')
sashimisalmaopreco = Label(text='R$18,00', font=('Arial',10,'bold'),bg='tomato')
sashimisalmao.place(x=20,y=540)
sashimisalmaopreco.place(x=40,y=570)
sashimisalmaospinbox =Spinbox(from_= 0, to=10, width=8)
sashimisalmaospinbox.place(x=280, y=542)

#LABEL NIGUIRI

niguiri = Label(text='Niguiri (5un)', font=('Arial',12,'bold'),bg='Lightskyblue4')
niguiripreco = Label(text='R$22,00',font=('Arial',10,'bold'),bg='tomato')
niguiri.place(x=20,y=640)
niguiripreco.place(x=40,y=670)
niguirispinbox =Spinbox(from_= 0, to=10, width=8)
niguirispinbox.place(x=280, y=642)


#LABEL PARA SUBGRUPO TEMAKI

subgrupotemaki = Label(text='TEMAKIS',font=('Arial',15,'bold'),bg='yellow')
subgrupotemaki.place(x=550,y=72)

########################### TEMAKIS ################################

#LABEL TEMAKI FILADELFIA

temakifiladelfia = Label(text='Temaki salmão filadélfia', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakifiladelfiapreco = Label(text='R$35,00',font=('Arial',10,'bold'),bg='tomato')
temakifiladelfia.place(x=500,y=125)
temakifiladelfiapreco.place(x=570,y=155)
temakifiladelfiaspinbox =Spinbox(from_= 0, to=10, width=8)
temakifiladelfiaspinbox.place(x=770, y=128)

#LABEL TEMAKI DE ATUM

temakideatum = Label(text='Temaki de atum maçaricado', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakideatumpreco = Label(text='R$32,00',font=('Arial',10,'bold'),bg='tomato')
temakideatum.place(x=500,y=225)
temakideatumpreco.place(x=570,y=255)
temakideatumspinbox =Spinbox(from_= 0, to=10, width=8)
temakideatumspinbox.place(x=770, y=228)

#LABEL TEMAKI SALMAO E RICOTA

temakisalmaoericota = Label(text='Temaki de salmão e ricota', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakisalmaoericotapreco = Label(text='R$35,00',font=('Arial',10,'bold'),bg='tomato')
temakisalmaoericota.place(x=500,y=325)
temakisalmaoericotapreco.place(x=570,y=355)
temakisalmaoericotaspinbox =Spinbox(from_= 0, to=10, width=8)
temakisalmaoericotaspinbox.place(x=770, y=328)

#LABEL TEMAKI SALMAO FRITO

temakisalmaofrito = Label(text='Temaki de salmão frito', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakisalmaofritopreco = Label(text='R$30,00',font=('Arial',10,'bold'),bg='tomato')
temakisalmaofrito.place(x=500,y=425)
temakisalmaofritopreco.place(x=570,y=455)
temakisalmaofritospinbox =Spinbox(from_= 0, to=10, width=8)
temakisalmaofritospinbox.place(x=770, y=428)

#LABEL TEMAKI SKIN

temakiskin = Label(text='Temaki de skin frito', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakiskinpreco = Label(text='R$23,00',font=('Arial',10,'bold'),bg='tomato')
temakiskin.place(x=500,y=525)
temakiskinpreco.place(x=570,y=555)
temakiskinspinbox =Spinbox(from_= 0, to=10, width=8)
temakiskinspinbox.place(x=770, y=528)

#LABEL TEMAKI DE KANI

temakikani = Label(text='Temaki de kani filadélfia', font=('Arial',12,'bold'),bg='Lightskyblue4')
temakikanipreco = Label(text='R$27,00',font=('Arial',10,'bold'),bg='tomato')
temakikani.place(x=500,y=625)
temakikanipreco.place(x=570,y=655)
temakikanispinbox =Spinbox(from_= 0, to=10, width=8)
temakikanispinbox.place(x=770, y=628)

################################ BEBIDAS #################################

subgrupobebidas = Label(text='BEBIDAS',font=('Arial',15,'bold'),bg='yellow')
subgrupobebidas.place(x=1050,y=70)

#LABEL COCA COLA LATA

cocalata = Label(text='Coca-Cola lata (350ml)',font=('Arial',12,'bold'),bg='lightskyblue4')
cocalatapreco = Label(text='R$5,00',font=('Arial',10,'bold'),bg='tomato')
cocalata.place(x=1000,y=125)
cocalatapreco.place(x=1070, y=155)
cocalataspinbox = Spinbox(from_= 0, to=10, width=8)
cocalataspinbox.place(x=1280,y=127)

#LABEL FANTA LARANJA LATA

fantalaranjalata = Label(text='Fanta laranja lata (350ml)',font=('Arial',12,'bold'),bg='lightskyblue4')
fantalaranjalatapreco = Label(text='R$5,00',font=('Arial',10,'bold'),bg='tomato')
fantalaranjalata.place(x=1000,y=225)
fantalaranjalatapreco.place(x=1070, y=255)
fantalaranjalataspinbox = Spinbox(from_= 0, to=10, width=8)
fantalaranjalataspinbox.place(x=1280,y=227)

#LABEL ÁGUA TÔNICA

aguatonica = Label(text='Água tônica lata (350ml)',font=('Arial',12,'bold'),bg='lightskyblue4')
aguatonicapreco = Label(text='R$3,00',font=('Arial',10,'bold'),bg='tomato')
aguatonica.place(x=1000,y=325)
aguatonicapreco.place(x=1070, y=355)
aguatonicaspinbox = Spinbox(from_= 0, to=10, width=8)
aguatonicaspinbox.place(x=1280,y=327)

#LABEL SCHWEPPES

schweppes = Label(text='SCHWEPPES lata (350ml)',font=('Arial',12,'bold'),bg='lightskyblue4')
schweppespreco = Label(text='R$3,00',font=('Arial',10,'bold'),bg='tomato')
schweppes.place(x=1000,y=425)
schweppespreco.place(x=1070, y=455)
schweppesspinbox = Spinbox(from_= 0, to=10, width=8)
schweppesspinbox.place(x=1280,y=427)

####################### FECHAR PEDIDO ################3

#DEFININDO UMA FUNÇÃO PARA CALCULAR O TOTAL DOS PEDIDOS




def fecharpedido():
    totalhotroll = int(hotrollspinbox.get()) * 15
    totalcarioca = int(cariocaspinbox.get()) * 15
    totalhossomaki = int(hossomakispinbox.get()) *13
    totaluramaki = int(uramakispinbox.get()) * 18
    totalsashimisalmao = int(sashimisalmaospinbox.get()) * 18
    totalniguiri = int(niguirispinbox.get()) * 22
    totaltemakisalmaofiladelfia = int(temakifiladelfiaspinbox.get()) * 35
    totaltemakiatummassaricado = int(temakideatumspinbox.get()) * 32
    totaltemakisalmaoericota = int(temakisalmaoericotaspinbox.get()) * 35
    totaltemakisalmaofrito = int(temakisalmaofritospinbox.get()) * 30
    totaltemakiskinfrito = int(temakiskinspinbox.get()) * 23
    totaltemakikanifiladelfia = int(temakikanispinbox.get()) * 27
    totalcocalata = int(cocalataspinbox.get()) * 5
    totalfantalata = int(fantalaranjalataspinbox.get()) * 5
    totalaguatonica = int(aguatonicaspinbox.get()) * 3
    totalschewppes = int(schweppesspinbox.get()) * 3
    conta = totalhotroll + totalcarioca + totalhossomaki + totaluramaki + totalsashimisalmao + totalniguiri + totaltemakisalmaofiladelfia + totaltemakiatummassaricado + totaltemakisalmaoericota + totaltemakisalmaofrito + totaltemakiskinfrito + totaltemakikanifiladelfia + totalcocalata + totalfantalata + totalschewppes + totalaguatonica
    totaldaconta = Label(text='escolha ao menos um produto para fechar o pedido',font=('Arial',12,'bold'),bg='lightblue')
    totaldaconta2 = Label(text=f'Sua conta é de: R${conta},00',font=('Arial',12,'bold'),bg='lightblue')

    lista.append(totaldaconta)
    lista.append(totaldaconta2)

    if conta == 0:
        totaldaconta = Label(text='escolha ao menos um produto para fechar o pedido', font=('Arial', 12, 'bold'),
                             bg='lightblue')
        totaldaconta.place(x=1100,y=527)

    if conta > 0:





    """""
    while conta == 0:
        totaldaconta = Label(text=f'Escolha ao menos um produto para poder fechar o pedido', font=('Arial', 10, 'bold'), bg='lightblue')
        totaldaconta.place(x=1100, y=527)
        break

    while conta > 0:
        totaldaconta = Label(text=f'Sua conta é de: R${conta},00', font=('Arial', 12, 'bold'), bg='lightblue')
        totaldaconta.place(x=1150, y=527)
        break
    """


def sair():
    restaurante.destroy()
    return

concluir = Button(text='Fechar Pedido', command=fecharpedido)
concluir.place(x=1000, y = 527)

sair = Button(text='Sair do programa', command=sair)
sair.place(x=1000,y=590)




restaurante.mainloop()