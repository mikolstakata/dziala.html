import random
proby=0
for i in range(3):
    liczba = random.randint(1,10)
    odpowiedz= int(input("podaj liczbe ="))
    if liczba == odpowiedz:
        print(f"brawo {liczba} to prawidllowa liczba")
    elif liczba > odpowiedz:
        print("liczba jest zbyt mala")
    else:
        print("liczba za wielka")
    



   
