from abc import ABC, abstractmethod 
class Fish(ABC):
    def __init__(self,name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def get_weight(self):
        return self.weight

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def feed(self):
        pass
class Clownfish(Fish):
    def __init__(self,name, weight, color, second_color):
        super().__init__(name, weight, color)
        self.second_color = second_color

    def status(self):
            print(f"{self.__class__.__name__} type of fish, {self.name}, weight: {self.weight}, color: {self.color}, color of the stripes: {self.second_color}")

    def feed(self):
        self.weight += 1


class Tang(Fish):
    def __init__(self, name, weight, color, short_memory = True):
        super().__init__(name, weight, color)
        self.short_memory = short_memory

    def status(self):
            print(f"{self.__class__.__name__} type of fish, {self.name}, weight: {self.weight}, color: {self.color}, short-term memory loss: {str(self.short_memory).lower()}")

    def feed(self):
        self.weight += 1


class Kong(Fish):
    def __init__(self,name, weight, color):
        super().__init__(name, weight, color)
    
    def status(self):
            print(f"{self.__class__.__name__} type of fish, {self.name}, weight: {self.weight}, color: {self.color}")

    def feed(self):
        self.weight += 2



    