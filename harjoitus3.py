#! /usr/bin/python3

def eka_funktio():
    print("eka funktio tulostaa!")

eka_funktio()

def toka_funktio(teksti):
    print("toka funktio tulostaa tämän + argumentin " + teksti)

toka_funktio("ihan mitä vaan")
toka_funktio("tällaista")

#funktio palautuksella "return"
def kolmas_funktio():
    luku = 25
    return luku

funktion_palautus = kolmas_funktio()
print(funktion_palautus)

#funktio palautuksella ja argumenteilla