class Bike:
    def __init__(self, number, bike_type, battery=100):
        # номер, тип ("regular" або "electric") і заряд 0–100
        self.number = number
        self.bike_type = bike_type
        self.battery = battery

    def __str__(self):
        # повертає опис велосипеда для виводу
        return f"велосипед №{self.number} ({self.bike_type})"

    def is_electric(self):
        # повертає True, якщо велосипед електричний
        return self.bike_type == "electric"

    def is_low_battery(self):
        # повертає True, якщо велосипед електричний і заряд нижче 20
        return self.is_electric() and self.battery < 20


class Station:
    def __init__(self, name):
        # назва станції і порожній список велосипедів
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        # ставить велосипед на станцію
        self.bikes.append(bike)

    def take_bike(self):
        # повертає придатний велосипед (з кінця списку) або None, якщо таких немає
        for bike in reversed(self.bikes):
            if not bike.is_low_battery():
                self.bikes.remove(bike)
                return bike
        return None

    def has_bikes(self):
        # повертає True, якщо є хоча б один придатний велосипед
        for bike in self.bikes:
            if not bike.is_low_battery():
                return True
        return False

    def count(self):
        # повертає кількість велосипедів на станції
        return len(self.bikes)

    def low_battery_bikes(self):
        # повертає список розряджених електричних велосипедів
        result = []
        for bike in self.bikes:
            if bike.is_low_battery():
                result.append(bike)
        return result
