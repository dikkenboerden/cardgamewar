from dataclasses import dataclass, field
from cardgamewar.card import Card

@dataclass()
class Player:
    name : str
    all_cards : list = field(default_factory=list,repr=True)

    def remove_one(self) -> Card:
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)}'

if __name__ == '__main__':
    player = Player('Louis')
    print(player)
    p = Player('Jan')
    c1 = Card('Hearts', 'Two')
    c2 = Card('Spades', 'Six')
    new_cards = [c1, c2]
    p.add_cards([c1, c2])
    print(p.all_cards)

    names = ['Nicholas', 'Michelle', 'Alex']
    copyNames = list(names)
    bla = names
    print(bla)
    names.pop(0)
    print(bla)
    print(copyNames)
