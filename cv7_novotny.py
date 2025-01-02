autor = []
kniha = []
class Autor:
    def data(self, autor):
        n = input("Jméno autora:")
        ln = input("Příjmení autora:")
        a = int(input("Věk autora:"))
        autor.append(n)
        autor.append(ln)
        autor.append(a)
    def data_add(self, autor):
        a_b = input("Zadejte jméno knížky:")
        autor.append(a_b)
class Kniha:
    def data_kniha(self, kniha):
        v = input("Vazba:")
        nol = int(input("Počet stran:"))
        ISBN = int(input("ISBN:"))
        py = int(input("Rok vydání:"))
        d = input("Popis:")
        z = input("Žánr:")
        c = int(input("Cena:"))
        kniha.append(v)
        kniha.append(nol)
        kniha.append(ISBN)
        kniha.append(py)
        kniha.append(d)
        kniha.append(z)
        kniha.append(c)
a = Autor
a.data(Autor, autor)
a.data_add(Autor, autor)
k = Kniha
k.data_kniha(Kniha, kniha)
print(autor, kniha)