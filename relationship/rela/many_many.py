from datetime import datetime
print(datetime.now())
print("Working on aggregate methods with a many-to-many relationship using an intermediary class")
#intermediary class
class Enrollment:
    all=[]
    def __init__(self,student,course):
        if isinstance(student,Student) and isinstance(course,Course):
            self.student=student
            self.course=course
            self._enrollment_date=datetime.now()
            type(self).all.append(self)
        else:
            TypeError("Invalid types for Student and/or Course")
    def get_enrollment_date(self):
        return self._enrollment_date
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count={}
        for enrollment in cls.all:
            date=enrollment.get_enrollment_date().date()
            enrollment_count[date]=enrollment_count.get(date,0)+1
        return enrollment_count
class Student:
    def __init__(self,name):
        self.name=name
        self._enrollments=[]
        self._grades={}
    def enroll(self,course,grade):
        if isinstance(course,Course):
            enrollment=Enrollment(self,course)
            self._grades[enrollment]=grade
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of the Course class")
    def get_grade(self):
        return self._grades
    def aggregate_average_grade(self):
        total_grade=sum(self._grades.values())
        num_courses=len(self._grades)
        average_grade=total_grade/num_courses
        return average_grade
    def get_enrollments(self):
        return self._enrollments.copy()
    def courses_count(self):
        return len(self._enrollments)
class Course:
    def __init__(self,title):
        self.title=title
        self._enrollments=[]
    def add_enrollment(self,enrollment):
        if isinstance(enrollment,Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of the Enrollment class")
    def get_enrollments(self):
        return self._enrollments.copy()


student1=Student("Guido")
student2=Student("Van")
student3=Student("Rossum")

course1=Course("Learn Python Programming")
course2=Course("Learn Flask")
course3=Course("Learn Javascript")
course4=Course("Learn React")

student1.enroll(course1,40)
student1.enroll(course2,60)

student3.enroll(course1,50)
student3.enroll(course2,60)
student3.enroll(course3,70)

student2.enroll(course4,80)
student2.enroll(course1,70)
student2.enroll(course2,60)

for enrollment in student1.get_enrollments():
    print(f"Student name: {enrollment.student.name}|| Course: {enrollment.course.title}")

print(Enrollment.aggregate_enrollments_per_day())
print(student1.get_grade())
print(student1.aggregate_average_grade())
print(student2.get_grade())
print(student2.aggregate_average_grade())