import time

print("Vítej v programu pro vytvoření seznamu jmen\n")

seznam_jmen = []

zadane_jmeno = False

konec = zadane_jmeno == "Konec" or zadane_jmeno == "konec" or zadane_jmeno == ""
while konec == False:

    zadane_jmeno = input("Zadejte jméno: ")
    seznam_jmen.append(zadane_jmeno)
    konec = zadane_jmeno == "Konec" or zadane_jmeno == "konec" or zadane_jmeno == ""

seznam_jmen.pop()
print("\nZadaný seznam: ",", ".join( repr(e) for e in seznam_jmen ))

seznam_jmen.sort()
print("\nSežazený seznam: ",", ".join( repr(e) for e in seznam_jmen ))

input("\nPro ukončení programu stiskni - Enter")
time.sleep(3)