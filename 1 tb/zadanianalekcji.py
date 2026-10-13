import random
proba= 1
wynikmn = 0
imie = input("podaj imie= ")
print(f" witaj {imie} ")

wylosowana = random.randint(1,20)
wylosowana2 = random.randint(1,20)
wynikpoprawny= wylosowana*wylosowana2
while wynikmn != wynikpoprawny and proba <=3:
    print(f" {wylosowana} * {wylosowana2}")
    wynikmn=int(input("podaj wynik mnozenia = "))
    proba += 1
    if wynikmn == wynikpoprawny:
        print(f" brawo {imie} {wynikmn} to poprawny wynik")
    else:
        print(f" zle {imie} {wynikmn} to nie poprawny wynik")

        

if proba == 2 and wynikmn == wynikpoprawny:
        print(f"zrobiles/as za pierszym razem {imie} dostajesz ocene 6")
elif proba== 3 and wynikmn == wynikpoprawny:
        print(f"zrobiles/as za drugim razem {imie} dostajesz ocene 4")
elif proba== 4 and wynikmn == wynikpoprawny:
         print(f"zrobiles/as za trzecim razem {imie} dostajesz ocene 2")
else:
        print("brak poprawnej odpowiedzi dostajesz 1")



