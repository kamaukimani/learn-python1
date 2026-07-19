print("Welcome to python",end=" ")
print("Its a good language",end="!!")
print("Enjoy",end="\n")
print("End of multiple lines")

#variable=undefined    //undefined is not a datatype in python ..
#print(variable)
i=0
while(i<10):
    print(f"i=${i}")
    i+=1

def my_function(param):
    print("Runnng my function")
    return param+1
my_function_return_value=my_function(1)
print("Function returns:",my_function_return_value)
def say_hi(name):
    print(f"Hello there {name}")
    return name
# print(say_hi())
print(say_hi("John"))

def say_hello(name="John"):
    print(f"Hello, {name}!")
    return name
print(say_hello())
print(say_hello("Doe"))

#function return value
def stylish_painter():
    best_hairstyle="Bob"
    return "Jane"
    return best_hairstyle
    print(best_hairstyle)
print(stylish_painter())
#using the pass keyword
def future_function():
    pass
print("Return value while using pass keyword:",future_function())
def add(a,b):
    sum=a+b
    return sum
print("The sum is:",add(1,2))
def halve(n):
    diff=n/2
    print(f"When you divide {n} by 2, the output is {diff}") # n can't be accessed outside the function scope
    return diff
print(halve(5))
#print(f"The output from the division is:",halve(2))
name="Joe"
def greetings(name):
    print(f"Hello, {name}!")
greetings("Rose")
#changing global variable using the local scope ==> use the global keyword 
change_the_world="Change yourself"
def change_yourself():
    global change_the_world  #using the global keyword to change the global variable
    change_the_world="World changed"
    return change_the_world
#change_yourself()
print("Change yourself is now equal to:", change_yourself())
