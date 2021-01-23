from cardgamewar.player import Player
from cardgamewar.card import Card

def test_construction():
    p = Player('Jan')
    assert 'Jan' == p.name

def test_remove_one():
    assert True

def test_add_one_card():
    p = Player('Jan')
    c = Card('Hearts', 'Two')
    p.add_cards(c)
    assert 'Two' == p.all_cards[0].rank
    assert 'Hearts' == p.all_cards[0].suit

def test_add_two_cards():
    p = Player('Jan')
    c1 = Card('Hearts', 'Two')
    c2 = Card('Spades', 'Six')
    new_cards = [c1, c2]
    p.add_cards(new_cards)
    print(p.all_cards)
    assert 2 == len(p.all_cards)