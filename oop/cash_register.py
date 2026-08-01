print("Tuckle CashRegister")
class CashRegister:
    def __init__(self,discount=0):
        self.discount=discount
        self.total=0
        self.items=[]
        self.previous_transactions=[]
    def add_items(self,item,price,quantity=1):
        self.total +=price*quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item":item, "price":price, "quantity":quantity
        })
    def apply_discount(self):
        if self.discount:
            self.total=int(self.total*((100-self.discount)/100))
            print(f"After the discount the total comes to: {self.total}")
        else:
            print("The is no discount to apply")
    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void"
        self.total -=(
            self.previous_transactions[-1]["price"] 
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()

#book=CashRegister(0)
book=CashRegister(20)
book.add_items("Learn Javascript",5000,3)
#book.apply_discount()
print(book.items)
print(f"The total is: {book.total}")
print(book.previous_transactions)
print('.........Book 1................')
book.add_items("Learn React",2000,2)
book.apply_discount()
print(book.items)
print(f"The total is: {book.total}")
print(book.previous_transactions)
print('.........Book 2................')
lucky_charms=CashRegister(5)
lucky_charms.add_items("Lucky Charm",4.5)
lucky_charms.apply_discount()
print(f"The total is: {lucky_charms.total}")
