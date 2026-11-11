class Payment:

    def __init__(self):
        self.total_revenue = 0.0

    def calc_cost(self, bike, minutes: int):
        if minutes <= 0:
            raise ValueError("Кількість хвилин має бути більшою за 0")

        if bike.is_electric():
            rate = 5
        else:
            rate = 2

        return rate * minutes


    def pay(self, client, bike, minutes: int):
        cost = self.calc_cost(bike, minutes)
        client.charge(cost)
        self.total_revenue += cost
        return cost


    def get_total_revenue(self):
        return self.total_revenue