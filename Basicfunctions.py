# Kolumnien nimet
data.columns

# Tarkistetaan datan muoto (pituus (rivimäärä), leveys (kolumnit))
data.shape

# Enemmän informaatiota datasta, edellisten lisäksi myös datatyypit ja NaN-määrät
data.info()

# Tietoa kolumneista, min, max, mean, std jne.
data.describe()

# Kolumnin datatyyppi
data['kolumnin nimi'].dtype

# Tarkistetaan dataryhmän kolumnin keskiarvo ja keskihajonta
data['kolumnin nimi'].mean()
data['kolumnin nimi'].std()

# Tarkistetaan kahden kolumnin välinen korrelaatio
data["kolumnin nimi"].corr(data["kolumnin nimi"])

# Tulosta kaikki data tiedostosta (ilman print-käskyä tulostus on epäformatoitua)
print(data.to_string())

# Tarkistetaan montako arvoa tietyllä kolumnin arvolla datasta löytyy
data["kolumnin nimi"].value_counts()

# To.String() funktiota voidaan soveltaa esim. näin yllä olevaan
print(data["kolumnin nimi"].value_counts().to_string())

# Tulostaa kaikki kolumnin saamat arvot
data["kolumnin nimi"].unique()
