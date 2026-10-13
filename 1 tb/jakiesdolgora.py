dol= 1
gora= 100
trafiony= False

print("pomysl liczba 1 do 100")
print("")
while trafiony != True:
    srodek= (dol+gora)//2

    print("czy twoja liczba to",srodek)
    odpowiedz= input("wypisz m -mniejsza, w- wieksza, t- trafiona.")

    if odpowiedz =="t":
        print("zgadlem")
        dol=gora +1
        trafiony = True
    elif odpowiedz =="m":
        gora= srodek -1

    elif odpowiedz =="w":
        dol= srodek +1
        
