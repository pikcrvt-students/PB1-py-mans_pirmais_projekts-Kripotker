import random

print('Akmens skeres papirs uzvaresanas noteikumi ir sadi:\n'
      + "Akmens vs Papirs -> Papirs Uzvar \n"
      + "Akmens vs Skeres -> Akmens Uzvar \n"
      + "Papirs vs Skeres -> Skeres Uzvar \n")

while True:

    print("Ievadi savu izveli: \n 1 - Akmens \n 2 - Papirs \n 3 - Skeres \n")

    choice = int(input("Ievadi savu izveli: "))

    while choice > 3 or choice < 1:
        choice = int(input('Ievadi derigu izveli: '))

    if choice == 1:
        choice_name = 'Akmens'
    elif choice == 2:
        choice_name = 'Papirs'
    else:
        choice_name = 'Skeres'

    print('Lietotāja izvēle ir:', choice_name)
    print("Datora izvele ir...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Akmens'
    elif comp_choice == 2:
        comp_choice_name = 'Papirs'
    else:
        comp_choice_name = 'Skeres'

    print("Datora izvele ir:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = "Neizskirts"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'Papirs'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'Akmens'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'Skeres'

    if result == "Neizskirts":
        print("<== Neizskirts! ==>")
    elif result == choice_name:
        print("<== Lietotājs uzvar! ==>")
    else:
        print("<== Dators uzvar! ==>")

    print("Vēlaties spēlēt vēlreiz? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Paldies ka spēlēji!")
