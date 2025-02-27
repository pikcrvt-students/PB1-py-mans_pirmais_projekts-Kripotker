from random import randint
import time
import sys

def print_animation(text, delay=0.1, repeat=1):
    """Prints a simple animation where the text prints with a delay."""
    for _ in range(repeat):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print('')  
        time.sleep(0.5)  

print('Datorspēle "Uzmini skaitli".')
print('Dators "Iedomajas" veselu skaitli no 1 līdz 10. ', end='\n\n')
print('Uzmini skaitli. ')


Datora_skaitlis = randint(1, 10)


countdown = ['3', '2', '1']
for number in countdown:
    print_animation(number, 0.5)


neuzmineja = True
while neuzmineja:
    ievade = input('Ievadiet skaitli no 1 līdz 10, ieskaitot 10: ')
    
    try:

        Cilveka_skaitlis = int(ievade)
    except ValueError:

        print('Lūdzu, ievadiet derīgu skaitli!')
        continue
    
    if Cilveka_skaitlis < Datora_skaitlis:
        print_animation('Neuzminējāt. Ievadiet lielāku skaitli. ', 0.1)
    elif Cilveka_skaitlis > Datora_skaitlis:
        print_animation('Neuzminējāt. Ievadiet mazāku skaitli. ', 0.1)
    else:

        neuzmineja = False
print('     ____.                                                  __  __')   
print('    |    |__ __  ______  __ _____________  _______ _______ |__|/  |_ ')
print('    |    |  |  \/  ___/ |  |  \___   /\  \/ /\__  \\_  __ \|  \   __\ ')
print('/\__|    |  |  /\___ \  |  |  //    /  \   /  / __ \|  | \/|  ||  |   ')
print('\________|____//____  > |____//_____ \  \_/  (____  /__/\__|  ||__|  ')
print('                    \/              \/            \/   \______| ')
print('Paldies, ka spēlējāt!')
