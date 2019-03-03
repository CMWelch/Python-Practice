import random

suits = ("Spades", "Hearts", "Clubs", "Diamonds")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10,  'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck = ""
        for card in self.deck:
            deck += card.__str__()
        return deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:
    def __init__(self, name, chips=100):
        self.name = name
        self.chips = chips
        self.cards = []
        self.total = 0
        self.aces = 0

    def bet(self, bet):
        self.chips -= bet

    def new_hand(self):
        self.cards = []

    def win(self, win):
        self.chips += win

    def hand(self, card):
        if card.rank == "Ace":
            self.aces += 1

        self.cards.append(card)
        self.total += values[card.rank]
        while self.total > 21 and self.aces:
                self.total -= 10
                self.aces -= 1

    def __str__(self):
        hand = []
        for card in self.cards:
            hand.append(f"{card.__str__()}: {values[card.rank]}")
        string = "\n".join(hand)
        return f"{self.name}'s hand: \n{string}"



