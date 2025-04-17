class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = (self.hunger-3) if self.hunger > 2 else self.hunger
        self.happiness = (self.happiness+1) if self.happiness < 10 else self.happiness

    def sleep(self):
        self.energy = (self.energy+5) if self.energy < 6 else self.energy


    def play(self):
        self.energy = (self.energy-2) if self.energy > 1 else self.energy
        self.happiness = (self.happiness+2) if self.happiness > 1 else self.happiness
        self.hunger = (self.hunger+1) if self.hunger < 10 else self.hunger


    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"\n{self.name}'s Tricks")
        print(f'{self.tricks}')
    
    def get_status(self):
        print(f'Name: {self.name}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}')
    
