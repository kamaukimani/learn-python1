from user1 import User
print("This the Student class a subclass of the User class")
class Student(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge=[]
    def learn(self,knowledge_string):
        self.knowledge.append(knowledge_string)
    
my_student=Student("My","Student")
my_student.learn("Learn Python Programming")
my_student.learn("Coding is my drug")
print(f"First name: {my_student.first_name} , Last name: {my_student.last_name}")
print(my_student.knowledge)