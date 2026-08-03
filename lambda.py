print("Let's learn lambdas........")
#using lambda as an argument
square=lambda n: n**2
print(square(5))
add=lambda a,b:a+b
print(add(7,3))
students=[
    ("Alice",90),
    ("Bob",75),
    ("Charlie",85)
]
sorted_students=sorted(students,key=lambda student: student[1])
print(sorted_students)
numbers=[1,2,3,4]
squares=list(map(lambda n:n**2,numbers))
print(squares)
nums=[1,2,3,4,5,6]
evens=list(filter(lambda n:n%2==0,nums))
#evens=filter(lambda n:n%2==0,nums)
print(evens)

#using lambda as the return value of a function

def myfunc(x):
    return lambda n:n+x
new_century=myfunc(100)
print(new_century)
print(new_century(400))

def funcmy(x):
    return lambda a,b:(a+b)*x
my_number=funcmy(2)
print(my_number)
print(my_number(20,30))