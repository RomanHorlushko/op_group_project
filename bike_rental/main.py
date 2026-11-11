from bikes import Bike, Station
from clients import Client
from rentals import Rental
from payments import Payment

REASONS = {
    "no_bikes": "на станції немає вільних велосипедів",
    "already_riding": "клієнт уже катається на іншому велосипеді",
    "no_bike": "у клієнта немає велосипеда, щоб повернути",
    "invalid_time": "некоректний час поїздки",
    "not_enough_money": "у клієнта недостатньо грошей",
    "payment_failed": "оплата не пройшла",
    "low_battery": "є лише розряджені велосипеди (заряд нижче 20%)",
}


def describe(client, action, ok, result):
    if ok:
        return f"{client.name} {action}: OK ({result})"
    return f"{client.name} {action}: ПОМИЛКА — {REASONS.get(result, result)}"


def main():
    # 1. Створити 3 станції: А, Б і В.
    station_a = Station("А")
    station_b = Station("Б")
    station_c = Station("В")

    # 2. Створити 7 велосипедів (3 звичайні, 4 електричні, з них 2 розряджені) і поставити на станції.
    station_a.add_bike(Bike(1, "regular"))
    station_a.add_bike(Bike(3, "regular"))
    station_a.add_bike(Bike(4, "regular"))
    station_a.add_bike(Bike(2, "electric"))
    station_a.add_bike(Bike(6, "electric", 10))  # розряджений, стоїть останнім, його мають пропустити
    station_b.add_bike(Bike(5, "electric"))
    station_c.add_bike(Bike(7, "electric", 15))  # на станції лише розряджений

    # 3. Створити 2 клієнтів з різним балансом: Оля (300 грн) і Петро (150 грн).
    olya = Client("Оля", 300)
    petro = Client("Петро", 150)
    payment = Payment()
    rental = Rental(payment)

    # 4. Оля бере електричний велосипед на станції А (розряджений №6 пропускається).
    ok, result = rental.rent_bike(olya, station_a)
    print(describe(olya, "бере велосипед на станції А", ok, result))

    # 5–7. Через 20 хвилин повертає його на станцію Б, списується 20 × 5 = 100 грн.
    ok, result = rental.return_bike(olya, station_b, 20)
    print(describe(olya, "повертає велосипед на станцію Б, грн", ok, result))

    # 8. Петро робить ще дві поїздки (обидві з Б на А).
    ok, result = rental.rent_bike(petro, station_b)
    print(describe(petro, "бере велосипед на станції Б", ok, result))
    ok, result = rental.return_bike(petro, station_a, 15)
    print(describe(petro, "повертає велосипед на станцію А, грн", ok, result))

    ok, result = rental.rent_bike(petro, station_b)
    print(describe(petro, "бере велосипед на станції Б", ok, result))
    ok, result = rental.return_bike(petro, station_a, 10)
    print(describe(petro, "повертає велосипед на станцію А, грн", ok, result))

    # 9. Спроба взяти велосипед на порожній станції.
    ok, result = rental.rent_bike(olya, station_b)
    print(describe(olya, "бере велосипед на станції Б", ok, result))

    # 9б. Спроба взяти велосипед, коли на станції лише розряджені.
    ok, result = rental.rent_bike(olya, station_c)
    print(describe(olya, "бере велосипед на станції В", ok, result))

    # 10. Баланси клієнтів і звіт адміністратора.
    print("=== Баланси ===")
    print(f"{olya.name}: {olya.balance} грн")
    print(f"{petro.name}: {petro.balance} грн")
    report([station_a, station_b, station_c], payment)

    # 11. Перевірки: числа пораховані вручну, а не взяті з програми.
    assert olya.balance == 200
    assert petro.balance == 25
    assert payment.get_total_revenue() == 225
    assert station_a.count() == 6 and station_b.count() == 0 and station_c.count() == 1
    print("Усі перевірки пройдено")


def report(stations, payment):
    print("=== Звіт адміністратора ===")
    for station in stations:
        print(f"Станція {station.name}: {station.count()} велосипедів")
    print("Розряджені електровелосипеди:")
    for station in stations:
        for bike in station.low_battery_bikes():
            print(f"  №{bike.number} на станції {station.name}: {bike.battery}%")
    print(f"Загальна виручка: {payment.get_total_revenue()} грн")


if __name__ == "__main__":
    main()
