class Employee:
    raiseAmount = 1.04
    numOfEmployees = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@piedpiper.com'
        Employee.numOfEmployees += 1

    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    # making a classmethod
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raiseAmount = amount

    # using classmethod as an alternative class constructor
    @classmethod
    def from_string(cls,emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    # making a staticmethod
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('James', 'Wijaya', 50000)
emp2 = Employee('Matthew', 'Halim', 50000)

# class method (set_raise_amount)
# it changes raiseAmount for every object in the class Employee
Employee.set_raise_amount(1.06)
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

# alternative class constructor
emp_string1 = 'Kenny-Chandra-100000'
emp_string2 = 'David-Soesilo-70000'
emp_string3 = 'Robby-Sutanto-75000'

new_emp_string1 = Employee.from_string(emp_string1)
new_emp_string2 = Employee.from_string(emp_string2)
new_emp_string3 = Employee.from_string(emp_string3)

print(new_emp_string1.email)
print(new_emp_string2.first)
print(new_emp_string3.last)

# staticmethod is_weekday
import datetime
my_date = datetime.date(2018, 11, 20)

print(Employee.is_weekday(my_date))
