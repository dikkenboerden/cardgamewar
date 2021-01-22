from dataclasses import dataclass, field
from typing import ClassVar

values = {'Two':2, 'Three':3,
          'Four':4, 'Five':5,
          'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':11,
          'Queen':12, 'King':13,
          'Ace':14}

@dataclass
class Vehicle():
    print('init called')
    spokes: str
    wheels: int
    _value: int = 0
    value: int = 0
    print('after init')
    #_value: int = 0
    #values: list = field(default_factory=list)
    #_wheels: int = field(init=False, repr=False)
    #_spokes: int = field(init=False, repr=False)

    # def __post_init__(self):
    #     print('calling post init')
    #     self.value = self.spokes

    @property
    def value(self) ->int:
        print('return')
        return self._value

    @value.setter
    def value(self, sps: str):
        print('setter called')
        self._value = values[sps]
        print('after setter')

if __name__ == '__main__':
    v = Vehicle('Five',5)
    print (v.wheels)
    print (v.spokes)
    print (v.value)


