#learn object oriented programming
class Dog:
    def bark(self):
        print("Whooaf!!!")
    def sit(self):
        print("The dog is sitting")
fido=Dog()
fido.bark()
fido.sit()
class Person:
    def __init__(self,name):
        self.name=name
        print(f"Hello {name}")
    def talk(self):
        print("Hello World!")
    def walk(self):
        print("The person is walking")
john=Person("John")
print(john.name)
john.talk()
john.walk()
class Dog1:
    def __init__(self,name,breed="Mutt"):
        self.name=name
        self.breed=breed
        print(f"{name} is born!")
    def bark(self):
        print("Woof!!")
fido1=Dog1("Fido")
print(fido1.name)
fido1.bark()
print(fido1.breed)