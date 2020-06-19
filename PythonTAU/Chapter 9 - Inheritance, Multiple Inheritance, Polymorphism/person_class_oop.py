class Person:
    def __init__(self, firstname, lastname, healthstatus, status):
        """
        Initialize the attributes to be used in available/all alss methods and \
        for all objects created by this class
        """
        self.firstname = firstname
        self.lastname = lastname
        self.healthstatus = healthstatus
        self.status = status

    def introduction(self):
        print("Hello, My Name is {} {}, My health is {}".format(self.firstname, self.lastname, self.status))


# Creating an object for the class. Initiating the Variables
srinivas = Person("Srinivas", "Kadiyala", 80, "Good")
# mark = Person("Mark", "Julie", 90, "Super")

# object.method() - Introducing both the persons
srinivas.introduction()

"""
It's working until Person Class.
O/p: 
Hello, My Name is Srinivas Kadiyala, My health is Good
Srinivas is not happy today
Health Status 70
Hey, Srinivas please take care
"""


# Inheritance from Person Class
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, healthstatus, status):
        super().__init__(firstname, lastname, healthstatus, status)
        # firstname, lastname, health, status are from person class
        # instead of reassigning those attributes, we'll use the super method, which will initialize those attributes as they are defined in the parent class.
        self.weapon = weapon
        # Accessing the weapon attributes

    def hurt(self, other):
        # here other is a person
        if self.weapon == "rock":
            other.healthstatus -= 10
        elif self.weapon == "stick":
            other.healthstatus -= 5
        elif self.weapon == "arrow":
            other.healthstatus -= 25
        print("Other.HealthStatus: ", other.healthstatus)

    def insult(self, other):
        if other.healthstatus < 80:
            print("{}, you look tired and weak".format(other.firstname))


# Creating an object for the class. Initiating the Variables
Marie = Enemy("rock", "Marie", "Gold", 80, "Good")
# Goldie = Enemy("Goldie", "Marrie", 90, "Super","arrow")

Marie.hurt(srinivas)
Marie.insult(srinivas)

#Error Condition
#srinivas.hurt(Marie)
#srinivas.hurt(srinivas)