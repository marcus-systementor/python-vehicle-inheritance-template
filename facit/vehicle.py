"""One possible core solution for the vehicle lab."""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def show_status(self):
        if self.is_running:
            status = "running"
        else:
            status = "stopped"
        return f"{self.brand} {self.model} is currently {status}"

    def move(self):
        return "The vehicle is moving"


class Car(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is driving on the road"

    def honk(self):
        return "Beep beep!"


class Motorcycle(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is riding on the road"

    def rev_engine(self):
        return "Vroom!"


class Boat(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} is sailing on the water"

    def drop_anchor(self):
        return "Anchor dropped"
