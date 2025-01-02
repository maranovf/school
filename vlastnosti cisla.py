c = int (input("Zjištění vlastností čísla:"))
if c < 1000 and c > 99:
    print ("Číslo je tříciferné.")
if c < 100 and c  > 9:
    print ("Číslo je tříciferné")
if c < 10 and c > -10:
    print ("Číslo je jednociferné.")
if c == 1000:
    print ("Číslo je čtyřciferné.")
if c < 0:
    print ("Číslo je záporné.")
if c > 0:
    print ("Číslo je kladné.")
else:
    print ("Nelze vyřešit")