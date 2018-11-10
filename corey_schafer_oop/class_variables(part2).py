class Employee:

    raise_amount = 1.04
    numOfEmployees = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@piedpiper.com'
        Employee.numOfEmployees += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('James', 'Wijaya', 50000)
emp_2 = Employee('Matthew', 'Halim', 50000)
emp_1.raise_amount = 1.06

emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.fullName)
