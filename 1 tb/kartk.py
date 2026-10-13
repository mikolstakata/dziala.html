import math
dlugosc_pokoju= float(input("dlugosc pokoju="))
szerokosc_pokoju= float(input("szerokosc pokoju="))
wysokosc_pokoju= float(input("wysokosc pokoju="))
sciana1=dlugosc_pokoju*wysokosc_pokoju
sciana2=dlugosc_pokoju*wysokosc_pokoju
sciana3=szerokosc_pokoju*wysokosc_pokoju
sciana4=szerokosc_pokoju*wysokosc_pokoju
powierzchnia_scian=sciana1+sciana2+sciana3+sciana4
cena_farby=15
wydajnosc_farby=13
potrzebna_farba=powierzchnia_scian/wydajnosc_farby
koszt_farby=cena_farby*potrzebna_farba

print(f"powierzchnia scian= {powierzchnia_scian}m2 potrzebna ilosc= {potrzebna_farba}l koszt= {koszt_farby} zl")

powierzchnia_scian:math.ceil(4.2)

potrzebna_farba:math.ceil(4.2)

koszt_farby:math.ceil(4.2)
