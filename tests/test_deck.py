from cardgamewar.deck import Deck
from cardgamewar.card import Card

def test_construction():
    d = Deck()
    mydeck = [Card(suit='Hearts', rank='Two'), Card(suit='Hearts', rank='Three'), Card(suit='Hearts', rank='Four'), Card(suit='Hearts', rank='Five'), Card(suit='Hearts', rank='Six'), Card(suit='Hearts', rank='Seven'), Card(suit='Hearts', rank='Eight'), Card(suit='Hearts', rank='Nine'), Card(suit='Hearts', rank='Ten'), Card(suit='Hearts', rank='Jack'), Card(suit='Hearts', rank='Queen'), Card(suit='Hearts', rank='King'), Card(suit='Hearts', rank='Ace'), Card(suit='Diamonds', rank='Two'), Card(suit='Diamonds', rank='Three'), Card(suit='Diamonds', rank='Four'), Card(suit='Diamonds', rank='Five'), Card(suit='Diamonds', rank='Six'), Card(suit='Diamonds', rank='Seven'), Card(suit='Diamonds', rank='Eight'), Card(suit='Diamonds', rank='Nine'), Card(suit='Diamonds', rank='Ten'), Card(suit='Diamonds', rank='Jack'), Card(suit='Diamonds', rank='Queen'), Card(suit='Diamonds', rank='King'), Card(suit='Diamonds', rank='Ace'), Card(suit='Spades', rank='Two'), Card(suit='Spades', rank='Three'), Card(suit='Spades', rank='Four'), Card(suit='Spades', rank='Five'), Card(suit='Spades', rank='Six'), Card(suit='Spades', rank='Seven'), Card(suit='Spades', rank='Eight'), Card(suit='Spades', rank='Nine'), Card(suit='Spades', rank='Ten'), Card(suit='Spades', rank='Jack'), Card(suit='Spades', rank='Queen'), Card(suit='Spades', rank='King'), Card(suit='Spades', rank='Ace'), Card(suit='Clubs', rank='Two'), Card(suit='Clubs', rank='Three'), Card(suit='Clubs', rank='Four'), Card(suit='Clubs', rank='Five'), Card(suit='Clubs', rank='Six'), Card(suit='Clubs', rank='Seven'), Card(suit='Clubs', rank='Eight'), Card(suit='Clubs', rank='Nine'), Card(suit='Clubs', rank='Ten'), Card(suit='Clubs', rank='Jack'), Card(suit='Clubs', rank='Queen'), Card(suit='Clubs', rank='King'), Card(suit='Clubs', rank='Ace')]
    assert mydeck == d.all_cards

def test_deal_one():

    assert True

def test_shuffle_deck():
    d = Deck()
    mydeck = [Card(suit='Hearts', rank='Two'), Card(suit='Hearts', rank='Three'), Card(suit='Hearts', rank='Four'),
              Card(suit='Hearts', rank='Five'), Card(suit='Hearts', rank='Six'), Card(suit='Hearts', rank='Seven'),
              Card(suit='Hearts', rank='Eight'), Card(suit='Hearts', rank='Nine'), Card(suit='Hearts', rank='Ten'),
              Card(suit='Hearts', rank='Jack'), Card(suit='Hearts', rank='Queen'), Card(suit='Hearts', rank='King'),
              Card(suit='Hearts', rank='Ace'), Card(suit='Diamonds', rank='Two'), Card(suit='Diamonds', rank='Three'),
              Card(suit='Diamonds', rank='Four'), Card(suit='Diamonds', rank='Five'), Card(suit='Diamonds', rank='Six'),
              Card(suit='Diamonds', rank='Seven'), Card(suit='Diamonds', rank='Eight'),
              Card(suit='Diamonds', rank='Nine'), Card(suit='Diamonds', rank='Ten'), Card(suit='Diamonds', rank='Jack'),
              Card(suit='Diamonds', rank='Queen'), Card(suit='Diamonds', rank='King'),
              Card(suit='Diamonds', rank='Ace'), Card(suit='Spades', rank='Two'), Card(suit='Spades', rank='Three'),
              Card(suit='Spades', rank='Four'), Card(suit='Spades', rank='Five'), Card(suit='Spades', rank='Six'),
              Card(suit='Spades', rank='Seven'), Card(suit='Spades', rank='Eight'), Card(suit='Spades', rank='Nine'),
              Card(suit='Spades', rank='Ten'), Card(suit='Spades', rank='Jack'), Card(suit='Spades', rank='Queen'),
              Card(suit='Spades', rank='King'), Card(suit='Spades', rank='Ace'), Card(suit='Clubs', rank='Two'),
              Card(suit='Clubs', rank='Three'), Card(suit='Clubs', rank='Four'), Card(suit='Clubs', rank='Five'),
              Card(suit='Clubs', rank='Six'), Card(suit='Clubs', rank='Seven'), Card(suit='Clubs', rank='Eight'),
              Card(suit='Clubs', rank='Nine'), Card(suit='Clubs', rank='Ten'), Card(suit='Clubs', rank='Jack'),
              Card(suit='Clubs', rank='Queen'), Card(suit='Clubs', rank='King'), Card(suit='Clubs', rank='Ace')]
    d.shuffle_deck()
    assert mydeck != d.all_cards
