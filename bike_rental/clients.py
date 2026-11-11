class Client:
    
    def __init__(self, name, balance=0, current_bike=None):
    #Створюємо онструктор для класу Client, він має імʼя - name, баланс - balance, велосипед на якому він катається - current_bike
        self.name = name
        self.balance = balance
        self.current_bike = current_bike

    def top_up(self, amount):
    #Метод щоб клієнт зміг поповнити баланс
        self.balance += amount
        return self.balance

    def can_pay(self, amount):
    #Метод, який перевіряє чи вистачає грошей щоб зняти велосипед
        if self.balance <= amount:
            return False
        return True

    def charge(self, amount):
    #Метод, який списує гроші з балансу клієнта
        self.balance -= amount
        return self.balance
