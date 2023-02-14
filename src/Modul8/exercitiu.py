# partea de compozitie

class Salary:
    def __init__(self, payment):  # constructor cu 1 parametru
        self._payment = payment

    def get_total(self):
        return 12 * self._payment // 5

    def get_meal_tickets(self):
        return 300


s = Salary(1000)
print(s.get_total())


class Employee:
    def __init__(self, payment, bonus):
        self._payment = Salary(payment)
        self._bonus = bonus

    def get_annual_revenue(self):
        return self._bonus + self._payment.get_total() + self._payment.get_meal_tickets()


income_Vasile = Employee(50000, 5000)
print(f'{income_Vasile.get_annual_revenue()} euro')  # metoda
