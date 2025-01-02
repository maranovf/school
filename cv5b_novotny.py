import math

a = int(input("Zadejte a"))
b = int(input("Zadejte b:"))
c = int(input("Zadejte c:"))

d1 = b**2
d2 = 4*a*c
d = d1 + d2

if d == 0:
    x1 = -b/(2*a)
    print("x1 = {}".format(x1))
elif d >0:
    x1 = ((-b)+(math.sqrt(d)))/2*a
    x2 = ((-b)-(math.sqrt(d)))/2*a
    print("x1 = {}".format(x1))
    print("x2=".format(x2))
else:
    print("Rovnice nemá řešení v reálném oboru.")
