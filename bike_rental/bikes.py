class Bike:
    def __init__(self, number, bike_type):
        # номер і тип: "regular" або "electric"
        self.number = number
        self.bike_type = bike_type

    def is_electric(self):
        # повертає True, якщо велосипед електричний
        return self.bike_type == "electric"


class Station:
    def __init__(self, name):
        # назва станції і порожній список велосипедів
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        # ставить велосипед на станцію
        self.bikes.append(bike)

    def take_bike(self):
        # повертає Bike або None, якщо станція порожня
        if not self.bikes:
            return None
        return self.bikes.pop()

    def has_bikes(self):
        # повертає True, якщо є хоча б один велосипед
        return len(self.bikes) > 0

    def count(self):
        # повертає кількість велосипедів на станції
        return len(self.bikes)
