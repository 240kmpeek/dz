import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 100)
        self.energy = random.randint(0, 100)
        self.happiness = random.randint(0, 100)

    def eat(self):
        food = random.randint(10, 30)
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

    def sleep(self):
        sleepiness = random.randint(10, 30)
        self.energy += sleepiness
        if self.energy > 100:
            self.energy = 100

    def play(self):
        fun = random.randint(10, 30)
        self.happiness += fun
        if self.happiness > 100:
            self.happiness = 100

    def is_hungry(self):
        return self.hunger > 50

    def is_tired(self):
        return self.energy < 30

    def is_happy(self):
        return self.happiness > 70

    def live_a_day(self):
        if self.is_hungry():
            self.eat()
        elif self.is_tired():
            self.sleep()
        else:
            self.play()

    def __str__(self):
        return f"{self.name}: голод - {self.hunger}, Енергия - {self.energy}, Радость - {self.happiness}"



cat = Cat("васька")

for day in range(random.randint(1, 366)):
    cat.live_a_day()
    print(f"День  этом мире: {day}: {cat}")
    if not cat.is_happy() or cat.hunger == 100:
        print(f"{cat.name} заикнулся и умер.")
        break
