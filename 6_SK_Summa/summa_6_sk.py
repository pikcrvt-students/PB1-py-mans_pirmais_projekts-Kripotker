"""
sešu skaitļu summa.
izveidoja:Krists Krupniks

"""

print("sešu skaitļu summa")
print()
summa = 0
for x in range (6): # skaitītājs no 0 līdz 6 (6 neieskaitot)
    skaitlis = int(input('ievadiet ' + str(x+1) + ' veselu skaitli: '))
    summa = summa + skaitlis # summas aprekins

print ("\nSumma ir", summa) #izvada rezūltātu
