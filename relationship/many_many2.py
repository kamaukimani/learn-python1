from datetime import datetime
print("Many-to-many with an intermediary class")
print(datetime.now())
print(datetime.now().date())  #.time()

class Author:
    all=[]
    def __init__(self,name):
        self.name=name
        self.log_author(name)
        Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    def log_author(self,name):
        with open("athor.txt","a") as file:
            file.write(f"{self.name} created at {datetime.now().time()} \n")

class Book:
    all=[]
    books_count=0
    def __init__(self,title):
        self.title=title
        self.increase_books()
        self.log_book(title)
        Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]
    @classmethod
    def increase_books(cls):
        cls.books_count +=1
    def log_book(self,title):
        with open("book.txt","a") as file:
            file.write(f"{self.title} created.Total books are:{Book.books_count} \n")
class Contract:
    all=[]
    contract_count=0
    def __init__(self,author,book,date,royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        self.increase_contracts()
        self.log_contract()
        Contract.all.append(self)
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,value):
        if not isinstance(value,Author):
            raise Exception
        self._author=value
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,value):
        if not isinstance(value,Book):
            raise Exception
        self._book=value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if not isinstance(value,str):
            raise Exception
        self._date=value
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,value):
        if not isinstance(value,int):
            raise Exception
        self._royalties=value
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]
    @classmethod
    def increase_contracts(cls):
        cls.contract_count +=1
    def log_contract(self):
        with open("contract.txt","a") as file:
            file.write(f"The total number of contracts signed is: {Contract.contract_count} \n")

author1=Author("Guido")
author2=Author("Rossum")
book1=Book("Learn Python")
book2=Book("Learn JavaScript")
book3=Book("Learn Flask")
book4=Book("Learn React")
book5=Book("Crack Python")
contract1=Contract(author1,book1,"01/01/2001",10)
contract2=Contract(author1,book2,"03/01/2001",20)
contract3=Contract(author1,book3,"01/01/2001",30)
contract4=Contract(author2,book4,"01/01/2001",40)
author1.sign_contract(book5,f"{datetime.now().date()}",30)

for contract in author1.contracts():
    print(f"Name:{contract.author.name}||Book:{contract.book.title}||Date:{contract.date}||Royalties:{contract.royalties}")
print(f"Total royalties for author1:{author1.total_royalties()}")

for contract in Contract.contracts_by_date("01/01/2001"):
    print(f"Book on 01/01/2001:{contract.book.title}")