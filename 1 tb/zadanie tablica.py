bartek=[]
daw=[]
kac=[]

ile= int(input("bartus ile masz ocen"))
suma_bartek=0
for i in range(ile):
     ocena= int(input("podaj ocene"))
     bartek.append(ocena)
     suma_bartek+=ocena
srednia_bartek=suma_bartek/len(bartek)

ile= int(input("daw ile masz ocen"))
suma_daw=0
for i in range(ile):
     ocena= int(input("podaj ocene"))
     daw.append(ocena)
     suma_daw+=ocena
srednia_daw=suma_daw/len(daw)

ile= int(input("kac ile masz ocen"))
suma_kac=0
for i in range(ile):
     ocena= int(input("podaj ocene"))
     kac.append(ocena)
     suma_kac+=ocena
srednia_kac=suma_kac/len(kac)

print("srednia bart",srednia_bartek)
print("srednia bart",srednia_daw)
print("srednia bart",srednia_kac)

