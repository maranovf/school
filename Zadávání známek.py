clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') #Smazaní konzole#
print("Výtejte v programu na zadávání známek")                          #Pozdrav#

seznam = []                                                             #Seznam#
x = "xd"

while x != "konec" or x != "Konec" or x != "" or x != " ":              #Loop pro zadávání známek#
    x = input("\nZadejte známku: ")
    clearConsole()
    if x == "konec" or x == "Konec" or x == "" or x == " ":             #Kontrola ukončení loopu#
        break
    try:                                                                #Error controll#
        x = int(x)
        if x >= 1 and x <= 5:
            seznam.append(x)                                            #Připsání zadané známky na seznam#
        else:
            print("Zadané číslo není v rozmezí běžného známkování")

    except ValueError:
        print("\nNezadal jsi číslo, skus to znovu")

print("\nZadaný seznam: ",", ".join( repr(e) for e in seznam ))         #Vypsání seznamu v hezčím provedení#

tridicka = input("\nPro seřazení známek zadejte - Seřadit / Pro statistiku - statistika / ukončení programu zmáčkněte - Enter\n")

serazeni = tridicka == "Seřadit" or tridicka == "seřadit" or tridicka == "seradit" or tridicka == "Seradit"

if serazeni == True:                                                    #Seřazení známek#
    clearConsole()
    seznam.sort()
    print("\nSeřazený seznam: ", ", ".join(repr(e) for e in seznam))
    input("\nPro statistiku - statistika / pro ukončení programu zmáčkněte - Enter")
    time.sleep(2)

koneckonec = tridicka == "statistika" or tridicka == "Statistika"       #Možnosti ukončení#
if koneckonec == False:
    exit()

clearConsole()
pocet_znamek = len(seznam)                                              #Počet zadanýcg známek#
if pocet_znamek == 0:                                                   #Debug s nezadaním ani jendé známky#
    print("Nezadal jsi známky, nelze vypočítat statistiku")
    input("Pro ukončení zmáčkněte - Enter")

                                                                        #Spočítání známek#
jednicky = seznam.count(1)
dvojky = seznam.count(2)
trojky = seznam.count(3)
ctyrky = seznam.count(4)
petky = seznam.count(5)
                                                                        #Tabulka se známkami#
print("Počet jedniček:", jednicky," |  ", round(100/pocet_znamek*jednicky),"%")
print("Počet dvojek:", dvojky,"   |  ", round(100/pocet_znamek*dvojky),"%")
print("Počet trojek:", trojky,"   |  ", round(100/pocet_znamek*trojky),"%")
print("Počet čtyřek:", ctyrky,"   |  ", round(100/pocet_znamek*ctyrky),"%")
print("Počet pětek:", petky,"    |  ", round(100/pocet_znamek*petky),"%")

prumer = 0                                                              #Součet známek#
for i in range(pocet_znamek):
    prumer_cislo = seznam.pop()
    prumer = prumer + prumer_cislo

prumer = prumer / pocet_znamek                                          #Vytvoření průměru
print("\nPrůměr:",round(prumer,2))

tridicka = input("\nPro ukončení programu zmáčkněte - Enter")           #Finální konec#
time.sleep(3)
