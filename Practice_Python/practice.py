class Car:
    wheels = 4

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels


car1 = Car("red", 2)
print(car1.color)
print(car1.wheels)
