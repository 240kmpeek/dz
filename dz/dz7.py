class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Прив, я гуль {self.name} и мне {self.age} лет.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} учится в университете с номером студенческого билета {self.student_id}.")

person1 = Person("Haise", 40)
student1 = Student("Toka", 14, "1000-7")

person1.introduce()
student1.introduce()
student1.study()
