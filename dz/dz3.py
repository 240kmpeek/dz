import random


class Pet:
    def __init__(self, name, gladness=50, hunger=50):
        self.name = name
        self.gladness = gladness
        self.hunger = hunger

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        self.gladness += 5

    def play(self):
        self.gladness += 10


class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pets = {}


    def get_home(self):
        self.home = Home()


    def get_car(self):
        self.car = Auto(brands_of_car)


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5


    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4



    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("FUEL BRO")
            self.money -= 5000
            self.car.fuel += 100
        elif manage == "food":
            print("YEAH EAT")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("delicacies!!!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15



    def chill(self):
        self.gladness += 15
        self.home.mess += 5



    def clean(self):
        self.gladness -= 5
        self.home.mess += 0


    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today is a {day} off {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")


        pet_indexes = "Pet Indexes"
        print(f"{pet_indexes:^50}", "\n")
        for pet_name, pet in self.pets.items():
            print(f"{pet_name}:")
            print(f"hunger - {pet.hunger}")
            print(f"gladness - {pet.gladness}")



    def is_alive(self):
        if self.gladness<0:
            print("Depression...")
            return False
        if self.satiety<0:
            print("dead")
            return False
        if self.money<- 500:
            print("Bankrut...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.days_indexes(day)
        dice = random.randint(1, 6)
        if dice == 1:
            print("time to chill")
            self.chill()
        elif dice == 2:
            print("time to work")
            self.work()
        elif dice == 3:
            print("time to clean")
            self.clean()
        elif dice == 4:
            print("time to shopping")
            self.shopping(manage="delicacies")
        elif dice == 5:
            pet_name = random.choice(list(self.pets.keys()))
            self.interact_with_pet(pet_name, "play")
        elif dice == 6:
            pet_name = random.choice(list(self.pets.keys()))
            self.interact_with_pet(pet_name, "feed")


        for pet_name, pet in self.pets.items():
            pet_action = random.choice(["feed", "play"])
            if pet_action == "feed":
                pet.feed()
                print(f"{self.name} fed {pet_name}.")
            elif pet_action == "play":
                pet.play()
                print(f"{self.name} played with {pet_name}.")

    def add_pet(self, pet_name):
        if pet_name not in self.pets:
            self.pets[pet_name] = Pet(pet_name)

    def interact_with_pet(self, pet_name, action):  #
        if pet_name in self.pets:
            pet = self.pets[pet_name]
            if action == "feed":
                pet.feed()
                print(f"{self.name} fed {pet_name}.")
            elif action == "play":
                pet.play()
                print(f"{self.name} played with {pet_name}.")
            # Вывод состояния питомца после взаимодействия
            print(f"{pet_name}'s state:")
            print(f"hunger - {pet.hunger}")
            print(f"gladness - {pet.gladness}")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("CAR SHIIIT ON")
            return False


class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java dev": {"salary": 50, "gladness_less": 10},
    "Python dev": {"salary": 40, "gladness_less": 3},
    "Rust dev": {"salary": 70, "gladness_less": 1},
    "C++ dev": {"salary": 45, "gladness_less": 25}
}


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "vedrocar": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

hum = Human(name="Vasya")

hum.add_pet("Kesha mladshiy")
hum.add_pet("Kesha")

for day in range(1, 8):
    if hum.live(day) == False:
        break

hum.interact_with_pet("Kesha mladshiy", "feed")
hum.interact_with_pet("Kesha mladshiy", "play")
hum.interact_with_pet("Kesha", "feed")
hum.interact_with_pet("Kesha", "play")