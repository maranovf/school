import math
a = int(input("Zadejte a:"))
b = int(input("Zadejte b:"))
c = int(input("Zadejte c:"))
if a < 0:
    exit
class Rovnice:
    def x(self, a, b, c):
        d = b ** 2 - 4 * a * c
        D = math.sqrt(d)
        x = -b + D
        X = x/2*a
        print (X)
rovnice = Rovnice
rovnice.x(Rovnice, a, b, c)