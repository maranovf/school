from random import randrange
s = 0
while s < 21:
    print ("Máš", s, "bodů.")
    o =input("Otočit kartu?")
    if o == "ano":
        karta = randrange (2, 11)
        print ("Otočil jsi.")
        s = s + karta
    elif o == "ne":
        break
    else:
        print ("Odpovídej ano nebo ne!")
if s == 21:
    print ("Gratuluji! Vyhrál jsi.")
elif s > 21:
    print ("Smůla,", s, "bodů je moc.")
else:
    print ("Chybělo jen", 21 - s, "bodů.")