a = int(input("Zadejte délku strany a:"))
if a > 0:
    V = a*a*a
    S = 6*a*a
    print ("Objem krychle je", V, ", povrch krychle je", S)
else:
    print ("Error.")