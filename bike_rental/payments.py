class Payment:
#Клас для обробки розрахунків та виручки.

    def __init__(self):
        #Ініціалізує загальну виручку початковим значенням 0.0.
        pass

    def calc_cost(self, bike, minutes: int):
        #Обчислює вартість поїздки залежно від типу велосипеда та хвилин.
        #Повертає підсумкову ціну.
        pass

    def pay(self, client, bike, minutes: int):
        #Списує кошти з balance клієнта, додає суму до total_revenue.
        #Повертає сплачену суму.
        pass

    def get_total_revenue(self):
        #Повертає загальну накопичену виручку.
        pass