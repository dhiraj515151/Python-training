class factorialMain:
    # Creating a function for getting the factorial
    def getFactorial(self, n):
        return 1 if (n == 1) or (n == 0) else (n * self.getFactorial(n-1)) #self = instance of the class

# Creating an instance of the factorialMain class
obj = factorialMain()

# Calling the getFactorial method on the obj instance
result = obj.getFactorial(5)
print(result)
