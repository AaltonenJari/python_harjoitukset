#! /usr/bin/python3

eka_lista = [12,21,54,12,75]

print(eka_lista)

print(eka_lista[0])

toka_lista = ["tämä","on","toinen","listamme"]

print(toka_lista)
print(toka_lista[0])

toka_lista[1] = "ei ole"
print(toka_lista)

toka_lista.append("toimiiko")
print(toka_lista)

eka_lista.extend(toka_lista)
print(eka_lista)

kolmas_lista = eka_lista + toka_lista
print(kolmas_lista)

kolmas_lista[0] = eka_lista
print(kolmas_lista)

# print(kolmas_lista[0][5]) #viitataan alaindeksiin

print(toka_lista)
eka_muuttuja = toka_lista.pop(0)
print(toka_lista)

for x in toka_lista:
    print(x)

for i in range (len(toka_lista)):
    print(toka_lista[i])

for i in range(30):
    print("luku" + str(i))
    if (i == 9):
        break



