l = []
x = 0
while x > -1:
    i = input("Zadejte položku:")
    if i == "exit":
        break
    l.append(i)
    x = x + 1
print(l)
print(max(l))
print(min(l))
print(len(l))