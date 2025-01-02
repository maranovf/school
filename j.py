import random
s = ([1, 2, 3])
r = random.choice(s)
i = int (input("Vyber si: - Kámen (1) - Nůžky (2) - papír (3)"))
if r == 1 and i == 3:
    print ("Vyhrál jsi. Já jsem zvolil kámen")
if r == 3 and i == 2:
    print ("Vyhrál jsi. Já jsem zvolil papír.")
if r == 2 and i == 1:
    print ("Vyhrál jsi. Já jsem zvolil nůžky.")
else:
    print ("Prohrál jsi, nebo jsme dali stejnou věc.")