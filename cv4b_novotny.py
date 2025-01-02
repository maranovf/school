import random as r
gchoice = []
l = 3
slova = [1, "hra", "python", "programování", "počítač", "monitor"]
while l > 0:
    g = input("Zadejte slovo:")
    print("Počet životů:", l)
    ind = r.randint(1, 5)
    solution = slova[ind]
    gchoice.append(solution)
    print (solution)
    if g == solution:
        print("Správně")
        break
    if g != solution and l > 0:
        l = l - 1
if l == 0:
    print("Prohrál jsi! Správná slova byla", gchoice)