from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, brand, details):
        self.brand = brand
        self.details = details

    @abstractmethod
    def ignite_engine(self):
        pass

    def halt_engine(self):
        print(f"Engine of {self.brand} stopped.")

class Truck(Transport):
    def __init__(self, brand, model, details):
        super().__init__(brand, details)
        self.model = model

    def ignite_engine(self):
        print(f"Engine of {self.brand} {self.model} is starting.")

# Create an object of Truck
truck = Truck("Volvo", "FMX", "Heavy-duty construction truck")
truck.ignite_engine()

# Attempting to instantiate abstract class
try:
    transport = Transport("Generic", "Abstract Vehicle")
except TypeError as e:
    print(e)
