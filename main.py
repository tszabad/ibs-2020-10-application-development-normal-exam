from fish import *
from aquarium import Aquarium

def main():
    aquarium = Aquarium()
    fish = Tang("Bubble", 3, "grey", False)
    fish2 = Clownfish("Nemo", 4, "red", "blue")
    fish3 = Kong("Sirilla", 5, "azure")
    fish4 = Kong("Moby", 11, "green")

    fish.feed()
    fish2.feed()
    fish3.feed()

    fish.status()
    fish2.status()
    fish3.status()
    fish4.status()

    aquarium.add_fish(fish)
    aquarium.add_fish(fish2)
    aquarium.add_fish(fish3)
    aquarium.feed()
    aquarium.remove_fish()
    aquarium.get_status()


if __name__ == "__main__":
    main()