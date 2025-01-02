
print("Vítej v programu pro nalezení největšího čísla v seznamu\n")

seznam_cisel = []

zadane_cislo = False

konec = zadane_cislo == "Konec" or zadane_cislo == "konec" or zadane_cislo == ""
while konec == False:

    zadane_cislo1 = input("Zadejte číslo: ")
    try:
        zadane_cislo = int(zadane_cislo1)
    except ValueError:
        break
    seznam_cisel.append(zadane_cislo)

print("\nZadaný seznam: ",", ".join( repr(e) for e in seznam_cisel ))
seznam_cisel_1 = seznam_cisel
print("\nNejvětší číslo je:",max(seznam_cisel))

input("Pro ukončení programu zmáčkněte - Enter")
