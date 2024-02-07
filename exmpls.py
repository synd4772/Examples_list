from random import *
spc = "\n--------------------\n"
nimed = ["Mati", "Meelis", "Mati", "Mati"]
while True:
    print("--------------------")
    v = input("N-näita andmeid\nL-lisada andmeid\nK-andmete\nH-andmete haldus\nI-Positsiooni otsing" + spc + "\n")
    if v.upper() == "N":
        v = input("Kas juhuslik(j) nimi või terve loetelu(t)? ")
        if v.lower() == "t":
            print(nimed)

        elif v.lower() == "j":
            print(choice(nimed))

    elif v.upper() == "L":
        v = input("Kas nimekirja lõppu(l) või positsioonile(p)? ")
        if v.lower() == "l":
            nimi = input("Sisesta nimi: ")
            nimed.append(nimi)
            print(spc, nimed, end=spc)

        elif v.lower() == "p":
            positsioonile = int(input("Sisesta positsioonile: "))
            nimi = input("Sisesta nimi: ")
            nimed.insert(positsioonile - 1, nimi)
            print(spc, nimed, end=spc)

    elif v.upper() == "K":
        v = input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed(k)")
        if v.lower() == "i":
            ind = int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
            print(spc, nimed, end=spc)

        elif v.lower() == "n":
            nimi = input("Sisesta nimi: ")
            mitu = nimed.count(nimi)
            if mitu > 0:
                if mitu > 1:
                    indeks = -1
                    indeks_list = []
                    for elem in nimed:
                        indeks += 1
                        if elem == nimi:
                            indeks_list.append(indeks)
                    print(indeks_list)
                    v = int(input("Mis indeks? "))
                    nimed.pop(v)
                else:
                    nimed.remove(nimi)
            else:
                print(f"{nimi} ei ole loetelus")
            print(spc, nimed, end=spc)

        elif v.lower() == "k":
            nimed.clear()
            print(spc, nimed, end=spc)

    elif v.upper() == "H":
        v = input("Sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
        if v.lower() == "s":
            v = int(input("A-z?(1) või Z-a(0)"))
            if v:
                nimed.sort(reverse = False)
            else:
                nimed.sort(reverse = True)

        elif v.lower() == "k":
            nimed_copy = nimed.copy()

        elif v.lower() == "p":
            nimed.reverse()

    elif v.upper() == "I":
        nimi = input("Mis nimi ? ")
        arv = nimed.count(nimi)
        if arv == 0:
            print(spc, f"{nimi} on vale nimi", spc) # spc = "\n--------------------\n"
        elif arv > 1:
            indeks = []
            sindeks = -1
            for i in range(arv):
                sindeks = nimed.index(nimi, sindeks + 1)
                indeks.append(sindeks)
            print(spc, f"{nimi} on {arv} tükki, nende indeks on {indeks}", spc) # spc = "\n--------------------\n"
        else:
            indeks = nimed.index(nimi)
            print(spc, f"{nimi} indeks on {indeks}", spc) 
        
        