sz = []
pv = 0
a = 0
while a == 0:
    z = input ("Zadejte jméno žáka:")
    if z == "":
        break
    v = int (input ("Zadejte věk žáka:"))
    sz.append(z)
    pv = pv + v
if pv > 0:
    psz = len(sz)
    pvz = pv / psz
    print (sz, pvz)