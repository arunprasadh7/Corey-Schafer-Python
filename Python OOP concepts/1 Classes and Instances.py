# 1 Classes and Instances.py

class Employee:
	def __init__(self,first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f'{self.first}{self.last}@company.com'.lower()

	def fullname(self):
		return f'{self.first} {self.last}'


e1 = Employee('Arun','Prasadh',50000)
e2  = Employee('Arc', 'Warden',60000)

print(e1)
print(e1.email, e1.pay)
print(e1.fullname())
print(e2.email)
print(e2.fullname())

print(Employee.fullname(e1))
