c = int(input("Zadejte cenu výrobku:"))
d = int(input("Kolik % je DPH?"))
if d == 21:
    f1 = c / 100
    f = f1 * d
    ce = c + f
    print ("Cena s DPH je", ce, "Kč, daň je", f, "Kč.")
if d == 15:
    f1 = c / 100
    f = f1 * d
    ce = c + f
    print ("Cena s DPH je", ce, "Kč, daň je", f, "Kč.")
if d == 10:
    f1 = c / 100
    f = f1 * d
    ce = c + f
    print ("Cena s DPH je", ce, "Kč, daň je", f, "Kč.")
if d == 0:
    print ("Cena je", c, ", daň žádná není.")
if d < 21 and d > 15:
    print ("DPH může být letos pouze 21, 15, 10 nebo 0 procent!")
if d < 15 and d > 10:
    print ("DPH může být letos pouze 21, 15, 10 nebo 0 procent!")
if d < 10 and d > 0:
    print ("DPH může být letos pouze 21, 15, 10 nebo 0 procent!")
if d < 0:
    print ("DPH může být letos pouze 21, 15, 10 nebo 0 procent!")
if d > 21:
    print ("DPH může být letos pouze 21, 15, 10 nebo 0 procent!")