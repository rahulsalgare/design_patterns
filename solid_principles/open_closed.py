from abc import ABC, abstractmethod


class Order:
    def __init__(self, ship_class):
        self.__line_items = []
        self.__shipping = ship_class()

    def get_shipping_cost(self):
        return self.__shipping.get_cost(self)

    def get_total(self):
        return 1000  # assume


class Shipping(ABC):
    @abstractmethod
    def get_cost(self, order):
        pass

    @abstractmethod
    def get_date(self, order):
        pass


class Ground(Shipping):
    def get_cost(self, order):
        if order.get_total() > 100:
            return 500  # assume
        else:
            return 800

    def get_date(self, order):
        pass


class Air(Shipping):
    def get_cost(self, order):
        pass

    def get_date(self, order):
        pass


if __name__ == '__main__':
    ship = Ground
    ordr = Order(ship)
    print(ordr.get_shipping_cost())
