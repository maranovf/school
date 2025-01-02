print("Textový editor 2022")
print ("1 - vytvoř nový textový soubor")
print ("2 - přidej text")
print ("3 - přečti text")
print ("4 - konec")
m = int(input("Vyberte si jednu z možností:"))
if m == 1:
    with open("data.txt", "w", encoding="utf-8") as d:
        pass
if m == 2:
    t = input("Zadejte text:")
    with open("data.txt", "a", encoding="utf-8") as d:
        d.write(t)
if m == 3:
    with open("data.txt", "r", encoding="utf-8") as d:
        for r in d.readlines():
            print(r.strip())
            input("Stiskněte jakékoliv tlačítko pro pokračování.")
if m == 4:
    exit