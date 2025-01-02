import random
pc = 40
a = 80
x = 0
print("Výtejte v programu na hledání čísel v seznamu, aktuální počet čísel v seznamu je: ", pc)
seznam = [x for x in range(pc)]                     #Seznam od do proměné pc#
nahodny_seznam = []                                 #Seznam na náhodné přeházení#

hledane = input("\nZadej hledáné číslo:")           #Zadávání čísla#
try:                                                #Eror problém řešení#
    hledane = int(hledane)
    hledane_cislo = 0
except ValueError:
    print("\nNezadal jsi číslo, skus to znovu")
    time.sleep(2)
    exit()

kontrola = hledane in seznam                        #Kontrola zadaného čísla#

if kontrola == True:
    kojot = "je"
else:
    kojot = "\nZadané číslo není v seznamu"
    print(kojot)
    time.sleep(2)
    exit()

for i in range(pc):                                 #Přeházení z seznam do nahodny_seznam#
    nahodne_cislo = random.choice(seznam)
    seznam.remove(nahodne_cislo)
    nahodny_seznam.append(nahodne_cislo)

seznam_kontrola = nahodny_seznam

while a != hledane:                                 #Počítání pozice v seznamu#
    a = nahodny_seznam.pop(0)
    x = x + 1

print("\nHledané číslo", kojot, "v seznamu", "na", x, "místě")

konec = input("\nPro vypsání seznamu zadejte - seznam / ukončení programu zmáčkněte - Enter\n")

vypsani_seznamu = konec == "seznam" or konec == "Seznam"

if vypsani_seznamu == True:
    print("\nSeznam čísel je: ", seznam_kontrola)
    input("\nPro ukončení programu zmáčkněte - Enter")