from user1 import User
import random

print("This the Teacher class subclass of the User class")

class Teacher(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge=[
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
    def teach(self):
        return self.knowledge[random.randint(0,len(self.knowledge)-1)]

my_teacher=Teacher("My","Teacher")
know=my_teacher.teach()
print(know)
print(f"My first name is: {my_teacher.first_name}")
print(f"My last name is: {my_teacher.last_name}")