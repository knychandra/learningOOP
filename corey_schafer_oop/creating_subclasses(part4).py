class Employee:
    raiseAmount = 1.04
    numOfEmployee = 0

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

# making a subclass called Developer that inherits from class Employee
class Developer(Employee):

    def __init__(self,first,last,pay,prog_lang):
        # this super() is just referring to the superclass -> Employee
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def showEmp(self):
        for emp in self.employees:
            print('-->', emp.fullName())

dev_1 = Developer('Axel', 'Geoffredo', 55000, 'Python')
dev_2 = Developer('Wirawan', 'Wijono', 55000, 'Java')

mgr_1 = Manager('Robby', 'Sutanto', 80000, [dev_1])
mgr_2 = Manager('Edward', 'Santoso', 90000, [dev_2])

print(mgr_1.fullName())
print(mgr_2.email)

mgr_1.showEmp()
mgr_2.showEmp()

# built in method to check if it is an instance of
print(isinstance(mgr_1,Manager))

# built in method to check if it is a subclass of
print(issubclass(Developer,Employee))
