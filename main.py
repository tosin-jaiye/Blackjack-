# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_dealer_turn():
    hand_value = 0
    i = 0
    while i < 2:
        card = randint(1, 13)
        card_name = draw(card)
        print(f"{card_name}")
        hand_value += card_value(card)
        i += 1
    if hand_value < 17:
        print(f"Dealer has {hand_value}.")

    while hand_value < 17:
        card = randint(1, 13)
        card_name = draw(card)
        print(f"{card_name}")
        hand_value += card_value(card)
        if hand_value < 17:
            print(f"Dealer has {hand_value}.")

    if hand_value == 21:
        return "Blackjack!"
    elif hand_value > 21:
        return "BUST"
    else:
        return(f"Final hand: {hand_value}.")
    
    return blackjack_or_bust


play_dealer_turn()
