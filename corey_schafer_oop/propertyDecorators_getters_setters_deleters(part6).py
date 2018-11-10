class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    # making email from method to a property
    @property
    def email(self):
        return '{}.{}@piedpiper.com'.format(self.first,self.last)

    # making fullName from method to a property
    @property
    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    # making a setter for full name (so we can change it using code)
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Name deleted!')
        self.first = None
        self.last = None

emp_1 = Employee('Kenny', 'Chandra', 50000)
# changing first name and last name
emp_1.first = 'Jim'
emp_1.last = 'Hutton'


print(emp_1.email)
print(emp_1.fullName)

# changing full name using @fullName.setter
emp_1.fullName = 'Rocky Rock'
print(emp_1.fullName)
print(emp_1.email)
print(emp_1.pay)

# deleting full name using @fullName.deleter
del emp_1.fullName
print(emp_1.fullName)
