#! /usr/bin/python3

class Ensimmain_luokka:
    x=2

luokka_objekti = Ensimmain_luokka()
print (luokka_objekti.x)

luokka_objekti.x = 4
print (luokka_objekti.x)

class Toinen_luokka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tulosta_arvot(self):
        print (self.x)
        print (self.y)

luokka2_objekti = Toinen_luokka(4,5)
luokka2_objekti.tulosta_arvot()

while True:
    Syote = input("kirjoita: ei")
    if Syote == "ei":
        break

Syote2 = ""
while Syote2 != "on":
    Syote2 = input("Kirjoita: On ")
