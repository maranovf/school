v = int(input("Zadejte váš věk:"))
if v < 60:
    di = 55-v
    print ("Do důchodu vám zbývá", di, "let")
if v > 60:
    di = v-560
    print ("Do předčasného důchodu vám zbývá", di, "let")
else:
    print ("Nelze vypočítat")