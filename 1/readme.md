## Task 1: Anagram maker
> - Write code to get the user to input a word<br/>
> - The program should then go through each letter, possibly putting it in an array might help<br/>
> - Each letter should then be randomly positioned into a random position in a new word<br/>
> - Display the new word to the user<br/>

<a href="https://anagrammakerpy.vilagamer999.repl.run/" target="_blank">Run the code</a>

#### Hints:
<details>
  <summary>Hint #1</summary>
  
  ```python
  import random
  ```
  
  Try importing the random module to allow you to randomize your input
</details>
<details>
  <summary>Hint #2</summary>
  
  ```python
  jumble = input("Write a random word: ")
  ```
  
  Get your user to give you a string as their original word
</details>
<details>
  <summary>Hint #3</summary>
  
  ```python
  j = list(jumble)
  random.shuffle(j)
  ```
  
  Use `random.shuffle` to randomize your string. As `random.shuffle` takes a list we will convert our jumble to a list
</details>
<details>
  <summary>Hint #4</summary>
  
  ```python
  input("".join(j))
  ```
  
  Join the list back together and present it to the user
</details>
