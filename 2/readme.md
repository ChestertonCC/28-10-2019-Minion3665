## Task 2: Anagram solver
> - Get the user to input a word 
> - Create a loop that repositions each letter into a new position in the word 
> - Decide on which of the different sorting methods that you know, that might help you do this

[Run the code](https://Anagram-Solver.minion3665.repl.run)
#### Hints:
<details>
  <summary>Hint #1</summary>
  
  ```python
  import itertools
  ```
  
  Try importing the itertools module to allow you to get all the possible arrangements of your input
</details>
<details>
  <summary>Hint #2</summary>
  
  ```python
  ang = input("Type an anagram: ")
  ```
  
  Get your user to give you a string as their original word
</details>
<details>
  <summary>Hint #3</summary>
  
  ```python
  ang1 = ["".join(perm) for perm in itertools.permutations(ang)]
  ```
  
  Join together all the different permutations (arrangements) of the letters
</details>
<details>
  <summary>Hint #4</summary>
  
  ```python
  input(ang1)
  ```
  
  Give the permutations back to the user
</details>
