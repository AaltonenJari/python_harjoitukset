#! /usr/bin/python3
from math import sqrt


print("Tama ohjelma laskee hypotenuusen kahden annetun kateetin avulla")
print("tai toisen kateetin annetun hypotenuusan ja kateetin avulla.")
print("Lisäksi voidaan laskea kolmion ala.")

oikein = False
ohjaus = int(input("Haluatko laskea hypotenuusan vai katetin?\n  1=hypotenuusa (oletus)\n  2=kateetti "))

while oikein == False:
    if ohjaus == 2:
        kateetti1 = int(input("anna kateetti: "))
        hypotenuusa = int(input("anna hypotenuusa: "))

        kateetti2 = sqrt(hypotenuusa**2 - kateetti1**2)

        vastaus_kateetti2 = int(input("toinen kateetti on: "))
        oikein = kateetti2 == vastaus_kateetti2

        if oikein:
            print ("Toisen kateetin pituus on = " , kateetti2)

    else:
        kateetti1 = int(input("anna ensimmäinen kateetti: "))
        kateetti2 = int(input("anna toinen kateetti: "))

        hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)
        vastaus_hypotenuusa = int(input("Hypotenuusa on: "))
        oikein = hypotenuusa == vastaus_hypotenuusa

        if oikein:
            print ("hypotenuusen pituus on = " , hypotenuusa)

    if oikein:
        ala_ohjaus = input("Haluatko tietää myös kolmion alan? K / <E> ")

        if ala_ohjaus == "K" or ala_ohjaus == "k":
            ala = kateetti1 * kateetti2 / 2

            vastaus_ala = int(input("Kolmion ala on: "))
            oikein = ala == vastaus_ala

            if oikein:
                print("Kolmion ala = ", ala)

    if not(oikein):
        print('Vastauksesi on väärin. Yritä uudelleen!')
 
