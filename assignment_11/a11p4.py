class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f"Max speed: {self.max_speed} mph, Mileage: {self.mileage} miles"


class Bus(Vehicle):
    pass


vehicle1 = Vehicle(120, 10000)
vehicle2 = Vehicle(80, 50000)

bus1 = Bus(60, 200000)
bus2 = Bus(70, 150000)

print("Vehicle 1:", vehicle1)
print("Vehicle 2:", vehicle2)
print("Bus 1:", bus1)
print("Bus 2:", bus2)
