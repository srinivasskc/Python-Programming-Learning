class computer:
    def __init__(self, ram, cpu):
        self.ram=ram
        self.cpu=cpu
        # init to initialize the variables
        #for every object, it will be called once __init and prints twice as we have two objects.

    def config(self):
        #print("Config is ", self.ram)
        #print("config is ", self.cpu)
        print("config is ", self.ram, self.cpu)

com1 = computer('i5', 8)  # computer() - This will instantiate and call init.
# Creating an Object for computer class
# print(type(com1))
com2 = computer('i7', 16)
# creating an object for computer class

# object.method() -- The com1 goes inside the argument of def config(self), in place of self.
com1.config()  # So, we are passing com1 in config()
com2.config()