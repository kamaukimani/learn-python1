from user import User
print("This is the Student class!!")
class Student(User):
    def __init__(self,name,grade):
        print("Student.__init__ callled")
        super().__init__(name)
        self.grade=grade
    def log_in(self):
        print("Student.log_in() called")
        super().log_in()
        self.in_class=True

oneil=Student("Oneil",10)
print(oneil.name)
kevoh=Student("Kevin",9)
print(kevoh.name)