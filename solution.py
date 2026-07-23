/*
  Write a method `admin_login` that takes two arguments, a username and a
  password. If the username is "admin" or "ADMIN" and the password is "12345",
  return "Access granted". Otherwise, return "Access denied".
*/
function adminLogin(username, password) {
  if ((username === "admin" || username === "ADMIN") && password === "12345") {
    return "Access granted";
  } else {
    return "Access denied";
  }
}

/*
  Write a method `hows_the_weather` that takes in one argument, a temperature.
  If the temperature is below 40, return "It's brisk out there!". If the temperature is
  between 40 and 65, return "It's a little chilly out there!". If the temperature is above 85,
  return "It's too dang hot out there!". Otherwise, return "It's perfect out there!"
*/
function howsTheWeather(temperature) {
  let response;
  if (temperature < 40) {
    response = "brisk";
  } else if (temperature >= 40 && temperature <= 65) {
    response = "a little chilly";
  } else if (temperature > 85) {
    response = "too dang hot";
  } else {
    response = "perfect";
  }
  return `It's ${response} out there!`;
}

/* 
  Write a method `fizzbuzz` takes in a number. For multiples of three, return
  "Fizz" instead of the number. For the multiples of five, return "Buzz". For
  numbers which are multiples of both three and five, return "FizzBuzz". For
  all other numbers, just return the number itself.
*/
function fizzbuzz(num) {
  if (num % 3 === 0 && num % 5 === 0) {
    return "FizzBuzz";
  } else if (num % 3 === 0) {
    return "Fizz";
  } else if (num % 5 === 0) {
    return "Buzz";
  } else {
    return num;
  }
}

/*
  Write a method `calculator` that takes three arguments: an operation and two
  numbers. If the operation is one of the following: `+`, `-`, `*`, or `\`,
  return the value of calling the operation on the two numbers. Otherwise,
  output a message saying "Invalid operation!" and return `nil`.
*/
function calculator(operation, num1, num2) {
  switch (operation) {
    case "+":
      return num1 + num2;
    case "-":
      return num1 - num2;
    case "*":
      return num1 * num2;
    case "/":
      return num1 / num2;
    default:
      console.log("Invalid operation!");
  }
}

#python
#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

    return "It's perfect out there!"

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    
    return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None


    spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

# def sort_by_heat(spicy_foods):
#     return sorted(spicy_foods, key=lambda h: h['heat_level'])

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)