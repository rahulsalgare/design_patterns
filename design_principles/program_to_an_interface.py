"""Program to an interface, not an implementation(page 43)."""
from abc import ABC, abstractmethod


class Employee(ABC):
    """Interface"""

    @abstractmethod
    def do_work(self):
        pass


class Designer(Employee):
    def do_work(self):
        print('Designing')


class Programmer(Employee):
    def do_work(self):
        print('Programming')


class Tester(Employee):
    def do_work(self):
        print('Testing')


class Artist(Employee):
    def do_work(self):
        print('Drawing characters...')


class Company(ABC):
    @abstractmethod
    def get_employees(self):
        pass

    def create_software(self):
        print('Creating software...')
        employees = self.get_employees()
        for employee in employees:
            employee.do_work()


class GameDevCompany(Company):
    def get_employees(self):
        return [Designer(), Artist(), Programmer(), Tester()]


class SoftwareCompany(Company):
    def get_employees(self):
        return [Programmer(), Tester()]



if __name__ == '__main__':
    comp = GameDevCompany()
    comp.create_software()