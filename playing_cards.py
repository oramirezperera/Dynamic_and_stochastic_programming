import random
import collections
from enum import IntEnum

TYPES = ['spades', 'hearts', 'diamonds', 'clubs']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #1 represents A, 11, 12, and 13 represents J, Q, K


def create_card(): #this function is to create the playing cards with the two list above
    playing_card = []
    for ctype in TYPES: #Ctype means card type refering to diamonds, etc.
        for cvalue in VALUES: #cvalue means the card value
            playing_card.append((ctype, cvalue))
    
    return playing_card


def get_hand(playing_card, hand_size): #give you a hand of cards
    hand = random.sample(playing_card, hand_size) #sample doesn't let you repeat the randomness

    return hand


def main(hand_size, tries):
    playing_card = create_card()

    hands = []

    for _ in range(tries):
        hand = get_hand(playing_card, hand_size)
        hands.append(hand)

    pairs = 0

    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])

        counter = dict(collections.Counter(values)) #Counter is a collections class 
        
        for val in counter.values():
            if val == 2:
                pairs += 1
                break
    

           
    pair_probability = pairs / tries
    print(f'The probability of getting a pair in one hand of {hand_size} playing cards is {pair_probability}')
    


def is_straight(hand_size, tries):

    playing_card2 = create_card()
    hands = []

    for _ in range(tries):
        straight_hand = get_hand(playing_card2, hand_size)
        hands.append(straight_hand)

    straights = 0

    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])
        counter = dict(collections.Counter(values))
        sorted_values = sorted(values)

        i = 0 
        while((sorted_values[i] - sorted_values[i+1]) == -1): #this checks if it's a straight
            i += 1
            if i == len(sorted_values) - 1:
                straights += 1
                break
    
    straights_probability = straights / tries
    print(f'The probability of getting a straight in one hand of {hand_size} is {straights_probability}')
        


if __name__ == '__main__':
    hand_size = int(input('How many cards are the hands in this game? '))
    tries = int(input('How many tries to calculate the probability? '))
    main(hand_size, tries)
    is_straight(hand_size, tries)