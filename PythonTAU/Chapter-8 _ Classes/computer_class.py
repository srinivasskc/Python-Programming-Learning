class computer:

    def config(self):
        print("Windows 10, 64-Bit, 8gb RAM, i5 RAM")

com1 = computer()
#Creating an Object for computer class
print(type(com1))

com2 = computer()
#creating an object for computer class

"""
#class.method(object)
computer.config(com1)
computer.config(com2)
"""

#object.method() -- The com1 goes inside the argument of def config(self), in place of self.
com1.config()   #So, we are passing com1 in config()
com2.config()
#Recommended format



"""
a=9
a.bit_length()
#To see method definitions, CTRL+Click on bit_length()
"""


