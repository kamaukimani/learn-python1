print("one-many relationships using aggregation")
class Car:
    def __init__(self,engine):
        self.engine=engine
class Engine:
    def __init__(self,cylinders,fuelType):
        self.cylinders=cylinders
        self.fuelType=fuelType
four_cylinder_engine=Engine(4,"regular")
acura_tlx=Car(four_cylinder_engine)
print(acura_tlx.engine.cylinders,acura_tlx.engine.fuelType)