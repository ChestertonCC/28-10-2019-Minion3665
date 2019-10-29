import random

jumble = input("Write a random word: ")

j = list(jumble)
random.shuffle(j)

input("".join(j))
