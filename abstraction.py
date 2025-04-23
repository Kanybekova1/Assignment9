from abc import abstractmethod, ABC

class Shape:
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,name):
        self.name=name
