class Geometrie:
    def Ctverec(self):
        a = int(input("Zadejte délku strany a:"))
        S = a*a
        print("Obsah čtverce je", S)
    def Obdelnik(self):
        a = int(input("Zadejte délku strany a:"))
        b = int(input("Zadejte délku strany b:"))
        S = a*b
        print("Obsah obdélníku je", S)
    def Ball(self):
        r = int(input("Zadejte poloměr koule:"))
        V = 4/3 * 3.14 * r ** 3
        print("Objem koule je", V)
    def Valec(self):
        r = int(input("Zadejte průměr základny:"))
        v = int(input("Zadejte výšku válce:"))
        V = 3.14 * r ** 2 * v
        print("Objem válce je", V)
    def Prumer(self):
        d = int(input("Zadejte průmšr:"))
        r = d / 2
        print("Poloměr je", r)
G = Geometrie
G.Ctverec(Geometrie)
G.Obdelnik(Geometrie)
G.Ball(Geometrie)
G.Valec(Geometrie)
G.Prumer(Geometrie)