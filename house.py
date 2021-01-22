from dataclasses import dataclass, field

@dataclass
class House:
    # def __init__(self, price):
    #     self._price = price
    _price: int
    price: int = field(init=False)

    def __post_init__(self):
        self.price = self._price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        print('setter called')
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price

if __name__ == '__main__':
    h = House(23)
    print (h.price)


