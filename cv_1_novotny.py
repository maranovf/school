n = input("Zadejte jméno:")
d = len(n)
if d < 11:
    with open ("jmeno.txt", "w", encoding="utf-8") as s:
        s.write(n)
else:
    print("Jméno nelze zapsat. Má více než deset znaků.")