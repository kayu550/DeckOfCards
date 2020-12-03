import random
class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.suit))
    

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            n = random.randint(0,i)
            self.cards[i], self.cards[n] = self.cards[n], self.cards[i]

    def drawC(self):
        return self.cards.pop()
            

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawC())

    def showHand(self):
        for c in self.hand:
            c.show()

    def discard(self):
        return self.hand.pop()




deck = Deck()
deck.shuffle()

p1 = Player("Bob")
p1.draw(deck)
p1.showHand()
p1.discard()

deck1 = Deck()
card1 = deck1.drawC()
card1.show()
deck1.shuffle()
p2 = Player("New")
p2.draw(deck1)
p2.showHand()
