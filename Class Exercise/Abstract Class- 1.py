from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Sedan(Transport):
    def __init__(self):
        pass

    def start(self):
        print("Sedan is starting.")

    def stop(self):
        print("Sedan is stopping.")


class Scooter(Transport):
    def __init__(self):
        pass

    def start(self):
        print("Scooter is starting.")

    def stop(self):
        print("Scooter is stopping.")


# Create objects
sedan = Sedan()
sedan.start()

# Attempting to instantiate abstract class
try:
    transport = Transport()  # Raises TypeError
except TypeError as e:
    print(e)
