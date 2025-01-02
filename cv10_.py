import time
t = time.localtime()
by = int(input("Zadejte rok narození:"))
bm = int(input("Zadejte měsíc narození:"))
bd = int(input("Zadejte den narození:"))
y = t[0]
m = t[1]
d = t[2]
h = t[3]
yl = y - by
ml = m - bm
dl = d - bd
ytd = yl * 365
dim = 365 / 12
mtd = ml * dim
dit = ytd + mtd + dl
sl = dit * 86400
print("Jste staří", dit, "dnů, nebo", sl, "sekund.")