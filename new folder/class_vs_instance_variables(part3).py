class BestCourse:
    # this is a class
    website = 'www.cleverprogrammer.com' # tied directly to a class (not to any object)
    
    def __init__(self,name):
        self.name = name


python = BestCourse('Learn Python Programming')
math = BestCourse('Learn Basic Mathematics')
# python and math are both an object

print(python.name) # printing object's variable
print(BestCourse.website) # printing class' variable

print(math.name) # printing object's variable
print(BestCourse.website) # printing class' variable
