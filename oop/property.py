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