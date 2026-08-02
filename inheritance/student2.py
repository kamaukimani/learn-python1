print("Student class is the superclass of ChattyStudent class")
class Student:
    def __init__(self):
        pass
    def hello(self):
        print("He there! I'm so excited to learn stuff.")
    def raise_hand(self):
        print("Pick me!")
student=Student()
student.hello()
student.raise_hand()