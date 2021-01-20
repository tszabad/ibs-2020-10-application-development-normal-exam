from fish import Fish, Tang, Clownfish, Kong,

class Aquarium():
    def __init__(self):
        self.fishes = []

    def addFish(self, fish):
        self.fishes.append(fish)

    def feed(self):
        for i in self.fishes:
            i.feed()
    
    def removeFish(self):
        for i in self.fishes:
            if i.weight >= 11:
                self.fishes.remove(i)

    def get_status(self):
        for i in self.fishes:
            i.status()


