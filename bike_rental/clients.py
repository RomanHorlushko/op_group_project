class Client:
    "Створюємо конструктор для класу Client, він має імʼя - name, баланс - balance, велосипед на якому він катається - current_bike"
    def __init__(self, name, balance=0, current_bike=None):
        pass

    "Метод щоб клієнт зміг поповнити баланс"
    def top_up(self, amount):
        pass

    "Метод, який перевіряє чи вистачає грошей щоб зняти велосипед"
    def can_pay(self, amount):
        pass

    "Метод, який списує гроші з балансу клієнта"
    def charge(self, amount):
        pass
