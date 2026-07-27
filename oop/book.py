print("Welcome to the Book class")
class Book:
    def __init__(self,title,page_count):
        self.title=title
        self.page_count=page_count
    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count
    @page_count.setter
    def page_count(self,page_count):
        """page_count must be of type integer"""
        if type(page_count) is int and 0 <= page_count <=200:
            
            self._page_count=page_count
        else:
            raise TypeError(f"{page_count} must be an integer between 0 and 200")
    @page_count.deleter
    def page_count(self):
        print("Going to the previous page.....")
        self.page_count-=1 
        #self.page_count=self.page_count-1      f  you want to still use the setter for validation
    def turn_page(self):
        print("Flippint the page...wow you read fast..Let's go to the next page....")
        #self.page_count=self.page_count+1
        self.page_count+=1
book=Book("Blossoms Of The Savannah", 10)
print(book.title)
print(book.page_count)
del book.page_count
print(book.page_count)
book.turn_page()
print(book.page_count)