import itertools
import string
import random
def get_shuffled_cards():
    suits=["clubs (♣)", "diamonds (♦)", "hearts (♥)","spades (♠)"]
    ranks=list(string.digits)[2:]+["10","A","J","Q","K"]
    card_deck=list(itertools.product(ranks,suits))
    card_deck_s=random.sample(card_deck,len(card_deck))
    return card_deck_s
class Deck:
    suits=["clubs (♣)", "diamonds (♦)", "hearts (♥)","spades (♠)"]
    ranks=list(string.digits)[2:]+["10","A","J","Q","K"]
    def __init__(self, available=list(itertools.product(ranks,suits)), spent=[]):
        self.available = available
        self.spent = spent

    def shuffle(self):
        print(random.sample(self.available,len(self.available)))
        return
    def get_cards(self,count=1):
        self.spent=list(random.sample(self.available,count))
        return
my_deck=Deck()
print(my_deck.shuffle())
print(my_deck.get_cards(2))
