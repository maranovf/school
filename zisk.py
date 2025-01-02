n = int(input("Zadejte nákupní cenu:"))
p = int(input("Zadejte prodejní cenu:"))
if n > p:
    c = n - p
    z = n/100
    z1 = p/z
    print ("Prodělal jsi", c, "Kč, to je", z1, "%.")
if n < p:
    c = p - n
    z = p/100
    z1 = n/z
    print ("Vydělal jsi", c, "Kč, to jsou zisky", z1, "%.")
else:
    print("Nelze vypočítat!")