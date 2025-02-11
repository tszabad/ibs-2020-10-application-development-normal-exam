from fish import Fish, Tang, Clownfish, Kong

class Aquarium():
    def __init__(self):
        self.fishes = []

    def add_fish(self, fish):
        self.fishes.append(fish)

    def feed(self):
        for i in self.fishes:
            i.feed()
    
    def remove_fish(self):
        for i in self.fishes:
            if i.get_weight() >= 11:
                self.fishes.remove(i)

    def get_status(self):
        for i in self.fishes:
            i.status()


