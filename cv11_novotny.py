import random as r
a = 1
s = 0
pcs = 0
while a > 0:
    i = input("Zadejte kámen/nužky/papír:")
    li = i.lower()
    rn = r.randint(0, 2)
    if rn == 0:
        pcch = "kámen"
        if li == "kámen":
            print("Nikdo nevyhrál! Zvolil jsem taky kámen.")
        if li == "nůžky":
            pcs = pcs + 1
            print("Prohrál jsi! Zvolil jsem kámen")
        if li == "papír":
            s = s + 1
            print("Vyhrál jsi! Zvolil jsem kámen")
    if rn == 1:
        pcch = "nůžky"
        if li == "kámen":
            s = s + 1
            print("Vyhrál jsi! Zvolil jsem kámen.")
        if li == "nůžky":
            print("Nikdo nevyhrál! Zvolil jsem taky nůžky.")
        if li == "papír":
            pcs = pcs + 1
            print("Prohrál jsi! Zvolil jsem nůžky.")
    if rn == 2:
        pcch = "papír"
        if li == "kámen":
            pcs = pcs + 1
            print("Prohrál jsi! Zvolil jsem papír.")
        if li == "nůžky":
            s = s + 1
            print("Vyhrál jsi! Zvolil jsem papír.")
        if li == "papír":
            print("Nikdo nevyhrál! Zvolil jsem taky papír.")
    if li == "konec":
        print("Vaše skóre:", s, "Skóre počítače:", pcs)
        break
exit