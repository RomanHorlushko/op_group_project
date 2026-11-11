class Rental:
    def __init__(self, payment):
        self.payment = payment

    def rent_bike(self, client, station):
        if client.current_bike is not None:
            return False, "already_riding"
        if not station.has_bikes():
            return False, "no_bikes"
        bike = station.take_bike()
        if bike is None:
            return False, "no_bikes"
        client.current_bike = bike
        return True, bike

    def return_bike(self, client, station, minutes):
        if client.current_bike is None:
            return False, "no_bike"
        if minutes <= 0:
            return False, "invalid_time"
        bike = client.current_bike
        cost = self.payment.calc_cost(bike, minutes)
        if not client.can_pay(cost):
            return False, "not_enough_money"
        paid = self.payment.pay(client, bike, minutes)
        if paid is False:
            return False, "payment_failed"
        station.add_bike(bike)
        client.current_bike = None
        return True, cost

