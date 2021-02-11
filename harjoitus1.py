#! /usr/bin/python3

# Kommentti
"""
Useampi
rivinen
kommentti
"""
ensimmainen_muuttuja = 1
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = "hello 'rk' world!"
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = 'hello "rk" world!'
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = 10
print(ensimmainen_muuttuja)

print(ensimmainen_muuttuja + 3)

ensimmainen_muuttuja = ensimmainen_muuttuja + 4
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = 'hello world!'
print(ensimmainen_muuttuja)

ensimmainen_muuttuja = ensimmainen_muuttuja + " , I say"
print(type(ensimmainen_muuttuja))

jaettava = 7
print(type(jaettava))
jakaja = 2
print(type(jaettava))

tulos = jaettava / jakaja
print(type(tulos))
print(tulos)

kokonaislukutulos = jaettava // jakaja
print(type(kokonaislukutulos))
print(kokonaislukutulos)

jakojaannos = jaettava % jakaja
print(jakojaannos)

print("tulos oli: " + str(tulos)) # Cast: int to str

#Kertolasku
kantaluku = 2
potenssi = 8
tulos = kantaluku ** potenssi
print(tulos)