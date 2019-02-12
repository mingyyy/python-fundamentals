'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car():
    '''
    class Car defines a car with three attributes: model, year of production, max speed in kilometer per hour
    model: string
    year: integer
    speed: km/h
    '''

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return self.model + " " + str(self.year)

    def speed_up(self): # increase by 5 km/h
        self.max_speed += 5
        return self.max_speed

    def show_details(self): # print out the year, model and max_speed of the car
        return f"This is a {self.year}, {self.model} with maximum speed of {self.max_speed} km per hour."


Bumblebee = Car("Volkswagen_Beetle", 1971, 250)
OptimusPrime = Car("Freightliner_FL86", 1981, 300)

print(Bumblebee)
print(OptimusPrime.speed_up())
print(OptimusPrime.show_details())

