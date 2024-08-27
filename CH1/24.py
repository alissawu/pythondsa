#Design a class to represent a playing card and another one to represent a deck of cards.
# Using these two classes, implement your favorite card game.
#Current game: 2048


import random
#card class. this does not generate the card but sets a template
class Card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite
    def __str__(self):
        return f"{self.number} of {self.suite}"

#deck class
#it's not really inheriting, it's just the deck is composed of cards
class Deck:
    #initialize a standard deck of cards
    def __init__(self):
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11/Jack", "12/Queen", "13/King", "1/Ace"]
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        #cards = the array that holds the Card objects
        self.cards = [Card(number, suite) for number in numbers for suite in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    #flip a card and add it in somewhere
    def flip(self, num):
        for _ in range(num):
            top_card = self.cards.pop(0) #pop the top
            print(top_card)
            newposition = random.randint(0, len(self.cards))
            self.cards.insert(newposition, top_card)


def main():
    deck = Deck()
    deck.shuffle()
    deck.flip(4)

# if this is the main file, run the main  
if __name__ == "__main__":
    main()

        