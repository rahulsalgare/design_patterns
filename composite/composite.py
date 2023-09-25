from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass


# Leaf class
class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"drawing dot at {self.x, self.y}")


# Leaf class
class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Drawing circle at {self.x, self.y} with radius {self.radius}")


# Composite class
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children: list[Graphic] = []

    def add(self, child: Graphic):
        self.children.append(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()


if __name__ == '__main__':
    """
            root_cg
             /
         child_cg
           /  \
        dot    circle 
    
    """
    root_cg = CompoundGraphic()
    child_cg = CompoundGraphic()
    dot = Dot(1, 2)
    circle = Circle(4, 5, 6)

    child_cg.add(dot)
    child_cg.add(circle)

    root_cg.add(child_cg)
    root_cg.draw()
