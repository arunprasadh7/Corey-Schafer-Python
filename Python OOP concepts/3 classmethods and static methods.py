# ckass nethods and static methods

class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}{self.last}@company.com'.lower()
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'.title()

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount


e1 = Employee('Arun', 'Prasadh', 5000)
print(e1.email)
print(e1.fullname())

e2 = Employee('Storm','spirit',6000)
print(Employee.fullname(e2))

print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)

print(e1.__dict__)
e1.bonus = 1.05
print(e1.__dict__)
print(e1.bonus)

Employee.set_raise_amount(1.06)
print(Employee.__dict__)