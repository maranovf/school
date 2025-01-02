r = int(input("Napiš, kolik ti je let:"))
d = 65
z1 = d - r
du = r - d
if r < d:
    print ("Ještě v důchodu nejsi! Zbývá ti", z1, "let.")
if r > d:
    print ("Už můžeš být v důchodu", du, "let!")