class Person:
    def __init__(self, fullName="Kostya", age=19):
        self.fullName = fullName 
        self.age = age 
        
    def move(self):
        print(f"Говорит: {self.fullName}")
        
    def talk(self):
        print(f"Говорит: {self.fullName}, возраст {self.age}")


person_2 = Person()
person_2.move()
person_2.talk()
print("="*27)
person_1 = Person("Olesya", 23)
person_1.move()
person_1.talk()