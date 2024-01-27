import tkinter
import random
krajIgre = False 
KvadratiZaOcistiti = 0


def igraj_izbegniteMine():
    napravi_minskoPolje(minskoPolje)
    prozor = tkinter.TK()
    raspored_prozor(prozor)
    prozor.mainloop()
    

minskoPolje = []


def napravi_minskoPolje(minskoPolje):
    global KvadratiZaOcistiti
    for red in range (0,10):
        redLista = []
        for kolona in range(0,10):
             if random.randint(1,100) < 20:
                redLista.append(1)
        else: 
                redLista.append(0)
                KvadratiZaOcistiti = KvadratiZaOcistiti + 1
        minskoPolje.append(redLista)
    #stampajPolje(minskoPolje)
def stampajPolje(minskoPolje):
     for redLista in minskoPolje:
          print(redLista)
igraj_izbegniteMine                           