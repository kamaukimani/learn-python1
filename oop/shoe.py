print("Welcome to the Shoe class")
class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size

    @property
    def size(self):
        """the size property"""
        return self._size
    @size.setter
    def size(self,size):
        """the size must be an integer"""
        if isinstance(size,int) and 1 <= size <= 10:
            print(f"Setting size to: {size}")
            self._size=size
        else:
            raise TypeError(f"Size must be an integer between 1 and 10 not ==> {size}")
    @size.deleter
    def size(self):
        raise AttributeError("Why delete the size? What shoe doesnt have a size?")
    def cobble(self):
        self.condititon="New"
        print(f"You {self.brand} is as good as new!!!!")
adidas=Shoe("Adidas",9)
nike=Shoe("Nike",5)
nike.cobble()