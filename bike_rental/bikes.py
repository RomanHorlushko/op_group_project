class Bike:
    def __init__(self, number, bike_type):
        # номер і тип: "regular" або "electric"
        pass

    def is_electric(self):
        # повертає True, якщо велосипед електричний
        pass


class Station:
    def __init__(self, name):
        # назва станції і порожній список велосипедів
        pass

    def add_bike(self, bike):
        # ставить велосипед на станцію
        pass

    def take_bike(self):
        # повертає Bike або None, якщо станція порожня
        pass

    def has_bikes(self):
        # повертає True, якщо є хоча б один велосипед
        pass

    def count(self):
        # повертає кількість велосипедів на станції
        pass
