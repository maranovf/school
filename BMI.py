va = float (input("Zadejte váhu v Kg:"))
vy = float(input ("Zadejte výšku v metrech:"))
v2y = vy*vy
VY = va/v2y
if VY > 35:
    print ("Máte obezitu.")
if VY < 36 and VY > 29:
    print ("Máte mírnou obezitu.")
if VY > 25 and VY < 30:
    print ("Máte nadváhu.")
if VY > 18.5 and VY < 26:
    print ("Vaše hmotnost je ideální.")
if VY > 16.5 and VY < 18.4:
    print ("Máte podváhu.")
if VY > 0 and VY < 16.5:
    print ("Máte podvýživu.")
if va < 1 or vy < 1:
    print ("Nelze vypočítat.")