print("one-to-many relationship between the owner class and the pet class")
class Owner:
    owner_count=0
    all=[]
    OWNER_COUNTRY=["Kenya","Ethiopia","Rwanda","America","Russia","China"]
    def __init__(self,name,country):
        self.name=name
        self.country=country
        self._pet=None
        self.increase_owner_count()
        self.log_owner(name,country)
        Owner.all.append(self)
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self,country):
        if country not in self.OWNER_COUNTRY:
            raise Exception("Country must be in the list of OWNER_COUNTRY")
        self._country=country
    @property
    def pet(self):
        return self._pet
    @pet.setter
    def pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("pet must be an instance of the Pet class")
        self._pet=pet
    @classmethod
    def increase_owner_count(cls,increment=1):
        cls.owner_count +=increment
    def log_owner(self,name,country):
        with open("owner.txt","a") as file:
            file.write(f"{self.name} from {self.country} created.Total owner instances:{Owner.owner_count} \n")
class Pet:
    #PET_TYPES=["dog","cat","rodent","bird","reptile","exotic"]
    pet_count=0
    def __init__(self,name):
        self.name=name
    # def check_type(self,pet_type):
    #     return pet_type in self.PET_TYPES
    def owners(self):
        return[owner for owner in Owner.all if owner.pet == self]
    def add_owner(self,owner):
        if not isinstance(owner,Owner):
            raise TypeError("owner must be an instance of the Owner class")
        owner.pet=self

owner1=Owner("John","Kenya")

owner2=Owner("Alice","Ethiopia")
owner3=Owner("Guido","America")
owner4=Owner("Doe","Russia")
owner5=Owner("Rossum","Rwanda")

pet1=Pet("Fido")
pet2=Pet("Smalla")
pet3=Pet("Bosco")

owner1.pet=pet1
pet1.add_owner(owner2)
pet2.add_owner(owner3)
#owner4.pet=None
