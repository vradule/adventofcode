import tkinter
import random

krajIgre = False
rezultat = 0
kvadratiZaOcistiti = 0


def igraj_izbegniteMine():
    napravi_minskoPolje(minskoPolje)
    prozor = tkinter.TK()
    raspored_prozor(prozor)
    prozor.mainloop()

    minskoPolje = []


def napravi_minskoPolje(minskoPolje):
    


def raspored_prozor(prozor):
    for redBroj, redLista in enumerate(minskoPolje):
        for kolonaBroj, kolonaUnos in enumerate(redLista):
            if random.randint(1, 100) < 25:
                kvadrat = tkinter.Label(prozor, text="    ", bg="darkgreen")
            elif random.randint(1, 100) > 75:
                kvadrat = tkinter.Label(prozor, text="    ", bg="seagreen")
            else:
                kvadrat = tkinter.Label(prozor, text="    ", bg="green")
            kvadrat.grid(row=redBroj, column=kolonaBroj)
            igraj_izbegniteMine()


igraj_izbegniteMine()
