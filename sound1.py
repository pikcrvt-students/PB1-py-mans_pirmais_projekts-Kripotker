from winsound import Beep

notes = {'C': 1000}


melodie = 'C'
for note in melodie:
    Beep(notes[note], 500)
