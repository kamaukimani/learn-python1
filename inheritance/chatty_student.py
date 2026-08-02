from student2 import Student
print("ChattyStudent is a subclass of the student class")
class ChattyStudent(Student):
    def __init__(self):
        pass
    def hello(self):
        super().hello()
        print("""
                How are you doing today? I'm okay,but i'm kind of tired. Did you watch The Walking Dead last
                night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay wel let 
                me just tell you who died...

            """)
    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()

chatty_student=ChattyStudent()
chatty_student.hello()
chatty_student.raise_hand()