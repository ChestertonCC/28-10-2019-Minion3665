import string
import random
import threading
import time
from miniutils import *

vowels = {"a", "e", "i", "o", "u"}
consonants = set(string.ascii_lowercase) ^ vowels

seconds = 30

def countdown():
    global seconds
    while seconds:
        time.sleep(1)
        seconds = seconds - 1

t = threading.Thread(target=countdown)
t.daemon = True
t.start()

word = ""
selected = 0
while seconds:
    letter = ""
    selected += 1
    if miniInput(bool,
          f"Selecting letter {selected} with {seconds} seconds to go"
          f"\nDo you want a vowel or a consonant? Enter True for vowel or False for consonant",
          errorMessage = "Please enter either True or False"):
        letter = random.choice(list(vowels))
    else:
        letter = random.choice(list(consonants))
    word = word + letter
    print(f"The letter is {letter}")
print(f"You ran our of time after selecting {len(word)} letters. Your silly word is {word}")
