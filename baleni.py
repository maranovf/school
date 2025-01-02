c = int (input("Kolik potřebujete dlaždic?"))
b = c/32
v = b + 1
if b > 0:
    if b < 4:
        auto = "Na jejich převezení je potřeba osobní automobil."
    if b > 3 and b < 10:
        auto = "Na jejich převezení je potřeba osobní auto s vozíkem."
    if b > 9 and b < 26:
        auto = "Na jejich převezení je potřeba dodávka."
    if b > 25 and b < 50:
        auto = "Na jejich převezení je potřeba kamion."
    if b > 49:
        auto = "Na jejich převezení je potřeba dvou a víc kamionů."


    print ("Počet dlaždic:", c, "Počet balení včetně 1 rezervního je", v, ".", auto)
if c < 1:
    print ("Nelze vypočítat. Počet dlaždic mudí být větší než nula.")
    exit