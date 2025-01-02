import datetime
import random
s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "t", "y", "x", "z", "u", "w", "r"]
v = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "T", "Y", "X", "Z", "U", "W", "R"]
n = datetime.datetime.now()
chck = hash(n)
while chck > 0:
    r1 = random.choice(s)
    r2 = random.choice(v)
    R = r1, r2
    h1 = hash(n)
    h2 = h1/10000000000000
    h3 = round(h2)
    break
print (r1, h3, r2)