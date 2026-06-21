#Object Oriented Programming 

#CLASS
class Car:
    total_cars = 0

    def __init__(self, brand, model): # can be considered a constructor
        self.__brand = brand # self is equivalent of 'this' to provide context for multiple instances of this class
        self.__model = model
        Car.total_cars += 1 #can also use self.total_cars

    def get_brand(self): #Encapsulated access
        return self.__brand + "!"

    @property
    def model(self): #getter
        return self.__model

    def model(self, value): #setter
        self.__model = value
    
    def model(self): #deleter
        del self.__model

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol/Diesel"
    
    @staticmethod
    def car_description():
        return "They are a means of transport"

my_car = Car("Tata", "Sierra")
print(my_car.full_name())

#INHERITANCE
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"
    

my_electric_car = ElectricCar("Tesla", "Model S", "85 KWh")
print(my_electric_car.full_name())

#ENCAPSULATION
#use __varibale to make it private and make it accessible using a get() function
#here we have encapsulated brand and model attribute making them accessible only inside the class
# print(my_car.__brand) #gives error
print(my_car.get_brand())

#POLYMORPHISM
#Nothing extra to do just two diffrenct instances although connected through inheritance still show differernt behaviour
print(my_car.fuel_type())
print(my_electric_car.fuel_type())

#CLASS VARIBLE
#these belong to a class rather than an instance
print(Car.total_cars)

#STATIC METHOD
#these belong to a class and but are also accessible by an instance, does not need self
print(my_car.car_description())
print(Car.car_description())

#Property Decorator
#helps define Class attributes
print(my_car.get_model())
