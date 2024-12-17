import random

# Ruokatyypit: Liha = 1, Kana = 2, Kala = 3, Vege = 4
ruokaData = [
    {"nimi":"Chorizopyttipannu", "tyyppi": 1, "terveys": False, "helppo": False},
    {"nimi":"Uunilohi", "tyyppi": 3, "terveys": True, "helppo": True},
    {"nimi":"Lasagne", "tyyppi": 1, "terveys": True, "helppo": False},
    {"nimi":"Broilerikiusaus", "tyyppi": 2, "terveys": True, "helppo": True},
    {"nimi":"Makaronilaatikko", "tyyppi": 1, "terveys": True, "helppo": True},
    {"nimi":"Kermainen broileripata", "tyyppi": 2, "terveys": True, "helppo": False},
    {"nimi":"Perunasosepelti", "tyyppi": 1, "terveys": True, "helppo": True},
    {"nimi":"Spagetti", "tyyppi": 1, "terveys": True, "helppo": True},
    {"nimi":"Tonnikalasalaatti", "tyyppi": 3, "terveys": True, "helppo": True},
    {"nimi":"Tonnikalanuudelit", "tyyppi": 3, "terveys": False, "helppo": True},
    {"nimi":"Fetasalaatti", "tyyppi": 4, "terveys": True, "helppo": True},
    {"nimi":"Fetanuudelit", "tyyppi": 4, "terveys": False, "helppo": True},
    {"nimi":"Uunimakkara", "tyyppi": 1, "terveys": False, "helppo": True},
    {"nimi":"Pizza", "tyyppi": 1, "terveys": False, "helppo": False},
    {"nimi":"Paistettu koipi + lisuke", "tyyppi": 2, "terveys": True, "helppo": True}
]

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

while True:

    print("Mitä söit eilen, tarvitseeko tämän päivän ruuan olla terveellistä (1/0) ja tarvitseeko sen olla helppoa (1)")
    print("Eilisen ruuan vaihtoehdot ovat 'k' = kanaruoka, 'f' = kalaruoka, 'l' = punainen liha, 'v' = vege")
    print("Syöte esim: f01 (eilen kalaa, tänään ei terveellistä ja helppoa) tai k (eilen kanaa, tänään ei terveellistä")
    print("ja helppoudella ei väliä) tai v1 (eilen vegeruokaa, tänään terveellistä ja helppoudella ei väliä)")
    print("Tee koko viikon ruokalista syötteellä 'vk'")
    print("")
    valinta = input("Syötteesi: ")

    if valinta == "k":
        kaikki_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["tyyppi"] != 2]
        print("Tälle päivälle suosittelen: " + str(random.choice(kaikki_ruuat)))
    elif valinta == "k1" or valinta == "k10":
        terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["helppo"] and ruoka["tyyppi"] != 2]
        print("Tälle päivälle suosittelen: " + str(random.choice(terveelliset_ruuat)))
    elif valinta == "k11":
        helpot_ja_terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["helppo"] and ruoka["terveys"] and ruoka["tyyppi"] != 2]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ja_terveelliset_ruuat)))
    elif valinta == "k01":
        helpot_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["terveys"] and ruoka["tyyppi"] != 2]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ruuat)))

    elif valinta == "f":
        kaikki_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["tyyppi"] != 3]
        print("Tälle päivälle suosittelen: " + str(random.choice(kaikki_ruuat)))
    elif valinta == "f1" or valinta == "f10":
        terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["helppo"] and ruoka["tyyppi"] != 3]
        print("Tälle päivälle suosittelen: " + str(random.choice(terveelliset_ruuat)))
    elif valinta == "f11":
        helpot_ja_terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if
                                        ruoka["helppo"] and ruoka["terveys"] and ruoka["tyyppi"] != 3]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ja_terveelliset_ruuat)))
    elif valinta == "f01":
        helpot_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["terveys"] and ruoka["tyyppi"] != 3]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ruuat)))

    elif valinta == "l":
        kaikki_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["tyyppi"] != 1]
        print("Tälle päivälle suosittelen: " + str(random.choice(kaikki_ruuat)))
    elif valinta == "l1" or valinta == "l10":
        terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["helppo"] and ruoka["tyyppi"] != 1]
        print("Tälle päivälle suosittelen: " + str(random.choice(terveelliset_ruuat)))
    elif valinta == "l11":
        helpot_ja_terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if
                                        ruoka["helppo"] and ruoka["terveys"] and ruoka["tyyppi"] != 1]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ja_terveelliset_ruuat)))
    elif valinta == "l01":
        helpot_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["terveys"] and ruoka["tyyppi"] != 1]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ruuat)))

    elif valinta == "v":
        kaikki_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["tyyppi"] != 4]
        print("Tälle päivälle suosittelen: " + str(random.choice(kaikki_ruuat)))
    elif valinta == "v1" or valinta == "v10":
        terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["helppo"] and ruoka["tyyppi"] != 4]
        print("Tälle päivälle suosittelen: " + str(random.choice(terveelliset_ruuat)))
    elif valinta == "v11":
        helpot_ja_terveelliset_ruuat = [ruoka['nimi'] for ruoka in ruokaData if
                                        ruoka["helppo"] and ruoka["terveys"] and ruoka["tyyppi"] != 4]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ja_terveelliset_ruuat)))
    elif valinta == "v01":
        helpot_ruuat = [ruoka['nimi'] for ruoka in ruokaData if ruoka["terveys"] and ruoka["tyyppi"] != 4]
        print("Tälle päivälle suosittelen: " + str(random.choice(helpot_ruuat)))

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


