print("Relationships in objects")
#association
class GroceryItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Shopper:
    def __init__(self,name):
        self.name=name
        self.grocery_items=[]  #storing GroceryItem objects

shopper=Shopper("Alice")
item1=GroceryItem("Apple",30)
item2=GroceryItem("Orange",20)
shopper.grocery_items.append(item1)
shopper.grocery_items.append(item2)
for item in shopper.grocery_items:
    print(item.name,item.price)