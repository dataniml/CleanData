import random

L1 = "Chorizopyttipannu"
F1 = "Uunilohi"
L2 = "Lasagne"
K1 = "Broilerikiusaus"
L3 = "Makaronilaatikko"
K2 = "Kermainen broileripata"
L4 = "Perunasosepelti"
L5 = "Spagetti"
F2 = "Tonnikalasalaatti"
F3 = "Tonnikalanuudelit"
V1 = "Fetasalaatti"
V2 = "Fetanuudelit"
L6 = "Uunimakkara"
L7 = "Pizza"
K3 = "Paistettu koipi + lisuke"

ruokalista = {"Chorizopyttipannu",
"Uunilohi",
"Lasagne",
"Broilerikiusaus",
"Makaronilaatikko",
"Kermainen broileripata",
"Perunasosepelti",
"Spagetti",
"Tonnikalasalaatti",
"Tonnikalanuudelit",
"Fetasalaatti",
"Fetanuudelit",
"Uunimakkara",
"Pizza",
"Paistettu koipi + lisuke"}

def suositus(ruoka, terveys, helppous):
    if ruoka == "k" and terveys and helppous:
        R = random.randint(1, 6)
        if R == 1:
            return F1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return F2
        else:
            return V1
    if ruoka == "k" and not terveys and not helppous:
        R = random.randint(1, 12)
        if R == 1:
            return F1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return F2
        if R == 6:
            return L2
        if R == 7:
            return F3
        if R == 8:
            return L6
        if R == 9:
            return L7
        if R == 10:
            return V2
        if R == 11:
            return L1
        else:
            return V1
    if ruoka == "k" and terveys and not helppous:
        R = random.randint(1, 7)
        if R == 1:
            return F1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return F2
        if R == 6:
            return L2
        else:
            return V1
    if ruoka == "k" and not terveys and helppous:
        R = random.randint(1, 9)
        if R == 1:
            return F1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return F2
        if R == 6:
            return F3
        if R == 7:
            return L6
        if R == 8:
            return V2
        else:
            return V1

    if ruoka == "f" and terveys and helppous:
        R = random.randint(1, 6)
        if R == 1:
            return K1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return K3
        else:
            return V1
    if ruoka == "f" and not terveys and not helppous:
        R = random.randint(1, 12)
        if R == 1:
            return K1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return K2
        if R == 6:
            return L2
        if R == 7:
            return K3
        if R == 8:
            return L6
        if R == 9:
            return L7
        if R == 10:
            return V2
        if R == 11:
            return L1
        else:
            return V1
    if ruoka == "f" and terveys and not helppous:
        R = random.randint(1, 8)
        if R == 1:
            return K1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return K3
        if R == 6:
            return L2
        if R == 7:
            return K2
        else:
            return V1
    if ruoka == "f" and not terveys and helppous:
        R = random.randint(1, 8)
        if R == 1:
            return K1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return K3
        if R == 6:
            return L6
        if R == 7:
            return V2
        else:
            return V1

    if ruoka == "l" and terveys and helppous:
        R = random.randint(1, 5)
        if R == 1:
            return K1
        if R == 2:
            return F1
        if R == 3:
            return F2
        if R == 4:
            return K3
        else:
            return V1
    if ruoka == "l" and not terveys and not helppous:
        R = random.randint(1, 8)
        if R == 1:
            return F1
        if R == 2:
            return F2
        if R == 3:
            return F3
        if R == 4:
            return K1
        if R == 5:
            return K2
        if R == 6:
            return K3
        if R == 7:
            return V2
        else:
            return V1
    if ruoka == "l" and terveys and not helppous:
        R = random.randint(1, 6)
        if R == 1:
            return F1
        if R == 2:
            return K1
        if R == 3:
            return K2
        if R == 4:
            return F2
        if R == 5:
            return K3
        else:
            return V1
    if ruoka == "l" and not terveys and helppous:
        R = random.randint(1, 7)
        if R == 1:
            return F1
        if R == 2:
            return K1
        if R == 3:
            return F2
        if R == 4:
            return K3
        if R == 5:
            return V1
        if R == 6:
            return F3
        else:
            return V2

    if ruoka == "v" and terveys and helppous:
        R = random.randint(1, 7)
        if R == 1:
            return K1
        if R == 2:
            return F1
        if R == 3:
            return L3
        if R == 4:
            return L4
        if R == 5:
            return L5
        if R == 6:
            return F2
        else:
            return K3
    if ruoka == "v" and not terveys and not helppous:
        R = random.randint(1, 13)
        if R == 1:
            return F1
        if R == 2:
            return L3
        if R == 3:
            return L4
        if R == 4:
            return L5
        if R == 5:
            return F2
        if R == 6:
            return L2
        if R == 7:
            return F3
        if R == 8:
            return L6
        if R == 9:
            return L7
        if R == 10:
            return K1
        if R == 11:
            return L1
        if R == 12:
            return K2
        else:
            return K3
    if ruoka == "v" and terveys and not helppous:
        R = random.randint(1, 9)
        if R == 1:
            return K1
        if R == 2:
            return F1
        if R == 3:
            return L3
        if R == 4:
            return L4
        if R == 5:
            return L5
        if R == 6:
            return F2
        if R == 7:
            return L2
        if R == 8:
            return K2
        else:
            return K3
    if ruoka == "v" and not terveys and helppous:
        R = random.randint(1, 9)
        if R == 1:
            return F3
        if R == 2:
            return L6
        if R == 3:
            return F2
        if R == 4:
            return K3
        if R == 5:
            return L4
        if R == 6:
            return L5
        if R == 7:
            return K1
        if R == 8:
            return F1
        else:
            return L3

while True:

    print("Mitä söit eilen, tarvitseeko tämän päivän ruuan olla terveellistä (1/0) ja tarvitseeko sen olla helppoa (1)")
    print("Eilisen ruuan vaihtoehdot ovat 'k' = kanaruoka, 'f' = kalaruoka, 'l' = punainen liha, 'v' = vege")
    print("Syöte esim: f01 (eilen kalaa, tänään ei terveellistä ja helppoa) tai k (eilen kanaa, tänään ei terveellistä")
    print("ja helppoudella ei väliä) tai v1 (eilen vegeruokaa, tänään terveellistä ja helppoudella ei väliä)")
    print("Tee koko viikon ruokalista syötteellä 'vk'")
    print("")
    valinta = input("Syötteesi: ")

    if valinta == "k":
        print("Tälle päivälle suosittelen: " + str(suositus("k", False, False)))
    elif valinta == "k1" or valinta == "k10":
        print("Tälle päivälle suosittelen: " + str(suositus("k", True, False)))
    elif valinta == "k11":
        print("Tälle päivälle suosittelen: " + str(suositus("k", True, True)))
    elif valinta == "k01":
        print("Tälle päivälle suosittelen: " + str(suositus("k", False, True)))

    elif valinta == "f":
        print("Tälle päivälle suosittelen: " + str(suositus("f", False, False)))
    elif valinta == "f1" or valinta == "f10":
        print("Tälle päivälle suosittelen: " + str(suositus("f", True, False)))
    elif valinta == "f11":
        print("Tälle päivälle suosittelen: " + str(suositus("f", True, True)))
    elif valinta == "f01":
        print("Tälle päivälle suosittelen: " + str(suositus("f", False, True)))

    elif valinta == "l":
        print("Tälle päivälle suosittelen: " + str(suositus("l", False, False)))
    elif valinta == "l1" or valinta == "l10":
        print("Tälle päivälle suosittelen: " + str(suositus("l", True, False)))
    elif valinta == "l11":
        print("Tälle päivälle suosittelen: " + str(suositus("l", True, True)))
    elif valinta == "l01":
        print("Tälle päivälle suosittelen: " + str(suositus("l", False, True)))

    elif valinta == "v":
        print("Tälle päivälle suosittelen: " + str(suositus("v", False, False)))
    elif valinta == "v1" or valinta == "v10":
        print("Tälle päivälle suosittelen: " + str(suositus("v", True, False)))
    elif valinta == "v11":
        print("Tälle päivälle suosittelen: " + str(suositus("k", True, True)))
    elif valinta == "v01":
        print("Tälle päivälle suosittelen: " + str(suositus("v", False, True)))

    elif valinta == "vk":
        viikonruokalista = random.sample(ruokalista, 7)
        print("MA: " + viikonruokalista[0])
        print("TI: " + viikonruokalista[1])
        print("KE: " + viikonruokalista[2])
        print("TO: " + viikonruokalista[3])
        print("PE: " + viikonruokalista[4])
        print("LA: " + viikonruokalista[5])
        print("SU: " + viikonruokalista[6])
        print("")

    else:
        print("Virheellinen syöte")

    print("")
    jatko = input("Otetaanko toinen valinta (k)?")

    if jatko != "k":
        exit()
    print("")


