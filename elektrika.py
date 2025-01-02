J1 = input("Jednotka 1 (V/A/W):")
H1 = int(input("Hodnota 1:"))
J2 = input("Jednotka 2 (V/A/W):")
H2 = int(input("Hodnota 2:"))
if J1 == "V":
    if J2 == "A":
        w = H1*H2
        print ("Výkon je", w, "wattů.")
        exit
    if J2 == "W":
        a = H2/H1
        print ("Proud je", a, "ampér.")
        exit
    else:
        print ("Nelze vypočítat.")
if J1 == "A":
    if J2 == "V":
        w = H1*H2
        print ("Výkon je", w, "wattů.")
        exit
    if J2 == "W":
        a = H2/H1
        print ("Napětí je", a, "voltů.")
        exit
    else:
        print ("Nelze vypočítat.")
        exit
if J1 == "W":
    if J2 == "A":
        w = H1/H2
        print ("Napětí je", w, "voltů.")
        exit
    if J2 == "V":
        a = H1/H2
        print ("Proud je", a, "ampér.")
        exit
    else:
        print ("Nelze vypočítat.")
        exit
else:
    print ("Nelze vypočítat.")
    exit