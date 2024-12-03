class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def vehicle_info(self):
        print(f"Color: {self.__color}")


class Car(Vehicle):
    def __init__(self, color, brand, seats, fuel_type):
        super().__init__(color)
        self.__brand = brand
        self.__seats = seats
        self.__fuel_type = fuel_type

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = seats

    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Brand: {self.__brand}")
        print(f"Seats: {self.__seats}")
        print(f"Fuel Type: {self.__fuel_type}")


# Create instances
car1 = Car("Blue", "Tesla Model S", 5, "Electric")
car2 = Car("White", "BMW X5", 7, "Diesel")

# Access and modify properties
car1.set_brand("Tesla Model X")
car2.set_fuel_type("Hybrid")

# Display vehicle information
car1.vehicle_info()
car2.vehicle_info()
