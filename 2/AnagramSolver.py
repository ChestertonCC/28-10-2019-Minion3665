import itertools
ang = input("Type an anagram: ")
ang1 = ["".join(perm) for perm in itertools.permutations(ang)]
input(ang1)
