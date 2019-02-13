#blackjack
#Dean Church
#Period 2

class Card(object):
    RANKS = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []

    def __str(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep
    def clear(self):
        self.cards = []


    def add(self, card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Can't continue deal. Out of cards")

class Unprintable_Card(Card):
    def __str__(self):
        return"<unprintable>"

class Positionable_Card(Card):
    def __init__(self,rank,suit,face_up = True):
        super(Positionable_Card,self).__init__(rank,suit)
        self.is_face_up = face_up

    def _str_(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep













if __name__=="__main__":
    print("You ran this module directly )and did not 'import' it")
    input("\n\nPress the enter key to exit")
