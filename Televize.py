zapnuto = False
aktualniKanal = 1
w = 0
if zapnuto == False:
    s = input("Chcete zapnout televizi?(a/n):")
    if s == "a":
        print("Televize je nyní zapnutá.")
        zapnuto = True
        while w == 0:
            print("Aktuální kanál:", aktualniKanal)
            v = input("Chcete vypnout televizi? (a/n):")
            if v == "a":
                w = w + 1
                zapnuto = False
                print("Televize je nyní vypnutá.")
                break
            k = int(input("Kanál, na který chcete přepnout:"))
            if k > 0:
                aktualniKanal = k
            if k < 1:
                aktualniKanal = aktualniKanal
            if v == "n":
                pass