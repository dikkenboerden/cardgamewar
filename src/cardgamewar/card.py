from dataclasses import dataclass, field
from typing import ClassVar
import cardgamewar.config as config

@dataclass
class Card:
    suit :str
    rank :str

    _value: int = field(init=False, repr=False)

    def __post_init__(self):
         self.value = self.rank

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, myrank):
        self._value = config.values[myrank]

    @value.deleter
    def value(self):
        del self._value

if __name__ == '__main__':
    card = Card('hearts','Two')
    print(card.suit)
    print(card.rank)
    print(card.value)