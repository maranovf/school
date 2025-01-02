vstup = float(input("Zadejte číslo od -100 do 100:"))
vstup2 = input("Jste žena nebo muž:")
vstup3 = float(input("Zadejte číslo pro dělení čísla 10:"))
if vstup % 1 == 0:
    print ("Je celé číslo.")
else:
    print ("Není celé číslo.")
if vstup > 100:
    print ("Vstup je větší než 100.")
if vstup < -100:
    print ("Vstup je menší než -100.")
if vstup % 2 == 0:
    print ("Číslo je celé sudé.")
else:
    print ("Číslo je liché.")
if vstup2 == "žena" or vstup2 == "muž":
    print()
else:
    print ("Chyba. Musí být žena nebo muž.")
if 10 % vstup3 != 0:
    print ("Číslo 10 není dělitelné  číslem", vstup3)
if 10 % vstup3 == 0:
    print ("Číslo 10 je dělitelné číslem", vstup3)
else:
    print ("Někde je jinbá chyba.")
exit