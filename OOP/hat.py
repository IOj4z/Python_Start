import random


class Hat:
    def __int__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    def sort(self, name):
        print(name, "is in ", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")