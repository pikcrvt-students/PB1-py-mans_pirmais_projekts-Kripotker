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
        print('')  # This creates a newline after each animation cycle.
        time.sleep(0.5)  # Short pause between repetitions of the text.

print('Datorspēle "Uzmini skaitli".')
print('Dators "Iedomajas" veselu skaitli no 1 līdz 10. ', end='\n\n')
print('Uzmini skaitli. ')

# Generate a random number between 1 and 10.
Datora_skaitlis = randint(1, 10)

# ASCII countdown animation
countdown = ['3', '2', '1', 'Start!']
for number in countdown:
    print_animation(number, 1)

# Game loop
neuzmineja = True
while neuzmineja:
    ievade = input('Ievadiet skaitli no 1 līdz 10, ieskaitot 10: ')
    
    try:
        # Try to convert the input to an integer.
        Cilveka_skaitlis = int(ievade)
    except ValueError:
        # If input is not an integer, prompt again.
        print('Lūdzu, ievadiet derīgu skaitli!')
        continue
    
    if Cilveka_skaitlis < Datora_skaitlis:
        print_animation('Neuzminējāt. Ievadiet lielāku skaitli. ', 0.1)
    elif Cilveka_skaitlis > Datora_skaitlis:
        print_animation('Neuzminējāt. Ievadiet mazāku skaitli. ', 0.1)
    else:
        # If the guess is correct, break the loop.
        neuzmineja = False
        print_animation('Uzminējāt!!!', 0.2, 2)
        print('Paldies, ka spēlējāt!')
