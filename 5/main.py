import deck, sys
from miniutils import *

cards = deck.Deck()
numbers = cards.get_numbers()
current_card = cards.draw()
for i in range(5):
    new_card = cards.draw()
    higher = miniInput(bool,
          f"This is round {i+1}. The current card is the {current_card['number']} of {current_card['suit']}"
          f"\nTrue or False, the next card will be higher?",
          errorMessage = "Please enter either True or False")
    if numbers.index(new_card['number']) > numbers.index(current_card['number']):
        print(f"Unlucky... Both cards had the same value. You lose on round "+str(i+1))
        sys.exit()
    elif higher and numbers.index(new_card['number']) > numbers.index(current_card['number']):
        print(f"YAY! The new card is the {new_card['number']} of {new_card['suit']} which is higher than the previous one. You have made it to round "+str(i+2))
    elif not higher and numbers.index(new_card['number']) < numbers.index(current_card['number']):
        print(f"YAY! The new card is the {new_card['number']} of {new_card['suit']} which is lower than the previous one. You have made it to round "+str(i+2))
    else:
        print(f"OOPS... The new card is the {new_card['number']} of {new_card['suit']}. You lose on round "+str(i+1))
        sys.exit()
    current_card = new_card
print("Yay! you made it through all 5 rounds!!! YOU WIN!")
        
