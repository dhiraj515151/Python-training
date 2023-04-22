#  defaultConstructor takes no arguments. It is used to create an object for default value for the attributes.
class defaultConstructor:
    #constructor
    def __init__(self):
        self.name = 'Dhiraj'

# Creating object  of the class
obj = defaultConstructor()

# calling the instance method using object - obj
print(obj.name)