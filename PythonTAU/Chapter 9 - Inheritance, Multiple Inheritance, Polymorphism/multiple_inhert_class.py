# Parent Class 1

class Item():
    def __init__(self,sku):
        self.sku = sku

    # One method in each class
    def print_sku(self):
        print("The SKU is {}".format(self.sku))

# Parent Class 2

class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The Garment is in section {} and of Type {} ".format(self.section, self.type))

# Child Class Inherit from Both Parents

class Shirts(Item,Garment):
    def __init__(self,sku,section,type,color,name):
        self.color = color
        self.name = name
        Item.__init__(self,sku)  #Attributes from Parent Class 1
        Garment.__init__(self,section,type)  #Attributes from Parent Class 2

    def print_shirt(self):
        print("The Shirt of {} and color {} is on sale".format(self.name,self.color))

#Intializing the Object for Child Class

Jeans = Shirts("SK001",20, "Jeans", "Blue", "Reymonds")

Jeans.print_sku()
Jeans.print_garment()
Jeans.print_shirt()

