

class Pets:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} is playing")
        return self

    def noise(self):
        if self.type == "dog":
            print("Bark")
        if self.type == "cat":
            print("Meow")
        if self.type == "bird":
            print("Chirp")
        if self.type == "cow":
            print("MOOOOOO")
        return self
    