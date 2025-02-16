class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Smalldog(Dog):
    def __init__(self, height):
        pass
dog1 = Dog("Rufus", 3)
