class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@piedpiper.com'

    # method used to return full name
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('James', 'Wijaya', 50000)
emp_2 = Employee('Matthew', 'Halim', 45000)

print(emp_1.fullName())
print(emp_2.email)
print(emp_1.pay)
print(emp_2.pay)
