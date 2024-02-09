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

#Sõna/Lause

#sona = input("Sisestage sõna: ")
#sona_list = list(sona)
#tyhik = 0
#vokaali = 0
#konsonanti = 0
#sumbolid = 0
#konsonantid = ["Q","R","T","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","W"]
#vokaalid = ["A","U","E","O","I","Ü","Õ","Ä","Ö","Y","Ä"]
#sona_len = len(sona_list)

#for i in sona_list:
#    if i == " ":
#        tyhik += 1
#    else:
#        for vokaal_sona in vokaalid:
#            if str(i).upper() == str(vokaal_sona):
#                vokaali += 1
#        for konsonanti_sona in konsonantid:
#            if str(i).upper() == str(konsonanti_sona):
#                konsonanti += 1        

#sumbolid = sona_len - konsonanti - vokaali - tyhik
   
#print(f"[{sona}] : tühikud on {tyhik}, vokaalid on {vokaali}, konsonantid on {konsonanti}; sumbolid on {sumbolid}")
    

#--------------------------------------------------------------------------------------------------------
# Loetelu

vanus_list = []
vanus_summa = 0
vanus_list1 = []
nimi_list = []
#2v
#while True:
#    if len(nimi_list) < 5:
#        nimi = input("Sisatege nimi : ")
#        if len(nimi_list) != 0:
#            if nimi_list.count(nimi) != 0:
#                print("See nimi on juba olemas.")
#                pass
#            else:
#                nimi_list.append(nimi)
#                pass
#        else:
#            nimi_list.append(nimi)
#            pass
#    else:
#        break
#1v
for i in range(5):
    nimi = input("Sisatege nimi : ")
    nimi_list.append(nimi)
    
print(f"{sorted(nimi_list)}")
print(f"Viimane nimi on {nimi_list[4]}")
while True:
    print("Vaata lehte(0)\nNime muuta(1)\nVanusenimede lisamine(2)\nKorduva nime kustutamine(3)\nLoo vanusenimekiri(4)")
    v = int(input("Mida te tahate? "))
    if v == 1:
        v = input("Millist nime soovite muuta? ")
        nimi_len = -1
        for i in nimi_list:
            nimi_len += 1
            if v == str(i):
                print(f"Mis nimele sa {v} muuta tahad? ", end="")
                uus_nimi = input("")
                nimi_list.remove(v)
                nimi_list.insert(nimi_len, uus_nimi)
                print(nimi_list)
    elif v == 0:
        nimi_len = len(nimi_list)
        for i in range(nimi_len):
            if vanus_list[i] in vanus_list:
                print(f"{nimi_list[i]} - {vanus_list[i]}")
            else:
                print(nimi_list[i])
    elif v == 2:
        for i in range(5):
            print(f"kui vana '{nimi_list[i]}' on? ", end="")
            vanus = int(input(""))
            vanus_list.append(vanus)
        print(nimi_list)
        print(vanus_list)
    elif v == 3:
        nimi_set = set(nimi_list)
        nimi_list = list(nimi_set)
        print(nimi_list)
    elif v == 4:
        v = int(input("Kui palju vanuseid? "))
        for i in range(v):
            vanus1 = input("Mitu ")
            vanus_list1.append(vanus1)
        vanus_list1_sorted = sorted(vanus_list1,reverse=True)
        for i in vanus_list1:
            vanus_summa += int(i)
        print(f"{vanus_list1_sorted[0]} on suurim vanus, {vanus_list1_sorted[-1]} on väikseim vanus. {vanus_summa} on summa , " )


    

    





        
        
        
        
