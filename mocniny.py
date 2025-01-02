c = int (input ("Zadejte číslo:"))
m = int (input ("Zadejte maximum:"))
s = []
mocnina = c * c
s.append(mocnina)
mc = 0
mn = mocnina + mc
while mn < m:
    my = mn * c
    s.append(my)
    mn = mc + my
max = max(s)
if max > m:
    s.remove(max)
print ("Mocniny čísla", c, "jsou", s)