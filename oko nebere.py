from random import randrange
s = 0
while s == 0:
    o = int (input("Na jaké číslo chceš vsadit?"))
    a = randrange (0, 38)
    if o == a:
        print ("Vyhrál jsi.")
    elif o == "nechci":
        break
    else:
        print ("Nevyhrál jsi.")
if o == a:
    print ("Gratuluji! Vyhrál jsi hlavní cenu.")
else:
    print ("Smůla.")