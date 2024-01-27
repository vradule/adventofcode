import tkinter
import random

kraj_igre = False
kvadrati_za_ocistiti = 0
minsko_polje = []


def raspored_prozor(prozor):
    for red_broj, red_lista in enumerate(minsko_polje):
        for kolona_broj, rsdLista in enumerate(minsko_polje):
            for kolona_broj, kolonaUnos in enumerate(red_lista):
                if random.randint(1, 100):
                    kvadrat = tkinter.Label(prozor, text="   ", bg="darkgreen")
                elif random.randint(1, 100) > 75:
                    kvadrat = tkinter.Label(prozor, text="   ", bg="seagreen")
                else:
                    kvadrat = tkinter.Label(prozor, text="   ", bg="green")
                kvadrat.grid(row=red_broj, column=kolona_broj)
                kvadrat.bind("<Button-1>", na_klik)


def napravi_minsko_polje(minsko_polje):
    global kvadrati_za_ocistiti
    for red in range(0, 10):
        red_lista = []
        for kolona in range(0, 10):
            if random.randint(1, 100) < 20:
                red_lista.append(1)
        else:
            red_lista.append(0)
            kvadrati_za_ocistiti = kvadrati_za_ocistiti + 1
        minsko_polje.append(red_lista)
    # stampajPolje(minskoPolje)


def stampaj_polje(minsko_polje):
    for red_lista in minsko_polje:
        print(red_lista)


def na_klik(event):
    global rezultat
    global kraj_igre
    global kvadrati_za_ocistiti
    kvadrat = event.widget
    red = int(kvadrat.grid_info()["row"])
    kolona = int(kvadrat.grid_info()["column"])
    tekuci_text = kvadrat.cget("text")
    if kraj_igre == False:
        if minsko_polje[red][kolona] == 1:
            kraj_igre = True
            kvadrat.config(bg="red")
            print("Igra zavrsena! Pogodio si minu!")
            print("Tvoj rezultat je: ", rezultat)
        elif tekuci_text == "   ":
            kvadrat.config(bg="brown")
            ukupno_mina = 0
            if red < 9:
                if minsko_polje[red + 1][kolona] == 1:
                    ukupno_mina = ukupno_mina + 1
            if red > 0:
                if minsko_polje[red - 1][kolona] == 1:
                    ukupno_mina = ukupno_mina + 1
            if kolona > 0:
                if minsko_polje[red][kolona - 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            if kolona < 9:
                if minsko_polje[red][kolona + 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            if red > 0 and kolona > 0:
                if minsko_polje[red - 1][kolona - 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            if red < 9 and kolona > 0:
                if minsko_polje[red + 1][kolona - 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            if red > 0 and kolona < 9:
                if minsko_polje[red - 1][kolona + 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            if red < 9 and kolona < 9:
                if minsko_polje[red + 1][kolona + 1] == 1:
                    ukupno_mina = ukupno_mina + 1
            kvadrat.config(text=" " + str(ukupno_mina) + " ")
            kvadrati_za_ocistiti = kvadrati_za_ocistiti - 1
            rezultat = rezultat + 1
            if kvadrati_za_ocistiti == 0:
                kraj_igre = True
                print("Cestitamo! Pobedio si!")
                print("Tvoj rezultat je: ", rezultat)


def igraj_izbegnite_mine():
    napravi_minsko_polje(minsko_polje)
    prozor = tkinter.Tk()
    raspored_prozor(prozor)
    prozor.mainloop()


igraj_izbegnite_mine()
