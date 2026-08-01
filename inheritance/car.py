from vehicle import Vehicle
print("Welcome.....Let's code the Car class")
class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOM!!!!!!!!!!!!"

car=Car("Ten",34)
print(car.go())
print(car.fill_up_tank())
print(f"The wheel size is : {car.wheel_size}")
print(f"The wheel number is : {car.wheel_number}")