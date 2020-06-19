import random

class Person:
    def __init__(self,firstname,lastname,health,status):
        """
        Initialize the attributes to be used in available/all alss methods and \
        for all objects created by this class
        """
        self.firstname = firstname
        self.lastname = lastname
        self.healthstatus = health
        self.status = status

    def introduction(self):
        print("Hello, My Name is {} {}, My health is {}".format(self.firstname,self.lastname,self.status))


    def emotions(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is not happy".format(self.firstname))

    def status_check(self):
        self.healthstatus = (self.healthstatus-20)
        print("Health Status", self.healthstatus)
        if self.healthstatus == 100:
            print("{} is fully healthy".format(self.firstname))
        elif self.healthstatus > 75 and self.healthstatus <= 99:
            print("{} is normal".format(self.firstname))
        elif self.healthstatus >= 50 and self.healthstatus<= 75:
            print("Hey, {} please take care".format(self.firstname))
        elif self.healthstatus >= 30 and self.healthstatus<50:
            print("Hello {}, you need to be admitted to hospital".format(self.firstname))
        else:
            print("{} is in unconsious state".format(self.firstname))


#Creating an object for the class. Initiating the Variables
person1 = Person("Srinivas", "Kadiyala", 80, "Good")
person2 = Person("Mark", "Julie", 90, "Super")

#object.method() - Introducing both the persons
person1.introduction()
person2.introduction()

person1.emotions()
person2.emotions()

person1.status_check()
person2.status_check()