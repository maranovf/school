import random
m = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
v = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
c = ["0", "1", "2", "3", "4", "5","6", "7","8","9"]
z = [".", "@"]
A = [m, v, c, z]
ra1 = random.choice(A)
RA1 = random.choice(ra1)
ra2 = random.choice(A)
RA2 = random.choice(ra2)
ra3 = random.choice(A)
RA3 = random.choice(ra3)
ra4 = random.choice(A)
RA4 = random.choice(ra4)
ra5 = random.choice(A)
RA5 = random.choice(ra5)
ra6 = random.choice(A)
RA6 = random.choice(ra6)
ra7 = random.choice(A)
RA7 = random.choice(ra7)
ra8 = random.choice(A)
RA8 = random.choice(ra8)
heslo = RA1 + RA2 +RA3 + RA4 + RA5 + RA6 + RA7 +RA8
print ("Vygenerované heslo je:", heslo)