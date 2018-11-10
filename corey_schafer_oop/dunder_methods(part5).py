class Employee:
    numOfEmployee = 0
    raiseAmount = 1.04
    # dunder method stands for double underscore method (magic or special method)
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@piedpiper.com'
        Employee.numOfEmployee += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    # dunder methods to make codes readable
    def __repr__(self):
        return 'Employee({} {}, {})'.format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullName(),self.email)

    # dunder method __add__ (to add combined salaries of 2 employees)
    def __add__(self, other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raiseAmount = amount

    # dunder method __len__(to count how many letters on employees' full name)
    def __len__(self):
        return len(self.fullName())

class Developer(Employee):

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emp(self):
        for emp in self.employees:
            print('-->', emp.fullName())

dev_1 = Developer('Axel', 'Geoffredo', 50000, 'Python')
dev_2 = Developer('Edward', 'Christian', 50000, 'Java')

mgr_1 = Manager('Robby', 'Sutanto', 80000, [dev_1])
mgr_2 = Manager('Kezia', 'Liman', 85000, [dev_2])

# checking dunder method (__repr__)
print(repr(mgr_1))

# checking dunder method (__str__)
print(str(mgr_1))

# checking dunder method (__add__)
print(dev_1 + dev_2)

# checking dunder method (__len__)
print(len(mgr_1))
