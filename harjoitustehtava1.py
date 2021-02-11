#! /usr/bin/python3
from math import sqrt


print("tama ohjelma laskee hypotenuusen, kahden annetun kateetin avulla")

ohjaus = int(input("Haluatko laskea hypotenuusan vai katetin?\n  1=hypotenuusa (oletus)\n  2=kateetti "))
if ohjaus == 2:
    kateetti1 = int(input("anna kateetti"))
    hypotenuusa = int(input("anna hypotenuusa"))

    kateetti2 = sqrt(hypotenuusa**2 - kateetti1**2)
    print ("Toisen kateetin pituus on = " , kateetti2)

else:
    kateetti1 = int(input("anna ensimmäinen kateetti"))
    kateetti2 = int(input("anna toinen kateetti"))

    hypotenuusa = sqrt(kateetti1**2 + kateetti2**2)

    print ("hypotenuusen pituus on = " , hypotenuusa)

ala_ohjaus = input("Haluatko tietää myös kolmion alan? K / <E> ")

if ala_ohjaus == "k":
    ala = kateetti1 * kateetti2 / 2
    print("Kolmion ala = ", ala)
 
if ala_ohjaus == "K":
    ala = kateetti1 * kateetti2 / 2
    print("Kolmion ala = ", ala)
