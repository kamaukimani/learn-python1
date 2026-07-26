print("Handle class dog")
approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
class Dog:
    def __init__(self,name="Fido",breed="Mastiff"):
        self.name=name
        self.breed=breed
        # print(f"The dogs name is: {name}")
        # print(f"The dogs breed is: {breed}")
    def get_name(self):
        print("Retrieving the name")
        return self._name 
    def set_name(self,name):
        if(type(name)is str) and (1<=len(name)<=25):
            print(f"Setting name to: {name}")
            self._name=name
        else:
            print(f"{name} <== must be a string between 1 and 25 characters")
    name=property(get_name,set_name)
    def get_breed(self):
        print("Retrieving the dogs breed")
        return self._breed 
    def set_breed(self,breed):
        if breed in approved_breeds:
            print(f"Setting breed to: {breed}")
            self._breed=breed 
        else:
            print(f"{breed} <== must be in list of approved breeds")
    breed=property(get_breed,set_breed)
fido=Dog("Fido","Beagle")
figo=Dog("sdsdjksdjkkksjksdjksdjksdjksd")
tiger=Dog("Tiger","Kiniuru")
        