## Task 4: Countdown
> - Create a random array of consonants 
> - Create a random array of vowels 
> - Start a loop for 8 times 
> - Ask the user whether they want a consonant or a vowel 
> - Display the random letter from the consonant or vowel list
> - Complete the loop 
> - Start a 30 second countdown
> - Display the number of seconds
> - Stop and ask the user what the maximum number of letters they have got

[Run the code](https://Countdown.minion3665.repl.run)
#### Hints:
<details>
  <summary>Hint #1</summary>
  
  ```python
  import string
  import random
  import threading
  import time
  from miniutils import *
  ```
  
  Import the string module so that we can get the letters of the alphabet<br/>
  Import random so that we can choose random letters<br/>
  Import threading for a multithreaded timer<br/>
  Import time to count the seconds going past<br/>
  Import miniutils, a program to add utilities to python (currently in development)
</details>
<details>
  <summary>Hint #2</summary>
  
  ```python
  vowels = {"a", "e", "i", "o", "u"}
  consonants = set(string.ascii_lowercase) ^ vowels

  seconds = 30
  ```
  
  Initialize starting variables
  - Vowels are a, e, i, o and u
  - Consonants are everything in the alphabet that aren't vowels
  - Set the time limit
</details>
<details>
  <summary>Hint #3</summary>
  
  ```python
  def countdown():
    global seconds
    while seconds:
      time.sleep(1)
      seconds = seconds - 1

  t = threading.Thread(target=countdown)
  t.daemon = True
  t.start()
  ```
  
  Create a countdown timer on a second thread
</details>
<details>
  <summary>Hint #4</summary>
  
  ```python
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
  ```
  
  Start a loop to choose letters, stop when the time runs out
</details>
<details>
  <summary>Hint #5</summary>
  
  ```python
  print(f"You ran our of time after selecting {len(word)} letters. Your silly word is {word}")
  ```
  
  Display the word to the user
</details>
