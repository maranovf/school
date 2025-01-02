a = int(input("Zadejte velikost strany a:"))
b = int(input("Zadejte velikost strany b:"))

if a > 0 and b > 0:
    S = a*b
    O = 2*(a*b)
    print ("Obsah je", S, "a obvod je", O)
else:
    print ("Nelze vypočítat")