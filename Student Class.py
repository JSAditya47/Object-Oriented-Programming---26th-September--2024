class Fruit:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
apple = Fruit("Appy", "Red")
print(apple.name)
print(apple.color)

orange = Fruit("Orangie", "Orange")
print(orange.name)
print(orange.color)

#================================================


class Student:
    grade = 10
    print(f"Hi I am a Student of Grade {grade}")
    
obj = Student()

