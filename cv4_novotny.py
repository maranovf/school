n = int(input("Zadejte číslo:"))
if (n % 2) == 0:
    if (n % 5) == 0:
        print("Číslo je dělitelné 2 a 5.")
    else:
        print("Číslo je dělitelné 2.")
if (n % 5) == 0:
    if (n % 2) != 0:
        print("Číslo je dělitelné pěti, ale není dělitelné 2.")
    else:
        pass
else:
    print("Číslo není dělitelné 2 ani 5.")
n2 = int(input("Zadejte druhé číslo:"))
s = n + n2
m = n * n2
print("Součet obou čísel je", s, "a jejich násobek je", m, ".")
ss = str(s)
ms = str(m)
with open("výsledky.txt", "w", encoding="utf-8") as v:
    v.write(ss)
    v.write(ms)