class Pet:
    PET_TYPES=["dog","cat","rodent","bird","reptile","exotic"]
    all=[]
    pet_count=0
    def __init__(self,name,pet_type):
        if self.check_pet_type(pet_type):
            self.increase_pet_count()
            self.name=name
            self.pet_type=pet_type
            self.write_log(name,pet_type)
            self._owner=None
            Pet.all.append(self)
        else:
            raise TypeError("The type of pet must be in the list of pet types")
    @classmethod
    def check_pet_type(cls,pet_type):
        return pet_type in cls.PET_TYPES
    @classmethod
    def increase_pet_count(cls):
        cls.pet_count +=1
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        if not isinstance(value,Owner):
            raise TypeError("owner must be an instance of the Owner class")
        self._owner=value
    def write_log(self,name,pet_type):
        with open("owner_pet.txt","a") as file:
            file.write(f"{self.name} of type {self.pet_type} has been successfully created \n")
    
class Owner:
    def __init__(self,name):
        self.name=name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("pet must be an instance of the Pet class")
        pet.owner=self
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

pet1=Pet("Fido","dog")
pet2=Pet("Smalla","cat")
for pet in Pet.all:
    print(pet.name,pet.pet_type)
owner1=Owner("Guido")
owner1.add_pet(pet1)
owner1.add_pet(pet2)
print(owner1.pets())
for pet in owner1.pets():
    print(f"Pet name is: {pet.name} || Pet type is: {pet.pet_type}")

pet3=Pet("Parot","bird")
owner2=Owner("Rossum")
owner2.add_pet(pet3)
print(f"We have {Pet.pet_count} pets")

print(owner1.get_sorted_pets())