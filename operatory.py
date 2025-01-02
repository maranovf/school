cislo = int(input("Zadejte číslo v rozmezí 0-10: "))

if ((cislo > -3) and (cislo <= 10)):

    print("Správně!")

if ((cislo < -3) or (cislo == -3)):

    print("Špatně!")
else:
    print("Špatně")