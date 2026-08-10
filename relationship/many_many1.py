print("many-to-many-relationship")
from datetime import datetime
#many-to-many relationship with an intermediary class

#Enrollment class  is the intermediary class
print(datetime.now())  # test if it working
class Enrollment:
    enrollment_count=0
    all=[]
    def __init__(self,student,course):
        self.student=student
        self.course=course
        self.enrollment_date=datetime.now()
        self.increase_enrollment()
        Enrollment.all.append(self)
    @classmethod
    def increase_enrollment(cls):
        cls.enrollment_count +=1

class Student:
    all=[]
    total=0
    def __init__(self,name):
        self.name=name
        self.increase_total()
        self.log_student(name)
        Student.all.append(self)
    def enroll_in_course(self,course):
        Enrollment(self,course)
    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]
    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]
    @classmethod
    def increase_total(cls):
        cls.total += 1
    def log_student(self,name):
        with open("student.txt","a") as file:
            file.write(f"Student:{self.name} has been created || Total student instances: {Student.total}\n")

class Course:
    all=[]
    def __init__(self,title):
        self.title=title
        self.log_course(title)
        Course.all.append(self)
    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]
    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]
    def enroll_student(self,student):
        Enrollment(student,self)
    def log_course(self,title):
        with open("course.txt","a") as file:
            file.write(f"Course: {self.title} has been created \n")

student1=Student("Doe")
course1=Course("Math 31")
student1.enroll_in_course(course1)
student2=Student("Joan")
course2=Course("Developer")
student1.enroll_in_course(course2)
student2.enroll_in_course(course2)
student2.enroll_in_course(course1)
for enrollment in student1.enrollments():
    print(enrollment.student.name,enrollment.course.title)
print("........................enrollments...................................")
for enrollment in Enrollment.all:
    print(enrollment.student.name,enrollment.course.title)
print("........................courses...................................")
for course in Course.all:
    print(course.title)
print("........................students...................................")
for student in Student.all:
    print(student.name)