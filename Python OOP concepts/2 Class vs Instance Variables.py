#2 Class variables and instance variables

class Employee:

    bonus = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}{self.last}@company.com'.lower()

    def fullname(self):
        return f'{self.first} {self.last}'.title()

    def pay_raise(self):
        return self.pay * self.bonus


e1 = Employee('Arun', 'Prasadh', 5000)
e2 = Employee('Storm', 'spirit', 6000)

print(e1.fullname())
print(e1.email)
e1.bonus = 1.05
print((e1).pay_raise())

print(e2.fullname())
print(e2.email)
print(e2.pay_raise())

print('Bonus variable')
print(Employee.bonus)
print(e1.bonus)
print(e2.bonus)

e2.bonus = 2.0
print(e2.__dict__)
print(e2.bonus)
print(e2.pay_raise())