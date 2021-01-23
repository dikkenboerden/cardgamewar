from dataclasses import dataclass, field
import random
import cardgamewar.config as config
from cardgamewar.card import Card
from typing import List

@dataclass()
class Deck:
    _all_cards : List[Card] = field(init=False, repr=False, default_factory=list)

    def __post_init__(self):
        for suit in config.suits:
            for rank in config.ranks:
                created_card = Card(suit,rank)
                self._all_cards.append(created_card)

    @property
    def all_cards(self) -> []:
        return self._all_cards

    def shuffle_deck(self) -> []:
        random.shuffle(self.all_cards)

    def deal_one(self) -> Card:
        return self.all_cards.pop()

if __name__ == '__main__':
    deck = Deck()
    print(deck.all_cards)
    first_card = deck.all_cards[0]
    bottom_card = deck.all_cards[-1]
    print(first_card)
    print(bottom_card)
    deck.shuffle_deck()
    print(deck.all_cards)
    my_card = deck.deal_one()
    print(my_card)



