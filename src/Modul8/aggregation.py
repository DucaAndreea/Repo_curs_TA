# partea de compozitie

class Salary:
    def __init__(self, payment):
        self._payment = payment

    def get_total(self):
        return 12 * self._payment // 5

    def get_meal_tickets(self):
        return 300


class Employee:
    def __init__(self, payment, bonus):
        self._payment = payment
        self._bonus = bonus

    def get_annual_revenue(self):
        return self._bonus + self._payment.get_total() + self._payment.get_meal_tickets()


s = Salary(1000)
income_Vasile = Employee(s, 5000)
print(f'{income_Vasile.get_annual_revenue()} euro')

#TODO: to read about Solid
