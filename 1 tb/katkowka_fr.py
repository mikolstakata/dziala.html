import random
liczba=0
proba=0
wylosowana = random.randint(1,10)
while liczba != wylosowana and proba <=3:
    liczba= int(input("podaj liczbe 1 do 10= "))

    if liczba == wylosowana:
        print(f" {liczba} to prawidlowa liczba brawo zgadles")
    elif liczba > wylosowana:
            print (f"liczba {liczba} jest za duza")
    else:
            print(f"liczba {liczba} jest za mala")
