# 5_init_false.py
from dataclasses import dataclass, field

@dataclass
class Vehicle:

    wheelzs: int
    _wheels: int = field(init=False, repr=False)

    @property
    def wheelzs(self) -> int:
        print("getting wheels")
        return self._wheels

    @wheelzs.setter
    def wheelzs(self, wheelzs: int):
        print("setting wheels to", wheelzs)
        self._wheels = wheelzs

if __name__ == '__main__':
    v = Vehicle(6)
    print (v.wheelzs)
