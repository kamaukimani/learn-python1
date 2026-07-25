print("Learn  getters and setters")
class Human:
    species="Homo Sapiens"
    def __init__(self,name):
        self.name=name
guido=Human("Guido")
print(guido.species)
print(Human.species)
#changing species and name using dot notation
guido.species="Python programmer"
guido.name="Guido van"
print(guido.species)
print(guido.name)
#adding new attributes using dot notation
guido.nationality="Dutch"
print(guido.nationality)
print(guido)
print(Human)
name=getattr(guido,"name") # returns the attribute if present
print(name)
name1=setattr(guido,"name","Guido van Rossum") #when successful returns ==>none
print(guido.name)
name2=hasattr(guido,"name") # returns ==>true<== if attribute is present and ==>false<== if attribute is absent
print(name2)
setattr(guido,"age",30)
print(guido.age)
delattr(guido,"age") #deletes the attribute from the object
#print(guido.age)
class Human1:
    species="Homo Sapien Sapiens"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_age(self):
        print(f"Retrieving age")
        return self._age
    def set_age(self,age):
        print(f"Setting age to {age}")
        self._age=age
    age=property(get_age,set_age)
guido1=Human1("Guido",30)
print(guido1.age)
guido.age=42
print(guido.age)
guido1.get_age()
guido1.set_age(54)
class Human2:
    species="Homo Erectus"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_age(self):
        print("Retrieving the age")
        return self._age
    def set_age(self,age):
        if(type(age)in(int,float)) and (0<=age<=120):
            print(f"Setting age to {age}")
            self._age=age 
        else:
            print(f"{age} must be a number between 0 and 120")
    age=property(get_age,set_age)
guido2=Human2(name="Guido",age=66)
guido2.get_age()
guido2.age="Alice"
guido2_age=guido2.get_age()
print(guido2_age)
setattr(guido2,"age",122)

