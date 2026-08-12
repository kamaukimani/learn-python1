print("Hello...Lets work on one-to-many relationships")

#Teacher class is the many in the relationship
class Teacher:
    all=[]
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self._student=None
        Teacher.all.append(self)
    @property
    def student(self):
        return self._student
    @student.setter
    def student(self,value):
        if isinstance(value,Student):
            self._student=value
        else:
            raise TypeError("student must be an instance of the Student class")

#Student class is the one in the relationship.....
#one student can have many teachers
class Student:
    def __init__(self,name):
        self.name=name
    def teachers(self):
        return [teacher for teacher in Teacher.all if teacher.student == self]
    def add_teacher(self,teacher):
        if not isinstance(teacher,Teacher):
            raise ValueError("teacher must be an instance of the Teacher class")
        teacher.student=self

john=Student("John")
doe=Teacher("Doe","Moringa")
guido=Teacher("Guido","Moringa")
doe.student=john
john.add_teacher(guido)
for teacher in john.teachers():
    print(f"{teacher.student.name} teacher is:{teacher.name}||The teacher is from school:{teacher.school}")