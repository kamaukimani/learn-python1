print("Relationships in objects")
#association
#one way
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

# two way
class Student:
    all=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._teacher=None
        Student.all.append(self)
    @property
    def teacher(self):
        return self._teacher
    @teacher.setter
    def teacher(self,value):
        if not isinstance(value,Teacher):
            raise TypeError("teacher must be an instance of Teacher class")
        self._teacher=value
class Teacher:
    def __init__(self,name):
        self.name=name
    def students(self):
        return [student for student in Student.all if student.teacher == self]
    def add_students(self,student):
        if not isinstance(student,Student):
            raise TypeError("student must be an instance of Student class")
        student.teacher = self

student=Student("Alice",20)
student1=Student("John",23)
teacher=Teacher("Bob")
student.teacher=teacher  #either have this
print(student.teacher.name)
teacher.add_students(student) 
teacher.add_students(student1) #or this
for student in teacher.students():
    print(student.name,student.age)