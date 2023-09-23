from abc import ABC, abstractmethod
from typing import Any


class Car:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def display_car(self):
        print(f"{'+'.join(self.parts)}")


class Manual:
    pass


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, n):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def set_seats(self, n):
        self._car.add(f"{n} seats")

    def set_engine(self):
        self._car.add("engine")

    def set_trip_computer(self):
        self._car.add("computer")

    def set_gps(self):
        self._car.add("gps")

    @property
    def product(self):
        product = self._car
        self.reset()
        return product


class CarManual(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._carmanual = CarManual()

    def set_seats(self, n):
        pass

    def set_engine(self):
        pass

    def set_trip_computer(self):
        pass

    def set_gps(self):
        pass

    @property
    def product(self):
        product = self._carmanual
        self.reset()
        return product


class Director:
    def __init__(self):
        self._builder = None

    # @property
    # def builder(self):
    #     return self._builder
    #
    # @builder.setter
    # def builder(self, builder: Builder) -> None:
    #     self._builder = builder

    def construct_sports_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine()
        builder.set_trip_computer()
        builder.set_gps()

    def construct_normal_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(4)
        builder.set_engine()


if __name__ == '__main__':
    director = Director()
    builder = CarBuilder()

    # get normal car
    director.construct_normal_car(builder)
    builder.product.display_car()

    # get sports car
    director.construct_sports_car(builder)
    builder.product.display_car()
