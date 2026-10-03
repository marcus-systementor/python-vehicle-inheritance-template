"""Show shared state, inherited methods, and polymorphic movement."""

from vehicle import Vehicle, Car, Motorcycle, Boat


base_vehicle = Vehicle("Generic", "Vehicle")
car = Car("Volvo", "V60")
motorcycle = Motorcycle("Honda", "CB650R")
boat = Boat("Yamaha", "242X")

print(base_vehicle.show_status())
print(base_vehicle.move())

vehicles = [car, motorcycle, boat]
for vehicle in vehicles:
    vehicle.start()
    print(vehicle.show_status())
    print(vehicle.move())

print(car.honk())
print(motorcycle.rev_engine())
print(boat.drop_anchor())

car.stop()
print(car.show_status())
print(motorcycle.show_status())
print(boat.show_status())
