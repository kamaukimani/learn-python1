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
#conditional rendering using if/else
def call_dog(dog):

    if dog=="hungry":
        owner="Reffiling food bowl"
    elif dog=="thirsty":
        owner="Reffiling water bowl"
    elif dog=="playful":
        owner="Playing tug-of-war"
    elif dog=="cuddly":
        owner="Snuggling"
    else:
        owner="Reading newspaper"
    return owner

print(f"The dog owner is:{call_dog('thirsty')}")

#usong ternary operator in python
age=20
is_adult="Adult" if age>17 else "A baby"
print (is_adult)

def divide():
    try:
        age=int(input("Enter age: "))
        is_even="even" if age%2 ==0 else "not even"    
    except ValueError:
        print("Enter a number greater than zero")
    except ZeroDivisionError:
        print("You can not divide age by zero")
    else:

        print(f"After getting the modulus {age} is: {is_even}")
    finally:
        print("Program ended successfully")
    return is_even

#print(divide())
def dictionary_mapping(dog):
    dict_map={
        "cuddy":"Snuggling",
        "hungry":"Reffiling food bowl",
        "thirsty":"Reffiling water bowl",
        "playful":"Playing tug-of-war"
    }
    owner=dict_map.get(dog,"Reading newspaper")
    return owner
# print(f"The dog owner is: {dictionary_mapping('thirsty')}")
print(f"The dog owner is: {dictionary_mapping('fighting')}")